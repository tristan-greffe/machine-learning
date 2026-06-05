import { useState, useRef } from 'react'
import Map from './components/Map.jsx'
import Sidebar from './components/Sidebar.jsx'
import TopBar from './components/TopBar.jsx'
import SidePanel from './components/SidePanel.jsx'

function App() {
  const mapRef = useRef(null)

  // Single active panel id, or null when closed
  const [activePanel, setActivePanel] = useState(null)

  function handleTogglePanel(id) {
    setActivePanel((prev) => (prev === id ? null : id))
  }

  // Called by TopBar when user selects an address
  function handleFlyTo(center) {
    mapRef.current?.flyTo(center)
  }

  return (
    <div className="app">
      {/* Top bar — full width, above everything */}
      <TopBar onFlyTo={handleFlyTo} />

      {/* Body: sidebar | side-panel (optional) | map */}
      <div className="app-body">
        <Sidebar activePanel={activePanel} onTogglePanel={handleTogglePanel} />

        {activePanel && (
          <SidePanel
            modelId={activePanel}
            onClose={() => setActivePanel(null)}
          />
        )}

        <div className="map-area">
          <Map ref={mapRef} />
        </div>
      </div>
    </div>
  )
}

export default App
