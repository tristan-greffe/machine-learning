import { useEffect, useRef, useState, forwardRef, useImperativeHandle } from 'react'
import maplibregl from 'maplibre-gl'
import 'maplibre-gl/dist/maplibre-gl.css'
import BasemapSwitcher, { BASEMAPS } from './BasemapSwitcher.jsx'

// forwardRef lets App.jsx call map methods (e.g. flyTo) via a ref
const Map = forwardRef(function Map(props, ref) {
  const mapContainer = useRef(null)
  const map          = useRef(null)
  const [coords, setCoords]       = useState(null)
  const [showCoords, setShowCoords] = useState(true)  // toggle coords visibility
  const [basemap, setBasemap]     = useState('satellite')

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

    // Scale bar — metric units, bottom-right
    map.current.addControl(new maplibregl.ScaleControl({ unit: 'metric' }), 'bottom-right')

    // Live coordinates on mouse move
    map.current.on('mousemove', (e) => {
      setCoords({
        lat: e.lngLat.lat.toFixed(5),
        lng: e.lngLat.lng.toFixed(5)
      })
    })

    map.current.on('mouseout', () => setCoords(null))

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

  return (
    <div className="map-wrapper">
      <div ref={mapContainer} className="map-container" />

      <BasemapSwitcher current={basemap} onSelect={handleBasemapSelect} />

      {/* Coordinates — clicking toggles visibility, scale bar adjusts below */}
      {coords && (
        <div
          className={`map-coords ${showCoords ? '' : 'coords-hidden'}`}
          onClick={() => setShowCoords((v) => !v)}
          title={showCoords ? 'Hide coordinates' : 'Show coordinates'}
        >
          {showCoords
            ? `Lat: ${coords.lat} · Lng: ${coords.lng}`
            : '···'
          }
        </div>
      )}
    </div>
  )
})

export default Map
