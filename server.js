const WebSocket = require('ws')
const Canvas = require('canvas')
const fs = require('fs')
const S = require('./shared')

// Init canvas and stamps
const layers = Object.create(null)

function newLayer(id) {
  const l = {
    id,
    color: randomColor(),
    dirty: false,
    canvas: new Canvas(S.width, S.height),
  }
  layers[id] = l
  return l
}

const stamps = []
stamps[0] = new Canvas.Image()
stamps[0].src = fs.readFileSync(__dirname + '/troupes.png')

// Load all existing layers
const layerFiles = fs.readdirSync(__dirname + '/layers')
layerFiles.forEach(f => {
  // Files are `id.png`
  const id = f.split('.')[0]

  // Register new layer
  const l = newLayer(id)

  // Restore layer image from disk
  const img = new Canvas.Image()
  img.src = fs.readFileSync(__dirname + '/layers/' + f)
  const ctx = l.canvas.getContext('2d')
  ctx.drawImage(img, 0, 0)
})

// Create WebSocket server
const wss = new WebSocket.Server({port: 8000})

// Add broadcast function
wss.broadcast = function broadcast(data) {
  wss.clients.forEach(function each(client) {
    if (client.readyState === WebSocket.OPEN) {
      client.send(data)
    }
  })
}

const users = Object.create(null)
const authMaxWait = 5000

wss.on('connection', function connection(ws) {
  console.log('Client connected')

  // Drop client if he does not send an auth message
  // before 5sec
  const authTimeout = setTimeout(function dropClient() {
    ws.terminate()
  }, authMaxWait)

  let id = false

  ws.on('message', function incoming(m) {
    const [cmd, ...args] = m.split(' ')

    switch (cmd) {
    case 'auth': {
      console.debug(`Auth request:`, m)

      // Ask Django for actual user ID
      id = djangoAuth(args[0])

      // Drop client if ID is invalid
      if (id === false) {
        ws.terminate()
      }

      clearTimeout(authTimeout)

      // Send current state to client
      const allLayers = Object.values(layers)
      allLayers.sort((a, b) => {
        // BG is first
        if (a.id === 'bg') {
          return -1
        } else if (b.id == 'bg') {
          return +1
        } else {
          return a.id < b.id
        }
      })

      ws.send(JSON.stringify({
        type: 'layers',
        layers: allLayers.map(l => ({
          id: l.id,
          color: l.color,
          canvas: l.canvas.toDataURL(),
        }))
      }))

      // If the layer existed, we already loaded it
      // and broadcasted it to clients.
      // If it didn't exist yet, then we create a new
      // one and inform clients.
      if (!layers[id]) {
        newLayer(id)

        wss.broadcast(JSON.stringify({
          type: 'new',
          id,
          color: layers[id].color,
        }))
      }
      break
    }

    case 'draw': {
      console.debug(`Message from ${id}:`, m)

      // Broadcast it back prefixed with user ID
      wss.broadcast(JSON.stringify({
        type: 'draw',
        id,
        cmd: args,
      }))

      // Draw it on the local layer
      const ctx = layers[id].canvas.getContext('2d')
      S.draw(ctx, args, stamps, createCanvas, canvasToImg)
      layers[id].dirty = true
      break
    }
    }
  })
})

// Save all dirty layers to PNG periodically
const saveMs = 5000

function saveToPNG(layer) {
  layer.canvas.toBuffer(function(err, png) {
    const filename = `layer${layer.id}.png`
    fs.writeFile(filename, png, function(err) {
      console.log("Saved", filename)
    })
  })
  layer.dirty = false
}

setInterval(function serialize() {
  Object.values(layers)
    .filter(l => l.dirty).forEach(saveToPNG)
}, saveMs)


function randomColor(alpha = 1.0) {
  const h = Math.round(Math.random()*360)
  const s = Math.round(40 + Math.random()*30)
  const l = Math.round(20 + Math.random()*50)
  return `hsla(${h}, ${s}%, ${l}%, ${alpha})`
}

function createCanvas() {
  return new Canvas(200, 200)
}

function canvasToImg(canvas) {
  const img = new Canvas.Image()
  img.src = canvas.toBuffer()
  return img
}

// Return an user ID as int, or false if the token is invalid
function djangoAuth(token) {
  // TODO: actually contact Django auth endpoint
  return token
}
