// Parse raw YOLOv8 output and run Non-Maximum Suppression (NMS) in JavaScript.
//
// YOLOv8 exported with nms=False produces a tensor of shape [1, 4+nc, N]
// (N ≈ 8400 anchors for a 640×640 input). For a single class (nc=1) that is
// [1, 5, N] laid out channel-major:
//   ch0 = cx, ch1 = cy, ch2 = w, ch3 = h   (box centre + size in input pixels)
//   ch4 = class confidence score             (already sigmoid-ed by the model)

// Decode one window's raw output tensor into bounding boxes in window-pixel coords.
// Returns an array of { x0, y0, x1, y1, score, classIndex } for boxes above
// the confidence threshold.
export function decodeDetections (rawData, dims, confidenceThreshold = 0.25) {
  const classCount  = dims[1] - 4   // number of object classes (nc)
  const anchorCount = dims[2]       // number of candidate anchor boxes (N)
  const boxes = []

  for (let anchorIndex = 0; anchorIndex < anchorCount; anchorIndex++) {
    // Find the class with the highest confidence score for this anchor
    let bestScore      = 0
    let bestClassIndex = 0
    for (let classIndex = 0; classIndex < classCount; classIndex++) {
      const classScore = rawData[(4 + classIndex) * anchorCount + anchorIndex]
      if (classScore > bestScore) {
        bestScore      = classScore
        bestClassIndex = classIndex
      }
    }
    if (bestScore < confidenceThreshold) continue

    // Decode center-format (cx, cy, w, h) → corner-format (x0, y0, x1, y1)
    const centerX   = rawData[0 * anchorCount + anchorIndex]
    const centerY   = rawData[1 * anchorCount + anchorIndex]
    const boxWidth  = rawData[2 * anchorCount + anchorIndex]
    const boxHeight = rawData[3 * anchorCount + anchorIndex]

    boxes.push({
      x0: centerX - boxWidth  / 2,
      y0: centerY - boxHeight / 2,
      x1: centerX + boxWidth  / 2,
      y1: centerY + boxHeight / 2,
      score: bestScore,
      classIndex: bestClassIndex
    })
  }
  return boxes
}

// Intersection-over-Union between two axis-aligned bounding boxes.
// Returns a value in [0, 1]; 1 means perfect overlap, 0 means no overlap.
function computeIoU (boxA, boxB) {
  const intersectLeft   = Math.max(boxA.x0, boxB.x0)
  const intersectTop    = Math.max(boxA.y0, boxB.y0)
  const intersectRight  = Math.min(boxA.x1, boxB.x1)
  const intersectBottom = Math.min(boxA.y1, boxB.y1)

  const intersectWidth  = Math.max(0, intersectRight  - intersectLeft)
  const intersectHeight = Math.max(0, intersectBottom - intersectTop)
  const intersectionArea = intersectWidth * intersectHeight

  const areaA     = (boxA.x1 - boxA.x0) * (boxA.y1 - boxA.y0)
  const areaB     = (boxB.x1 - boxB.x0) * (boxB.y1 - boxB.y0)
  const unionArea = areaA + areaB - intersectionArea

  return intersectionArea / (unionArea + 1e-6)  // +1e-6 avoids division by zero
}

// Greedy Non-Maximum Suppression.
// Keeps the highest-scoring box, then suppresses any box that overlaps it by
// more than iouThreshold. Repeats until no boxes remain.
export function nms (boxes, iouThreshold = 0.45) {
  const sortedByScore = [...boxes].sort((a, b) => b.score - a.score)
  const suppressed    = new Array(sortedByScore.length).fill(false)
  const keptBoxes     = []

  for (let i = 0; i < sortedByScore.length; i++) {
    if (suppressed[i]) continue
    keptBoxes.push(sortedByScore[i])
    for (let j = i + 1; j < sortedByScore.length; j++) {
      if (suppressed[j]) continue
      if (computeIoU(sortedByScore[i], sortedByScore[j]) > iouThreshold) {
        suppressed[j] = true
      }
    }
  }
  return keptBoxes
}
