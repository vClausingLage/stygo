<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    
<h1>Promi Generator</h1>

<p>
    Hier entstehen random Särtze für die Yellow Press.
</p>

<?php

$exclamations = ["Skandal!", "Endlich enthüllt!", "Erschütternder Anblick!", "Enthüllungs-Hammer!"];
$promis = ["Meghan", "Helene Fischer", "Daniel Kübelböck"];
$newsT = ["trennt sich.", "verliert in aller Öffentlichkeit die Nerven", "Die Wahrheit über den tragischen Tod", "verliert die letzte Würde", "in Lebensgefahr", "in dramatischem Zustand", "wurde jahrelang misshandelt"];
$newsO = ["Große Sorge um", "Die ganze Welt betrauert"];
$newsOT = ["trennt sich von"];
$newsG = ["So sexy waren $promi's Kurven früher"];

$allNews = [$newsT, $newsO, $newsOT, $newsG];


function pickNews($allNews) {
    $i;
    $j;
    $newsLength = count($allNews);
    $i = rand(0,$newsLength - 1);
    $j = rand(0,count($allNews[$i]) - 1);
    // print_r($allNews[$i][$j]);
    return [$i, $allNews[$i][$j]];
}



$news = pickNews($allNews);
print_r($news);

function choosePromi($promis) {
    
}

?>

<h1>Satz Generator</h1>

</body>
</html>