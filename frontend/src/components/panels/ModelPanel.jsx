import { useState } from 'react'
import { ChevronUp, ChevronDown, Play, Check } from 'lucide-react'
import LeftPane from '../layout/LeftPane.jsx'
import { MODELS, RUN_CONDITIONS } from '../../config.js'

// Collapsible section block — title + icon header, body with stat + hint.
function Section({ title, icon: Icon, value, hint, defaultOpen = true }) {
  const [open, setOpen] = useState(defaultOpen)
  return (
    <div className="panel-section">
      <button className="section-header" onClick={() => setOpen((v) => !v)}>
        <span className="section-title-wrap">
          <Icon size={13} strokeWidth={1.5} />
          <span>{title}</span>
        </span>
        {open ? <ChevronUp size={13} /> : <ChevronDown size={13} />}
      </button>
      {open && (
        <div className="section-body">
          {value && <p className="stat-value">{value}</p>}
          {hint && <p className="stat-hint">{hint}</p>}
        </div>
      )}
    </div>
  )
}

// Run-detection button — enabled only when the map state satisfies
// RUN_CONDITIONS (zoom level + active basemap).
function RunButton({ zoom, basemap }) {
  const [status, setStatus] = useState('idle') // 'idle' | 'running' | 'done'
  const { minZoom, requiredBasemap, hints } = RUN_CONDITIONS
  const canRun = zoom >= minZoom && basemap === requiredBasemap

  const hint = !canRun
    ? basemap !== requiredBasemap
      ? hints.basemap
      : hints.zoom(zoom, minZoom)
    : null

  function handleRun() {
    if (!canRun || status === 'running') return
    setStatus('running')
    setTimeout(() => setStatus('done'), 2500)
  }

  return (
    <div className="run-detection-wrap">
      <button
        className={`run-detection-btn${status === 'running' ? ' running' : ''}${status === 'done' ? ' done' : ''}`}
        disabled={!canRun || status === 'running'}
        onClick={handleRun}
      >
        {status === 'running' && <span className="run-spinner" />}
        {status === 'done'    && <Check size={12} />}
        {status === 'idle'    && <Play size={12} />}
        {status === 'running' ? 'Running…' : status === 'done' ? 'Done' : 'Run detection'}
      </button>
      {hint && <p className="run-hint">{hint}</p>}
    </div>
  )
}

// Data-driven model panel — renders a section per entry in the
// model's config.sections array, plus a single run button.
function ModelPanel({ modelId, onClose, zoom = 5, basemap = 'satellite' }) {
  const model = MODELS.find((m) => m.id === modelId)
  if (!model) return null

  return (
    <LeftPane title={model.label} onClose={onClose}>
      {model.sections.map((section, i) => (
        <Section
          key={i}
          title={section.title}
          icon={section.icon}
          value={section.value}
          hint={section.hint}
          defaultOpen={section.defaultOpen !== false}
        />
      ))}
      <RunButton zoom={zoom} basemap={basemap} />
    </LeftPane>
  )
}

export default ModelPanel
