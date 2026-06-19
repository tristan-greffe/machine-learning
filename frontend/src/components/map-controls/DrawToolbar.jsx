import { DRAW_TOOLS } from '../../config.js'

// Draw toolbar — inline to the left of the ruler button.
function DrawToolbar({ drawMode, onSetMode }) {
  return (
    <div className="draw-toolbar">
      {DRAW_TOOLS.map(({ id, icon: Icon, label, hint }) => (
        <div key={id} className="draw-btn-wrap">
          <button
            className={`draw-btn ${drawMode === id ? 'active' : ''}`}
            onClick={() => onSetMode(drawMode === id ? null : id)}
          >
            <Icon size={16} strokeWidth={1.5} />
          </button>
          <span className="draw-btn-tooltip">
            {label}<br /><span className="draw-btn-hint">{hint}</span>
          </span>
        </div>
      ))}
    </div>
  )
}

export default DrawToolbar
