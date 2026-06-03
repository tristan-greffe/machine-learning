import { useEffect, useRef, useState, forwardRef, useImperativeHandle } from 'react'
import maplibregl from 'maplibre-gl'
import 'maplibre-gl/dist/maplibre-gl.css'
import BasemapSwitcher, { BASEMAPS } from './BasemapSwitcher.jsx'
import MapSettings from './MapSettings.jsx'
import northArrowSvg from '../assets/north-arrow.svg'

// forwardRef lets App.jsx call map methods (e.g. flyTo) via a ref
const Map = forwardRef(function Map(props, ref) {
  const mapContainer = useRef(null)
  const map          = useRef(null)
  const [coords, setCoords]   = useState(null)
  const [basemap, setBasemap] = useState('satellite')
  const [bearing, setBearing] = useState(0)   // map rotation in degrees

  // Visibility settings controlled by the gear panel
  const [mapSettings, setMapSettings] = useState({
    northArrow: true,
    scale:      true,
    coords:     true
  })

  // Expose flyTo so parent components can move the map
  useImperativeHandle(ref, () => ({
    flyTo: (center, zoom = 14) => {
      map.current?.flyTo({ center, zoom, duration: 1500 })
    }
  }))

  useEffect(() => {
    if (map.current) return

    map.current = new maplibregl.Map({
      container: mapContainer.current,
      style: {
        version: 8,
        sources: {
          'basemap': {
            type: 'raster',
            tiles: BASEMAPS[0].tiles,
            tileSize: 256,
            attribution: 'Tiles © Esri'
          }
        },
        layers: [{ id: 'basemap-layer', type: 'raster', source: 'basemap' }]
      },
      center: [2.2137, 46.2276],
      zoom: 5,
      renderWorldCopies: false
    })

    // Navigation controls (zoom +/- and compass)
    map.current.addControl(new maplibregl.NavigationControl(), 'top-right')

    // Scale bar — metric units, bottom-left
    map.current.addControl(new maplibregl.ScaleControl({ unit: 'metric' }), 'bottom-left')

    // Live coordinates on mouse move
    map.current.on('mousemove', (e) => {
      setCoords({
        lat: e.lngLat.lat.toFixed(5),
        lng: e.lngLat.lng.toFixed(5)
      })
    })

    map.current.on('mouseout', () => setCoords(null))

    // Track map rotation to rotate the north arrow accordingly
    map.current.on('rotate', () => setBearing(map.current.getBearing()))

    return () => {
      map.current?.remove()
      map.current = null
    }
  }, [])

  function handleBasemapSelect(id) {
    const selected = BASEMAPS.find((bm) => bm.id === id)
    if (!selected || !map.current) return
    map.current.getSource('basemap').setTiles(selected.tiles)
    setBasemap(id)
  }

  // Click on north arrow resets map rotation to north
  function handleResetNorth() {
    map.current?.rotateTo(0, { duration: 500 })
  }

  function handleSettingChange(key, value) {
    setMapSettings((prev) => ({ ...prev, [key]: value }))
  }

  return (
    // hide-scale class toggles the MapLibre scale control via CSS
    <div className={`map-wrapper${mapSettings.scale ? '' : ' hide-scale'}`}>
      <div ref={mapContainer} className="map-container" />

      <BasemapSwitcher current={basemap} onSelect={handleBasemapSelect} />
      <MapSettings settings={mapSettings} onChange={handleSettingChange} />

      {/* North arrow — top-left, rotates with map, click to reset north */}
      {mapSettings.northArrow && (
        <button
          className="north-arrow"
          onClick={handleResetNorth}
          title="Reset north"
        >
          <img
            src={northArrowSvg}
            alt="North arrow"
            style={{ transform: `rotate(${-bearing}deg)`, transition: 'transform 0.1s' }}
          />
        </button>
      )}

      {/* Coordinates — bottom-left, hidden via settings panel */}
      {mapSettings.coords && coords && (
        <div className="map-coords">
          {`Lat: ${coords.lat} · Lng: ${coords.lng}`}
        </div>
      )}
    </div>
  )
})

export default Map
