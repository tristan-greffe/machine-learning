import { useEffect, useRef, useState, forwardRef, useImperativeHandle } from 'react'
import maplibregl from 'maplibre-gl'
import 'maplibre-gl/dist/maplibre-gl.css'
import BasemapSwitcher, { BASEMAPS } from './BasemapSwitcher.jsx'
import MapSettings from './MapSettings.jsx'
import GlobeToggle from './GlobeToggle.jsx'
import DrawToolbar from './DrawToolbar.jsx'
import DrawToggle from './DrawToggle.jsx'
import northArrowSvg from '../assets/north-arrow.svg'

const EMPTY_FC = { type: 'FeatureCollection', features: [] }

// Approximate distance in km between two [lng, lat] points
function haversineKm([lng1, lat1], [lng2, lat2]) {
  const R = 6371
  const dLat = (lat2 - lat1) * Math.PI / 180
  const dLng = (lng2 - lng1) * Math.PI / 180
  const a = Math.sin(dLat / 2) ** 2 +
    Math.cos(lat1 * Math.PI / 180) * Math.cos(lat2 * Math.PI / 180) *
    Math.sin(dLng / 2) ** 2
  return R * 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a))
}

// Generate a GeoJSON Polygon approximating a circle
function makeCircleFeature([lng, lat], radiusKm, steps = 64) {
  const coords = Array.from({ length: steps }, (_, i) => {
    const angle = (i / steps) * 2 * Math.PI
    return [
      lng + (radiusKm / (111.32 * Math.cos(lat * Math.PI / 180))) * Math.sin(angle),
      lat + (radiusKm / 111.32) * Math.cos(angle)
    ]
  })
  coords.push(coords[0]) // close ring
  return { type: 'Feature', geometry: { type: 'Polygon', coordinates: [coords] }, properties: {} }
}

const Map = forwardRef(function Map({ onShapesChange }, ref) {
  const mapContainer = useRef(null)
  const map          = useRef(null)
  const [coords, setCoords]     = useState(null)
  const [basemap, setBasemap]   = useState('satellite')
  const [bearing, setBearing]   = useState(0)
  const [isGlobe, setIsGlobe]   = useState(false)
  const [mapSettings, setMapSettings] = useState({ northArrow: true, scale: true, coords: true })

  // Draw state
  const [showDrawToolbar, setShowDrawToolbar]   = useState(false) // toggled by ruler button
  const [drawMode, setDrawModeState]            = useState(null)  // 'polygon' | 'circle' | null
  const [drawnFeatures, setDrawnFeatures]       = useState([])
  const [pendingPoints, setPendingPointsState]  = useState([])

  // Refs so event handlers always read fresh values (no stale closures)
  const drawModeRef      = useRef(null)
  const pendingPointsRef = useRef([])
  const clickTimerRef    = useRef(null)

  function setDrawMode(mode) {
    drawModeRef.current = mode
    setDrawModeState(mode)
  }

  function setPendingPoints(pts) {
    pendingPointsRef.current = pts
    setPendingPointsState(pts)
  }

  // Expose methods to parent via ref
  useImperativeHandle(ref, () => ({
    flyTo: (center, zoom = 14) => map.current?.flyTo({ center, zoom, duration: 1500 }),
    clearShapes: () => {
      setDrawnFeatures([])
      setPendingPoints([])
      setDrawMode(null)
    }
  }))

  // Notify parent when shapes are added / all cleared
  useEffect(() => {
    onShapesChange?.(drawnFeatures.length > 0)
  }, [drawnFeatures, onShapesChange])

  // Sync drawn shapes to map source
  useEffect(() => {
    const src = map.current?.getSource('draw-shapes')
    if (src) src.setData({ type: 'FeatureCollection', features: drawnFeatures })
  }, [drawnFeatures])

  // Sync in-progress preview (pending points + connecting line)
  useEffect(() => {
    const src = map.current?.getSource('draw-preview')
    if (!src) return
    const features = []
    if (pendingPoints.length >= 2) {
      features.push({ type: 'Feature', geometry: { type: 'LineString', coordinates: pendingPoints } })
    }
    pendingPoints.forEach((pt) =>
      features.push({ type: 'Feature', geometry: { type: 'Point', coordinates: pt } })
    )
    src.setData({ type: 'FeatureCollection', features })
  }, [pendingPoints])

  // Update cursor when draw mode changes
  useEffect(() => {
    const canvas = map.current?.getCanvas()
    if (canvas) canvas.style.cursor = drawMode ? 'crosshair' : ''
  }, [drawMode])

  // ── Map initialisation ─────────────────────────────────────
  useEffect(() => {
    if (map.current) return

    const m = new maplibregl.Map({
      container: mapContainer.current,
      style: {
        version: 8,
        sources: {
          'basemap': { type: 'raster', tiles: BASEMAPS[0].tiles, tileSize: 256, attribution: 'Tiles © Esri' }
        },
        layers: [
          { id: 'background',    type: 'background', paint: { 'background-color': '#fafafa' } },
          { id: 'basemap-layer', type: 'raster',     source: 'basemap' }
        ]
      },
      center: [2.2137, 46.2276],
      zoom: 5,
      renderWorldCopies: false
    })
    map.current = m

    m.addControl(new maplibregl.NavigationControl(), 'top-right')
    m.addControl(new maplibregl.ScaleControl({ unit: 'metric' }), 'bottom-left')
    m.on('mousemove', (e) => setCoords({ lat: e.lngLat.lat.toFixed(5), lng: e.lngLat.lng.toFixed(5) }))
    m.on('mouseout', () => setCoords(null))
    m.on('rotate', () => setBearing(m.getBearing()))

    // Add draw sources and layers after style loads
    m.on('load', () => {
      m.addSource('draw-shapes',  { type: 'geojson', data: EMPTY_FC })
      m.addSource('draw-preview', { type: 'geojson', data: EMPTY_FC })

      // Completed shapes
      m.addLayer({ id: 'draw-fill',    type: 'fill', source: 'draw-shapes',
        paint: { 'fill-color': '#0891b2', 'fill-opacity': 0.15 } })
      m.addLayer({ id: 'draw-outline', type: 'line', source: 'draw-shapes',
        paint: { 'line-color': '#0891b2', 'line-width': 2 } })

      // In-progress preview — dashed line + vertex dots
      m.addLayer({ id: 'draw-preview-line', type: 'line', source: 'draw-preview',
        filter: ['==', '$type', 'LineString'],
        paint: { 'line-color': '#0891b2', 'line-width': 2, 'line-dasharray': [3, 2] } })
      m.addLayer({ id: 'draw-dots', type: 'circle', source: 'draw-preview',
        filter: ['==', '$type', 'Point'],
        paint: { 'circle-radius': 4, 'circle-color': '#fff',
          'circle-stroke-color': '#0891b2', 'circle-stroke-width': 2 } })
    })

    // ── Click: add polygon vertex or circle center/radius ──
    m.on('click', (e) => {
      const mode = drawModeRef.current
      if (!mode) return
      const pt = [e.lngLat.lng, e.lngLat.lat]

      if (mode === 'polygon') {
        // 200 ms delay so double-click can cancel before the point is added
        clearTimeout(clickTimerRef.current)
        clickTimerRef.current = setTimeout(() => {
          const updated = [...pendingPointsRef.current, pt]
          pendingPointsRef.current = updated
          setPendingPointsState(updated)
        }, 200)
      } else if (mode === 'circle') {
        if (pendingPointsRef.current.length === 0) {
          // First click — store center
          pendingPointsRef.current = [pt]
          setPendingPointsState([pt])
        } else {
          // Second click — compute radius, close shape
          const radius = haversineKm(pendingPointsRef.current[0], pt)
          const circle = makeCircleFeature(pendingPointsRef.current[0], radius)
          setDrawnFeatures((prev) => [...prev, circle])
          pendingPointsRef.current = []
          setPendingPointsState([])
          drawModeRef.current = null
          setDrawModeState(null)
        }
      }
    })

    // ── Double-click: close polygon ────────────────────────
    m.on('dblclick', (e) => {
      if (drawModeRef.current !== 'polygon') return
      e.preventDefault() // prevent map zoom
      clearTimeout(clickTimerRef.current)
      const pts = pendingPointsRef.current
      if (pts.length >= 3) {
        const polygon = {
          type: 'Feature',
          geometry: { type: 'Polygon', coordinates: [[...pts, pts[0]]] },
          properties: {}
        }
        setDrawnFeatures((prev) => [...prev, polygon])
        pendingPointsRef.current = []
        setPendingPointsState([])
        drawModeRef.current = null
        setDrawModeState(null)
      }
    })

    return () => {
      clearTimeout(clickTimerRef.current)
      m.remove()
      map.current = null
    }
  }, [])

  function handleBasemapSelect(id) {
    const selected = BASEMAPS.find((bm) => bm.id === id)
    if (!selected || !map.current) return
    map.current.getSource('basemap').setTiles(selected.tiles)
    setBasemap(id)
  }

  function handleResetNorth() {
    map.current?.rotateTo(0, { duration: 500 })
  }

  function handleSettingChange(key, value) {
    setMapSettings((prev) => ({ ...prev, [key]: value }))
  }

  function handleToggleGlobe() {
    if (!map.current) return
    const next = !isGlobe
    map.current.setProjection({ type: next ? 'globe' : 'mercator' })
    if (next) {
      map.current.flyTo({ zoom: 2, duration: 1200 })
    } else {
      map.current.flyTo({ zoom: 5, center: [2.2137, 46.2276], duration: 1200 })
    }
    setIsGlobe(next)
  }

  function handleSetDrawMode(mode) {
    setPendingPoints([]) // reset any in-progress shape
    setDrawMode(mode)
  }

  function handleToggleDrawToolbar() {
    const next = !showDrawToolbar
    if (!next) {
      // Hide toolbar → cancel active draw mode too
      setPendingPoints([])
      setDrawMode(null)
    }
    setShowDrawToolbar(next)
  }

  return (
    <div className={`map-wrapper${mapSettings.scale ? '' : ' hide-scale'}`}>
      <div ref={mapContainer} className="map-container" />

      {/* Right-side controls — stacked vertically */}
      <BasemapSwitcher current={basemap} onSelect={handleBasemapSelect} />
      <DrawToggle
        active={showDrawToolbar}
        onToggle={handleToggleDrawToolbar}
        drawMode={drawMode}
        onSetMode={handleSetDrawMode}
      />
      <MapSettings settings={mapSettings} onChange={handleSettingChange} />
      <GlobeToggle isGlobe={isGlobe} onToggle={handleToggleGlobe} />

      {/* North arrow — top-left */}
      {mapSettings.northArrow && (
        <button className="north-arrow" onClick={handleResetNorth} title="Reset north">
          <img
            src={northArrowSvg}
            alt="North arrow"
            style={{ transform: `rotate(${-bearing}deg)`, transition: 'transform 0.1s' }}
          />
        </button>
      )}


      {/* Coordinates — bottom-left */}
      {mapSettings.coords && coords && (
        <div className="map-coords">
          {`Lat: ${coords.lat} · Lng: ${coords.lng}`}
        </div>
      )}
    </div>
  )
})

export default Map
