// Slice a mosaic canvas into YOLO input windows (640×640) and convert each
// into a CHW float32 tensor normalised to [0, 1] — the exact format expected
// by the YOLOv8 models trained on zoom-18 aerial imagery.

export const YOLO_SIZE = 640

// Convert an RGBA ImageData (HWC uint8) to a Float32Array in CHW layout [0, 1].
// Output shape: [3 × height × width]  (R plane, then G plane, then B plane).
function imageDataToTensor (imageData) {
  const { data: pixels, width, height } = imageData
  const pixelCount  = width * height
  const channelData = new Float32Array(3 * pixelCount)

  for (let pixelIndex = 0; pixelIndex < pixelCount; pixelIndex++) {
    channelData[pixelIndex]                  = pixels[pixelIndex * 4]     / 255  // R
    channelData[pixelCount + pixelIndex]     = pixels[pixelIndex * 4 + 1] / 255  // G
    channelData[2 * pixelCount + pixelIndex] = pixels[pixelIndex * 4 + 2] / 255  // B
  }
  return channelData
}

// Compute the list of start positions for sliding windows along one axis.
// The last window is shifted back to avoid going out of bounds (causing overlap
// rather than a truncated window), so the whole axis is always fully covered.
function computeWindowStarts (totalLength, windowSize, stride) {
  if (totalLength <= windowSize) return [0]

  const starts = []
  for (let start = 0; start + windowSize <= totalLength; start += stride) {
    starts.push(start)
  }
  // Ensure the final window reaches the very end of the axis
  const lastStart = totalLength - windowSize
  if (starts[starts.length - 1] !== lastStart) starts.push(lastStart)
  return starts
}

// Iterate over 640×640 sliding windows of a canvas.
// Each yielded object contains { x, y, size, tensor } where (x, y) is the
// top-left corner of the window in canvas-pixel coordinates.
// The 20% overlap lets global NMS clean up detections that straddle a boundary.
export function* iterWindows (canvas, windowSize = YOLO_SIZE, overlap = 0.2) {
  const canvasCtx    = canvas.getContext('2d')
  const canvasWidth  = canvas.width
  const canvasHeight = canvas.height
  const stride       = Math.round(windowSize * (1 - overlap))

  const xStarts = computeWindowStarts(canvasWidth,  windowSize, stride)
  const yStarts = computeWindowStarts(canvasHeight, windowSize, stride)

  for (const topY of yStarts) {
    for (const leftX of xStarts) {
      const sliceWidth  = Math.min(windowSize, canvasWidth  - leftX)
      const sliceHeight = Math.min(windowSize, canvasHeight - topY)

      // When the canvas is smaller than a full window, copy onto a black
      // 640×640 canvas so the tensor is always the expected size.
      if (sliceWidth !== windowSize || sliceHeight !== windowSize) {
        const paddedCanvas  = document.createElement('canvas')
        paddedCanvas.width  = windowSize
        paddedCanvas.height = windowSize
        const paddedCtx     = paddedCanvas.getContext('2d')
        paddedCtx.fillStyle = '#000'
        paddedCtx.fillRect(0, 0, windowSize, windowSize)
        paddedCtx.drawImage(canvas, leftX, topY, sliceWidth, sliceHeight, 0, 0, sliceWidth, sliceHeight)
        const imageData = paddedCtx.getImageData(0, 0, windowSize, windowSize)
        yield { x: leftX, y: topY, size: windowSize, tensor: imageDataToTensor(imageData) }
      } else {
        const imageData = canvasCtx.getImageData(leftX, topY, windowSize, windowSize)
        yield { x: leftX, y: topY, size: windowSize, tensor: imageDataToTensor(imageData) }
      }
    }
  }
}
