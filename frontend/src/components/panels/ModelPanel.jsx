import { useState, useEffect } from 'react'
import { Play, RotateCcw, MapPin, AlertTriangle, Loader } from 'lucide-react'
import LeftPane from '../layout/LeftPane.jsx'
import { MODELS, RUN_CONDITIONS, MODEL_COLORS } from '../../config.js'
import { isModelAvailable } from '../../inference/runtime.js'

function fmtGps(lat, lon) {
  const ns = lat >= 0 ? 'N' : 'S'
  const ew = lon >= 0 ? 'E' : 'W'
  return `${Math.abs(lat).toFixed(5)}° ${ns}, ${Math.abs(lon).toFixed(5)}° ${ew}`
}

// One detected object: index chip + approximate GPS location + fly-to.
function DetectionRow({ index, det, color, onFlyTo }) {
  return (
    <div className="detect-row">
      <span className="detect-row-num" style={{ background: color }}>{index}</span>
      <span className="detect-row-gps">{fmtGps(det.lat, det.lon)}</span>
      <button
        className="detect-row-flyto"
        title="Center map here"
        onClick={() => onFlyTo([det.lon, det.lat])}
      >
        <MapPin size={11} />
      </button>
    </div>
  )
}

// Results: count headline + scrollable list of approximate locations.
function ResultsView({ modelId, result, onFlyTo, onReset }) {
  const color = MODEL_COLORS[modelId]?.fill ?? '#888'
  const dets = [...result.detections]
    .sort((a, b) => b.score - a.score)
    .slice(0, 200)

  return (
    <>
      <div className="detect-count">
        <span className="detect-count-num">{result.count}</span>
        <span className="detect-count-label">
          {result.count > 1 ? 'objects detected' : 'object detected'}
        </span>
      </div>

      <p className="detect-list-title">Approximate locations</p>
      <div className="detect-list">
        {dets.map((det, i) => (
          <DetectionRow key={i} index={i + 1} det={det} color={color} onFlyTo={onFlyTo} />
        ))}
        {result.count > 200 && (
          <p className="detect-truncated">Showing top 200 of {result.count}</p>
        )}
        {result.count === 0 && (
          <p className="detect-truncated">Nothing found in the visible area.</p>
        )}
      </div>

      <div className="detect-footer">
        <button className="run-detection-btn" onClick={onReset}>
          <RotateCcw size={12} /> Run again
        </button>
      </div>
    </>
  )
}

// Idle/error view: description, model-availability check, run button.
function IdleView({ model, modelAvailable, zoom, basemap, onRun, error }) {
  const { minZoom, requiredBasemap, hints } = RUN_CONDITIONS
  const canRun = zoom >= minZoom && basemap === requiredBasemap && modelAvailable

  const hint = !modelAvailable ? null
    : basemap !== requiredBasemap ? hints.basemap
    : zoom < minZoom ? hints.zoom(zoom, minZoom)
    : null

  return (
    <>
      <div className="panel-section">
        <div className="section-body">
          <p className="stat-hint" style={{ fontStyle: 'normal', marginBottom: 8 }}>
            {model.description}
          </p>
          {modelAvailable === false && (
            <div className="detect-no-model">
              <AlertTriangle size={13} />
              <span>Model not trained yet. Run <code>train.py --model {model.id}</code>.</span>
            </div>
          )}
          {modelAvailable === null && <p className="stat-hint">Checking model…</p>}
        </div>
      </div>

      <div className="run-detection-wrap">
        <button className="run-detection-btn" disabled={!canRun} onClick={onRun}>
          <Play size={12} /> Run detection
        </button>
        {hint && <p className="run-hint">{hint}</p>}
        {error && <p className="run-hint" style={{ color: '#ef4444' }}>{error}</p>}
      </div>
    </>
  )
}

function ModelPanel({ modelId, onClose, zoom = 5, basemap = 'satellite', onRun, onFlyTo }) {
  const model = MODELS.find((m) => m.id === modelId)
  const [status, setStatus]             = useState('idle')
  const [result, setResult]             = useState(null)
  const [error, setError]               = useState(null)
  const [modelAvailable, setModelAvail] = useState(null)

  // Reset everything when the selected model changes - fixes results from
  // one model leaking into another's panel.
  useEffect(() => {
    setStatus('idle')
    setResult(null)
    setError(null)
    setModelAvail(null)
    isModelAvailable(modelId).then(setModelAvail)
  }, [modelId])

  async function handleRun() {
    setStatus('running')
    setError(null)
    try {
      const r = await onRun(modelId)
      setResult(r)
      setStatus('done')
    } catch (e) {
      setError(e?.message ?? String(e))
      setStatus('error')
    }
  }

  if (!model) return null

  return (
    <LeftPane title={model.label} onClose={onClose}>
      {status === 'running' && (
        <div className="detect-running">
          <Loader size={18} className="detect-spinner" />
          <span>Running detection…</span>
        </div>
      )}

      {status === 'done' && result && (
        <ResultsView
          modelId={modelId}
          result={result}
          onFlyTo={onFlyTo}
          onReset={() => { setStatus('idle'); setResult(null) }}
        />
      )}

      {(status === 'idle' || status === 'error') && (
        <IdleView
          model={model}
          modelAvailable={modelAvailable}
          zoom={zoom}
          basemap={basemap}
          onRun={handleRun}
          error={status === 'error' ? error : null}
        />
      )}
    </LeftPane>
  )
}

export default ModelPanel
