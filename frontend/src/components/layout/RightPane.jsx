import { ChevronRight } from 'lucide-react'

// Generic right-side pane - collapse tab sticks out to the left.
function RightPane({ title, children, onClose }) {
  return (
    <aside className="right-pane">
      {onClose && (
        <button className="right-pane-tab" onClick={onClose} title="Hide panel">
          <ChevronRight size={12} />
        </button>
      )}

      <div className="right-pane-inner">
        {title && <p className="pane-title">{title}</p>}
        {children}
      </div>
    </aside>
  )
}

export default RightPane
