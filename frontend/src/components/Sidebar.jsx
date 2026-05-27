import { TreePine, Building2 } from 'lucide-react'

const MODELS = [
  {
    id: 'trees',
    icon: TreePine,
    label: 'Tree Detection',
    description: 'Outlines individual tree crowns — count, area, type.'
  },
  {
    id: 'buildings',
    icon: Building2,
    label: 'Building Detection',
    description: 'Outlines buildings — count, area, type.',
    disabled: true
  }
]

// Slim icon-only sidebar — clicking an icon toggles its floating panel
function Sidebar({ openPanels, onTogglePanel }) {
  return (
    <aside className="sidebar">
      {/* Logo */}
      <div className="sidebar-logo-wrap">
        <img src="/logo.svg" alt="GeoML" width="28" height="32" />
      </div>

      {/* Model icon buttons */}
      <nav className="sidebar-nav">
        {MODELS.map((model) => {
          const Icon = model.icon
          return (
            <button
              key={model.id}
              className={[
                'sidebar-icon-btn',
                openPanels.includes(model.id) ? 'active' : '',
                model.disabled ? 'disabled' : ''
              ].join(' ')}
              onClick={() => !model.disabled && onTogglePanel(model.id)}
              title={model.disabled ? `${model.label} — coming soon` : model.label}
            >
              <Icon size={20} strokeWidth={1.5} />
            </button>
          )
        })}
      </nav>
    </aside>
  )
}

export default Sidebar
