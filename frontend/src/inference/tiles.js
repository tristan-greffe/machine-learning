// IGN WMTS tile downloader for in-browser inference.
// Same maths as model/src/tiles.py, ported to JS.

const IGN_WMTS_URL = (zoom, tileX, tileY) =>
  `https://data.geopf.fr/wmts?SERVICE=WMTS&REQUEST=GetTile&VERSION=1.0.0` +
  `&LAYER=ORTHOIMAGERY.ORTHOPHOTOS&STYLE=normal&FORMAT=image/jpeg` +
  `&TILEMATRIXSET=PM&TILEMATRIX=${zoom}&TILEROW=${tileY}&TILECOL=${tileX}`

export const TILE_SIZE = 256

// Convert WGS84 (lat, lon) to tile coordinates at a given zoom level.
// Uses the Web Mercator (EPSG:3857) projection formula.
export function latlonToTile(lat, lon, zoom) {
  const tileCount = 2 ** zoom
  const tileX     = Math.floor((lon + 180) / 360 * tileCount)
  const latRad    = lat * Math.PI / 180
  const tileY     = Math.floor(
    (1 - Math.log(Math.tan(latRad) + 1 / Math.cos(latRad)) / Math.PI) / 2 * tileCount
  )
  return [tileX, tileY]
}

// Convert tile coordinates back to WGS84 (lat, lon) at a given zoom level.
// Returns the coordinate of the tile's top-left corner.
export function tileToLatLon(tileX, tileY, zoom) {
  const tileCount = 2 ** zoom
  const lon = tileX / tileCount * 360 - 180
  const lat = Math.atan(Math.sinh(Math.PI * (1 - 2 * tileY / tileCount))) * 180 / Math.PI
  return [lat, lon]
}

// Convert a WGS84 bounding box [west, south, east, north] to tile index bounds
// { txMin, tyMin, txMax, tyMax } at the given zoom level.
export function bboxToTiles(bbox, zoom) {
  const [west, south, east, north] = bbox
  const [txMin, tyMax] = latlonToTile(south, west, zoom)
  const [txMax, tyMin] = latlonToTile(north, east, zoom)
  return { txMin, tyMin, txMax, tyMax }
}

// Load an image from a URL and resolve with the HTMLImageElement.
function loadImage(url) {
  return new Promise((resolve, reject) => {
    const img       = new Image()
    img.crossOrigin = 'anonymous'
    img.onload      = () => resolve(img)
    img.onerror     = reject
    img.src         = url
  })
}

// Fetch and stitch all IGN WMTS tiles that cover the given bbox into one canvas.
// Returns { canvas, width, height, txMin, tyMin, txMax, tyMax, zoom }.
export async function fetchMosaic(bbox, zoom) {
  const tileBounds                     = bboxToTiles(bbox, zoom)
  const { txMin, tyMin, txMax, tyMax } = tileBounds

  const columnCount  = txMax - txMin + 1
  const rowCount     = tyMax - tyMin + 1
  const mosaicWidth  = columnCount * TILE_SIZE
  const mosaicHeight = rowCount    * TILE_SIZE

  const mosaicCanvas  = document.createElement('canvas')
  mosaicCanvas.width  = mosaicWidth
  mosaicCanvas.height = mosaicHeight
  const mosaicCtx     = mosaicCanvas.getContext('2d')

  // Download all tiles in parallel and draw each at its correct position
  const tileDownloads = []
  for (let tileY = tyMin; tileY <= tyMax; tileY++) {
    for (let tileX = txMin; tileX <= txMax; tileX++) {
      tileDownloads.push((async () => {
        const tileImage = await loadImage(IGN_WMTS_URL(zoom, tileX, tileY))
        const drawX     = (tileX - txMin) * TILE_SIZE
        const drawY     = (tileY - tyMin) * TILE_SIZE
        mosaicCtx.drawImage(tileImage, drawX, drawY)
      })())
    }
  }
  await Promise.all(tileDownloads)

  return { canvas: mosaicCanvas, width: mosaicWidth, height: mosaicHeight, ...tileBounds, zoom }
}

// Convert a pixel position (pixelX, pixelY) inside the mosaic to WGS84 (lat, lon).
// Uses fractional tile coordinates to interpolate within a tile.
export function pixelToLatLon(pixelX, pixelY, mosaic) {
  const fractionalTileX = mosaic.txMin + pixelX / TILE_SIZE
  const fractionalTileY = mosaic.tyMin + pixelY / TILE_SIZE
  return tileToLatLon(fractionalTileX, fractionalTileY, mosaic.zoom)
}
