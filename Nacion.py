from Toolkit import ToolkitCSV
class Nacion:
    def __init__(self, baseUrl, uri):
        self.baseUrl = baseUrl
        self.uri = uri
        self.urls = []
        self.endpoints = []

    def setEndpoints(self,soup):
        #l'exercice etant de refaire une fonction pour VOTRE site a scraper (ici: www.nacion.com)
        swoup = BeautifulSoup(response.text, "html.parser")
        #MAIN ARTICLES
        articles = swoup.findAll("article", {"class": "top-table-list"})
        liens = []
        for article in articles:
            a = article.find("a")
            try: 
                liens.append(a['href'])# tableau ayant les href, mais pas la BaseUrlS
            except:
                pass
        self.endpoints.extend(Toolkit.addBaseUrl(self.baseUrl, liens))# attachement des hrefs via cyberthéurgie
        return self.endpoints

    def getEndpoints(self):
        return self.endpoints
    
    def getResult(self):
        return self.result

    def getDictResult(self):
        result = []
        for res in self.getResult():
            result.append(res.getDictEntry())
        return result