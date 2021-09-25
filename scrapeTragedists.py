import re
import requests
from bs4 import BeautifulSoup

aeschylus_url = [
"http://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.01.0003%3Acard%3D",
"http://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.01.0005%3Acard%3D",
"http://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.01.0007%3Acard%3D",
"http://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.01.0011%3Acard%3D",
"http://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.01.0009%3Acard%3D",
"http://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.01.0013%3Acard%3D",
"http://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.01.0015%3Acard%3D"
]
sophocles_url = [
"http://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.01.0183%3Acard%3D",
"http://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.01.0185%3Acard%3D",
"http://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.01.0187%3Acard%3D",
"http://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.01.0189%3Acard%3D",
"http://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.01.0191%3Acard%3D",
"http://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.01.0193%3Acard%3D",
"http://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.01.0195%3Acard%3D"
]
euripides_url = [
"http://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.01.0087%3Acard%3D",
"http://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.01.0089%3Acard%3D",
"http://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.01.0091%3Acard%3D",
"http://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.01.0093%3Acard%3D",
"http://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.01.0095%3Acard%3D",
"http://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.01.0097%3Acard%3D",
"http://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.01.0099%3Acard%3D",
"http://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.01.0103%3Acard%3D",
"http://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.01.0101%3Acard%3D",
"http://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.01.0105%3Acard%3D",
"http://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.01.0109%3Acard%3D",
"http://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.01.0107%3Acard%3D",
"http://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.01.0111%3Acard%3D",
"http://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.01.0113%3Acard%3D",
"http://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.01.0115%3Acard%3D",
"http://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.01.0117%3Acard%3D",
"http://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.01.0119%3Acard%3D",
"http://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.01.0121%3Acard%3D",
"http://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.01.0123%3Acard%3D"
]

pages = []

urls = aeschylus_url + sophocles_url + euripides_url
test_urls = urls[:3]

# REPLACE TEST URLS !!!
def NEWgetContent(test_urls):
    results_pages = []
    for el in test_urls:
        URL = el + str(1)
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, "html.parser")
        result_pages = soup.find_all("div", class_="sidetoc mbot ind0")
        for result in result_pages:
            result = result.find_all("a")
            for el in result:
                results_pages.append(el.text)
    for el in results_pages:
        el = re.sub("lines\s", "", el)
    return results_pages

# REPLACE TEST URLS !!!
result_pages = NEWgetContent(test_urls)
print(result_pages)

def getContent(page, url):
    word_list = []
    URL = url + page
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find_all("a", class_="text")
    for result in results:
        word_list.append(result.text)
    return word_list

#new_result = []
#for page in pages:
#    new_result.append(getContent(page, url))
    
#with open(".txt", "w") as file:
#    file.write(str(new_result))