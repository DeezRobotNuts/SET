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
    #   ...pygame.image.load('C:\\Users\\yunus\\Downloads\\kaarten\\kaarten\\greendiamondempty1.gif')
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
    

class Timer:
    def __init__(self,scherm, duur =30, font_grootte = 30,positie=(1100,100)):
        self.scherm = scherm
        self.duur = duur
        self.tijd_over = duur
        self.positie = positie
        self.font = pygame.font.Font(None,font_grootte)

    def reset(self):
        self.tijd_over = self.duur
    
    def update(self):
        self.tijd_over -= 1
        if self.tijd_over <= 0:
            self.reset()
    
    def teken(self,tijd_over):
        tijd_tekst = self.font.render(f"tijd over {tijd_over}", True, (rd1,gr1,bl1))
        self.scherm.blit(tijd_tekst, self.positie)
        
#zo kan de module starten met shit doen
pygame.init()
pygame.font.init()
random_font = pygame.font.SysFont(None, 30)
zwarte_font = pygame.font.SysFont(None, 30)
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

lijst = []
for i in range(12):
    lijst.append(grid[i].kaart)
print(elkeSET(lijst))

#timer
timer = Timer(scherm, positie=(1100,100))
timer_spel = pygame.USEREVENT + 1
pygame.time.set_timer(timer_spel, 1000)


#textinvoer omdat de Texvak class nog niet af is
tekstinvoer = ""
lettertype = pygame.font.SysFont(None,40)


#spel = True #waarom moet deze erbij @Yunus?

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
            timer.update()
            if timer.tijd_over <= 0:
                print("beurt voorbij")
                timer.update = timer.duur
                
        #hier past toetsenbord input
        elif event.type == pygame.KEYDOWN:
             if event.key == pygame.K_UP:
                timer.duur = 15  #druk op arrow key up zodat timer 15 sec is
                timer.reset()
             elif event.key == pygame.K_DOWN:
                timer.duur = 30  #druk op arrow key down zodat timer 30 sec is
                timer.reset()
             elif event.key == pygame.K_LEFT:
                timer.duur = 45  #druk op arrow key left zodat timer 45 sec is
                timer.reset()
             elif event.key == pygame.K_ESCAPE:
                lekkerspelen == False
             elif event.key == pygame.K_RSHIFT:
                 puntenspeler += 1
                 #als je op right shift drukt krijgt speler 1 punt.
             elif event.key == pygame.K_RCTRL:
                 puntenpc += 1
                 #als je op right ctrl drukt krijgt de pc 1 punt.
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
    
    kaart1 = zwarte_font.render(f'->1', True, (rd1,gr1,bl1))
    scherm.blit(kaart1, (200,100))
    kaart2 = zwarte_font.render(f'->2', True, (rd1,gr1,bl1))
    scherm.blit(kaart2, (475,100))
    kaart3 = zwarte_font.render(f'->3', True, (rd1,gr1,bl1))
    scherm.blit(kaart3, (750,100))
    kaart4 = zwarte_font.render(f'->4', True, (rd1,gr1,bl1))
    scherm.blit(kaart4, (1025,100))
    kaart5 = zwarte_font.render(f'->5', True, (rd1,gr1,bl1))
    scherm.blit(kaart5, (200,350))
    kaart6 = zwarte_font.render(f'->6', True, (rd1,gr1,bl1))
    scherm.blit(kaart6, (475,350))
    kaart7 = zwarte_font.render(f'->7', True, (rd1,gr1,bl1))
    scherm.blit(kaart7, (750,350))
    kaart8 = zwarte_font.render(f'->8', True, (rd1,gr1,bl1))
    scherm.blit(kaart8, (1025,350))
    kaart9 = zwarte_font.render(f'->9', True, (rd1,gr1,bl1))
    scherm.blit(kaart9, (200,585))
    kaart10 = zwarte_font.render(f'->10', True, (rd1,gr1,bl1))
    scherm.blit(kaart10, (475,585))
    kaart11 = zwarte_font.render(f'->11', True, (rd1,gr1,bl1))
    scherm.blit(kaart11, (750,585))
    kaart12 = zwarte_font.render(f'->12', True, (rd1,gr1,bl1))
    scherm.blit(kaart12, (1025,585))
    
    
    tekst_score_speler = random_font.render(f'speler punten: {puntenspeler}', True, (rd1, gr1, bl1))
    scherm.blit(tekst_score_speler, (1100, 150))
    
    tekst_score_pc = random_font.render(f'pc punten: {puntenpc}', True, (rd1, gr1, bl1))
    scherm.blit(tekst_score_pc, (1100, 200))
    
    textvlak = lettertype.render(tekstinvoer,True, (rd1, gr1, bl1))
    scherm.blit(textvlak,(1100, 50))
    
    timer.teken(timer.tijd_over)
    
    for n in range(len(grid)):
        scherm.blit(grid[n].plaatje, grid[n].plek)
    #zonder deze line zie je niets
    pygame.display.flip()


#deze om pygame.init weer af te sluiten
pygame.quit()




