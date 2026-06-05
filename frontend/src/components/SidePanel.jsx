import { useState } from 'react'
import { ChevronLeft, ChevronUp, ChevronDown, Hash, Ruler, Leaf } from 'lucide-react'

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
        {open
          ? <ChevronUp size={13} />
          : <ChevronDown size={13} />
        }
      </button>
      {open && <div className="section-body">{children}</div>}
    </div>
  )
}

// ── Tree detection content ────────────────────────────────────
function TreeContent() {
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
    </>
  )
}

// ── Side panel ────────────────────────────────────────────────
const CONTENT = {
  trees: {
    title: 'Tree Detection',
    component: TreeContent
  }
}

function SidePanel({ modelId, onClose }) {
  const entry = CONTENT[modelId]
  if (!entry) return null
  const Content = entry.component

  return (
    <aside className="side-panel">
      {/* Scrollable content */}
      <div className="side-panel-inner">
        <p className="side-panel-title">{entry.title}</p>
        <Content />
      </div>

      {/* Collapse tab — sticks out to the right */}
      <button
        className="side-panel-tab"
        onClick={onClose}
        title="Hide panel"
      >
        <ChevronLeft size={12} />
      </button>
    </aside>
  )
}

export default SidePanel
