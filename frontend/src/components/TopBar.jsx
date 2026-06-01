import { useState, useRef } from 'react'
import { MapPin } from 'lucide-react'

function TopBar({ onFlyTo }) {
  const [query, setQuery]     = useState('')
  const [results, setResults] = useState([])
  const [loading, setLoading] = useState(false)
  const inputRef = useRef(null)

  // Search via Nominatim (OpenStreetMap geocoder — free, no API key)
  async function handleSearch(e) {
    e.preventDefault()
    if (!query.trim()) return

    setLoading(true)
    try {
      const url = `https://nominatim.openstreetmap.org/search?q=${encodeURIComponent(query)}&format=json&limit=5`
      const res  = await fetch(url, { headers: { 'Accept-Language': 'fr' } })
      const data = await res.json()
      setResults(data)
    } finally {
      setLoading(false)
    }
  }

  function handleSelect(result) {
    // Fly the map to the selected location
    onFlyTo([parseFloat(result.lon), parseFloat(result.lat)])
    // Show only the first part of the address in the input
    setQuery(result.display_name.split(',')[0])
    setResults([])
    inputRef.current?.blur()
  }

  function handleBlur() {
    // Delay so click on result fires before clearing
    setTimeout(() => setResults([]), 150)
  }

  return (
    <header className="topbar">
      {/* Brand */}
      <div className="topbar-brand">
        <img src="/logo.svg" alt="GeoML" width="22" height="25" />
        <span className="topbar-title">GeoML</span>
      </div>

      {/* Address search — right side */}
      <div className="topbar-search-wrap">
        <form className="topbar-search" onSubmit={handleSearch}>
          <MapPin size={14} className="search-pin-icon" />
          <input
            ref={inputRef}
            className="search-input"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            onBlur={handleBlur}
            placeholder="Search address…"
          />
          {loading && <span className="search-spinner" />}
        </form>

        {/* Results dropdown */}
        {results.length > 0 && (
          <ul className="search-results">
            {results.map((r) => (
              <li key={r.place_id}>
                <button
                  className="search-result-item"
                  onMouseDown={() => handleSelect(r)}
                >
                  <MapPin size={12} className="result-pin" />
                  <span>{r.display_name}</span>
                </button>
              </li>
            ))}
          </ul>
        )}
      </div>
    </header>
  )
}

export default TopBar
