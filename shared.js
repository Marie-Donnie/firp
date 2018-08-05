const S = (function(){
  return {
    width: 1857,
    height: 2142,

    draw(ctx, m, stamps, createCanvas, canvasToImg) {
      let [cmd, ...args] = m

      switch (cmd) {
      case 'stamp': {
        const x = parseFloat(args[0])
        const y = parseFloat(args[1])
        const scale = parseFloat(args[2])
        const stamp = stamps[args[3]]
        const size = 200

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

      case 'erase': {
        const size = 200
        const x = parseFloat(args[0])
        const y = parseFloat(args[1])

        ctx.clearRect(x - size/2, y - size/2, size, size)
        break
      }
      }
    }
  }
}())

if (typeof global !== 'undefined') {
  module.exports = S
}
