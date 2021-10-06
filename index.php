<!DOCTYPE html>
<html lang="en-us">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="icon" href="favicon.ico"/>
  <link rel="stylesheet" href="hatred.css">
  <title>Data Viewer</title>
</head>
<body>


<?php
$data = file_get_contents('tragedistsData.json');
$data = json_decode($data);

$fh = fopen('hatred.css','r') or die("error");
while ($line = fgets($fh)) {
  if (preg_match("/--/", $line))
  {
    $result = preg_match("/(?<=:).*?(?=;)/", $line, $match);
    $colors .= $match[0];
  }
}
fclose($fh);
?>

<h1>How <span class="anger">angry</span> was Greek Tragedy?</h1>
<h2>discover how often the three great tragedists use words of <span class="anger">anger</span> or words of <span class="love">love</span>.<sup>[1]</sup></h2>

<div class='flex'>
<div class='title'>
<h2>Aeschylus</h2>
<svg width="221" height="221" viewBox="0 0 221 221" fill="none" xmlns="http://www.w3.org/2000/svg">
<circle id="aeschylus" cx="110" cy="110" r="110" fill="#B10303"/>
<circle id="aeschylus" cx="168" cy="89" r="45" fill="#D67400"/>
<circle id="aeschylus" cx="70" cy="70" r="45" fill="#4B8C0A"/>
<circle id="aeschylus" cx="84" cy="160" r="45" fill="#0DBCBC"/>
</svg>
</div>
<div class='title'>
<h2>Sophocles</h2>
<svg width="221" height="221" viewBox="0 0 221 221" fill="none" xmlns="http://www.w3.org/2000/svg">
<circle id="sophocles" cx="110" cy="110" r="110" fill="#B10303"/>
<circle id="sophocles" cx="168" cy="89" r="45" fill="#D67400"/>
<circle id="sophocles" cx="70" cy="70" r="45" fill="#4B8C0A"/>
<circle id="sophocles" cx="84" cy="160" r="45" fill="#0DBCBC"/>
</svg>
</div>
<div class='title'>
<h2>Euripides</h2>
<svg width="221" height="221" viewBox="0 0 221 221" fill="none" xmlns="http://www.w3.org/2000/svg">
<circle id="euripides" cx="110" cy="110" r="110" fill="#B10303"/>
<circle id="euripides" cx="168" cy="89" r="45" fill="#D67400"/>
<circle id="euripides" cx="70" cy="70" r="45" fill="#4B8C0A"/>
<circle id="euripides" cx="84" cy="160" r="45" fill="#0DBCBC"/>
</svg>
</div>
</div>

<div class='legende'>
<h2>Legend</h2>
<ul class='colors'>
  <li class="anger">ANGRY</li>
  <li class="nasty">NASTY</li>
  <li class="love">AFFECTIONATE</li>
  <li class="nice">NICE</li>
</ul>
</div>

<!-- ADD WORDCLOUD -->
<div id="chartdiv"></div>

<!-- LIST To Do -->
<p>[1] Click here for a list of words that underlie the statistical analysis:
<br></br>
<button onclick=showList() class="button">show list</button>
<div style='display: none' id='list'>
<p>! under construction !</p>
<p>too lazy at the moment</p>
<table>
  <tr>
    <th>angry</th>
    <th>nasty</th>
    <th>affectionate</th>
    <th>nice</th>
  </tr>
</table>
</div>
</p>

<footer>
  <p>&copy; vincent clausing-lage <?php echo date("Y"); ?></p>
</footer>
<script>
let data = '<?php echo json_encode($data); ?>'
let colors = '<?php echo $colors; ?>'
</script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/d3@7"></script>
<script src="js/vectors.js"></script>
<!-- <script src="js/renderer.js"></script> -->
<!-- WORD CLOUD SCRIPT -->
<script src="https://cdn.amcharts.com/lib/4/core.js"></script>
<script src="https://cdn.amcharts.com/lib/4/charts.js"></script>
<script src="https://cdn.amcharts.com/lib/4/plugins/wordCloud.js"></script>
<script src="https://cdn.amcharts.com/lib/4/themes/material.js"></script>
<script src="https://cdn.amcharts.com/lib/4/themes/animated.js"></script>
<script src="js/wordcloud.js"></script>
</body>
</html>