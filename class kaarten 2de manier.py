def verglijk_nummer(kaart1, kaart2, kaart3): 
     if kaart1.nummer == kaart2.nummer == kaart3.nummer or (kaart1.nummer != kaart2.nummer and kaart1.nummer != kaart3.nummer and kaart2.nummer != kaart3.nummer):
        return True
     else:
        return False

def verglijk_symbool(kaart1, kaart2, kaart3): 
     if kaart1.symbool == kaart2.symbool == kaart3.symbool or (kaart1.symbool != kaart2.symbool and kaart1.symbool != kaart3.symbool and kaart2.symbool != kaart3.symbool):
        return True
     else:
        return False

def verglijk_kleur(kaart1, kaart2, kaart3):
     if kaart1.kleur == kaart2.kleur == kaart3.kleur or (kaart1.kleur != kaart2.kleur and kaart1.kleur != kaart3.kleur and kaart2.kleur != kaart3.kleur):
        return True
     else:
        return False
def verglijk_shading(kaart1, kaart2, kaart3): 
     if kaart1.shading == kaart2.shading == kaart3.shading or (kaart1.shading != kaart2.shading and kaart1.shading != kaart3.shading and kaart2.shading != kaart3.shading):
        return True
     else:
        return False
def verglijk(kaart1, kaart2, kaart3):
    if verglijk_nummer(kaart1, kaart2 ,kaart3) and verglijk_symbool(kaart1,kaart2, kaart3) and verglijk_kleur(kaart1, kaart2, kaart3) and verglijk_shading(kaart1, kaart2, kaart3):
        return True
    else:
        return False
    
class Kaart:
    def __init__(self, nummer, symbool, kleur, shading):
        self.nummer = nummer
        self.symbool = symbool
        self.kleur = kleur
        self.shading = shading


#testen:
#card1 = Kaart(0,0,0,0)
#card2 = Kaart(1,1,1,1)
#card3 = Kaart(2,2,2,2)
#print(verglijk(card1, card2, card3))