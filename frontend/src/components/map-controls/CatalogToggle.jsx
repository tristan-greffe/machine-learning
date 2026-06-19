import { Database } from 'lucide-react'

function CatalogToggle({ active, onToggle }) {
  return (
    <div className="catalog-toggle-wrap">
      <button
        className={`catalog-toggle-btn ${active ? 'active' : ''}`}
        onClick={onToggle}
      >
        <Database size={16} strokeWidth={1.5} />
      </button>
      {!active && <span className="catalog-tooltip">Data catalog</span>}
    </div>
  )
}

export default CatalogToggle
