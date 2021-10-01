import re
import requests
from bs4 import BeautifulSoup
from requests.api import request

aeschylus_urls = [
"http://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.01.0003%3Acard%3D",
"http://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.01.0005%3Acard%3D",
"http://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.01.0007%3Acard%3D",
"http://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.01.0011%3Acard%3D",
"http://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.01.0009%3Acard%3D",
"http://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.01.0013%3Acard%3D",
"http://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.01.0015%3Acard%3D"
]
sophocles_urls = [
"http://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.01.0183%3Acard%3D",
"http://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.01.0185%3Acard%3D",
"http://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.01.0187%3Acard%3D",
"http://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.01.0189%3Acard%3D",
"http://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.01.0191%3Acard%3D",
"http://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.01.0193%3Acard%3D",
"http://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.01.0195%3Acard%3D"
]
euripides_urls = [
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

data = [
{"author": "aeschylus", "urls": aeschylus_urls, "pages": [], "text": []},
{"author": "sophocles", "urls": sophocles_urls, "pages": [], "text": []},
{"author": "euripides", "urls": euripides_urls, "pages": [], "text": []}
]

# JUST SOPHOCLES!
data_sophocles = data[1]
print(data_sophocles)

# GET PAGES // LOOP AUTHORS! ! !
def getPages(data):
    for el in data:
        pages_total = []
        word_list = []
        urls = el["urls"]
        for url in urls:
            # get pages for URL scraping
            pages = []
            URL_pages = url + str(1)
            page = requests.get(URL_pages)
            soup = BeautifulSoup(page.content, "html.parser")
            result_pages = soup.find_all("div", class_="sidetoc mbot ind0")
            for results in result_pages:
                results = results.find_all("a")
                for result in results:
                    result = result.text
                    result = re.sub("lines\s", "", result)
                    result = re.sub("line\s", "", result)
                    result = re.sub("ff.", "", result)
                    result = result.split("-")
                    if len(result) > 1:
                        pages.append(result[1])
                    else:
                        pages.append(result[0])
            # TEST
            print(pages)
            #
            # use pages for url scraping
            for page in pages:
                URL = url + page
                # TEST
                print(URL)
                # 
                page = requests.get(URL)
                soup = BeautifulSoup(page.content, "html.parser")
                results = soup.find_all("a", class_="text")
                for result in results:
                    word_list.append(result.text)
            print(word_list)
            el["text"] = word_list
            el["pages"] = pages_total

def getPage(data):
    pages_total = []
    word_list = []
    urls = data["urls"]
    for url in urls:
        # get pages for URL scraping
        pages = []
        URL_pages = url + str(1)
        page = requests.get(URL_pages)
        soup = BeautifulSoup(page.content, "html.parser")
        result_pages = soup.find_all("div", class_="sidetoc mbot ind0")
        for results in result_pages:
            results = results.find_all("a")
            for result in results:
                result = result.text
                result = re.sub("lines\s", "", result)
                result = re.sub("line\s", "", result)
                result = re.sub("ff.", "", result)
                result = result.split("-")
                if len(result) > 1:
                    pages.append(result[1])
                else:
                    pages.append(result[0])
        # TEST
        print(pages)
        #
        # use pages for url scraping
        for page in pages:
            URL = url + page
            # TEST
            print(URL)
            # 
            page = requests.get(URL)
            soup = BeautifulSoup(page.content, "html.parser")
            results = soup.find_all("a", class_="text")
            for result in results:
                word_list.append(result.text)
        print(word_list)
        data["text"] = word_list
        data["pages"] = pages_total

# TEST
# GET SOPHOCLES
getPage(data_sophocles)
print(data_sophocles)

# getPages(data)
print(data)
    
with open("tragedistsData.json", "w") as file:
    # file.write(str(data))
    file.write(str(data_sophocles))