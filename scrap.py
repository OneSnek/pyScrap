import requests
from bs4 import BeautifulSoup

baseUrl = 'https://studyrama.com'
uri = "/megamoteur/recherche?query=developement&type=E%20F%20O"
response = requests.get(baseUrl + uri)
if response.ok:
    # print(response.text)# imprime la reponse en texte
    swoup = BeautifulSoup(response.text, "html.parser")

    ul = swoup.find("ul", {"class": "results"})
    lis = ul.findAll("li")
    for li in lis:
        a = li.find("a")
    lis = ul.findAll("tabindex")
    for li in lis:
        a = i.find("a")
        print(baseUrl + a["href"])

    print("Is the site "+str(baseUrl)+" scrappable?")
    print(response.ok) #verifie si le site est scrappable:


# -------------------------------------
# ---- ATTEMPT WITH DIFFERENT SITE ----
# -------------------------------------


baseUrl = "https://www.nacion.com"
uri = "/ultimas-noticias/"

response = requests.get(baseUrl + uri)

if response.ok:
    swoup = BeautifulSoup(response.text, "html.parser")
    divs = swoup.find("div", {"class": "top-table-list-section"})
    for div in divs:
        a = div.find("a")
        print(baseUrl+a["href"])


print("Is the site "+str(baseUrl)+" scrappable?")
print(response.ok) #verifie si le site est scrappable:
#END OF CODE