import { useState, useRef } from 'react'
import { TreePine, Building2 } from 'lucide-react'
import Map from './components/Map.jsx'
import Sidebar from './components/Sidebar.jsx'
import TopBar from './components/TopBar.jsx'
import FloatingPanel from './components/FloatingPanel.jsx'

const PANELS = {
  trees:     { icon: TreePine,  title: 'Tree Detection' },
  buildings: { icon: Building2, title: 'Building Detection' }
}

function App() {
  const mapRef = useRef(null)

  // List of currently open panel ids (e.g. ['trees'])
  const [openPanels, setOpenPanels] = useState([])

  function handleTogglePanel(id) {
    setOpenPanels((prev) =>
      prev.includes(id) ? prev.filter((p) => p !== id) : [...prev, id]
    )
  }

  function handleClosePanel(id) {
    setOpenPanels((prev) => prev.filter((p) => p !== id))
  }

  // Called by TopBar when user selects an address
  function handleFlyTo(center) {
    mapRef.current?.flyTo(center)
  }

  return (
    <div className="app">
      {/* Top bar — full width, above everything */}
      <TopBar onFlyTo={handleFlyTo} />

      {/* Body: sidebar + map side by side */}
      <div className="app-body">
        <Sidebar openPanels={openPanels} onTogglePanel={handleTogglePanel} />

        {/* Map area fills remaining space; panels float inside it */}
        <div className="map-area">
          <Map ref={mapRef} />

          {openPanels.map((id, i) => (
            <FloatingPanel
              key={id}
              id={id}
              icon={PANELS[id].icon}
              title={PANELS[id].title}
              onClose={() => handleClosePanel(id)}
              initialPos={{ x: 24 + i * 32, y: 24 + i * 32 }}
            >
              <p className="panel-placeholder">
                Detection results will appear here.
              </p>
            </FloatingPanel>
          ))}
        </div>
      </div>
    </div>
  )
}

export default App
