import RightPane from '../layout/RightPane.jsx'
import { CATALOG_LAYERS, CATALOG_GROUPS } from '../../config.js'

// Toggle-list catalog of overlay tile layers, grouped by theme.
function CatalogPanel({ activeLayers, onToggle, onClose }) {
  return (
    <RightPane title="Data Catalog" onClose={onClose}>
      {CATALOG_GROUPS.map((group) => {
        const layers = CATALOG_LAYERS.filter((l) => l.group === group)
        if (layers.length === 0) return null
        return (
          <div key={group}>
            <p className="catalog-group-title">{group}</p>
            {layers.map(({ id, icon: Icon, label, description }) => (
              <div key={id} className="catalog-layer-row">
                <div className="catalog-layer-icon">
                  <Icon size={14} strokeWidth={1.5} />
                </div>
                <div className="catalog-layer-info">
                  <span className="catalog-layer-label">{label}</span>
                  <span className="catalog-layer-desc">{description}</span>
                </div>
                <label className="toggle-switch">
                  <input
                    type="checkbox"
                    checked={activeLayers.includes(id)}
                    onChange={() => onToggle(id)}
                  />
                  <span className="toggle-slider" />
                </label>
              </div>
            ))}
          </div>
        )
      })}
    </RightPane>
  )
}

export default CatalogPanel
