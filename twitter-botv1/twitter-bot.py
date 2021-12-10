#import libraries
from os import link
from bs4 import BeautifulSoup
import urllib.request

import twitter
# from urllib import urlopen
from config import getApi
import random

api = getApi("hcJVNswdLvpNRqCLmUDcqwspN","EiUHT9yuPbamp7jElC63PYQDKxmNzLHSPAhU4idmDTK0SSfUlD","1402177276708544516-bxx2LjLGQeIyq7e09aeH2CWU3YKtpI","BWWe2IfG6jW2F4G1LOlzNPGp02mSYi4k1kYFe27nX7BSb")
ArticlesToPublish = []
randomPublication = ""

#Class representant une publication
class Publication:
    def __init__(self,title,link):
        self.title = title
        self.link = link

def getArticle(link,element,classe):
    #on requette le site et on parse le html
    page = urllib.request.urlopen(link)
    soup = BeautifulSoup(page,"html.parser")

    # le schema utilisé pour récupérer les liens est le suivant ( ont considere dans tous les cas que la balise <a> contenant le lien est dans un element parent )
    if classe  == "":
        liens = soup.find_all(element)
    else:
        liens = soup.find_all(element,attrs={'class': classe})
    # après avoir récupéré un tableau de liens
    # on parcourt notre tableau récuperer precedement , et on récupére l'element enfant  qui correspond aux liens de l'article
    for link in liens:
        ## recuperation du contenu du href
        href = link.findChild("a").get("href")
        #si le lien récupéré commence par /blog (sur le site de gamme her), on est obligé de rajouter le lien https avant, pour avoir une URL complète
        if href.startswith('/blog'):
            href = "https://gameher.fr" + href
        # ici on entre dans le liens récupérer precedement pour recuperer le site de l'article
        titleRequest = urllib.request.urlopen(href)
        titleSoup = BeautifulSoup(titleRequest,"html.parser")
        #on récupère le contenu du premier h1 qui correspond au titre de l'article.
        h1 = titleSoup.find("h1").contents[0]
        # on constitue notre publication avec le titre et le lien
        newPublication = Publication(h1,href)
        # on ajoute notre publication dans un tableau
        ArticlesToPublish.append(newPublication)
     # on retourne le tableau
    return ArticlesToPublish

#random sur le tableau d'article retourné precedement
def getRandomArticle(articleList):
    return random.choice(articleList)



# getArticle("https://gameher.fr/blog","div","imageWithFooter")
getArticle("https://womeningamesfrance.org/category/esport/","h2","")
# getArticle("https://www.afrogameuses.com/news-et-articles/","h2","")

# on recupere un publication au hasard a publier
randomPublication = getRandomArticle(ArticlesToPublish)


#  on poste sur twitter
api.PostUpdate(randomPublication.title + ' ' + randomPublication.link)


