import { Globe } from 'lucide-react'

// Floating button below MapSettings — toggles 2D/3D globe projection
function GlobeToggle({ isGlobe, onToggle }) {
  return (
    <div className="globe-toggle-wrap">
      <button
        className={`globe-toggle-btn ${isGlobe ? 'active' : ''}`}
        onClick={onToggle}
      >
        <Globe size={18} strokeWidth={1.5} />
      </button>

      {/* Tooltip text changes with current mode */}
      <span className="globe-tooltip">
        {isGlobe ? 'Switch to 2D map' : 'Switch to 3D globe'}
      </span>
    </div>
  )
}

export default GlobeToggle
