# Aperçu

Le frontend de **geo-ml** est une SPA [React](https://react.dev/) + [MapLibre](https://maplibre.org/) servie par [Vite](https://vite.dev/), sans backend. La détection s'effectue entièrement dans le navigateur via **ONNX Runtime Web**.

## Structure des fichiers

<img src="/guide/frontend_structure.png" style="display:block;margin:1.5rem auto;width:100%;height:auto;">

## Layout

<img src="/guide/layout.png" style="display:block;margin:1.5rem auto;width:100%;height:auto;">

## Config

`config.js` contient toutes les constantes. Elles sont exportées et lues directement par les composants

| Constante | Contenu | Consommateurs |
| --- | --- | --- |
| `BASEMAPS` | 5 fonds de carte : Esri Satellite, OSM Streets, CARTO Light, CARTO Dark, Sentinel-2 Cloudless | `BasemapSwitcher`, `Map` |
| `CATALOG_GROUPS` | 5 groupes ordonnés : Administrative, Transport, Outdoor, Infrastructure, Copernicus | `CatalogPanel` |
| `CATALOG_LAYERS` | 14 couches géographiques publiques (WMTS + WMS, aucune clé API) | `CatalogPanel`, `App` |
| `DRAW_TOOLS` | 2 outils : polygone (`Lasso`), cercle (`Circle`) | `DrawToolbar` |
| `DISPLAY_OPTIONS` | 3 flags : flèche nord, barre d'échelle, coordonnées | `MapSettings` |
| `DEFAULT_DISPLAY_SETTINGS` | `{ northArrow: true, scale: true, coords: true }` | état initial de `Map` |
| `MODEL_COLORS` | Couleurs `fill` / `outline` / `fillOpacity` par modèle | `Map` (source `detections`) |
| `MODELS` | 2 modèles : `buildings`, `pools` - `id`, icône, label, description | `Sidebar`, `ModelPanel` |
| `RUN_CONDITIONS` | `{ minZoom: 18, requiredBasemap: 'satellite', hints }` | `ModelPanel` (bouton Run) |
| `MAP_DEFAULTS` | `{ center: [2.21, 46.23], zoom: 5 }` - vue initiale centrée sur la France | `Map`, `App` |
| `GEOCODER` | `{ url: nominatim.openstreetmap.org/search, limit: 5 }` | `TopBar` |

:::tip Ajouter un modèle de détection
Ajouter un objet à `MODELS` et une entrée à `MODEL_COLORS` dans `config.js` :

```js
// Dans MODELS
{ id: 'parking', icon: ParkingCircle, label: 'Parking Detection', description: '...' }

// Dans MODEL_COLORS
parking: { fill: '#8b5cf6', outline: '#7c3aed', fillOpacity: 0.30 }
```
:::

:::tip Ajouter une couche au catalogue
Ajouter un objet à `CATALOG_LAYERS` dans `config.js` :

```js
{
  id: 'ndvi',
  group: 'Copernicus',          // doit exister dans CATALOG_GROUPS
  icon: Sprout,                 // icône lucide-react
  label: 'Indice de végétation NDVI',
  description: 'Couverture végétale · Terrascope',
  tiles: ['https://.../{z}/{x}/{y}.png'],   // WMTS
  // ou pour WMS :
  tiles: ['https://...?BBOX={bbox-epsg-3857}&...'],
  attribution: '© Terrascope'
}
```
:::
