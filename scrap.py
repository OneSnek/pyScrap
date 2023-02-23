import requests
from bs4 import BeautifulSoup

baseUrl = 'https://studyrama.com'
uri = "/megamoteur/recherche?query=developement&type=E%20F%20O"

response = requests.get(baseUrl + uri)

if response.ok:
    print(response.text)# imprime la reponse en texte
    swoup = BeautifulSoup(response.text, "html.parser")

    ul = swoup.find("ul", {"class": "results"})
    lis = ul.findAll("li")
    for li in lis:
        a = li.find("a")
        print(baseUrl + a["href"])

print("Is the site "+str(baseUrl)+" scrappable?")
print(response.ok) #verifie si le site est scrappable:

# -------------------------------------
# ---- ATTEMPT WITH DIFFERENT SITE ----
# -------------------------------------

baseUrl = 'https://www.monster.fr/'
uri = "/emploi/recherche?q=Cybersecurité&where=Lyon&page=1&et=INTERN&so=m.h.s"

response = requests.get(baseUrl + uri)

if response.ok:
    print(response.text)# imprime la reponse en texte
    swoup = BeautifulSoup(response.text, "html.parser")

    ul = swoup.find("ul", {"class": "job-search-resultsstyle__CardGrid-sc-1wpt60k-0 jnjWtZ"})
    lis = ul.findAll("job-search-resultsstyle__JobCardWrap-sc-1wpt60k-5")
    for li in lis:
        a = li.find("a")
        print(baseUrl + a["href"])

print("Is the site "+str(baseUrl)+" scrappable?")
print(response.ok) #verifie si le site est scrappable:



#END OF CODE