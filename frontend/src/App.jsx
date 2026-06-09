import { useState, useRef } from 'react'
import Map from './components/Map.jsx'
import Sidebar from './components/Sidebar.jsx'
import TopBar from './components/TopBar.jsx'
import SidePanel from './components/SidePanel.jsx'

function App() {
  const mapRef = useRef(null)

  const [activePanel, setActivePanel] = useState(null)
  const [hasShapes, setHasShapes]     = useState(false)

  function handleTogglePanel(id) {
    setActivePanel((prev) => (prev === id ? null : id))
  }

  function handleFlyTo(center) {
    mapRef.current?.flyTo(center)
  }

  function handleClear() {
    mapRef.current?.clearShapes()
  }

  return (
    <div className="app">
      <TopBar onFlyTo={handleFlyTo} hasShapes={hasShapes} onClear={handleClear} />

      <div className="app-body">
        <Sidebar activePanel={activePanel} onTogglePanel={handleTogglePanel} />

        {activePanel && (
          <SidePanel modelId={activePanel} onClose={() => setActivePanel(null)} />
        )}

        <div className="map-area">
          <Map ref={mapRef} onShapesChange={setHasShapes} />
        </div>
      </div>
    </div>
  )
}

export default App
