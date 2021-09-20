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

<h1>How <span style='color: #FD3A0F'>angry</span> was Greek Tragedy?</h1>

<h2>discover how often the three great tragedists use words of <span style='color: #FD3A0F'>anger</span> or words of <span style='color: #CBE432'>love</span><sup>[1]</sup></h2>

<div class='flex'>
<div class='title'>
<h3>Euripides</h3>
<div id='eur'>
</div>
</div>
<div class='title'>
<h3>Aeschylus</h3>
<div id='aesch'>
</div>
</div>
<ul class='colors'>
  <li style='color: #FD3A0F; padding: 1rem'>ANGRY</li> 
  <li style='color: #C21460; padding: 1rem'>NASTY</li> 
  <li style='color: #CBE432; padding: 1rem'>AFFECTIONATE</li> 
  <li style='color: #98CA32; padding: 1rem'>NICE</li>
</ul>
</div>

<p>[1] Click here for a list of words that underlie the statistical analysis:
<br></br>
<button onclick=showList()>show list</button>
<div style='display: none' id='list'>
  <ul>
    <p>! under construction !</p>
    <p>angry</p>
    <li></li>
  </ul>
</div>
</p>

<script>
let data = '<?php echo json_encode($data); ?>'
data = JSON.parse(data)

function setSVG(data, author) {
  let angry = data.angry
  let nasty = data.nasty
  let affectionate = data.affectionate
  let nice = data.nice

  let startVector = [120,120]
  let accelerator = 10000

  let angryColor = '#FD3A0F'
  let nastyColor = '#C21460'
  let affectionateColor = '#CBE432'
  let niceColor = '#98CA32'

  let angryVector = [startVector[0],startVector[1],angry * accelerator,angryColor]
  let nastyVector = [startVector[0] + (angry * accelerator + nasty * accelerator),startVector[1],nasty * accelerator,nastyColor]
  let affectionateVector = [startVector[0] + (angry * accelerator + nasty * accelerator),startVector[1] + (nasty * accelerator + affectionate * accelerator),affectionate * accelerator,affectionateColor]
  let niceVector = [startVector[0] + (angry * accelerator + nasty * accelerator) - (nice * accelerator + affectionate * accelerator),startVector[1] + (nasty * accelerator + affectionate * accelerator),nice * accelerator,niceColor]

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
console.log(setSVG(data[1], 'eur'))
console.log(setSVG(data[0], 'aesch'))

function showList() {
  var x = document.getElementById('list');
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}



</script>
</body>
</html>