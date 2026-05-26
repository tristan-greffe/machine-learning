import { useState } from 'react'
import Map from './components/Map.jsx'
import Sidebar from './components/Sidebar.jsx'
import FloatingPanel from './components/FloatingPanel.jsx'

const PANELS = {
  trees:     { icon: '🌳', title: 'Tree Detection' },
  buildings: { icon: '🏠', title: 'Building Detection' }
}

function App() {
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

  return (
    <div className="app">
      {/* Sidebar is outside the map — flex sibling, not overlay */}
      <Sidebar openPanels={openPanels} onTogglePanel={handleTogglePanel} />

      {/* Map area fills remaining space; panels float inside it */}
      <div className="map-area">
        <Map />

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
  )
}

export default App
