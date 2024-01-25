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
    #we kunnen mogelijk "==" betekenis geven voor onze class om de vergelijkfunctie wat eleganter te maken
    #def __eq__(self, kaart2):
        #if self.nummer == kaart2.nummer and 

        
        
#twaalf handingevoerdekaarten voor het testen, later hebben we natuurlijk 12 wisselende kaarten
K1, K2, K3, K4, K5, K6, K7, K8, K9, K10, K11, K12 = (Kaart(0,0,0,0), Kaart(1,2,2,1), Kaart(1,2,1,0), Kaart(2,1,0,0),Kaart(2,2,2,2),
                                                     Kaart(1,1,2,1), Kaart(1,0,0,0), Kaart(2,1,2,1), Kaart(0,2,2,2), Kaart(1,1,1,0), Kaart(1,0,2,0), Kaart(0,2,0,1))

twaalfkaarten = [K1, K2, K3, K4, K5, K6, K7, K8, K9, K10, K11, K12]

def elkeSET(lijst):
    #voor nu een dict ipv een list voor de SETs, voor het geval we andere indices dan gewone getallen willen voor pygame (nog niet naar gekeken), ook meen ik dat dict intern sneller is
    SETs = {}
    n = len(lijst)
    teller = 0
    for i in range(0, n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if verglijk(lijst[i], lijst[j], lijst[k]) == True:
                    SETs[teller] = lijst[i], lijst[j], lijst[k]
                    teller += 1
                else:
                    pass #voor nu
    return SETs
        

print(elkeSET(twaalfkaarten))

#we moeten de bot een van de sets laten kiezen (het liefst eerste van de sets)
def kiesSET():
    n = 1
    random(0,81)
    a = elkeSET(twaalfkaarten)[r]
    print(a)

b = rndm(0,81)
print(b)