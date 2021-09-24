<!DOCTYPE html>
<html lang="en-us">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="hatred.css">
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
<h2>Euripides</h2>
<div id='eur'>
</div>
</div>
<div class='title'>
<h2>Aeschylus</h2>
<div id='aesch'>
</div>
</div>
<div class='legende'>
<h2>Legend</h2>
<ul class='colors'>
  <li style='color: #FD3A0F; padding: 1rem'>ANGRY</li> 
  <li style='color: #C21460; padding: 1rem'>NASTY</li> 
  <li style='color: #CBE432; padding: 1rem'>AFFECTIONATE</li> 
  <li style='color: #98CA32; padding: 1rem'>NICE</li>
</ul>
</div>
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
</script>
<script src="js/three.js"></script>
<script src="js/d3.js"></script>
<script src="js/vector.js"></script>
<script src="js/renderer.js"></script>
</body>
</html>