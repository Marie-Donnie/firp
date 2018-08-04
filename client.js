document.addEventListener('DOMContentLoaded', start)

// Send all commands to websocket server
// Draw all server commands on corresponding canvas

let zoom = 1
let action = 'erase'

const layers = Object.create(null)

function start() {
  const holder = document.getElementById('holder')

  const stamps = []
  stamps[0] = document.getElementById("gh")

  const ws = new WebSocket('ws://localhost:8000')
  ws.addEventListener('open', function(ev) {
    console.log('Connected to server')
  })
  ws.addEventListener('message', function(ev) {
    const m = JSON.parse(ev.data)

    console.log('Message received:', m)

    switch (m.type) {
      // Get existing layers
    case 'layers': {
      m.layers.forEach(l => {
        const c = document.createElement('canvas')
        c.width = S.width
        c.height = S.height
        c.setAttribute('data-id', l.id)
        holder.append(c)

        // Restore canvas from saved state
        const ctx = c.getContext('2d')
        const img = document.createElement('img')
        img.src = l.canvas
        ctx.drawImage(img, 0, 0)

        layers[l.id] = {
          id: l.id,
          color: l.color,
          canvas: c,
        }

        rescale()
      })
      break
    }

    case 'join': {
      // When a user joins, create a new layer
      const c = document.createElement('canvas')
      c.width = S.width
      c.height = S.height
      c.setAttribute('data-id', m.id)
      holder.append(c)
      layers[m.id] = {
        id: m.id,
        color: m.color,
        canvas: c,
      }
      rescale()
      break
    }

    case 'draw': {
      // Find the corresponding layer and draw
      const ctx = layers[m.id].canvas.getContext('2d')
      ctx.fillStyle = layers[m.id].color
      S.draw(ctx, m.cmd, stamps, createCanvas, canvasToImg)
    }
    }
  })

  function rescale() {
    Object.values(layers).forEach(l => {
      l.canvas.style.width = S.width * zoom + 'px'
      l.canvas.style.height = S.height * zoom + 'px'
    })
  }

  document.getElementById('zoom')
    .addEventListener('change', function() {
      zoom = this.value / 100
      rescale()
    })
  zoom = document.getElementById('zoom').value / 100

  holder.addEventListener('click', function(ev) {
    // Mouse coordinates
    const [mx, my] = [ev.layerX, ev.layerY]

    // Turn into canvas coordinates
    const [x, y] = [mx / zoom, my / zoom]

    ws.send(`${action} ${x} ${y}`)
  })

  document.getElementById('stamp')
    .addEventListener('click', _ => action = 'stamp')
  document.getElementById('erase')
    .addEventListener('click', _ => action = 'erase')
}

function createCanvas() {
  const c = document.createElement('canvas')
  c.width = 200
  c.height = 200
  return c
}

function canvasToImg(canvas) {
  return canvas
}
