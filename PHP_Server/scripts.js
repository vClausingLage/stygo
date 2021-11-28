let exclamations = ["Krasses Geständnis!", "Trauriger Abschied!", "Bitter!", "Ehrliche Beichte!", "Skandal!", "Endlich enthüllt!", "Erschütternder Anblick!", "Enthüllungs-Hammer!"]
let promis = [["Ewok", "evok.jpg", 0], ["C-3PO", "c3po.jpg", 0], ["Boba Fett", "fett.jpg", 0], ["Yoda", "yoda.jpg", 0], ["Chewbacca", "chew.jpg", 0], ["Han Solo", "solo.jpg", 0], ["Prinzessin Leia", "leia.jpg", 1], ["Jabba the Hut", "jabba.jpg", 0], ["Imperator", "imperator.jpg", 0], ["Amidala", "amidala.jpg", 1]]
let newsT = [": Pikante Porno-Beichte", ": Nackt-Offensive, jetzt lässt %pronpers alle Hüllen fallen", ": Jetzt ist es raus", ": Jetzt geht es immer mehr bergab", ": Mieser Betrug! Diese dreiste Masche ist aufgeflogen", ": Neue Liebe? Jetzt platzt es aus %prondat heraus", ": Krass, was jetzt ans Licht kommt", "hat eine neue Frisur", ": Es geht ums Geld", ": Jetzt wird %pronposs Leben im Trash-TV zerrissen", ": Neuer Auftritt sorgt für Hohn und Spott", ": Jetzt verliert %pronpers wirklcih alles", "beim Koksen erwischt", "verliert in aller Öffentlichkeit die Nerven", ", die Wahrheit über den tragischen Tod", "verliert die letzte Würde", "in Lebensgefahr", "in dramatischem Zustand", "wurde jahrelang misshandelt"]
let newsO = ["Große Sorge um", "Die ganze Welt betrauert"]
let newsOT = ["trennt sich von", "zurück in den Armen von"]
let newsG = ["So sexy waren %ss Kurven früher"]
let newsD = ["Experte: Ich weiß nicht, ob %s das aushält", "%s und %t, heiße Partynächte mit der Ex", "Liebes Aus! %s und %t machen es offiziell", "%s und %t, es herrscht nur noch der pure Hass", "%s und %t lassen Liebes-Bombe platzen. Jetzt ist es raus"]

let sloganDiv = document.getElementById("slogan")
let headlineDiv = document.getElementById("headline")

let allNews = {"T": newsT, "O": newsO, "OT": newsOT, "G": newsG, "D": newsD}

function generateSlogan(exclamations) {
    let i = Math.floor(Math.random() * exclamations.length)
    let pickedSlogan = exclamations[i]
    return pickedSlogan
}
let slogan = generateSlogan(exclamations)

function pickNews(allNews) {
    let sumNews = []
    for (let [key, val] of Object.entries(allNews)) {
        val.forEach((x) => sumNews.push(x))
    }
    let i = Math.floor(Math.random() * sumNews.length)
    let pickedNews = sumNews[i]
    for (let [key, val] of Object.entries(allNews)) {
        if (val.includes(pickedNews)) {
            return [key, pickedNews]
        }
    }
}
let news = pickNews(allNews)

function pickPromi(promis) {
    let i = Math.floor(Math.random() * promis.length)
    let pickedPromi = promis[i][0]
    let picture = promis[i][1]
    let promiGender = promis[i][2]
    return [pickedPromi, picture, promiGender]
}
let promi = pickPromi(promis)
let promiPicture = promi[1]
let promiGender = promi[2]
promi = promi[0]
let promi2 = pickPromi(promis)
promi2 = promi2[0]
if (promi == promi2) {
    promi2 = pickPromi(promis)
    promi2 = promi2[0]
}

function genderer(promiGender, news) {
    if (promiGender == 0) {
        news[1] = news[1].replace('%pronpers', 'er')
        news[1] = news[1].replace('%pronposs', 'sein')
        news[1] = news[1].replace('%prondat', 'ihm')
    } else {
        news[1] = news[1].replace('%pronpers', 'sie')
        news[1] = news[1].replace('%pronposs', 'ihr')
        news[1] = news[1].replace('%prondat', 'ihr')
    }
}
genderer(promiGender, news)

function generateNews(slogan, news, promi) {
    switch (news[0]) {
        case "T":
            sloganDiv.innerHTML = slogan
            if (news[1][0] == "," || news[1][0] == ":") {
                headlineDiv.innerHTML = promi + news[1] + "."
            } else {
                headlineDiv.innerHTML = promi + " " + news[1] + "."
            }
            break
        case "O":
            sloganDiv.innerHTML = slogan
            headlineDiv.innerHTML = news[1] + " " + promi + "."
            break
        case "OT":
            sloganDiv.innerHTML = slogan
            headlineDiv.innerHTML = promi + " " + news[1] + " " + promi2 + "."
            break
        case "G":
            sloganDiv.innerHTML = slogan
            headlineDiv.innerHTML = news[1].replace("%s", promi) + "."
            break
        case "D":
            sloganDiv.innerHTML = slogan
            let news1 = "" 
            news1 = news[1].replace("%s", promi)
            news1 = news1.replace("%t", promi2)
            headlineDiv.innerHTML = news1 + "."
            break
        default:
            break
    }
}
generateNews(slogan, news, promi)

function setPicture() {
    let pictureDiv = document.getElementById("pic")
    pictureDiv.src = promiPicture
}
setPicture()

function renew() {
    slogan = generateSlogan(exclamations)
    news = pickNews(allNews)
    promi = pickPromi(promis)
    promiPicture = promi[1]
    promiGender = promi[2]
    promi = promi[0]
    promi2 = pickPromi(promis)
    promi2 = promi2[0]
    genderer(promiGender, news)
    generateNews(slogan, news, promi)
    setPicture()
}