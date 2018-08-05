document.addEventListener('DOMContentLoaded', start)

// Send all commands to websocket server
// Draw all server commands on corresponding canvas

let zoom = 1
let scale = 1
let stamp = ''
let action = 'erase'
let actionLayer = ''

const layers = Object.create(null)
let preview

function start() {
  const holder = document.getElementById('holder')

  const stamps = Object.create(null)
  Array.prototype.forEach.call(
    document.querySelectorAll('.palette button[data-action="stamp"]'),
    s => {
      const img = s.children[0]
      stamps[s.getAttribute('data-stamp')] = img
    })

  const ws = new WebSocket('ws://' + window.location.hostname + ':' + S.port)
  ws.addEventListener('open', function connected(ev) {
    console.debug('Connected to server')

    // TODO: grab token from page
    ws.send('auth ' + Math.floor(Math.random() * 10))
  })
  ws.addEventListener('close', function closed() {
    console.debug('Disconnected from server')
    // TODO: notify user
  })
  ws.addEventListener('message', function incoming(ev) {
    const m = JSON.parse(ev.data)

    //console.debug('Message received:', m)

    switch (m.type) {
      // Get existing layers
    case 'layers': {
      m.layers.forEach(l => {
        const layer = newLayer(l.id, l.color)

        // Restore canvas from saved state
        const ctx = layer.canvas.getContext('2d')
        const img = document.createElement('img')
        img.src = l.canvas
        img.onload = function imageLoaded() {
          ctx.drawImage(img, 0, 0)
        }
      })
      rescaleAll()
      removeSpinner()
      break
    }

    case 'new': {
      // When a new user joins the fray, create layer
      const l = newLayer(m.id, m.color)
      rescale(l)
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

  function rescale(layer) {
    layer.canvas.style.width  = S.width  * zoom + 'px'
    layer.canvas.style.height = S.height * zoom + 'px'
  }

  function rescaleAll() {
    Object.values(layers).forEach(rescale)
  }

  let lastPoint
  holder.addEventListener('mousemove', function(ev) {
    // Erase or pencil if the left button is held down
    if (ev.buttons === 1
        && (action === 'erase' || action === 'pencil')) {
      // Mouse coordinates
      const [mx, my] = [ev.layerX, ev.layerY]

      // Turn into canvas coordinates
      const [x, y] = [mx / zoom, my / zoom]

      if (lastPoint != null) {
        ws.send(`draw ${actionLayer} ${action} ${x} ${y} ${scale} ${lastPoint.x} ${lastPoint.y}`)
      } else {
        ws.send(`draw ${actionLayer} ${action} ${x} ${y} ${scale}`)
      }
      lastPoint = {x, y}
    }
  })

  holder.addEventListener('mousedown', function(ev) {
    if (ev.buttons === 1) {
      lastPoint = null
    }
  })

  holder.addEventListener('click', function(ev) {
    // Mouse coordinates
    const [mx, my] = [ev.layerX, ev.layerY]

    // Turn into canvas coordinates
    const [x, y] = [mx / zoom, my / zoom]

    ws.send(`draw ${actionLayer} ${action} ${x} ${y} ${scale} ${stamp}`)
  })

  // Preview stamp below cursor
  preview = document.createElement('canvas')
  preview.id = 'preview'
  preview.width = 200
  preview.height = 200
  holder.appendChild(preview)

  function updatePreview(button) {
    const action = button.getAttribute('data-action')
    const ctx = preview.getContext('2d')
    ctx.clearRect(0,0,200,200)

    switch (action) {
    case 'stamp': {
      const img = button.children[0]
      ctx.drawImage(img, 0, 0, 200, 200)
      break
    }

    case 'erase': {
      ctx.fillStyle = 'white'
      ctx.fillRect(0, 0, 200, 200)
      break
    }

    case 'pencil': {
      ctx.fillStyle = 'black'
      ctx.beginPath()
      ctx.arc(100, 100, 25, 0, 2 * Math.PI)
      ctx.fill()
      break
    }
    }
  }

  holder.addEventListener('mousemove', function(ev) {
    // Mouse coordinates
    const [mx, my] = [ev.layerX, ev.layerY]

    preview.style.left = (mx - 100) + 'px'
    preview.style.top = (my - 100) + 'px'
    preview.style.transform = `scale(${scale * zoom})`
  })

  document.getElementById('palettes')
    .addEventListener('click', function(ev) {
      const newAction = ev.target.getAttribute('data-action')
      actionLayer = ev.target.parentNode.getAttribute('data-layer') || ''
      if (newAction === 'nuke') {
        let msg
        if (actionLayer === 'horde') {
          msg = "Voulez-vous écraser tout le calque de la Horde ?"
        } else {
          msg = "Voulez-vous écraser tout votre calque ?"
        }
        if (window.confirm(msg)) {
          ws.send(`draw ${actionLayer} nuke`)
        }
      } else {
        action = newAction

        if (action === 'stamp') {
          stamp = ev.target.getAttribute('data-stamp')
        } else {
          stamp = ''
        }

        updatePreview(ev.target)
      }
    })

  document.getElementById('zoom')
    .addEventListener('change', function() {
      zoom = this.value / 100
      rescaleAll()
    })
  zoom = document.getElementById('zoom').value / 100

  document.getElementById('scale')
    .addEventListener('change', function() {
      scale = this.value / 100
    })
  scale = document.getElementById('scale').value / 100

  updatePreview(document.querySelector('button[data-action="erase"]'))
}

function createCanvas() {
  const c = document.createElement('canvas')
  c.width = 200
  c.height = 200
  return c
}

function newLayer(id, color) {
  const canvas = document.createElement('canvas')
  canvas.width = S.width
  canvas.height = S.height
  canvas.setAttribute('data-id', id)
  // TODO: insert new canvas in proper order
  // to ensure every client has the same view
  holder.insertBefore(canvas, preview)
  layers[id] = { id, color, canvas }
  return layers[id]
}

function canvasToImg(canvas) {
  return canvas
}

function enableInteraction() {
}

function disableInteraction() {
}

function removeSpinner() {
  document.querySelector('.spinner').remove()
}
