import { Lasso, Circle } from 'lucide-react'

const TOOLS = [
  { id: 'polygon', icon: Lasso,  label: 'Draw polygon',                hint: 'Double-click to finish' },
  { id: 'circle',  icon: Circle, label: 'Draw circle',                 hint: 'Click center, click radius' }
]

// Draw toolbar — inline to the left of the ruler button
function DrawToolbar({ drawMode, onSetMode }) {
  return (
    <div className="draw-toolbar">
      {TOOLS.map(({ id, icon: Icon, label, hint }) => (
        <div key={id} className="draw-btn-wrap">
          <button
            className={`draw-btn ${drawMode === id ? 'active' : ''}`}
            onClick={() => onSetMode(drawMode === id ? null : id)}
          >
            <Icon size={16} strokeWidth={1.5} />
          </button>
          {/* Styled tooltip above the button */}
          <span className="draw-btn-tooltip">
            {label}<br /><span className="draw-btn-hint">{hint}</span>
          </span>
        </div>
      ))}
    </div>
  )
}

export default DrawToolbar
