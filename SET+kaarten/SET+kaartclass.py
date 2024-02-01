import pygame
from pygame import Rect

from random import randrange as rndm
from random import shuffle

def verglijk_nummer(kaart1, kaart2, kaart3): 
     if kaart1.nummer == kaart2.nummer == kaart3.nummer or (kaart1.nummer != kaart2.nummer and kaart1.nummer != kaart3.nummer and kaart2.nummer != kaart3.nummer):
        return True
     else:
        return False

def verglijk_symbool(kaart1, kaart2, kaart3): 
     if (kaart1.symbool == kaart2.symbool == kaart3.symbool or 
         (kaart1.symbool != kaart2.symbool and kaart1.symbool != kaart3.symbool and kaart2.symbool != kaart3.symbool)):
        return True
     else:
        return False

def verglijk_kleur(kaart1, kaart2, kaart3):
     if (kaart1.kleur == kaart2.kleur == kaart3.kleur or (kaart1.kleur != kaart2.kleur and kaart1.kleur != kaart3.kleur and kaart2.kleur != kaart3.kleur)):
        return True
     else:
        return False
def verglijk_shading(kaart1, kaart2, kaart3): 
     if (kaart1.shading == kaart2.shading == kaart3.shading or 
         (kaart1.shading != kaart2.shading and kaart1.shading != kaart3.shading and kaart2.shading != kaart3.shading)):
        return True
     else:
        return False
def verglijk(kaart1, kaart2, kaart3):
    if (verglijk_nummer(kaart1, kaart2 ,kaart3) and verglijk_symbool(kaart1,kaart2, kaart3)
        and verglijk_kleur(kaart1, kaart2, kaart3) and verglijk_shading(kaart1, kaart2, kaart3)):
        return True
    else:
        return False
    
class Kaart:
    def __init__(self, nummer, symbool, kleur, shading):
        self.nummer, self.symbool, self.kleur, self.shading = nummer, symbool, kleur, shading    
    def __str__(self):
        return "|{self.nummer}, {self.symbool}, {self.kleur}, {self.shading}|".format(self=self)
    def __repr__(self):
        return "|{self.nummer}, {self.symbool}, {self.kleur}, {self.shading}|".format(self=self)
    #we kunnen mogelijk "==" betekenis geven voor onze class om de vergelijkfunctie wat eleganter te maken,

#hier de handingevoerde kaarten en het werk om ze daadwerkelijk tot de bruikbare class te maken, om te laten zien dat we niet op onze reet hebben gezeten mocht het niet afkomen
class Kaart:
    def __init__(self, nummer, symbool, kleur, shading):
        self.nummer, self.symbool, self.kleur, self.shading = nummer, symbool, kleur, shading    
    def __str__(self):
        return "|{self.nummer}, {self.symbool}, {self.kleur}, {self.shading}|".format(self=self)
    def __repr__(self):
        return "|{self.nummer}, {self.symbool}, {self.kleur}, {self.shading}|".format(self=self)
    #we kunnen mogelijk "==" betekenis geven voor onze class om de vergelijkfunctie wat eleganter te maken,

#hier de eerst fout ingevoerde kaarten en het werk om ze daadwerkelijk tot de bruikbare class te maken, om te laten zien dat we niet op onze reet hebben gezeten mocht het niet afkomen
kaart_eigenschappen = {
        'greendiamondempty1.gif': (0,0,0,0), 'greendiamondempty2.gif':(1,0,0,0), 'greendiamondempty3.gif': (2,0,0,0), 'greendiamondfilled1.gif': (0,0,0,1), 'greendiamondfilled2.gif': (1,0,0,1), 'greendiamondfilled3.gif': (2,0,0,1), 'greendiamondshaded1.gif': (0,0,0,2), 'greendiamondshaded2.gif': (1,0,0,2), 'greendiamondshaded3.gif': (2,0,0,2), 'greenovalempty1.gif': (0,1,0,0), 'greenovalempty2.gif': (1,1,0,0), 'greenovalempty3.gif': (2,1,0,0), 'greenovalfilled1.gif': (0,1,0,1), 'greenovalfilled2.gif': (1,1,0,1), 'greenovalfilled3.gif': (2,1,0,1), 'greenovalshaded1.gif': (0,1,0,2), 'greenovalshaded2.gif': (1,1,0,2), 'greenovalshaded3.gif': (2,1,0,2), 'greensquiggleempty1.gif': (0,2,0,0), 'greensquiggleempty2.gif': (1,2,0,0), 'greensquiggleempty3.gif': (2,2,0,0), 'greensquigglefilled1.gif': (0,2,0,1), 'greensquigglefilled2.gif': (1,2,0,1), 'greensquigglefilled3.gif': (2,2,0,1), 'greensquiggleshaded1.gif': (0,2,0,2), 'greensquiggleshaded2.gif': (1,2,0,2), 'greensquiggleshaded3.gif': (2,2,0,2),
        'purplediamondempty1.gif': (0,0,1,0), 'purplediamondempty2.gif': (1,0,1,0), 'purplediamondempty3.gif': (2,0,1,0), 'purplediamondfilled1.gif': (0,0,1,1), 'purplediamondfilled2.gif': (1,0,1,1), 'purplediamondfilled3.gif': (2,0,1,1), 'purplediamondshaded1.gif': (0,0,1,2), 'purplediamondshaded2.gif': (1,0,1,2), 'purplediamondshaded3.gif': (2,0,1,2), 'purpleovalempty1.gif': (0,1,1,0), 'purpleovalempty2.gif': (1,1,1,0), 'purpleovalempty3.gif': (2,1,1,0), 'purpleovalfilled1.gif': (0,1,1,1), 'purpleovalfilled2.gif': (1,1,1,1), 'purpleovalfilled3.gif': (2,1,1,1), 'purpleovalshaded1.gif': (0,1,1,2), 'purpleovalshaded2.gif': (1,1,1,2), 'purpleovalshaded3.gif': (2,1,1,2), 'purplesquiggleempty1.gif': (0,2,1,0), 'purplesquiggleempty2.gif': (1,2,1,0), 'purplesquiggleempty3.gif': (2,2,1,0), 'purplesquigglefilled1.gif': (0,2,1,1), 'purplesquigglefilled2.gif': (1,2,1,1), 'purplesquigglefilled3.gif': (2,2,1,1), 'purplesquiggleshaded1.gif': (0,2,1,2), 'purplesquiggleshaded2.gif': (1,2,1,2), 'purplesquiggleshaded3.gif': (2,2,1,2), 
        'reddiamondempty1.gif': (0,0,2,0), 'reddiamondempty2.gif': (1,0,2,0), 'reddiamondempty3.gif': (2,0,2,0), 'reddiamondfilled1.gif': (0,0,2,1), 'reddiamondfilled2.gif': (1,0,2,1), 'reddiamondfilled3.gif': (2,0,2,1), 'reddiamondshaded1.gif': (0,0,2,2), 'reddiamondshaded2.gif': (1,0,2,2), 'reddiamondshaded3.gif': (2,0,2,2), 'redovalempty1.gif': (0,1,2,0), 'redovalempty2.gif': (1,1,2,0), 'redovalempty3.gif': (2,1,2,0), 'redovalfilled1.gif': (0,1,2,1), 'redovalfilled2.gif': (1,1,2,1), 'redovalfilled3.gif': (2,1,2,1), 'redovalshaded1.gif': (0,1,2,2), 'redovalshaded2.gif': (1,1,2,2), 'redovalshaded3.gif': (2,1,2,2), 'redsquiggleempty1.gif': (0,2,2,0), 'redsquiggleempty2.gif': (1,2,2,0), 'redsquiggleempty3.gif': (2,2,2,0), 'redsquigglefilled1.gif': (0,2,2,1), 'redsquigglefilled2.gif': (1,2,2,1), 'redsquigglefilled3.gif': (2,2,2,1), 'redsquiggleshaded1.gif': (0,2,2,2), 'redsquiggleshaded2.gif': (1,2,2,2), 'redsquiggleshaded3.gif': (2,2,2,2)}

def en_nu_goed_om(boek):
    kaartmitplaatje = {}
    kaartvolgorde = []
    alternatief = {}
    altvolg = []
    for naam_gif in boek:
        vector = boek[naam_gif]
        n, v, k, sh = vector
        kaart = Kaart(n, v, k, sh)
        kaartmitplaatje[kaart] = naam_gif
        kaartvolgorde.append(kaart)
        #hier voor de tweede visualiesatiemethode:
        if v == 0:
            v2 = "\u25b2"
        elif v == 1:
            v2 = "\u2B2D"
        elif v == 2:
            v2 = "~"
        if k == 0:
            k2 = "g"
        elif k == 1:
            k2 = "p"
        elif k == 2:
            k2 = "r"
        if sh == 0:
            sh2 = "()"
            #@yunus het doet pijn aan mijn hart te zien dat je shaded niet tussen open en dicht hebt gedaan
        elif sh == 1:
            sh2 = "]["
        elif sh == 2:
            sh2 = "//"
        kaart2 = Kaart((n+1), v2, k2, sh2)
        alternatief[kaart2] = naam_gif
        altvolg.append(kaart2)
    return kaartmitplaatje, alternatief, kaartvolgorde, altvolg




#we vinden hiermee alle SETs uit 12 willekeurige kaarten
def elkeSET(kaarten):
    #SETs onthoudt de plek van een SET, showSETs de kaarten zelf om dingen te testen
    SETs = {}
    showSETs ={}
    #het algoritme werkt voor n != 12, maar de tijdscomplexiteit van dit algoritme is O(n^3), het is namelijk een 3-dimensionaal driehoeksgetal (pyramidegetal?):
    #dus mochten we supercomputers ooit tegen elkaar willen laten spelen met gigantisch veel kaarten met gigantisch veel eigenschappen (n <= 3^4 = 81 kan zo n <= 6^9 ~ 10E7 worden als je er geen jpg's aan hoeft te koppelen)
    #moeten  we misschien iets beters bedenken
    n = len(kaarten)
    teller = 0
    #(dit kan misschien beter los in het verslag samen met mijn handgeschreven versie, maar voor jou @Yunus zet ik hier wat de tripel for loop doet):
    #vergelijk de:
    #1ste kaart met de
    #   2e - en
    #       met de 3e t/m laatste -
    #   3e - en
    #       met de 4e t/m laatste -
    #   ...
    #   1 na laatste - en
    #       met de laatste - t/m laatste -
    #2e kaart met de...
    #...
    #2 na laatste - met de
    #   1 na laatste - en
    #       met de laatste - t/m laatste -
    for i in range(0, n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if verglijk(kaarten[i], kaarten[j], kaarten[k]) == True:
                    showSETs[teller] = kaarten[i], kaarten[j], kaarten[k]
                    SETs[teller] = i, j, k
                    teller += 1
                else:
                    pass
    return SETs, showSETs

#test of alle kaarten het doen met een willekeurige shuffle van het deck
kaartgoed, kaartalternatief, kaartlijst, alterlijst = en_nu_goed_om(kaart_eigenschappen)
#je kan ook "kaartlijst" gebruiken
testkaartm = [alterlijst[i] for i in range(81)]
shuffle(testkaartm)
jnfo, keesbaarantwoord = elkeSET(testkaartm[:12])
for i in range(len(keesbaarantwoord)):
    a, b, c = keesbaarantwoord[i]
    print(" {} \n {} \n {} \n ...".format(a, b, c))

#we moeten de bot een van de sets laten kiezen (het liefst eerste van de sets)
def kiesSET(kaarten):
    SETs, showSETs = elkeSET(kaarten)
    n = len(SETs)
    if n == 0:
        #we moeten er wel voor zorgen dat dit geen geldig antwoord is als de speler het invoert
        #of juist een manier om "Cap set" in te voeren voor 2 punten, maar 2 punten voor de computer als er wel een SET is
        return (0,1,2), (kaarten[0], kaarten[1], kaarten[2])
    else:
        r = rndm(0,n)
        a, b = SETs[r], showSETs[r]
        return a, b

      
#deze toetsen wil ik graag om de kaarten in te voeren, paar extra om uit te vinden wat goed voelt
from pygame.locals import (K_1, K_2, K_3, K_4,
                           K_q, K_w, K_e, K_r,
                           K_a, K_s, K_d, K_f,
                           K_z, K_x, K_c, K_v)

class Timer:
    def __init__(self,scherm,font_grootte = 30,positie=(25,650)):
        self.scherm = scherm
        self.positie = positie
        self.font = pygame.font.Font(None,font_grootte)
    
    def teken(self,tijd_over):
        tijd_tekst = self.font.render(f"tijd over {tijd_over}", True, (139,0,0))
        self.scherm.blit(tijd_tekst, self.positie)
#zo kan de module starten met shit doen
pygame.init()

#Resulotie van het spel
breed, hoog = 1280, 720
scherm = pygame.display.set_mode((breed, hoog))

#voor willekeurige achtergrond kleur zonder epilepsie te krijgen moet dit buiten de running loop
r0, g0, b0 = rndm(1,16), rndm(1,16), rndm(1,16)


#verander door middel van ctrl + f alle yunus namen naar je eigen naam en zet de bestand van de fotos van kaarten in een map in downloads genaamd kaarten en daarin nog een map genaamd kaarten en dan kan jij ze ook gebruiken
kaart_images = {
    'greendiamondempty1.gif': pygame.image.load('C:\\Users\\yunus\\Downloads\\kaarten\\kaarten\\greendiamondempty1.gif'), 'greendiamondempty2.gif': pygame.image.load('C:\\Users\\yunus\\Downloads\\kaarten\\kaarten\\greendiamondempty2.gif'), 'greendiamondempty3.gif': pygame.image.load('C:\\Users\\yunus\\Downloads\\kaarten\\kaarten\\greendiamondempty3.gif'), 'greendiamondfilled1.gif': pygame.image.load('C:\\Users\\yunus\\Downloads\\kaarten\\kaarten\\greendiamondfilled1.gif'), 'greendiamondfilled2.gif': pygame.image.load('C:\\Users\\yunus\\Downloads\\kaarten\\kaarten\\greendiamondfilled2.gif'), 'greendiamondfilled3.gif': pygame.image.load('C:\\Users\\yunus\\Downloads\\kaarten\\kaarten\\greendiamondfilled3.gif'), 'greendiamondshaded1.gif': pygame.image.load('C:\\Users\\yunus\\Downloads\\kaarten\\kaarten\\greendiamondshaded1.gif'), 'greendiamondshaded2.gif': pygame.image.load('C:\\Users\\yunus\\Downloads\\kaarten\\kaarten\\greendiamondshaded2.gif'), 'greendiamondshaded3.gif': pygame.image.load('C:\\Users\\yunus\\Downloads\\kaarten\\kaarten\\greendiamondshaded3.gif'), 'greenovalempty1.gif': pygame.image.load('C:\\Users\\yunus\\Downloads\\kaarten\\kaarten\\greenovalempty1.gif'), 'greenovalempty2.gif': pygame.image.load('C:\\Users\\yunus\\Downloads\\kaarten\\kaarten\\greenovalempty2.gif'), 'greenovalempty3.gif': pygame.image.load('C:\\Users\\yunus\\Downloads\\kaarten\\kaarten\\greenovalempty3.gif'), 'greenovalfilled1.gif': pygame.image.load('C:\\Users\\yunus\\Downloads\\kaarten\\kaarten\\greenovalfilled1.gif'), 'greenovalfilled2.gif': pygame.image.load('C:\\Users\\yunus\\Downloads\\kaarten\\kaarten\\greenovalfilled2.gif'), 'greenovalfilled3.gif': pygame.image.load('C:\\Users\\yunus\\Downloads\\kaarten\\kaarten\\greenovalfilled3.gif'), 'greenovalshaded1.gif': pygame.image.load('C:\\Users\\yunus\\Downloads\\kaarten\\kaarten\\greenovalshaded1.gif'), 'greenovalshaded2.gif': pygame.image.load('C:\\Users\\yunus\\Downloads\\kaarten\\kaarten\\greenovalshaded2.gif'), 'greenovalshaded3.gif': pygame.image.load('C:\\Users\\yunus\\Downloads\\kaarten\\kaarten\\greenovalshaded3.gif'), 'greensquiggleempty1.gif': pygame.image.load('C:\\Users\\yunus\\Downloads\\kaarten\\kaarten\\greensquiggleempty1.gif'), 'greensquiggleempty2.gif': pygame.image.load('C:\\Users\\yunus\\Downloads\\kaarten\\kaarten\\greensquiggleempty2.gif'), 'greensquiggleempty3.gif': pygame.image.load('C:\\Users\\yunus\\Downloads\\kaarten\\kaarten\\greensquiggleempty3.gif'), 'greensquigglefilled1.gif': pygame.image.load('C:\\Users\\yunus\\Downloads\\kaarten\\kaarten\\greensquigglefilled1.gif'), 'greensquigglefilled2.gif': pygame.image.load('C:\\Users\\yunus\\Downloads\\kaarten\\kaarten\\greensquigglefilled2.gif'), 'greensquigglefilled3.gif': pygame.image.load('C:\\Users\\yunus\\Downloads\\kaarten\\kaarten\\greensquigglefilled3.gif'), 'greensquiggleshaded1.gif': pygame.image.load('C:\\Users\\yunus\\Downloads\\kaarten\\kaarten\\greensquiggleshaded1.gif'), 'greensquiggleshaded2.gif': pygame.image.load('C:\\Users\\yunus\\Downloads\\kaarten\\kaarten\\greensquiggleshaded2.gif'), 'greensquiggleshaded3.gif': pygame.image.load('C:\\Users\\yunus\\Downloads\\kaarten\\kaarten\\greensquiggleshaded3.gif'),
    'purplediamondempty1.gif': pygame.image.load('C:\\Users\\yunus\\Downloads\\kaarten\\kaarten\\purplediamondempty1.gif'), 'purplediamondempty2.gif': pygame.image.load('C:\\Users\\yunus\\Downloads\\kaarten\\kaarten\\purplediamondempty2.gif'), 'purplediamondempty3.gif': pygame.image.load('C:\\Users\\yunus\\Downloads\\kaarten\\kaarten\\purplediamondempty3.gif'), 'purplediamondfilled1.gif': pygame.image.load('C:\\Users\\yunus\\Downloads\\kaarten\\kaarten\\purplediamondfilled1.gif'), 'purplediamondfilled2.gif': pygame.image.load('C:\\Users\\yunus\\Downloads\\kaarten\\kaarten\\purplediamondfilled2.gif'), 'purplediamondfilled3.gif': pygame.image.load('C:\\Users\\yunus\\Downloads\\kaarten\\kaarten\\purplediamondfilled3.gif'), 'purplediamondshaded1.gif': pygame.image.load('C:\\Users\\yunus\\Downloads\\kaarten\\kaarten\\purplediamondshaded1.gif'), 'purplediamondshaded2.gif': pygame.image.load('C:\\Users\\yunus\\Downloads\\kaarten\\kaarten\\purplediamondshaded2.gif'), 'purplediamondshaded3.gif': pygame.image.load('C:\\Users\\yunus\\Downloads\\kaarten\\kaarten\\purplediamondshaded3.gif'), 'purpleovalempty1.gif': pygame.image.load('C:\\Users\\yunus\\Downloads\\kaarten\\kaarten\\purpleovalempty1.gif'), 'purpleovalempty2.gif': pygame.image.load('C:\\Users\\yunus\\Downloads\\kaarten\\kaarten\\purpleovalempty2.gif'), 'purpleovalempty3.gif': pygame.image.load('C:\\Users\\yunus\\Downloads\\kaarten\\kaarten\\purpleovalempty3.gif'), 'purpleovalfilled1.gif': pygame.image.load('C:\\Users\\yunus\\Downloads\\kaarten\\kaarten\\purpleovalfilled1.gif'), 'purpleovalfilled2.gif': pygame.image.load('C:\\Users\\yunus\\Downloads\\kaarten\\kaarten\\purpleovalfilled2.gif'), 'purpleovalfilled3.gif': pygame.image.load('C:\\Users\\yunus\\Downloads\\kaarten\\kaarten\\purpleovalfilled3.gif'), 'purpleovalshaded1.gif': pygame.image.load('C:\\Users\\yunus\\Downloads\\kaarten\\kaarten\\purpleovalshaded1.gif'), 'purpleovalshaded2.gif': pygame.image.load('C:\\Users\\yunus\\Downloads\\kaarten\\kaarten\\purpleovalshaded2.gif'), 'purpleovalshaded3.gif': pygame.image.load('C:\\Users\\yunus\\Downloads\\kaarten\\kaarten\\purpleovalshaded3.gif'), 'purplesquiggleempty1.gif': pygame.image.load('C:\\Users\\yunus\\Downloads\\kaarten\\kaarten\\purplesquiggleempty1.gif'), 'purplesquiggleempty2.gif': pygame.image.load('C:\\Users\\yunus\\Downloads\\kaarten\\kaarten\\purplesquiggleempty2.gif'), 'purplesquiggleempty3.gif': pygame.image.load('C:\\Users\\yunus\\Downloads\\kaarten\\kaarten\\purplesquiggleempty3.gif'), 'purplesquigglefilled1.gif': pygame.image.load('C:\\Users\\yunus\\Downloads\\kaarten\\kaarten\\purplesquigglefilled1.gif'), 'purplesquigglefilled2.gif': pygame.image.load('C:\\Users\\yunus\\Downloads\\kaarten\\kaarten\\purplesquigglefilled2.gif'), 'purplesquigglefilled3.gif': pygame.image.load('C:\\Users\\yunus\\Downloads\\kaarten\\kaarten\\purplesquigglefilled3.gif'), 'purplesquiggleshaded1.gif': pygame.image.load('C:\\Users\\yunus\\Downloads\\kaarten\\kaarten\\purplesquiggleshaded1.gif'), 'purplesquiggleshaded2.gif': pygame.image.load('C:\\Users\\yunus\\Downloads\\kaarten\\kaarten\\purplesquiggleshaded2.gif'), 'purplesquiggleshaded3.gif': pygame.image.load('C:\\Users\\yunus\\Downloads\\kaarten\\kaarten\\purplesquiggleshaded3.gif'),
    'reddiamondempty1.gif': pygame.image.load('C:\\Users\\yunus\\Downloads\\kaarten\\kaarten\\reddiamondempty1.gif'), 'reddiamondempty2.gif': pygame.image.load('C:\\Users\\yunus\\Downloads\\kaarten\\kaarten\\reddiamondempty2.gif'), 'reddiamondempty3.gif': pygame.image.load('C:\\Users\\yunus\\Downloads\\kaarten\\kaarten\\reddiamondempty3.gif'), 'reddiamondfilled1.gif': pygame.image.load('C:\\Users\\yunus\\Downloads\\kaarten\\kaarten\\reddiamondfilled1.gif'), 'reddiamondfilled2.gif': pygame.image.load('C:\\Users\\yunus\\Downloads\\kaarten\\kaarten\\reddiamondfilled2.gif'), 'reddiamondfilled3.gif': pygame.image.load('C:\\Users\\yunus\\Downloads\\kaarten\\kaarten\\reddiamondfilled3.gif'), 'reddiamondshaded1.gif': pygame.image.load('C:\\Users\\yunus\\Downloads\\kaarten\\kaarten\\reddiamondshaded1.gif'), 'reddiamondshaded2.gif': pygame.image.load('C:\\Users\\yunus\\Downloads\\kaarten\\kaarten\\reddiamondshaded2.gif'), 'reddiamondshaded3.gif': pygame.image.load('C:\\Users\\yunus\\Downloads\\kaarten\\kaarten\\reddiamondshaded3.gif'), 'redovalempty1.gif': pygame.image.load('C:\\Users\\yunus\\Downloads\\kaarten\\kaarten\\redovalempty1.gif'), 'redovalempty2.gif': pygame.image.load('C:\\Users\\yunus\\Downloads\\kaarten\\kaarten\\redovalempty2.gif'), 'redovalempty3.gif': pygame.image.load('C:\\Users\\yunus\\Downloads\\kaarten\\kaarten\\redovalempty3.gif'), 'redovalfilled1.gif': pygame.image.load('C:\\Users\\yunus\\Downloads\\kaarten\\kaarten\\redovalfilled1.gif'), 'redovalfilled2.gif': pygame.image.load('C:\\Users\\yunus\\Downloads\\kaarten\\kaarten\\redovalfilled2.gif'), 'redovalfilled3.gif': pygame.image.load('C:\\Users\\yunus\\Downloads\\kaarten\\kaarten\\redovalfilled3.gif'), 'redovalshaded1.gif': pygame.image.load('C:\\Users\\yunus\\Downloads\\kaarten\\kaarten\\redovalshaded1.gif'), 'redovalshaded2.gif': pygame.image.load('C:\\Users\\yunus\\Downloads\\kaarten\\kaarten\\redovalshaded2.gif'), 'redovalshaded3.gif': pygame.image.load('C:\\Users\\yunus\\Downloads\\kaarten\\kaarten\\redovalshaded3.gif'), 'redsquiggleempty1.gif': pygame.image.load('C:\\Users\\yunus\\Downloads\\kaarten\\kaarten\\redsquiggleempty1.gif'), 'redsquiggleempty2.gif': pygame.image.load('C:\\Users\\yunus\\Downloads\\kaarten\\kaarten\\redsquiggleempty2.gif'), 'redsquiggleempty3.gif': pygame.image.load('C:\\Users\\yunus\\Downloads\\kaarten\\kaarten\\redsquiggleempty3.gif'), 'redsquigglefilled1.gif': pygame.image.load('C:\\Users\\yunus\\Downloads\\kaarten\\kaarten\\redsquigglefilled1.gif'), 'redsquigglefilled2.gif': pygame.image.load('C:\\Users\\yunus\\Downloads\\kaarten\\kaarten\\redsquigglefilled2.gif'), 'redsquigglefilled3.gif': pygame.image.load('C:\\Users\\yunus\\Downloads\\kaarten\\kaarten\\redsquigglefilled3.gif'), 'redsquiggleshaded1.gif': pygame.image.load('C:\\Users\\yunus\\Downloads\\kaarten\\kaarten\\redsquiggleshaded1.gif'), 'redsquiggleshaded2.gif': pygame.image.load('C:\\Users\\yunus\\Downloads\\kaarten\\kaarten\\redsquiggleshaded2.gif'), 'redsquiggleshaded3.gif': pygame.image.load('C:\\Users\\yunus\\Downloads\\kaarten\\kaarten\\redsquiggleshaded3.gif')
}

#het onderstaande verwijdert de meest oogverblindende kleuren
def goedgekleurd(r,g,b):
    if (((r == g == 14 or r == b == 14 or g == b == 14) == False) and
    ((r > 14 or g >14  or b > 14) and (22 > r+g+b or r+g+b > 30)) == False):
            return True

while goedgekleurd(r0, g0, b0) != True:
    r0, g0, b0 = rndm(1,16), rndm(1,16), rndm(1,16)

rd, gr, bl = r0**2 - 1, g0**2 - 1, b0**2 - 1

#zo zijn de dummyrechthoeken waar de kaarten op komen altijd zichtbaar
rd1, gr1, bl1 = (255 - rd), (255 - gr), (255 - bl)
timer = Timer(scherm, positie=(25,650))
timer_spel = pygame.USEREVENT + 1
pygame.time.set_timer(timer_spel, 1000)
aftellen = 30

spel = True
#start het spel
lekkerspelen = True
while lekkerspelen:

    #events
    for event in pygame.event.get():
        #hier kan mogelijk toetsenbord input
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                lekkerspelen == False
        #sluit het spel 
        elif event.type == pygame.QUIT:
            lekkerspelen = False
            spel = False
        else:
            if event.type == timer_spel:
                aftellen -= 1
                if aftellen <= 0:
                    print("beurt voorbij")
                    aftellen = 30
    #hier kan ook toetsenbord input
    toetsinvoer = pygame.key.get_pressed()
    
  
    
    #achtergrond kleur
    #a, b, c = 5, 13, 3 #voor mooi groene kleur, aangezien dit er één is kan het wel hier
    scherm.fill(((rd, gr, bl)))
    
    kaarthoeken = [Rect(40 + 100*i, 40 + 240*(i % 3), 90, 160) for i in range(12)]
    for rechthoek in kaarthoeken:
        pygame.draw.rect(scherm, (rd1, gr1, bl1), rechthoek)
    
    timer.teken(aftellen)
    #zonder deze line zie je niets
    pygame.display.flip()


    
#deze om pygame.init weer af te sluiten
pygame.quit()




