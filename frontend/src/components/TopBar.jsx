import { useState, useRef } from 'react'
import { MapPin, Trash2, LocateFixed } from 'lucide-react'

// Top-of-app content — brand, clear button (when shapes exist),
// address search and "my location" button. Mounted inside <TopPane>.
function TopBar({ onFlyTo, hasShapes, onClear }) {
  const [query, setQuery]       = useState('')
  const [results, setResults]   = useState([])
  const [loading, setLoading]   = useState(false)
  const [locating, setLocating] = useState(false)
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
    onFlyTo([parseFloat(result.lon), parseFloat(result.lat)])
    setQuery(result.display_name.split(',')[0])
    setResults([])
    inputRef.current?.blur()
  }

  function handleBlur() {
    setTimeout(() => setResults([]), 150)
  }

  function handleLocate() {
    if (!navigator.geolocation) return
    setLocating(true)
    navigator.geolocation.getCurrentPosition(
      (pos) => {
        onFlyTo([pos.coords.longitude, pos.coords.latitude])
        setLocating(false)
      },
      () => setLocating(false)
    )
  }

  return (
    <>
      <div className="topbar-brand">
        <img src="/logo.svg" alt="GeoML" width="22" height="25" />
        <span className="topbar-title">GeoML</span>
      </div>

      {hasShapes && (
        <button className="topbar-clear" onClick={onClear}>
          <Trash2 size={13} />
          <span>Clear</span>
        </button>
      )}

      <div className="topbar-search-wrap">
        <div className="topbar-search-row">
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

          <div className="locate-btn-wrap">
            <button
              className={`locate-btn${locating ? ' locating' : ''}`}
              type="button"
              onClick={handleLocate}
              disabled={locating}
            >
              {locating
                ? <span className="search-spinner" />
                : <LocateFixed size={14} strokeWidth={1.5} />}
            </button>
            <span className="locate-tooltip">My location</span>
          </div>
        </div>

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
    </>
  )
}

export default TopBar
