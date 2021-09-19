<!DOCTYPE html>
<html lang="en-us">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="hatred.css">
  <script src="https://d3js.org/d3.v6.min.js"></script>
  <title>Data Viewer</title>
</head>
<body>

<div class="container">

<?php
$data = file_get_contents('Data.json');
$data = json_decode($data);
?>
</div>

<h1>How angry was Greek Tragedy?</h1>

<h2>discover how often the three great tragedists use words of anger or words of love[1]</h2>

<div id='svg'>
</div>

<p>[1] Click here for a list of words that underlie the statistical analysis:
<br></br>
<button>show list</button>
<div>
  <ul>

  </ul>
</div>
</p>

<script>
let data = '<?php echo json_encode($data); ?>'
data = JSON.parse(data)

function setSVG(data) {
  let angry = data.angry
  let nasty = data.nasty
  let affectionate = data.affectionate
  let nice = data.nice

  let startVector = [200,200]
  let accelerator = 10000

  let angryColor = 'red'
  let nastyColor = 'gray'
  let affectionateColor = 'yellow'
  let niceColor = 'blue'

  let angryVector = [startVector[0],startVector[1],angry * accelerator,angryColor]
  let nastyVector = [startVector[0] + (angry * accelerator + nasty * accelerator),startVector[1],nasty * accelerator,nastyColor]
  let affectionateVector = [startVector[0] + (angry * accelerator + nasty * accelerator),startVector[1] + (nasty * accelerator + affectionate * accelerator),affectionate * accelerator,affectionateColor]
  let niceVector = [startVector[0] + (angry * accelerator + nasty * accelerator) - (nice * accelerator + affectionate * accelerator),startVector[1] + (nasty * accelerator + affectionate * accelerator),nice * accelerator,niceColor]

  let vectors = [angryVector,nastyVector,affectionateVector,niceVector] // d[0] = x-axis d[1] = y-axis d[2] = radius

  let selector = d3.select('#svg')
    .append('svg')
    .attr('width', 500)
    .attr('height', 500)

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
console.log(setSVG(data[1]))





</script>
</body>
</html>