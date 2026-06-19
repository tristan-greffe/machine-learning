import { useState } from 'react'
import { Layers } from 'lucide-react'
import { BASEMAPS } from '../../config.js'

function BasemapSwitcher({ current, onSelect }) {
  const [open, setOpen] = useState(false)

  function handleSelect(id) {
    onSelect(id)
    setOpen(false)
  }

  return (
    <div className="basemap-switcher">
      <button
        className={`basemap-toggle ${open ? 'active' : ''}`}
        onClick={() => setOpen((v) => !v)}
      >
        <Layers size={18} strokeWidth={1.5} />
      </button>

      {!open && (
        <span className="basemap-tooltip">
          Manage basemap layers
        </span>
      )}

      {open && (
        <div className="basemap-panel">
          <p className="basemap-panel-title">Basemap</p>
          <div className="basemap-grid">
            {BASEMAPS.map((bm) => (
              <button
                key={bm.id}
                className={`basemap-card ${current === bm.id ? 'active' : ''}`}
                onClick={() => handleSelect(bm.id)}
                title={bm.label}
              >
                <img
                  src={bm.thumbnail}
                  alt={bm.label}
                  className="basemap-thumb"
                />
                <span className="basemap-label">{bm.label}</span>
              </button>
            ))}
          </div>
        </div>
      )}
    </div>
  )
}

export default BasemapSwitcher
