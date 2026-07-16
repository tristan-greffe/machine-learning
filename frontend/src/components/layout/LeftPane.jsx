import { ChevronLeft } from 'lucide-react'

// Generic left-side pane - collapse tab sticks out to the right.
function LeftPane({ title, children, onClose }) {
  return (
    <aside className="left-pane">
      <div className="left-pane-inner">
        {title && <p className="pane-title">{title}</p>}
        {children}
      </div>

      {onClose && (
        <button className="left-pane-tab" onClick={onClose} title="Hide panel">
          <ChevronLeft size={12} />
        </button>
      )}
    </aside>
  )
}

export default LeftPane
