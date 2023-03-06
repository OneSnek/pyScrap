import requests
import csv
from bs4 import BeautifulSoup
#All imports ready

#Base URL + uri + response
baseUrl = "https://www.nacion.com"
uri = "/ultimas-noticias/"
response = requests.get(baseUrl + uri)

if response.ok:
    skoup = BeautifulSoup(response.text, "html.parser")
    #MAIN ARTICLES
    articles = skoup.findAll("article", {"class": "top-table-list"})
    url = []
    for article in articles:
        a = article.find("a")
        url.append({"link":baseUrl+a["href"]})
    print(url)

print("Is the site "+str(baseUrl)+" scrappable?")
print(response.ok) #verifie si le site est scrappable:

#GET ENDPOINTS
def getEndpoints(swoup):
    articles = swoup.findAll("article", {"class": "top-table-list"})
    url = []
    for article in articles:
        a = article.find("a")
        url.append({"link":baseUrl+a["href"]})
    return url


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

#GET INFO BY PAGE
def getInfoByPage(soup):
        fiches = []
        infos = soup.findAll("div", {"class": "primary-font__PrimaryFontStyles-o56yd5-0"})
        if infos != None:
            for info in infos:
                overline = tryToCleanOrReturnBlank(info.find("div", {"class": "overline"}))
                headline = tryToCleanOrReturnBlank(info.find("div", {"class": "headline"}))
                subline = tryToCleanOrReturnBlank(info.find("div", {"class": "sub-headline"}))
                #print(headline)


                #fiche = [overline, headline, subline]
                fiche = { 
                "headline": headline, 
                "overline": overline,
                "subline": subline,
                }
                #printing fiche
                #print(fiche)
                fiches = fiches.append(fiche)
        return fiches

#==========================================================filewriter + filereader = alternative
def fileReader(file):
    result = []
    with open(file, 'r', encoding="UTF8", newline="") as f:
        reader = csv.DictReader(f)
        for line in reader:
           result.append(line) 
    return result

def fileWriting(file, fieldnames, data):
    with open(file, 'w', encoding="UTF8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
    return fileReader(file)
#============================================================
#"""
#definir SWOUP
def swoup(URL, process):
    print("printing URL")
    print(URL)
    response = requests.get(URL[0])
    if response.ok:
        print("yes")
        soup = BeautifulSoup(response.text, 'html.parser')
        return process(soup)
    return []
#"""

#ENDPOINTS
endpoints = swoup(baseUrl + uri,  getEndpoints)
print("printing endpoints:")
print(endpoints)

#presentation
fields = ['lien']
rows = []
for endpoint in endpoints:
    row = {}
    row['lien'] = endpoint
    rows.append(row)
fileWriting('links.csv', fields, rows )
print("links.csv completed")

lignes = []
for link in fileReader('links.csv'):
    lignes.extend(swoup(link['lien'], getInfoByPage))

fields = ["headline", "overline","subline"]
fileWriting('infos.csv', fields, lignes )
print("infos.csv completed")


#END OF THE CODE