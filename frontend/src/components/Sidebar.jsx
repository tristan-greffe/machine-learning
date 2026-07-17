import { HelpCircle } from 'lucide-react'
import { MODELS } from '../config.js'

// Sidebar shows a button per model on top and a docs shortcut at the
// bottom. Clicking a model toggles its panel; clicking the help button
// opens the documentation site in a new tab.
function Sidebar({ activePanel, onTogglePanel }) {
  const docsHref = `${import.meta.env.BASE_URL}documentation/`

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
                {model.disabled ? `${model.label} - coming soon` : model.label}
              </span>
            </div>
          )
        })}
      </nav>

      {/* Docs shortcut at the bottom of the sidebar */}
      <div className="sidebar-footer">
        <div className="sidebar-btn-wrap">
          <a
            className="sidebar-icon-btn sidebar-help-btn"
            href={docsHref}
            target="_blank"
            rel="noreferrer"
          >
            <HelpCircle size={20} strokeWidth={1.5} />
          </a>
          <span className="sidebar-tooltip">Documentation</span>
        </div>
      </div>
    </aside>
  )
}

export default Sidebar
