import { MODELS } from '../config.js'

// Slim icon-only sidebar — clicking an icon toggles the model panel.
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
