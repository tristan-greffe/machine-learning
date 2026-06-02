import { useState } from 'react'
import { ChevronLeft, ChevronUp, ChevronDown, Hash, Ruler, Leaf, Building2, Waves, Play, Check } from 'lucide-react'

// ── Collapsible section ───────────────────────────────────────
function Section({ title, icon: Icon, children, defaultOpen = true }) {
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
      {open && <div className="section-body">{children}</div>}
    </div>
  )
}

// ── Run detection button ──────────────────────────────────────
// Active only when zoom ≥ 15 AND basemap === 'satellite'
function RunButton({ zoom, basemap }) {
  const [status, setStatus] = useState('idle') // 'idle' | 'running' | 'done'
  const canRun = zoom >= 15 && basemap === 'satellite'

  const hint = !canRun
    ? basemap !== 'satellite'
      ? 'Switch to satellite view first'
      : `Zoom in more (level ${Math.floor(zoom)} / 15 required)`
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

// ── Tree detection ────────────────────────────────────────────
function TreeContent({ zoom, basemap }) {
  return (
    <>
      <Section title="Tree count" icon={Hash}>
        <p className="stat-value">—</p>
        <p className="stat-hint">Run detection on the visible area to see results.</p>
      </Section>
      <Section title="Estimated area" icon={Ruler}>
        <p className="stat-value">—</p>
        <p className="stat-hint">Total canopy coverage will appear here.</p>
      </Section>
      <Section title="Tree type" icon={Leaf} defaultOpen={false}>
        <p className="stat-hint">Species breakdown will appear here.</p>
      </Section>
      <RunButton zoom={zoom} basemap={basemap} />
    </>
  )
}

// ── Building detection ────────────────────────────────────────
function BuildingContent({ zoom, basemap }) {
  return (
    <>
      <Section title="Building count" icon={Hash}>
        <p className="stat-value">—</p>
        <p className="stat-hint">Run detection to count buildings in the visible area.</p>
      </Section>
      <Section title="Footprint area" icon={Ruler}>
        <p className="stat-value">—</p>
        <p className="stat-hint">Total building footprint will appear here.</p>
      </Section>
      <Section title="Building type" icon={Building2} defaultOpen={false}>
        <p className="stat-hint">Residential / commercial breakdown will appear here.</p>
      </Section>
      <RunButton zoom={zoom} basemap={basemap} />
    </>
  )
}

// ── Pool detection ────────────────────────────────────────────
function PoolContent({ zoom, basemap }) {
  return (
    <>
      <Section title="Pool count" icon={Hash}>
        <p className="stat-value">—</p>
        <p className="stat-hint">Run detection to count pools in the visible area.</p>
      </Section>
      <Section title="Estimated area" icon={Ruler}>
        <p className="stat-value">—</p>
        <p className="stat-hint">Total water surface will appear here.</p>
      </Section>
      <Section title="Pool shape" icon={Waves} defaultOpen={false}>
        <p className="stat-hint">Rectangular / freeform breakdown will appear here.</p>
      </Section>
      <RunButton zoom={zoom} basemap={basemap} />
    </>
  )
}

// ── Content registry ──────────────────────────────────────────
const CONTENT = {
  trees:     { title: 'Tree Detection',     Component: TreeContent     },
  buildings: { title: 'Building Detection', Component: BuildingContent },
  pools:     { title: 'Pool Detection',     Component: PoolContent     }
}

// ── Side panel ────────────────────────────────────────────────
function SidePanel({ modelId, onClose, zoom = 5, basemap = 'satellite' }) {
  const entry = CONTENT[modelId]
  if (!entry) return null
  const { title, Component } = entry

  return (
    <aside className="side-panel">
      <div className="side-panel-inner">
        <p className="side-panel-title">{title}</p>
        <Component zoom={zoom} basemap={basemap} />
      </div>

      {/* Collapse tab — sticks out to the right */}
      <button className="side-panel-tab" onClick={onClose} title="Hide panel">
        <ChevronLeft size={12} />
      </button>
    </aside>
  )
}

export default SidePanel
