import { useState } from 'react'
import { Settings } from 'lucide-react'
import { DISPLAY_OPTIONS } from '../../config.js'

function MapSettings({ settings, onChange }) {
  const [open, setOpen] = useState(false)

  return (
    <div className="map-settings">
      <button
        className={`settings-toggle ${open ? 'active' : ''}`}
        onClick={() => setOpen((v) => !v)}
      >
        <Settings size={18} strokeWidth={1.5} />
      </button>

      {!open && <span className="settings-tooltip">Map settings</span>}

      {open && (
        <div className="settings-panel">
          <p className="settings-panel-title">Display</p>
          {DISPLAY_OPTIONS.map(({ key, label }) => (
            <label key={key} className="settings-row">
              <span className="settings-label">{label}</span>
              <span className="toggle-switch">
                <input
                  type="checkbox"
                  checked={settings[key]}
                  onChange={(e) => onChange(key, e.target.checked)}
                />
                <span className="toggle-slider" />
              </span>
            </label>
          ))}
        </div>
      )}
    </div>
  )
}

export default MapSettings
