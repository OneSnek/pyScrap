import requests
from bs4 import BeautifulSoup
import csv
#"""
#Base URL + uri + response
baseUrl = "https://www.nacion.com"
uri = "/ultimas-noticias/"
response = requests.get(baseUrl + uri)

print("Is the site "+str(baseUrl)+" scrappable?")
print(response.ok) #verifie si le site est scrappable:


#Get Endpoints = create list of links
def getEndpoints(swoup):
    urls = []

    articles = swoup.findAll("article", {"class": "top-table-list"})
    for article in articles:
        a = article.find("a")
        urls.append(baseUrl + a["href"])
    return urls

#Get info by page = create list of fiches & return them
def getInfoByPage(soup):
    fiches = []
    infos = soup.findAll("div", {"class": "primary-font__PrimaryFontStyles-o56yd5-0"})
    if infos is not None:
        for info in infos:
                overline = tryToCleanOrReturnBlank(info.find("div", {"class": "overline"}))
                headline = tryToCleanOrReturnBlank(info.find("div", {"class": "headline"}))
                #subline = tryToCleanOrReturnBlank(info.find("div", {"class": "sub-headline"}))
                #print(headline)


                fiche = { 
                "overline": overline, 
                "headline": headline,
                }
                #print("printing fiche: "+str(fiche))
                fiches.append(fiche)
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
    schema = URL
    print("\nswoup printing schema = "+str(schema)+", for process: "+str(process))
    response = requests.get(URL)
    if response.ok:
        print("swoup completing for: " + str(URL)+"\n")
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
url = baseUrl+uri
print("\ngathering endpoints from getEndpoints, via = swoup(baseUrl+uri,  getEndpoints)")
endpoints = swoup(url,  getEndpoints)
print("These are the Endpoints: "+str(endpoints)+"\n")

#creation of links.csv
print("creating links.csv")
fields = ['lien']
rows = []
for endpoint in endpoints:
    row = {}
    row['lien'] = endpoint
    rows.append(row)
fileWriter('links.csv', fields, rows )
print("links.csv completed\n")

#creation of infos.csv array from links.csv listing
print("creating infos.csv")
lignes = []
for link in fileReader('links.csv'):
    print("this is link['lien'] to be swoup'ed by getInfoByPage:")
    print(link['lien'])
    soupe = swoup(link['lien'], getInfoByPage)
    print("this is the SOUPE = link[lien] + getInfoByPage:")
    print(soupe)
    print("\n")
    print(soupe)
    lignes.extend(soupe)

fields = ["overline", "headline"]
print("\nvoici les LIGNES:")
print(lignes)

fileWriter('infos.csv', fields, lignes )
print("infos.csv completed\n")

#segment
"""
import requests
from bs4 import BeautifulSoup
import csv


baseUrl = 'https://www.studyrama.com'
uri = "/megamoteur/recherche?query=developpement&type=E%20F%20O"
response = requests.get(baseUrl + uri)



def getEndpoints(swoup):
    links = []

    ul = swoup.find("ul", {"class": "results"})
    lis = ul.findAll("li")
    for li in lis:
        a = li.find("a")
        links.append(baseUrl + a["href"])

    return links

def getInfoByPage(soup):
    fiches = []
    contacts = soup.find("div",{"class": "coordonnees"})
    if contacts is not None:
        tabs = contacts.findAll('li', {"class": "accordeon-item"})
        if tabs is not None:
            for contact in tabs:
                name = tryToCleanOrReturnBlank(contact.find("div", {"class": "accordeon-header"}))
                coord = contact.find("div", {"class": "accordeon-body"})
                adress = coord.find("p")
                tel = tryToCleanOrReturnBlank(coord.find("a", {"class": "tel"}))
                email = tryToCleanOrReturnBlank(coord.find("a", {"class": "email"}))
                title = tryToCleanOrReturnBlank(soup.find("title"))
                
                try:
                    adress = adress.getText()
                    cleanArrAdress = []
                    for ele in str(adress).split("\n"):
                        if ele != "":
                                cleanArrAdress.append(ele.strip())
                    
                    realAdress = cleanArrAdress[0]
                    realCC = cleanArrAdress[1]
                    realCountry = cleanArrAdress[2]
                except:
                    adress = ""
                    realAdress =""
                    realCC =""
                    realCountry =""
                    cleanArrAdress = []


                fiche = { 
                "name": name, 
                "adress": " ".join(cleanArrAdress),
                "realAdress": realAdress,
                "departement":realCC,
                "country": realCountry,
                "tel": tel,
                "email": email, 
                "title": title.replace(' - Studyrama', "")
                }
                fiches.append(fiche)
    return fiches 
def tryToCleanOrReturnBlank(str):
    try:
        result = str.getText().strip()
    except:
        result = ''
    return result
def swoup(url, process):
    schema = url
    print("\nswoup printing schema = "+str(schema)+", for process: "+str(process))
    response = requests.get(url)
    if response.ok:
        #print("yes")
        print("swoup completing for: " + str(url)+"\n")
        soup = BeautifulSoup(response.text, 'html.parser')
        return process(soup)
    return []


def fileReader(file):
    result = []
    with open(file, 'r', encoding="UTF8", newline="") as f:
        reader = csv.DictReader(f)
        for line in reader:
           result.append(line) 
    return result

def fileWriter(file, fieldnames, data):
    with open(file, 'w', encoding="UTF8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
    return fileReader(file)



# fileWriter('infos.csv', fields, data)

print("\ngathering endpoints from getEndpoints, via = swoup(baseUrl+uri,  getEndpoints)")
endpoints = swoup(baseUrl + uri,  getEndpoints)
print("These are the Endpoints: "+str(endpoints))

print("\ncreating links.csv")
fields = ['lien']
rows = []
for endpoint in endpoints:
    row = {}
    row['lien'] = endpoint
    rows.append(row)
fileWriter('links.csv', fields, rows )
print("links.csv completed")

print("\ncreating infos.csv")
lignes = []
for link in fileReader('links.csv'):
    print("this is link['lien'] to be swoup'ed by getInfoByPage:")
    print(link['lien'])
    soupe = swoup(link['lien'], getInfoByPage)
    print("this is the SOUPE = link[lien] + getInfoByPage:")
    print(soupe)
    print("\n")
    lignes.extend(soupe)
print("\nvoici les LIGNES:")
print(lignes)

fields = ["name", "adress","realAdress","departement","country", "tel", "email", "title"]
fileWriter('infos.csv', fields, lignes )
print("infos.csv completed")
"""
#END OF THE CODE