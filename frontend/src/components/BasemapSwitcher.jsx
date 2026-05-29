import { useState } from 'react'
import { Layers } from 'lucide-react'

// Available basemaps — tiles + thumbnail (real tile at zoom 5 over France)
export const BASEMAPS = [
  {
    id: 'satellite',
    label: 'Satellite',
    tiles: ['https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}'],
    thumbnail: 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/5/11/16'
  },
  {
    id: 'streets',
    label: 'Streets',
    tiles: ['https://tile.openstreetmap.org/{z}/{x}/{y}.png'],
    thumbnail: 'https://tile.openstreetmap.org/5/16/11.png'
  },
  {
    id: 'light',
    label: 'Light',
    tiles: ['https://a.basemaps.cartocdn.com/light_all/{z}/{x}/{y}.png'],
    thumbnail: 'https://a.basemaps.cartocdn.com/light_all/5/16/11.png'
  },
  {
    id: 'dark',
    label: 'Dark',
    tiles: ['https://a.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}.png'],
    thumbnail: 'https://a.basemaps.cartocdn.com/dark_all/5/16/11.png'
  }
]

function BasemapSwitcher({ current, onSelect }) {
  const [open, setOpen] = useState(false)

  function handleSelect(id) {
    onSelect(id)
    setOpen(false)
  }

  return (
    <div className="basemap-switcher">
      {/* Toggle button — positioned below zoom controls */}
      <button
        className={`basemap-toggle ${open ? 'active' : ''}`}
        onClick={() => setOpen((v) => !v)}
        title="Change basemap"
      >
        <Layers size={18} strokeWidth={1.5} />
      </button>

      {/* Basemap selection panel */}
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
