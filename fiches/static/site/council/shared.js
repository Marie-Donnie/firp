const S = (function(){
  const width = 1857
  const height = 2142

  return {
    port: 8000,

    width, height,

    draw(ctx, m, stamps, createCanvas, canvasToImg) {
      let [cmd, ...args] = m

      const x = parseFloat(args[0])
      const y = parseFloat(args[1])
      const scale = parseFloat(args[2])
      const lastX = parseFloat(args[3])
      const lastY = parseFloat(args[4])

      switch (cmd) {
      case 'stamp': {
        const size = 200
        const stamp = stamps[args[3]]

        // Create a new sprite
        const colored = createCanvas()

        // Paste the original sprite
        const c = colored.getContext('2d')
        c.drawImage(stamp, 0, 0, 200, 200)

        // Apply a colored overlay where the original sprite isn't transparent
        c.globalCompositeOperation = 'source-in'
        c.fillStyle = ctx.fillStyle
        c.fillRect(0, 0, colored.width, colored.height)

        // Now `c` is a color sprite, we can draw it
        // on the layer

        ctx.save()
        ctx.translate(x, y)
        // Flip
        ctx.scale(scale, scale)
        ctx.drawImage(canvasToImg(colored),
                      -size/2, -size/2, size, size)
        ctx.restore()
        break
      }

      case 'nuke': {
        ctx.clearRect(0, 0, width, height)
        break
      }

      case 'erase': {
        const size = 200

        ctx.save()
        ctx.translate(x, y)
        ctx.scale(scale, scale)
        ctx.clearRect(-size/2, -size/2, size, size)
        ctx.restore()
        break
      }

      case 'pencil': {
        const size = 200
        ctx.lineWidth = scale * 40
        ctx.strokeStyle = ctx.fillStyle
        ctx.lineCap = 'round'
        ctx.lineJoin = 'round'

        ctx.beginPath()

        if (Number.isNaN(lastX)) {
          ctx.moveTo(x, y)
        } else {
          ctx.moveTo(lastX, lastY)
        }
        ctx.lineTo(x, y)
        ctx.stroke()
        break
      }
      }
    }
  }
}())

if (typeof global !== 'undefined') {
  module.exports = S
}
