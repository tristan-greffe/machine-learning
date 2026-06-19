import { useState, useRef } from 'react'
import Map from './components/Map.jsx'
import Sidebar from './components/Sidebar.jsx'
import TopBar from './components/TopBar.jsx'
import TopPane from './components/layout/TopPane.jsx'
import ModelPanel from './components/panels/ModelPanel.jsx'
import CatalogPanel from './components/panels/CatalogPanel.jsx'
import { CATALOG_LAYERS, MAP_DEFAULTS } from './config.js'

function App() {
  const mapRef = useRef(null)

  const [activePanel, setActivePanel] = useState(null)
  const [hasShapes, setHasShapes]     = useState(false)

  // Catalog state
  const [showCatalog, setShowCatalog]                 = useState(false)
  const [activeCatalogLayers, setActiveCatalogLayers] = useState([])

  // Map state — forwarded to ModelPanel to gate the Run button
  const [mapState, setMapState] = useState({ zoom: MAP_DEFAULTS.zoom, basemap: 'satellite' })

  function handleTogglePanel(id) {
    setActivePanel((prev) => (prev === id ? null : id))
  }

  function handleFlyTo(center) {
    mapRef.current?.flyTo(center)
  }

  function handleClear() {
    mapRef.current?.clearShapes()
  }

  function handleToggleCatalog() {
    setShowCatalog((v) => !v)
  }

  function handleToggleCatalogLayer(id) {
    const layer    = CATALOG_LAYERS.find((l) => l.id === id)
    const isActive = activeCatalogLayers.includes(id)

    if (!isActive) {
      mapRef.current?.toggleCatalogLayer(id, layer.tiles, layer.attribution)
    } else {
      mapRef.current?.toggleCatalogLayer(id, null, null)
    }

    setActiveCatalogLayers((prev) =>
      prev.includes(id) ? prev.filter((l) => l !== id) : [...prev, id]
    )
  }

  return (
    <div className="app">
      <TopPane>
        <TopBar onFlyTo={handleFlyTo} hasShapes={hasShapes} onClear={handleClear} />
      </TopPane>

      <div className="app-body">
        <Sidebar activePanel={activePanel} onTogglePanel={handleTogglePanel} />

        {/* Left pane — model results */}
        {activePanel && (
          <ModelPanel
            modelId={activePanel}
            onClose={() => setActivePanel(null)}
            zoom={mapState.zoom}
            basemap={mapState.basemap}
          />
        )}

        {/* Map */}
        <div className="map-area">
          <Map
            ref={mapRef}
            onShapesChange={setHasShapes}
            showCatalog={showCatalog}
            onToggleCatalog={handleToggleCatalog}
            onMapStateChange={setMapState}
          />
        </div>

        {/* Right pane — data catalog */}
        {showCatalog && (
          <CatalogPanel
            activeLayers={activeCatalogLayers}
            onToggle={handleToggleCatalogLayer}
            onClose={() => setShowCatalog(false)}
          />
        )}
      </div>
    </div>
  )
}

export default App
