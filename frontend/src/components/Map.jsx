import { useEffect, useRef, useState, forwardRef, useImperativeHandle } from 'react'
import maplibregl from 'maplibre-gl'
import 'maplibre-gl/dist/maplibre-gl.css'
import BasemapSwitcher, { BASEMAPS } from './BasemapSwitcher.jsx'

// forwardRef lets App.jsx call map methods (e.g. flyTo) via a ref
const Map = forwardRef(function Map(props, ref) {
  // useRef: points to the DOM <div> where MapLibre will attach
  const mapContainer = useRef(null)
  // useRef: stores the map instance without triggering re-renders
  const map = useRef(null)
  // useState: current mouse coordinates (updated on every mousemove)
  const [coords, setCoords] = useState(null)
  // useState: currently active basemap id
  const [basemap, setBasemap] = useState('satellite')

  // Expose flyTo so parent components can move the map
  useImperativeHandle(ref, () => ({
    flyTo: (center, zoom = 14) => {
      map.current?.flyTo({ center, zoom, duration: 1500 })
    }
  }))

  useEffect(() => {
    // Prevent double initialization (React StrictMode mounts twice in dev)
    if (map.current) return

    map.current = new maplibregl.Map({
      container: mapContainer.current, // target <div>
      style: {
        version: 8,
        sources: {
          'basemap': {
            type: 'raster',
            tiles: BASEMAPS[0].tiles, // satellite by default
            tileSize: 256,
            attribution: 'Tiles © Esri'
          }
        },
        layers: [
          {
            id: 'basemap-layer',
            type: 'raster',
            source: 'basemap'
          }
        ]
      },
      center: [2.2137, 46.2276], // default center: France [lng, lat]
      zoom: 5,
      renderWorldCopies: false  // prevent infinite world repetition on zoom out
    })

    // Add navigation controls (zoom +/- and compass)
    map.current.addControl(new maplibregl.NavigationControl(), 'top-right')

    // Update coordinates on mouse move — e.lngLat is provided by MapLibre
    map.current.on('mousemove', (e) => {
      setCoords({
        lat: e.lngLat.lat.toFixed(5),
        lng: e.lngLat.lng.toFixed(5)
      })
    })

    // Clear coordinates when mouse leaves the map
    map.current.on('mouseout', () => setCoords(null))

    // Cleanup: destroy map instance when component unmounts
    return () => {
      map.current?.remove()
      map.current = null
    }
  }, []) // [] = run once on mount

  // Change basemap tiles when user selects a new one
  function handleBasemapSelect(id) {
    const selected = BASEMAPS.find((bm) => bm.id === id)
    if (!selected || !map.current) return

    // MapLibre allows updating a source's tiles on the fly
    map.current.getSource('basemap').setTiles(selected.tiles)
    setBasemap(id)
  }

  return (
    <div className="map-wrapper">
      {/* MapLibre fills this div with a WebGL canvas */}
      <div ref={mapContainer} className="map-container" />

      {/* Basemap switcher — positioned below zoom controls (top-right) */}
      <BasemapSwitcher current={basemap} onSelect={handleBasemapSelect} />

      {/* Live coordinates display — bottom left */}
      {coords && (
        <div className="map-coords">
          Lat: {coords.lat} &nbsp;·&nbsp; Lng: {coords.lng}
        </div>
      )}
    </div>
  )
})

export default Map
