import { getSession, ort } from './runtime.js'
import { fetchMosaic, pixelToLatLon } from './tiles.js'
import { iterWindows, YOLO_SIZE } from './preprocess.js'
import { decodeDetections, nms } from './postprocess.js'

// Data
const CONF_THRESHOLD = 0.30
const IOU_THRESHOLD  = 0.45

// In-browser object detection with YOLOv8 (ONNX Runtime Web).
//   const result = await detect({ modelId: 'buildings', bbox, zoom })
//   const result = await detect({ modelId: 'pools',     bbox, zoom })
//
// Returns:
//   {
//     model,                               // 'buildings' | 'pools'
//     count,                               // number of objects detected
//     detections: [{ lat, lon, score }],   // approximate centre of each detection
//     features: FeatureCollection          // Point per detection + bbox polygon
//   }
export async function detect ({ modelId, bbox, zoom = 19 }) {
  const session = await getSession(modelId)
  const mosaic  = await fetchMosaic(bbox, zoom)

  // Run the model on every 640×640 sliding window.
  // Boxes are translated from window-pixel coords to mosaic-pixel coords so
  // that global NMS can compare boxes across overlapping windows.
  const allBoxes = []
  for (const tileWindow of iterWindows(mosaic.canvas, YOLO_SIZE)) {
    const inputTensor = new ort.Tensor('float32', tileWindow.tensor, [1, 3, YOLO_SIZE, YOLO_SIZE])
    const outputMap   = await session.run({ images: inputTensor })
    const rawOutput   = outputMap.output0 ?? Object.values(outputMap)[0]

    const windowBoxes = decodeDetections(rawOutput.data, rawOutput.dims, CONF_THRESHOLD)
    for (const box of windowBoxes) {
      allBoxes.push({
        x0: box.x0 + tileWindow.x,
        y0: box.y0 + tileWindow.y,
        x1: box.x1 + tileWindow.x,
        y1: box.y1 + tileWindow.y,
        score: box.score
      })
    }
  }

  // Global NMS removes duplicate detections from overlapping windows.
  const finalBoxes = nms(allBoxes, IOU_THRESHOLD)

  // Convert each surviving box to geo coordinates and build GeoJSON features.
  const detections = []
  const features   = []
  for (const box of finalBoxes) {
    const centerPixelX = (box.x0 + box.x1) / 2
    const centerPixelY = (box.y0 + box.y1) / 2
    const [lat, lon]   = pixelToLatLon(centerPixelX, centerPixelY, mosaic)
    const roundedScore = Math.round(box.score * 100) / 100

    detections.push({ lat, lon, score: roundedScore })

    // Bounding box corners → geo coordinates for the polygon outline on the map
    const [northWestLat, northWestLon] = pixelToLatLon(box.x0, box.y0, mosaic)
    const [southEastLat, southEastLon] = pixelToLatLon(box.x1, box.y1, mosaic)

    features.push({
      type: 'Feature',
      geometry: {
        type: 'Polygon',
        coordinates: [[
          [northWestLon, northWestLat],
          [southEastLon, northWestLat],
          [southEastLon, southEastLat],
          [northWestLon, southEastLat],
          [northWestLon, northWestLat]  // closed ring
        ]]
      },
      properties: { score: box.score, center_lat: lat, center_lon: lon, kind: 'bbox' }
    })
    features.push({
      type: 'Feature',
      geometry: { type: 'Point', coordinates: [lon, lat] },
      properties: { score: box.score, kind: 'center' }
    })
  }

  return {
    model:    modelId,
    count:    finalBoxes.length,
    detections,
    features: { type: 'FeatureCollection', features }
  }
}
