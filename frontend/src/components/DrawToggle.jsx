import { Ruler } from 'lucide-react'
import DrawToolbar from './DrawToolbar.jsx'

// Ruler button + inline tool buttons (appear to its left when active)
function DrawToggle({ active, onToggle, drawMode, onSetMode }) {
  return (
    <div className="draw-toggle-wrap">
      {/* Tool buttons slide in to the left of the ruler */}
      {active && <DrawToolbar drawMode={drawMode} onSetMode={onSetMode} />}

      {/* Ruler toggle — always visible */}
      <button
        className={`draw-toggle-btn ${active ? 'active' : ''}`}
        onClick={onToggle}
      >
        <Ruler size={18} strokeWidth={1.5} />
      </button>

      {!active && <span className="draw-toggle-tooltip">Draw tools</span>}
    </div>
  )
}

export default DrawToggle
