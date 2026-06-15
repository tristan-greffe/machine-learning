import { ChevronRight, Landmark, CloudRain, Train } from 'lucide-react'

export const CATALOG_LAYERS = [
  {
    id: 'admin',
    icon: Landmark,
    label: 'Administrative limits',
    description: 'Boundaries · IGN Géoportail',
    tiles: [
      'https://data.geopf.fr/wmts?SERVICE=WMTS&REQUEST=GetTile&VERSION=1.0.0' +
      '&LAYER=LIMITES_ADMINISTRATIVES_EXPRESS.LATEST&STYLE=normal&FORMAT=image/png' +
      '&TILEMATRIXSET=PM&TILEMATRIX={z}&TILEROW={y}&TILECOL={x}'
    ],
    attribution: '© IGN Géoportail'
  },
  {
    id: 'rain',
    icon: CloudRain,
    label: 'Rain radar',
    description: 'Live precipitation · RainViewer',
    tiles: null,  // fetched dynamically on activation
    attribution: '© RainViewer'
  },
  {
    id: 'railways',
    icon: Train,
    label: 'Railway network',
    description: 'Rail lines · OpenRailwayMap',
    tiles: ['https://a.tiles.openrailwaymap.org/standard/{z}/{x}/{y}.png'],
    attribution: '© OpenRailwayMap © OpenStreetMap'
  }
]

function CatalogPanel({ activeLayers, onToggle, onClose }) {
  return (
    <aside className="catalog-panel">
      {/* Close tab — sticks out to the LEFT */}
      <button className="catalog-panel-tab" onClick={onClose} title="Hide catalog">
        <ChevronRight size={12} />
      </button>

      <div className="catalog-panel-inner">
        <p className="side-panel-title">Data Catalog</p>

        <div className="catalog-layer-list">
          {CATALOG_LAYERS.map(({ id, icon: Icon, label, description }) => (
            <div key={id} className="catalog-layer-row">
              <div className="catalog-layer-icon">
                <Icon size={15} strokeWidth={1.5} />
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
      </div>
    </aside>
  )
}

export default CatalogPanel
