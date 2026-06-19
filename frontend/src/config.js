import {
  TreePine, Building2, Waves,
  Hash, Ruler, Leaf,
  Lasso, Circle,
  Landmark, Type, Train, Anchor, Bike, Navigation, Mountain, Snowflake,
  Zap, Droplets, Fuel, Radio
} from 'lucide-react'

// ── Basemaps
export const BASEMAPS = [
  {
    id: 'satellite',
    label: 'Satellite',
    tiles: ['https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}'],
    thumbnail: 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/5/11/16',
    attribution: 'Tiles © Esri'
  },
  {
    id: 'streets',
    label: 'Streets',
    tiles: ['https://tile.openstreetmap.org/{z}/{x}/{y}.png'],
    thumbnail: 'https://tile.openstreetmap.org/5/16/11.png',
    attribution: '© OpenStreetMap contributors'
  },
  {
    id: 'light',
    label: 'Light',
    tiles: ['https://a.basemaps.cartocdn.com/light_all/{z}/{x}/{y}.png'],
    thumbnail: 'https://a.basemaps.cartocdn.com/light_all/5/16/11.png',
    attribution: '© CARTO © OpenStreetMap contributors'
  },
  {
    id: 'dark',
    label: 'Dark',
    tiles: ['https://a.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}.png'],
    thumbnail: 'https://a.basemaps.cartocdn.com/dark_all/5/16/11.png',
    attribution: '© CARTO © OpenStreetMap contributors'
  }
]

// ── Catalog layers
export const CATALOG_GROUPS = ['Administrative', 'Transport', 'Outdoor', 'Infrastructure']

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

// ── Draw tools
export const DRAW_TOOLS = [
  { id: 'polygon', icon: Lasso,  label: 'Draw polygon', hint: 'Double-click to finish' },
  { id: 'circle',  icon: Circle, label: 'Draw circle',  hint: 'Click center, click radius' }
]

// ── Display options
export const DISPLAY_OPTIONS = [
  { key: 'northArrow', label: 'North arrow' },
  { key: 'scale',      label: 'Scale bar' },
  { key: 'coords',     label: 'Coordinates' }
]

export const DEFAULT_DISPLAY_SETTINGS = {
  northArrow: true,
  scale:      true,
  coords:     true
}

// ── Detection models
// Each model declares the sections shown inside its panel — keeps
// ModelPanel completely data-driven.
export const MODELS = [
  {
    id: 'trees',
    icon: TreePine,
    label: 'Tree Detection',
    description: 'Outlines individual tree crowns — count, area, type.',
    sections: [
      { title: 'Tree count',     icon: Hash,  value: '—', hint: 'Run detection on the visible area to see results.' },
      { title: 'Estimated area', icon: Ruler, value: '—', hint: 'Total canopy coverage will appear here.' },
      { title: 'Tree type',      icon: Leaf,  defaultOpen: false, hint: 'Species breakdown will appear here.' }
    ]
  },
  {
    id: 'buildings',
    icon: Building2,
    label: 'Building Detection',
    description: 'Outlines buildings — count, area, type.',
    sections: [
      { title: 'Building count', icon: Hash,       value: '—', hint: 'Run detection to count buildings in the visible area.' },
      { title: 'Footprint area', icon: Ruler,      value: '—', hint: 'Total building footprint will appear here.' },
      { title: 'Building type',  icon: Building2,  defaultOpen: false, hint: 'Residential / commercial breakdown will appear here.' }
    ]
  },
  {
    id: 'pools',
    icon: Waves,
    label: 'Pool Detection',
    description: 'Detects swimming pools from aerial imagery.',
    sections: [
      { title: 'Pool count',     icon: Hash,  value: '—', hint: 'Run detection to count pools in the visible area.' },
      { title: 'Estimated area', icon: Ruler, value: '—', hint: 'Total water surface will appear here.' },
      { title: 'Pool shape',     icon: Waves, defaultOpen: false, hint: 'Rectangular / freeform breakdown will appear here.' }
    ]
  }
]

// ── Run conditions
// Conditions a model must satisfy before its "Run detection" button
// becomes enabled.
export const RUN_CONDITIONS = {
  minZoom:         15,
  requiredBasemap: 'satellite',
  hints: {
    basemap: 'Switch to satellite view first',
    zoom:    (current, required) => `Zoom in more (level ${Math.floor(current)} / ${required} required)`
  }
}

// ── Map defaults
export const MAP_DEFAULTS = {
  center: [2.2137, 46.2276],
  zoom:   5
}
