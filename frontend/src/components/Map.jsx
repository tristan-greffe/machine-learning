import { useEffect, useRef, useState } from 'react'
import maplibregl from 'maplibre-gl'
import 'maplibre-gl/dist/maplibre-gl.css'

function Map() {
  // useRef: points to the DOM <div> where MapLibre will attach
  const mapContainer = useRef(null)
  // useRef: stores the map instance without triggering re-renders
  const map = useRef(null)
  // useState: current mouse coordinates (updated on every mousemove)
  const [coords, setCoords] = useState(null)

  useEffect(() => {
    // Prevent double initialization (React StrictMode mounts twice in dev)
    if (map.current) return

    map.current = new maplibregl.Map({
      container: mapContainer.current, // target <div>
      style: {
        version: 8,
        sources: {
          // ESRI satellite imagery (free, no API key required)
          'esri-satellite': {
            type: 'raster',
            tiles: [
              'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}'
            ],
            tileSize: 256,
            attribution: 'Tiles © Esri'
          }
        },
        layers: [
          {
            id: 'satellite',
            type: 'raster',
            source: 'esri-satellite'
          }
        ]
      },
      center: [2.3488, 48.8534], // default center: Paris [lng, lat]
      zoom: 14,
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

  return (
    <div className="map-wrapper">
      {/* MapLibre fills this div with a WebGL canvas */}
      <div ref={mapContainer} className="map-container" />

      {/* Live coordinates display — bottom right, like ARLAS */}
      {coords && (
        <div className="map-coords">
          Lat: {coords.lat} &nbsp;·&nbsp; Lng: {coords.lng}
        </div>
      )}
    </div>
  )
}

export default Map
