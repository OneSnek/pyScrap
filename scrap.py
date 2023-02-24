import requests
import csv
from bs4 import BeautifulSoup

# baseUrl = 'https://studyrama.com'
# uri = "/megamoteur/recherche?query=developement&type=E%20F%20O"
# response = requests.get(baseUrl + uri)
# if response.ok:
#     # print(response.text)# imprime la reponse en texte
#     swoup = BeautifulSoup(response.text, "html.parser")

#     ul = swoup.find("ul", {"class": "results"})
#     lis = ul.findAll("li")
#     for li in lis:
#         a = li.find("a")
#     lis = ul.findAll("tabindex")
#     for li in lis:
#         a = i.find("a")
#         print(baseUrl + a["href"])

#     print("Is the site "+str(baseUrl)+" scrappable?")
#     print(response.ok) #verifie si le site est scrappable:

# -------------------------------------
# ---- ATTEMPT WITH DIFFERENT SITE ----
# -------------------------------------


baseUrl = "https://www.nacion.com"
uri = "/ultimas-noticias/"

response = requests.get(baseUrl + uri)

if response.ok:
    swoup = BeautifulSoup(response.text, "html.parser")
    #MAIN ARTICLES
    articles = swoup.findAll("article", {"class": "top-table-list"})
    for article in articles:
        a = article.find("a")
        print(baseUrl+a["href"])
    #SECONDARY ARTICLES [impossible! Uses JavaScript]
    # divs = swoup.findAll("div", {"class": "list-item"})
    # for div in divs:
    #     a = article.find("a")
    #     print(baseUrl+a["href"])

print("Is the site "+str(baseUrl)+" scrappable?")
print(response.ok) #verifie si le site est scrappable:

#TOOLKIT FUNCTIONS
def fileWriter(file,fieldnames, data):
        with open(file, 'w', encoding='UTF8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)

def addBaseUrl(baseUrl, urls):
        res = []
        for url in urls:
            res.append(baseUrl + url)
        return res

#END OF THE CODE