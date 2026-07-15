# Overview

The **geo-ml** frontend is a [React](https://react.dev/) + [MapLibre](https://maplibre.org/) SPA served by [Vite](https://vite.dev/), with no backend. Detection runs entirely in the browser via **ONNX Runtime Web**.

## File structure

<img src="/guide/frontend_structure.png" style="display:block;margin:1.5rem auto;width:100%;height:auto;">

## Layout

<img src="/guide/layout.png" style="display:block;margin:1.5rem auto;width:100%;height:auto;">

## Config

`config.js` contains all constants. They are exported and read directly by components.

| Constant | Content | Consumers |
| --- | --- | --- |
| `BASEMAPS` | 5 basemaps: Esri Satellite, OSM Streets, CARTO Light, CARTO Dark, Sentinel-2 Cloudless | `BasemapSwitcher`, `Map` |
| `CATALOG_GROUPS` | 5 ordered groups: Administrative, Transport, Outdoor, Infrastructure, Copernicus | `CatalogPanel` |
| `CATALOG_LAYERS` | 14 public geographic layers (WMTS + WMS, no API key) | `CatalogPanel`, `App` |
| `DRAW_TOOLS` | 2 tools: polygon (`Lasso`), circle (`Circle`) | `DrawToolbar` |
| `DISPLAY_OPTIONS` | 3 flags: north arrow, scale bar, coordinates | `MapSettings` |
| `DEFAULT_DISPLAY_SETTINGS` | `{ northArrow: true, scale: true, coords: true }` | `Map` initial state |
| `MODEL_COLORS` | `fill` / `outline` / `fillOpacity` colours per model | `Map` (`detections` source) |
| `MODELS` | 2 models: `buildings`, `pools` - `id`, icon, label, description | `Sidebar`, `ModelPanel` |
| `RUN_CONDITIONS` | `{ minZoom: 18, requiredBasemap: 'satellite', hints }` | `ModelPanel` (Run button) |
| `MAP_DEFAULTS` | `{ center: [2.21, 46.23], zoom: 5 }` - initial view centred on France | `Map`, `App` |
| `GEOCODER` | `{ url: nominatim.openstreetmap.org/search, limit: 5 }` | `TopBar` |

:::tip Add a detection model
Add an object to `MODELS` and an entry to `MODEL_COLORS` in `config.js`:

```js
// In MODELS
{ id: 'parking', icon: ParkingCircle, label: 'Parking Detection', description: '...' }

// In MODEL_COLORS
parking: { fill: '#8b5cf6', outline: '#7c3aed', fillOpacity: 0.30 }
```
:::

:::tip Add a catalog layer
Add an object to `CATALOG_LAYERS` in `config.js`:

```js
{
  id: 'ndvi',
  group: 'Copernicus',          // must exist in CATALOG_GROUPS
  icon: Sprout,                 // lucide-react icon
  label: 'NDVI vegetation index',
  description: 'Vegetation cover · Terrascope',
  tiles: ['https://.../{z}/{x}/{y}.png'],   // WMTS
  // or for WMS:
  tiles: ['https://...?BBOX={bbox-epsg-3857}&...'],
  attribution: '© Terrascope'
}
```
:::
