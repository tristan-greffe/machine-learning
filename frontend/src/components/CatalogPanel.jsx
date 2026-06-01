import { ChevronRight, Landmark, Type, Train, Anchor, Bike, Navigation, Mountain, Snowflake, Zap, Droplets, Fuel, Radio } from 'lucide-react'

// ── Layer catalogue ─────────────────────────────────────────────
export const CATALOG_LAYERS = [
  // Administrative
  {
    id: 'admin', group: 'Administrative', icon: Landmark,
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
    id: 'labels', group: 'Administrative', icon: Type,
    label: 'City labels',
    description: 'Place names overlay · CARTO',
    tiles: ['https://a.basemaps.cartocdn.com/light_only_labels/{z}/{x}/{y}.png'],
    attribution: '© CARTO © OpenStreetMap contributors'
  },

  // Transport
  {
    id: 'railways', group: 'Transport', icon: Train,
    label: 'Railways',
    description: 'Rail lines & stations · OpenRailwayMap',
    tiles: ['https://a.tiles.openrailwaymap.org/standard/{z}/{x}/{y}.png'],
    attribution: '© OpenRailwayMap © OpenStreetMap contributors'
  },
  {
    id: 'maritime', group: 'Transport', icon: Anchor,
    label: 'Marine navigation',
    description: 'Seamark buoys & marks · OpenSeaMap',
    tiles: ['https://tiles.openseamap.org/seamark/{z}/{x}/{y}.png'],
    attribution: '© OpenSeaMap contributors'
  },
  {
    id: 'cycling', group: 'Transport', icon: Bike,
    label: 'Cycling routes',
    description: 'Bike paths · Waymarked Trails',
    tiles: ['https://tile.waymarkedtrails.org/cycling/{z}/{x}/{y}.png'],
    attribution: '© Waymarked Trails'
  },

  // Outdoor
  {
    id: 'hiking', group: 'Outdoor', icon: Navigation,
    label: 'Hiking trails',
    description: 'Footpaths · Waymarked Trails',
    tiles: ['https://tile.waymarkedtrails.org/hiking/{z}/{x}/{y}.png'],
    attribution: '© Waymarked Trails'
  },
  {
    id: 'mtb', group: 'Outdoor', icon: Mountain,
    label: 'Mountain bike',
    description: 'MTB tracks · Waymarked Trails',
    tiles: ['https://tile.waymarkedtrails.org/mtb/{z}/{x}/{y}.png'],
    attribution: '© Waymarked Trails'
  },
  {
    id: 'slopes', group: 'Outdoor', icon: Snowflake,
    label: 'Ski slopes',
    description: 'Pistes · Waymarked Trails',
    tiles: ['https://tile.waymarkedtrails.org/slopes/{z}/{x}/{y}.png'],
    attribution: '© Waymarked Trails'
  },

  // Infrastructure
  {
    id: 'power', group: 'Infrastructure', icon: Zap,
    label: 'Power grid',
    description: 'Lines & substations · OpenInfraMap',
    tiles: ['https://tiles.openinframap.org/power/{z}/{x}/{y}.png'],
    attribution: '© OpenInfraMap'
  },
  {
    id: 'water', group: 'Infrastructure', icon: Droplets,
    label: 'Water network',
    description: 'Pipes & treatment plants · OpenInfraMap',
    tiles: ['https://tiles.openinframap.org/water/{z}/{x}/{y}.png'],
    attribution: '© OpenInfraMap'
  },
  {
    id: 'petroleum', group: 'Infrastructure', icon: Fuel,
    label: 'Petroleum',
    description: 'Refineries & pipelines · OpenInfraMap',
    tiles: ['https://tiles.openinframap.org/petroleum/{z}/{x}/{y}.png'],
    attribution: '© OpenInfraMap'
  },
  {
    id: 'telecoms', group: 'Infrastructure', icon: Radio,
    label: 'Telecoms',
    description: 'Towers & cables · OpenInfraMap',
    tiles: ['https://tiles.openinframap.org/telecoms/{z}/{x}/{y}.png'],
    attribution: '© OpenInfraMap'
  }
]

const GROUPS = ['Administrative', 'Transport', 'Outdoor', 'Infrastructure']

// ── Component ───────────────────────────────────────────────────
function CatalogPanel({ activeLayers, onToggle, onClose }) {
  return (
    <aside className="catalog-panel">
      {/* Collapse tab — sticks out to the LEFT into the map */}
      <button className="catalog-panel-tab" onClick={onClose} title="Hide catalog">
        <ChevronRight size={12} />
      </button>

      <div className="catalog-panel-inner">
        <p className="side-panel-title">Data Catalog</p>

        {GROUPS.map((group) => {
          const layers = CATALOG_LAYERS.filter((l) => l.group === group)
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
      </div>
    </aside>
  )
}

export default CatalogPanel
