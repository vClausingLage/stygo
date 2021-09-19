import requests
from bs4 import BeautifulSoup

pages = [' 1', '48', '98', '122', '153', '176', '197', '214', '230', '239', '278', '292', '308', '341', '386', '424', '444', '462', '511', '531', '551', '568', '577', '582', '587', '591', '595', '601', '608', '634', '673', '709', '740', '782', '799', '809', '820', '840', '860', '895', '945', '987', '1033', '1060', '1071', '1081', '1100', '1118', '1123', '1156', '1168', '1216', '1218', '1226', '1232', '1235', '1240', '1251', '1260', '1287', '1302', '1317 ']
url = 'http://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.01.0123%3Acard%3D'

def getContent(page, url):
    word_list = []
    URL = url + page
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find_all("a", class_="text")
    for result in results:
        word_list.append(result.text)
    return word_list

new_result = []
for page in pages:
    new_result.append(getContent(page, url))
    
with open('eurTroi.txt', 'w') as file:
    file.write(str(new_result))