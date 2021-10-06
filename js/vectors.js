data = JSON.parse(data)

let len = data.length
let circleData = []
let textData = []

function mapCircles(data) {
    data.map((data) => {
        circleData = [...circleData, [data.angry, data.nasty, data.affectionate, data.nice]]
        textData = [...textData, [data.author, data.tokens]]
    })
}
function setCircles(circleData) {
    for (i = 0; i < circleData.length; i++) {
        let circles = document.querySelectorAll(`#${textData[i][0]}`)
        circles[0].setAttribute('r', circleData[i][0] * 5000)
        circles[1].setAttribute('r', circleData[i][1] * 5000)
        circles[2].setAttribute('r', circleData[i][2] * 5000)
        circles[3].setAttribute('r', circleData[i][3] * 5000)
    }
}

mapCircles(data)
setCircles(circleData)

function showList() {
    var x = document.getElementById('list')
    if (x.style.display === "none") {
        x.style.display = "block"
    } else {
        x.style.display = "none"
}
}
  
function greeetings() {
    console.log('Hi there! 👋')
}
greeetings()