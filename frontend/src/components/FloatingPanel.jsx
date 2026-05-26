import { useRef, useState, useEffect } from 'react'

function FloatingPanel({ id, title, icon, onClose, children, initialPos }) {
  const [pos, setPos] = useState(initialPos ?? { x: 80, y: 60 })
  const dragging = useRef(false)   // is the user currently dragging?
  const offset   = useRef({ x: 0, y: 0 }) // cursor offset from panel corner

  // Attach mousemove / mouseup on the document so drag works even if cursor
  // moves outside the panel header quickly
  useEffect(() => {
    function onMouseMove(e) {
      if (!dragging.current) return
      setPos({
        x: e.clientX - offset.current.x,
        y: e.clientY - offset.current.y
      })
    }

    function onMouseUp() {
      dragging.current = false
    }

    document.addEventListener('mousemove', onMouseMove)
    document.addEventListener('mouseup', onMouseUp)

    return () => {
      document.removeEventListener('mousemove', onMouseMove)
      document.removeEventListener('mouseup', onMouseUp)
    }
  }, [])

  function handleHeaderMouseDown(e) {
    dragging.current = true
    // Store cursor position relative to panel top-left corner
    offset.current = {
      x: e.clientX - pos.x,
      y: e.clientY - pos.y
    }
  }

  return (
    <div
      className="floating-panel"
      style={{ left: pos.x, top: pos.y }}
    >
      {/* Drag handle — mousedown here starts the drag */}
      <div className="panel-header" onMouseDown={handleHeaderMouseDown}>
        <span className="panel-title">
          <span>{icon}</span> {title}
        </span>
        <button className="panel-close" onClick={onClose} title="Close">✕</button>
      </div>

      <div className="panel-body">
        {children}
      </div>
    </div>
  )
}

export default FloatingPanel
