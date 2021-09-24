import requests
from bs4 import BeautifulSoup

pages = []
url = ''

aeschylus_url = [
''
]
sophocles_url = [
'http://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.01.0183%3Acard%3D',
'http://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.01.0185%3Acard%3D',
'http://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.01.0187%3Acard%3D',
'http://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.01.0220%3Acard%3D',
'http://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.01.0189%3Acard%3D',
'http://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.01.0191%3Acard%3D',
'http://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.01.0193%3Acard%3D',
'http://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.01.0195%3Acard%3D'
]
euripides_url = [
''
]

def getContent(page, url):
    word_list = []
    URL = url + page
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    # find_all CLASS 'sidetoc mbot ind0'
    results = soup.find_all("a", class_="text")
    for result in results:
        word_list.append(result.text)
    return word_list

new_result = []
for page in pages:
    new_result.append(getContent(page, url))
    
with open('.txt', 'w') as file:
    file.write(str(new_result))