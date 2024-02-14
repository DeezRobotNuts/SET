import pygame
from pygame import Rect
#deze toetsen wil ik graag om de kaarten in te voeren, paar extra om uit te vinden wat goed voelt
from pygame.locals import (K_1, K_2, K_3, K_4,
                           K_q, K_w, K_e, K_r,
                           K_a, K_s, K_d, K_f,
                           K_z, K_x, K_c, K_v)
import random
from random import randrange as rndm
from random import shuffle

def verglijk_nummer(kaart1, kaart2, kaart3): 
     if kaart1.nummer == kaart2.nummer == kaart3.nummer or (kaart1.nummer != kaart2.nummer and kaart1.nummer != kaart3.nummer and kaart2.nummer != kaart3.nummer):
        return True
     else:
        return False
#de notequal delen kunnen natuurlijk veel sneller door gewoon een laatste ongelijkheid achter twee ongelijkheden te zetten, maar ja het staat er nu toch al zo
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

#hier de eerst fout ingevoerde kaarten en het werk om ze daadwerkelijk tot de bruikbare class te maken, om te laten zien dat we niet op onze reet hebben gezeten mocht het niet afkomen
kaart_eigenschappen = {
        'greendiamondempty1.gif': (0,0,0,0), 'greendiamondempty2.gif':(1,0,0,0), 'greendiamondempty3.gif': (2,0,0,0), 'greendiamondfilled1.gif': (0,0,0,1), 'greendiamondfilled2.gif': (1,0,0,1), 'greendiamondfilled3.gif': (2,0,0,1), 'greendiamondshaded1.gif': (0,0,0,2), 'greendiamondshaded2.gif': (1,0,0,2), 'greendiamondshaded3.gif': (2,0,0,2), 'greenovalempty1.gif': (0,1,0,0), 'greenovalempty2.gif': (1,1,0,0), 'greenovalempty3.gif': (2,1,0,0), 'greenovalfilled1.gif': (0,1,0,1), 'greenovalfilled2.gif': (1,1,0,1), 'greenovalfilled3.gif': (2,1,0,1), 'greenovalshaded1.gif': (0,1,0,2), 'greenovalshaded2.gif': (1,1,0,2), 'greenovalshaded3.gif': (2,1,0,2), 'greensquiggleempty1.gif': (0,2,0,0), 'greensquiggleempty2.gif': (1,2,0,0), 'greensquiggleempty3.gif': (2,2,0,0), 'greensquigglefilled1.gif': (0,2,0,1), 'greensquigglefilled2.gif': (1,2,0,1), 'greensquigglefilled3.gif': (2,2,0,1), 'greensquiggleshaded1.gif': (0,2,0,2), 'greensquiggleshaded2.gif': (1,2,0,2), 'greensquiggleshaded3.gif': (2,2,0,2),
        'purplediamondempty1.gif': (0,0,1,0), 'purplediamondempty2.gif': (1,0,1,0), 'purplediamondempty3.gif': (2,0,1,0), 'purplediamondfilled1.gif': (0,0,1,1), 'purplediamondfilled2.gif': (1,0,1,1), 'purplediamondfilled3.gif': (2,0,1,1), 'purplediamondshaded1.gif': (0,0,1,2), 'purplediamondshaded2.gif': (1,0,1,2), 'purplediamondshaded3.gif': (2,0,1,2), 'purpleovalempty1.gif': (0,1,1,0), 'purpleovalempty2.gif': (1,1,1,0), 'purpleovalempty3.gif': (2,1,1,0), 'purpleovalfilled1.gif': (0,1,1,1), 'purpleovalfilled2.gif': (1,1,1,1), 'purpleovalfilled3.gif': (2,1,1,1), 'purpleovalshaded1.gif': (0,1,1,2), 'purpleovalshaded2.gif': (1,1,1,2), 'purpleovalshaded3.gif': (2,1,1,2), 'purplesquiggleempty1.gif': (0,2,1,0), 'purplesquiggleempty2.gif': (1,2,1,0), 'purplesquiggleempty3.gif': (2,2,1,0), 'purplesquigglefilled1.gif': (0,2,1,1), 'purplesquigglefilled2.gif': (1,2,1,1), 'purplesquigglefilled3.gif': (2,2,1,1), 'purplesquiggleshaded1.gif': (0,2,1,2), 'purplesquiggleshaded2.gif': (1,2,1,2), 'purplesquiggleshaded3.gif': (2,2,1,2), 'reddiamondempty1.gif': (0,0,2,0), 'reddiamondempty2.gif': (1,0,2,0), 'reddiamondempty3.gif': (2,0,2,0), 'reddiamondfilled1.gif': (0,0,2,1), 'reddiamondfilled2.gif': (1,0,2,1), 'reddiamondfilled3.gif': (2,0,2,1), 'reddiamondshaded1.gif': (0,0,2,2), 'reddiamondshaded2.gif': (1,0,2,2), 'reddiamondshaded3.gif': (2,0,2,2), 'redovalempty1.gif': (0,1,2,0), 'redovalempty2.gif': (1,1,2,0), 'redovalempty3.gif': (2,1,2,0), 'redovalfilled1.gif': (0,1,2,1), 'redovalfilled2.gif': (1,1,2,1), 'redovalfilled3.gif': (2,1,2,1), 'redovalshaded1.gif': (0,1,2,2), 'redovalshaded2.gif': (1,1,2,2), 'redovalshaded3.gif': (2,1,2,2),
        'redsquiggleempty1.gif': (0,2,2,0), 'redsquiggleempty2.gif': (1,2,2,0), 'redsquiggleempty3.gif': (2,2,2,0), 'redsquigglefilled1.gif': (0,2,2,1), 'redsquigglefilled2.gif': (1,2,2,1), 'redsquigglefilled3.gif': (2,2,2,1), 'redsquiggleshaded1.gif': (0,2,2,2), 'redsquiggleshaded2.gif': (1,2,2,2), 'redsquiggleshaded3.gif': (2,2,2,2)}

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
  
    n = len(kaarten)
    teller = 0

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

#we moeten de bot een van de sets laten kiezen (het liefst eerste van de sets)
def kiesSET(kaarten):
    SETs, showSETs = elkeSET(kaarten)
    n = len(SETs)
    if n == 0:
        return "CAP"
    else:
        r = rndm(0,n)
        a, b = SETs[r], showSETs[r]
        return a, b
    

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

#Resolutie van het spelscherm
breed, hoog = 1280, 720
scherm = pygame.display.set_mode((breed, hoog))

#voor willekeurige achtergrond kleur zonder epilepsie te krijgen moet dit buiten de running loop
r0, g0, b0 = rndm(1,16), rndm(1,16), rndm(1,16)

#het onderstaande verwijdert de meest oogverblindende kleuren
def goedgekleurd(r,g,b):
    if (((r == g == 14 or r == b == 14 or g == b == 14) == False) and
    ((r > 14 or g >14  or b > 14) and (22 > r+g+b or r+g+b >28)) == False):
            return True
        
while goedgekleurd(r0, g0, b0) != True:
    r0, g0, b0 = rndm(1,16), rndm(1,16), rndm(1,16)

rd, gr, bl = r0**2 - 1, g0**2 - 1, b0**2 - 1
#zo zijn de dummyrechthoeken waar de kaarten op komen altijd zichtbaar
(rd1, gr1, bl1) = (255 - rd), (255 - gr), (255 - bl)

#gebruik één van de twee dict/lijstcombos
kaartdict, altdict, kaartlijst, altlijst = en_nu_goed_om(kaart_eigenschappen)


#ons probeersel om de kaart class van eerder op het spelbord te krijgen
class Grid(pygame.sprite.Sprite):
    def __init__(self, positie, kleur):
        pygame.sprite.Sprite.__init__(self)
    #hier kunnen we de kaartafbeeldingen doen
        self.positie = positie
        self.kleur = kleur
        
        self.kaart = altlijst[rndm(81)]
        
        self.plaatje = pygame.image.load(altdict[self.kaart]).convert()
        self.plaatje.set_colorkey((self.kleur), pygame.RLEACCEL)
        
        self.rij, self.kolom = divmod(self.positie, 4)
            
        self.plek = self.plaatje.get_rect(left=(95 + 270*self.kolom)
                                       ,top = (20 + 240*(self.rij)))
        self.gekozen = False
        
#deze class is niet af en het moet nu echt ingeleverd, maar wie weet klooien we er later nog mee dus laat'n we hem blijven
class textinput(pygame.sprite.Sprite):
    def __init__(self, kleur):
        self.kleur = kleur
        
        self.vlak = pygame.Surface([100, 100])
        self.vlak.fill(self.kleur)
        self.plek = self.vlak.get_rect(right= 20, top = 20)
        self.font = pygame.font.SysFont(None,120)
        self.text = ""
        
        def maak(self, scherm):
            scherm.blit(self.tekst, (self.plek))
            pygame.draw.Rect(self.scherm, self.kleur, self.plek)
        
grid = [Grid(i, (rd1, gr1, bl1)) for i in range(12)]

# dit is om te testen of de invoer werkt, maar niet valsspelen: laat het zo tijdens het spelen
"""lijst = []
for i in range(12):
    lijst.append(grid[i].kaart)
print(elkeSET(lijst))"""

#timer
timer = Timer(scherm, positie=(25,650))
timer_spel = pygame.USEREVENT + 1
pygame.time.set_timer(timer_spel, 1000)
aftellen = 30

#simpelere maar minder flexibele textinvoer omdat de textvak class niet af is
tekstinvoer = ""
lettertype = pygame.font.SysFont(None,40)


spel = True #waarom moet deze erbij @Yunus?

#start het spel
lekkerspelen = True

puntenpc = 0
puntenspeler = 0
while lekkerspelen:
    #events
    for event in pygame.event.get():
        #sluit het spel
        if event.type == pygame.QUIT:
            lekkerspelen = False
            spel = False
            
        elif event.type == timer_spel:
            aftellen -= 1
            if aftellen <= 0 and len(elkeSET([grid[i].kaart for i in range(12)])[0]) ==0 :
                print("niksaanhethandje") #dit moest natuurlijk ingame
                #hadden de computer dezemmoeten laten weghalen en een punt krijgen
            else:
                kiesSET(([grid[i].kaart for i in range(12)]))
                aftellen = 30
        
        #hier past toetsenbord input
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                lekkerspelen == False
            #onderstaande zorgt ervoor dat backspace, tekst, spatie en enter intuitief werken voor tekstinvoer
            elif event.key == pygame.K_BACKSPACE:
                tekstinvoer = tekstinvoer[:-1]
            else:
                tekstinvoer += event.unicode
                if event.key == pygame.K_RETURN:
                    a, b, c = tekstinvoer.split()
                    a, b, c = int(a), int(b), int(c)
                    if verglijk(grid[a].kaart, grid[b].kaart, grid[c].kaart):
                        tekstinvoer = "lekkerbezig"
            
#helaas heb ik heel veel code die veel smoother was niet goed geimplementeerd gekregen
        """if event.key == pygame.K_BACKSPACE:
            if event.key == pygame.K_DELETE:
                for i in range(3):
                    a = grid[i].kaart
                    while a == grid[i].kaart:                             a = altlijst[rndm(81)]
                    grid[i].kaart = a
                puntenpc += 1
                #teller = 0
                setje = []
                pygame.event.clear"""
            
    
    
    
    #achtergrond kleur
    #rd, gr, bl = 5, 13, 3 #voor mooi groene kleur, aangezien dit er één is kan het wel hier
    scherm.fill(((rd, gr, bl)))
    
    textvlak = lettertype.render(tekstinvoer,True, (rd1, gr1, bl1))
    scherm.blit(textvlak,(1100, 50))
    
    timer.teken(aftellen)
    
    for n in range(len(grid)):
        scherm.blit(grid[n].plaatje, grid[n].plek)
    #zonder deze line zie je niets
    pygame.display.flip()


#deze om pygame.init weer af te sluiten
pygame.quit()





