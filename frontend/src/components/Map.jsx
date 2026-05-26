import { useEffect, useRef } from 'react'
import maplibregl from 'maplibre-gl'
import 'maplibre-gl/dist/maplibre-gl.css'

function Map() {
  // useRef: points to the DOM <div> where MapLibre will attach
  const mapContainer = useRef(null)
  // useRef: stores the map instance without triggering re-renders
  const map = useRef(null)

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
      zoom: 14
    })

    // Add navigation controls (zoom +/- and compass)
    map.current.addControl(new maplibregl.NavigationControl(), 'top-right')

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
    </div>
  )
}

export default Map
