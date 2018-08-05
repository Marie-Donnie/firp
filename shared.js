const S = (function(){
  return {
    width: 1857,
    height: 2142,

    draw(ctx, m, stamps, createCanvas, canvasToImg) {
      let [cmd, ...args] = m
      args = args.map(parseFloat)

      switch (cmd) {
      case 'line': {
        ctx.lineWidth = 10
        ctx.beginPath()
        ctx.moveTo(args[0], args[1])
        ctx.lineTo(args[2], args[3])
        ctx.stroke()
        break
      }

      case 'stamp': {
        const s = 200

        // Create a new sprite
        const colored = createCanvas()

        // Paste the original sprite
        const c = colored.getContext('2d')
        c.drawImage(stamps[0], 0, 0, 200, 200)

        // Apply a colored overlay where the original sprite isn't transparent
        c.globalCompositeOperation = 'source-in'
        c.fillStyle = ctx.fillStyle
        c.fillRect(0, 0, colored.width, colored.height)

        // Now `c` is a color sprite, we can draw it
        // on the layer

        ctx.save()
        ctx.translate(args[0], args[1])
        // Flip
        ctx.scale(args[2], args[2])
        ctx.drawImage(canvasToImg(colored),
                      -s/2, -s/2, s, s)
        ctx.restore()
        break
      }

      case 'erase': {
        const s = 200
        ctx.clearRect(args[0] - s/2,
                      args[1] - s/2, s, s)
        break
      }
      }
    }
  }
}())

if (typeof global !== 'undefined') {
  module.exports = S
}
