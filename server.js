const WebSocket = require('ws')
const Canvas = require('canvas')
const fs = require('fs')
const S = require('./shared')

// Init canvas and stamps
const layers = Object.create(null)

function addLayer(id) {
  const l = {
    id,
    color: randomColor(),
    dirty: false,
    canvas: new Canvas(S.width, S.height),
  }
  layers[id] = l
  return l
}
addLayer('bg')
addLayer('surface')

const stamps = []
stamps[0] = new Canvas.Image()
stamps[0].src = fs.readFileSync(__dirname + '/troupes.png')

// @Temp: load a map instead
const bg = layers['bg'].canvas.getContext('2d')
bg.fillStyle = '#fff'
bg.fillRect(0,0,S.width,S.height)

// Run server
const wss = new WebSocket.Server({port: 8000})

// Add broadcast function
wss.broadcast = function broadcast(data) {
  wss.clients.forEach(function each(client) {
    if (client.readyState === WebSocket.OPEN) {
      client.send(data)
    }
  })
}

const users = []

wss.on('connection', function connection(ws) {
  console.log('Client connected')

  users.push(ws)
  const id = users.length - 1

  // Send current state to client
  ws.send(JSON.stringify({
    type: 'layers',
    layers: Object.values(layers).map(l => ({
      id: l.id,
      color: l.color,
      canvas: l.canvas.toDataURL(),
    }))
  }))

  // Allocate new layer
  addLayer(id)

  // Broadcast a new client
  // TODO: retrieve saved layer from Django
  wss.broadcast(JSON.stringify({
    type: 'join',
    id,
    color: layers[id].color,
  }))

  ws.on('message', function incoming(m) {
    console.log(`Message from ${id}:`, m)

    // Broadcast it back prefixed with user ID
    wss.broadcast(JSON.stringify({
      type: 'draw',
      id,
      cmd: m,
    }))

    // Draw it on the local layers
    const ctx = layers[id].canvas.getContext('2d')
    S.draw(ctx, m, stamps, createCanvas, canvasToImg)
    layers[id].dirty = true
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
