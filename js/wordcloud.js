function tokensToText(data) {
    let tokens = []
    let tokens_str = ''
    data.forEach (el => {
      for (const [key,val] of Object.entries(el)) {
        if (key == 'tokens') {
          tokens.push(val)
        }
      }
    })
    tokens.forEach(el => {
      for (let i = 0; i < el.length; i++) {
        for (let j = 0; j < el[i][1]; j++) {
          tokens_str += el[i][0] + ' '
        }
      }
    })
    return tokens_str
}

am4core.ready(function() {

am4core.useTheme(am4themes_material);
am4core.useTheme(am4themes_animated);

var chart = am4core.create("chartdiv", am4plugins_wordCloud.WordCloud);
var series = chart.series.push(new am4plugins_wordCloud.WordCloudSeries());

series.accuracy = 4;
series.step = 15;
series.rotationThreshold = 0.7;
series.maxCount = 200;
series.minWordLength = 2;
series.labels.template.tooltipText = "{word}: {value}";
series.fontFamily = "Courier New";
series.maxFontSize = am4core.percent(30);

series.text = tokensToText(data)
});