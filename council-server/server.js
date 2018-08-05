const WebSocket = require('ws')
const Canvas = require('canvas')
const fs = require('fs')
const S = require('../fiches/static/site/council/shared')

// Configuragion
const layerDir = __dirname + '/layers'
const stampDir = __dirname + '/../fiches/static/site/council/stamps'
const saveMs = 5000
const authMaxWait = 5000

// Init canvas and stamps
const layers = Object.create(null)

function newLayer(id) {
  const l = {
    id,
    color: id === 'horde' ? 'red' : randomColor(),
    dirty: false,
    canvas: new Canvas(S.width, S.height),
  }
  layers[id] = l
  return l
}

const stamps = Object.create(null)
const stampFiles = fs.readdirSync(stampDir)
stampFiles.forEach(f => {
  const name = f.split('.')[0]

  const img = new Canvas.Image()
  img.src = fs.readFileSync(stampDir + '/' + f)
  stamps[name] = img
})

// Load all existing layers
const layerFiles = fs.readdirSync(layerDir)
layerFiles.forEach(f => {
  // Files are `id.png`
  const id = f.split('.')[0]

  // Register new layer
  const l = newLayer(id)

  // Restore layer image from disk
  const img = new Canvas.Image()
  img.src = fs.readFileSync(layerDir + '/' + f)
  const ctx = l.canvas.getContext('2d')
  ctx.drawImage(img, 0, 0)
})

// Create WebSocket server
const wss = new WebSocket.Server({port: S.port})

// Add broadcast function
wss.broadcast = function broadcast(data) {
  wss.clients.forEach(function each(client) {
    if (client.readyState === WebSocket.OPEN) {
      client.send(data)
    }
  })
}

const users = Object.create(null)

wss.on('connection', function connection(ws) {
  //console.log('Client connected')

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
      //console.debug(`Auth request:`, m)

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
        // BG is first, 'horde' is last
        if (a.id === 'bg') {
          return -1
        } else if (b.id == 'bg') {
          return +1
        } else if (a.id === 'horde') {
          return +1
        } else if (b.id === 'horde') {
          return -1
        } else {
          return parseInt(a.id) < parseInt(b.id)
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
      //console.debug(`Message from ${id}:`, m)

      const [layer_id, ...draw_args] = args
      const draw_id = layer_id === 'horde' ? layer_id : id

      // Broadcast it back prefixed with user ID
      wss.broadcast(JSON.stringify({
        type: 'draw',
        id: draw_id,
        cmd: draw_args,
      }))

      // Draw it on the local layer
      const ctx = layers[draw_id].canvas.getContext('2d')
      ctx.fillStyle = layers[draw_id].color
      S.draw(ctx, draw_args, stamps, createCanvas, canvasToImg)
      layers[draw_id].dirty = true
      break
    }
    }
  })
})

// Save all dirty layers to PNG periodically
function saveToPNG(layer) {
  layer.canvas.toBuffer(function(err, png) {
    if (err) {
      console.error('Error creating PNG from layer, cannot save')
      return
    }
    const filename = layerDir + '/' + layer.id + '.png'
    fs.writeFile(filename, png, function(err) {
      if (err) {
        console.error('Error saving layer ' + filename)
      }
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
  const s = Math.round(60 + Math.random()*30)
  const l = Math.round(50 + Math.random()*30)
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
