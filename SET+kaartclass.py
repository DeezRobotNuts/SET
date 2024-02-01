import pygame

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

#print(kiesSET(twaalfkaarten))
    


###ik weet nog niet hoe je de gifs toe moetvoegen aan de code zelf etc dus ik heb alleen de fotos gekoppeld aan een ding + het lukte niet met letters zoals jij had gezegd
kaart_eigenschappen = {
    'greendiamondempty1.gif': (0,0,0,0), 'greendiamondempty2.gif':(1,0,0,0), 'greendiamondempty3.gif': (2,0,0,0), 'greendiamondfilled1.gif': (0,0,0,1), 'greendiamondfilled2.gif': (1,0,0,1), 'greendiamondfilled3.gif': (2,0,0,1), 'greendiamondshaded1.gif': (0,0,0,2), 'greendiamondshaded2.gif': (1,0,0,2), 'greendiamondshaded3.gif': (2,0,0,2), 'greenovalempty1.gif': (0,1,0,0), 'greenovalempty2.gif': (1,1,0,0), 'greenovalempty3.gif': (2,1,0,0), 'greenovalfilled1.gif': (0,1,0,1), 'greenovalfilled2.gif': (1,1,0,1), 'greenovalfilled3.gif': (2,1,0,1), 'greenovalshaded1.gif': (0,1,0,2), 'greenovalshaded2.gif': (1,1,0,2), 'greenovalshaded3.gif': (2,1,0,2), 'greensquiggleempty1.gif': (0,2,0,0), 'greensquiggleempty2.gif': (1,2,0,0), 'greensquiggleempty3.gif': (2,2,0,0), 'greensquigglefilled1.gif': (0,2,0,1), 'greensquigglefilled2.gif': (1,2,0,1), 'greensquigglefilled3.gif': (2,2,0,1), 'greensquiggleshaded1.gif': (0,2,0,2), 'greensquiggleshaded2.gif': (1,2,0,2), 'greensquiggleshaded3.gif': (2,2,0,2),
    'purplediamondempty1.gif': (0,0,1,0), 'purplediamondempty2.gif': (1,0,1,0), 'purplediamondempty3.gif': (2,0,1,0), 'purplediamondfilled1.gif': (0,0,1,1), 'purplediamondfilled2.gif': (1,0,1,1), 'purplediamondfilled3.gif': (2,0,1,1), 'purplediamondshaded1.gif': (0,0,1,2), 'purplediamondshaded2.gif': (1,0,1,2), 'purplediamondshaded3.gif': (2,0,1,2), 'purpleovalempty1.gif': (0,1,1,0), 'purpleovalempty2.gif': (1,1,1,0), 'purpleovalempty3.gif': (2,1,1,0), 'purpleovalfilled1.gif': (0,1,1,1), 'purpleovalfilled2.gif': (1,1,1,1), 'purpleovalfilled3.gif': (2,1,1,1), 'purpleovalshaded1.gif': (0,1,1,2), 'purpleovalshaded2.gif': (1,1,1,2), 'purpleovalshaded3.gif': (2,1,1,2), 'purplesquiggleempty1.gif': (0,2,1,0), 'purplesquiggleempty2.gif': (1,2,1,0), 'purplesquiggleempty3.gif': (2,2,1,0), 'purplesquigglefilled1.gif': (0,2,1,1), 'purplesquigglefilled2.gif': (1,2,1,1), 'purplesquigglefilled3.gif': (2,2,1,1), 'purplesquiggleshaded1.gif': (0,2,1,2), 'purplesquiggleshaded2.gif': (1,2,1,2), 'purplesquiggleshaded3.gif': (2,2,1,2), 'reddiamondempty1.gif': (0,0,2,0), 'reddiamondempty2.gif': (1,0,2,0), 'reddiamondempty3.gif': (2,0,2,0), 'reddiamondfilled1.gif': (0,0,2,1), 'reddiamondfilled2.gif': (1,0,2,1), 'reddiamondfilled3.gif': (2,0,2,1), 'reddiamondshaded1.gif': (0,0,2,2), 'reddiamondshaded2.gif': (1,0,2,2), 'reddiamondshaded3.gif': (2,0,2,2), 'redovalempty1.gif': (0,1,2,0), 'redovalempty2.gif': (1,1,2,0), 'redovalempty3.gif': (2,1,2,0), 'redovalfilled1.gif': (0,1,2,1), 'redovalfilled2.gif': (1,1,2,1), 'redovalfilled3.gif': (2,1,2,1), 'redovalshaded1.gif': (0,1,2,2), 'redovalshaded2.gif': (1,1,2,2), 'redovalshaded3.gif': (2,1,2,2),
    'redsquiggleempty1.gif': (0,2,2,0), 'redsquiggleempty2.gif': (1,2,2,0), 'redsquiggleempty3.gif': (2,2,2,0), 'redsquigglefilled1.gif': (0,2,2,1), 'redsquigglefilled2.gif': (1,2,2,1), 'redsquigglefilled3.gif': (2,2,2,1), 'redsquiggleshaded1.gif': (0,2,2,2), 'redsquiggleshaded2.gif': (1,2,2,2), 'redsquiggleshaded3.gif': (2,2,2,2)
}

#print(kaart_eigenschappen['redsquigglefilled1.gif']) dit is voor test
      
#pygame spul vanaf hier, aanzetten als je het spel test:
pygame.init()

#Resulotie van het spel
screen = pygame.display.set_mode([800,600])

#voor willekeurige achtergrond kleur zonder epilepsie te krijgen moet dit buiten de running loop
a, b, c = rndm(1,17), rndm(1,17), rndm(1,17)

#zo kan het spel aan 
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #achtergrond kleur
    #a, b, c = 5, 13, 3 #voor mooi groene kleur, aangezien dit er één is kan het wel hier
    screen.fill(((a**2 -1), (b**2 -1), (c**2 -1)))


#ik weet niet waarom dit nodig is, maar zonder deze line zie je niets
    pygame.display.flip()

#deze om pygame.init weer af te sluiten
pygame.quit()





