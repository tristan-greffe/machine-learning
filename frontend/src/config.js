import {
  Building2, Waves,
  Lasso, Circle,
  Landmark, Type, Train, Anchor, Bike, Navigation, Mountain, Snowflake,
  Zap, Droplets, Fuel, Radio,
  Sprout, Layers3
} from 'lucide-react'

// Basemaps
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
  },
  {
    id: 'sentinel2',
    label: 'Sentinel-2',
    tiles: ['https://tiles.maps.eox.at/wmts/1.0.0/s2cloudless-2023_3857/default/g/{z}/{y}/{x}.jpg'],
    thumbnail: 'https://tiles.maps.eox.at/wmts/1.0.0/s2cloudless-2023_3857/default/g/5/11/16.jpg',
    attribution: 'Sentinel-2 cloudless 2023 by EOX · Copernicus data'
  }
]

// Catalog layers
export const CATALOG_GROUPS = ['Administrative', 'Transport', 'Outdoor', 'Infrastructure', 'Copernicus']

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
  },

  // Copernicus - public services, no auth required
  {
    id: 'worldcover', group: 'Copernicus', icon: Sprout,
    label: 'ESA WorldCover 2021',
    description: 'Global 10 m land cover · Terrascope',
    tiles: [
      'https://services.terrascope.be/wmts/v2?' +
      'layer=WORLDCOVER_2021_MAP&style=default&tilematrixset=g' +
      '&Service=WMTS&Request=GetTile&Version=1.0.0&Format=image%2Fpng' +
      '&TileMatrix={z}&TileCol={x}&TileRow={y}'
    ],
    attribution: '© ESA WorldCover project · Terrascope'
  },
  {
    id: 'corine', group: 'Copernicus', icon: Layers3,
    label: 'Corine Land Cover 2018',
    description: 'European land cover · Copernicus Land Monitoring',
    tiles: [
      'https://image.discomap.eea.europa.eu/arcgis/services/Corine/CLC2018_WM/MapServer/WMSServer?' +
      'SERVICE=WMS&REQUEST=GetMap&VERSION=1.1.1&LAYERS=12&STYLES=' +
      '&FORMAT=image/png&TRANSPARENT=TRUE&SRS=EPSG:3857' +
      '&WIDTH=256&HEIGHT=256&BBOX={bbox-epsg-3857}'
    ],
    attribution: '© European Environment Agency · Copernicus Land Monitoring Service'
  }
]

// Draw tools
export const DRAW_TOOLS = [
  { id: 'polygon', icon: Lasso,  label: 'Draw polygon', hint: 'Double-click to finish' },
  { id: 'circle',  icon: Circle, label: 'Draw circle',  hint: 'Click center, click radius' }
]

// Display options
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

// Per-model map colours
export const MODEL_COLORS = {
  buildings: { fill: '#f97316', outline: '#ea580c', fillOpacity: 0.28 },
  pools:     { fill: '#0ea5e9', outline: '#0284c7', fillOpacity: 0.40 },
}

// Detection models (YOLOv8 object detectors)
// Each detector returns a count and the approximate location (bbox centre)
// of every object found in the visible area.
export const MODELS = [
  {
    id: 'buildings',
    icon: Building2,
    label: 'Building Detection',
    description: 'Detects buildings from aerial imagery and reports how many were found, with the approximate location of each.',
  },
  {
    id: 'pools',
    icon: Waves,
    label: 'Pool Detection',
    description: 'Detects swimming pools from aerial imagery and reports how many were found, with the approximate location of each.',
  }
]

// Run conditions
// Conditions a model must satisfy before its "Run detection" button
// becomes enabled.
export const RUN_CONDITIONS = {
  minZoom:         18,
  requiredBasemap: 'satellite',
  hints: {
    basemap: 'Switch to satellite view first',
    zoom:    (current, required) => `Zoom in more (level ${Math.floor(current)} / ${required} required)`
  }
}

// Geocoder
export const GEOCODER = {
  url:   'https://nominatim.openstreetmap.org/search',
  limit: 5
}

// Map defaults
export const MAP_DEFAULTS = {
  center: [2.2137, 46.2276],
  zoom:   5
}
