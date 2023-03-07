import requests
from bs4 import BeautifulSoup
import csv

#Base URL + uri + response
baseUrl = "https://www.nacion.com"
uri = "/ultimas-noticias/"
response = requests.get(baseUrl + uri)

print("Is the site "+str(baseUrl)+" scrappable?")
print(response.ok) #verifie si le site est scrappable:


#Get Endpoints = create list of links
def getEndpoints(swoup):
    articles = swoup.findAll("article", {"class": "top-table-list"})
    url = []
    for article in articles:
        a = article.find("a")
        url.append({"link":baseUrl+a["href"]})
    return url

#Get info by page = create list of fiches & return them
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

#Cleaner function
def tryToCleanOrReturnBlank(str):
    try:
        result = str.getText().strip()
    except:
        result = ''
    return result
#SWOUP = URL(BaseUrl+uri) + function
def swoup(URL, process):
    response = requests.get(URL)
    if response.ok:
        print("swoup completing for: " + str(URL))
        soup = BeautifulSoup(response.text, 'html.parser')
        return process(soup)
    return []

#===============================================================READER
def fileReader(file):
    result = []
    with open(file, 'r', encoding="UTF8", newline="") as f:
        reader = csv.DictReader(f)
        for line in reader:
           result.append(line) 
    return result
#======================
def fileWriter(file, fieldnames, data):
    with open(file, 'w', encoding="UTF8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
    return fileReader(file)
#===============================================================WRITER


# fileWriter('infos.csv', fields, data)

#Begin presentation
endpoints = swoup(baseUrl + uri,  getEndpoints)

#creation of links.csv
fields = ['lien']
rows = []
for endpoint in endpoints:
    row = {}
    row['lien'] = endpoint
    rows.append(row)
fileWriter('links.csv', fields, rows )
print("links.csv completed")

#creation of infos.csv array from links.csv listing
lignes = []
for link in fileReader('links.csv'):
    lignes.extend(swoup(link['lien'], getInfoByPage))

fields = ["name", "email", "title"]

fileWriter('infos.csv', fields, lignes )
print("infos.csv completed")


#END OF THE CODE