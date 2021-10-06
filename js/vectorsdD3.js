// CSS
// get CSS
colors = colors.trim()
colors = colors.split(" ")
colors = colors.slice(0,7)

// DATA
data = JSON.parse(data)

function setSVG(data, author) {
  let angry = data.angry
  let nasty = data.nasty
  let affectionate = data.affectionate
  let nice = data.nice

  let startVector = [120,120]
  let accelerator = 5000

  let angryColor = colors[3]
  let nastyColor = colors[5]
  let affectionateColor = colors[4]
  let niceColor = colors[6]

  let angryVector = [startVector[0],startVector[1],angry * accelerator,angryColor]
  let nastyVector = [startVector[0] + (angry * accelerator + nasty * accelerator - (nasty * accelerator / 100 * 40)),startVector[1],nasty * accelerator,nastyColor]
  let affectionateVector = [startVector[0] + (angry * accelerator + nasty * accelerator - (nasty * accelerator / 100 * 60)),startVector[1] + (nasty * accelerator + affectionate * accelerator - (affectionate * accelerator / 100 * 10)),affectionate * accelerator,affectionateColor]
  let niceVector = [startVector[0] + (angry * accelerator + nasty * accelerator - (nasty * accelerator / 100 * 60)) - (nice * accelerator + affectionate * accelerator),startVector[1] + (nasty * accelerator + affectionate * accelerator),nice * accelerator,niceColor]

  let vectors = [angryVector,nastyVector,affectionateVector,niceVector] // d[0] = x-axis d[1] = y-axis d[2] = radius

  let selector = d3.select(`#${author}`)
    .append('svg')
    .attr('width', 400)
    .attr('height', 300)

  let figures = selector.selectAll('forms')
    .data(vectors)
    .enter()
    .append('circle')

  let formAttributes = figures
    .attr('cx', function (d) { return d[0] })
    .attr('cy', function (d) { return d[1] })
    .attr('r', function (d) { return d[2] })
    .style('fill', function (d) { return d[3] })
  return data
}

setSVG(data[0], 'aesch')
setSVG(data[1], 'eur')
setSVG(data[2], 'soph')