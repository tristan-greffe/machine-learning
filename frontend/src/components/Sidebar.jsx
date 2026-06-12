import { TreePine, Building2, Waves } from 'lucide-react'

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
  },
  {
    id: 'pools',
    icon: Waves,
    label: 'Pool Detection',
    description: 'Detects swimming pools from aerial imagery.',
    disabled: true
  }
]

// Slim icon-only sidebar — clicking an icon toggles the side panel
function Sidebar({ activePanel, onTogglePanel }) {
  return (
    <aside className="sidebar">
      <nav className="sidebar-nav">
        {MODELS.map((model) => {
          const Icon = model.icon
          return (
            <div key={model.id} className="sidebar-btn-wrap">
              <button
                className={[
                  'sidebar-icon-btn',
                  activePanel === model.id ? 'active' : '',
                  model.disabled ? 'disabled' : ''
                ].join(' ')}
                onClick={() => !model.disabled && onTogglePanel(model.id)}
              >
                <Icon size={20} strokeWidth={1.5} />
              </button>
              <span className="sidebar-tooltip">
                {model.disabled ? `${model.label} — coming soon` : model.label}
              </span>
            </div>
          )
        })}
      </nav>
    </aside>
  )
}

export default Sidebar
