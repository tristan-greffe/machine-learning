import * as ort from 'onnxruntime-web'

// We intentionally do NOT set ort.env.wasm.wasmPaths — Vite copies the
// onnxruntime-web WASM into the build assets, and the bundler rewrites
// the internal `new URL(...)` lookups to point at the hashed filename.
// Letting ort auto-resolve via import.meta.url keeps everything aligned.

const sessions = new Map()

// Returns true if the .onnx file exists
export async function isModelAvailable (modelId) {
  try {
    const modelUrl = `${import.meta.env.BASE_URL}models/${modelId}.onnx`
    const response = await fetch(modelUrl, { method: 'HEAD' })
    return response.ok
  } catch {
    return false
  }
}

// Lazy-loaded, cached InferenceSession per modelId.
// On first call the ONNX file is fetched and compiled; subsequent calls
// return the cached session instantly.
export async function getSession (modelId) {
  if (sessions.has(modelId)) return sessions.get(modelId)

  const modelUrl = `${import.meta.env.BASE_URL}models/${modelId}.onnx`
  const session = await ort.InferenceSession.create(modelUrl, {
    executionProviders: ['wasm'],
    graphOptimizationLevel: 'all'
  })
  sessions.set(modelId, session)
  return session
}

export { ort }
