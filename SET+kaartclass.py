import pygame
from pygame import Rect

from random import randrange as rndm

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
    #het is ons alleen niet gelukt ongelijkheid van een attribuut transitief te maken van 2 kaarten naar alle drie: 
    #(groen, paars, rood) gaat prima met (rood, groen) (paars, rood) (rood, paars), maar je krijgt problemen met bijv (rood, groen, rood),
    #def __eq__(self, kaart2):

        
#twaalf handingevoerdekaarten voor het testen, later hebben we natuurlijk 12 wisselende kaarten
K1, K2, K3, K4, K5, K6, K7, K8, K9, K10, K11, K12 = (Kaart(0,0,0,0), Kaart(1,2,2,1), Kaart(1,2,1,0), Kaart(2,1,0,0),Kaart(2,2,2,2),
                                                     Kaart(1,1,2,1), Kaart(1,0,0,0), Kaart(2,1,2,1), Kaart(0,2,2,2), Kaart(1,1,1,0), Kaart(1,0,2,0), Kaart(0,2,0,1))

twaalfkaarten = [K1, K2, K3, K4, K5, K6, K7, K8, K9, K10, K11, K12]

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

      
#pygame spul vanaf hier
from pygame.locals import (K_1, K_2, K_3,
                           K_q, K_w, K_e,
                           K_a, K_s, K_d,
                           K_z, K_x, K_c)

#zo kan de module starten met shit doen
pygame.init()

#Resulotie van het spel
breed, hoog = 1280, 720
scherm = pygame.display.set_mode((breed, hoog))

#voor willekeurige achtergrond kleur zonder epilepsie te krijgen moet dit buiten de running loop
r0, g0, b0 = rndm(1,16), rndm(1,16), rndm(1,16)

def goedgekleurd(r,g,b):
    if (((r == g == 14 or r == b == 14 or g == b == 14) == False) and
    ((r > 14 or g >14  or b > 14) and (22 > r+g+b or r+g+b > 30)) == False):
            return True

while goedgekleurd(r0, g0, b0) != True:
    r0, g0, b0 = rndm(1,16), rndm(1,16), rndm(1,16)

rd, gr, bl = r0**2 - 1, g0**2 - 1, b0**2 - 1

rd1, gr1, bl1 = (255 - rd), (255 - gr), (255 - bl)

#z 
lekkerspelen = True
while lekkerspelen:

    #sluit de spel-loop als je het venster sluit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lekkerspelen = False

    #achtergrond kleur
    #a, b, c = 5, 13, 3 #voor mooi groene kleur, aangezien dit er één is kan het wel hier
    scherm.fill(((rd, gr, bl)))
    
    kaarthoeken = [Rect(40 + 100*i, 20, 90, 160) for i in range(12)]
    
    for rechthoek in kaarthoeken:
        pygame.draw.rect(scherm, (rd1, gr1, bl1), rechthoek)
    
    #pygame.key.get_pressed()
    #invoervak = pygame.Rect()
    #pygame.key.set_text_input_rect(invoervak)
   
    
    #zonder deze line zie je niets
    pygame.display.flip()


#deze om pygame.init weer af te sluiten
pygame.quit()





