import requests
import csv
from bs4 import BeautifulSoup
#All imports ready

#Base URL + URI + response
baseUrl = "https://www.nacion.com"
uri = "/ultimas-noticias/"
response = requests.get(baseUrl + uri)

if response.ok:
    swoup = BeautifulSoup(response.text, "html.parser")
    #MAIN ARTICLES
    articles = swoup.findAll("article", {"class": "top-table-list"})
    url = []
    for article in articles:
        a = article.find("a")
        url.append({"link":baseUrl+a["href"]})
    print(url)



print("Is the site "+str(baseUrl)+" scrappable?")
print(response.ok) #verifie si le site est scrappable:


#TOOLKIT FUNCTIONS ------------------------
#------------------------------------------
def fileWriter(file, data):
        with open(file, 'w+', encoding='UTF8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)

def addBaseUrl(baseUrl, urls):
        res = []
        for url in urls:
            res.append(baseUrl + url)
        return res

def tryToCleanOrReturnBlank(str):
        try:
            result = str.getText().strip()
        except:
            result = ""
        return result
# ------------------------------------------------------
# ------------------------------------------csv imported
fileWriter('links.csv', url)

#GET ENDPOINTS
def getInfoByPage(soup):
        fiches = []
        infos = swoup.findAll("div", {"class": "primary-font__PrimaryFontStyles-o56yd5-0"})
        if infos != None:
            for info in infos:
                overline = tryToCleanOrReturnBlank(info.find("div", {"class": "overline"}))
                headline = tryToCleanOrReturnBlank(info.find("div", {"class": "headline"}))
                subline = tryToCleanOrReturnBlank(info.find("div", {"class": "sub-headline"}))
                #print(headline)
                fiche = [overline, headline, subline] #en POO doit être une instance de classe "NacionEntry"
                fiches = fiches.append(fiche)
        return fiches



#END OF THE CODE