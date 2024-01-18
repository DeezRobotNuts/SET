import math, sys
class Kaart:
    def __init__(self, nummer, symbool, kleur, shading):
        self.nummer = nummer
        self.symbool = symbool
        self.kleur = kleur
        self.shading = shading
     
     #door deze functie worden de nummers van de kaarten  met elkaar vergleken, als ze hetzelfde zijn of ze zijn allemaal verschillend van elkaar dan gaat het returnen als true en anders is het false   
    def verglijk_nummer(self, kaart2, kaart3): 
        if self.nummer == kaart2.nummer == kaart3.nummer or (self.nummer != kaart2.nummer and self.nummer != kaart3.nummer and kaart2.nummer != kaart3.nummer):
            return True
        else:
            return False
        #door deze functie worden de symbolen van de kaarten met elkaar vergleken, als ze dezelfde zijn of ze zijn allemaal verschillend van elkaar dan gaat het returnen als true en anders is het false
    def verglijk_symbool(self, kaart2, kaart3):
        if self.symbool == kaart2.symbool == kaart3.symbool or (self.symbool != kaart2.symbool and self.symbool != kaart3.symbool and kaart2.symbool != kaart3.symbool):
            return True
        else:
            return False
        #door deze functie worden de kleur van de kaarten met elkaar vergleken, als ze dezelfde zijn of ze zijn allemaal verschillend van elkaar dan gaat het returnen als true en anders is het false
    def verglijk_kleur(self, kaart2, kaart3):
        if self.kleur == kaart2.kleur == kaart3.kleur or (self.kleur != kaart2.kleur and self.kleur != kaart3.kleur and kaart2.kleur != kaart3.kleur):
            return True
        else: 
            return False
    
    #door deze functie worden de shading van de kaarten met elkaar vergleken, als ze dezelfde zijn of ze zijn allemaal verschillend van elkaar dan gaat het returnen als true en anders is het false
    def verglijk_shading(self, kaart2, kaart3):
        if self.shading == kaart2.shading == kaart3.shading or (self.shading != kaart2.shading and self.shading != kaart3.shading and kaart2.shading != kaart3.shading):
            return True
        else:
            return False
    def set(self, kaart2, kaart3):
        return(self.verglijk_nummer(kaart2,kaart3) and self.verglijk_symbool(kaart2, kaart3) and self.verglijk_kleur(kaart2, kaart3) and self.verglijk_shading(kaart2, kaart3))
        
        
Kaart(0,0,0,1)