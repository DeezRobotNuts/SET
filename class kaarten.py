#import math, sys
class Kaart:
    def __init__(self, nummer, symbool, kleur, shading):
        self.a = nummer
        self.b = symbool
        self.c = kleur
        self.d = shading
     
     #door deze functie worden de as van de kaarten  met elkaar vergleken, als ze hetzelfde zijn of ze zijn allemaal verschillend van elkaar dan gaat het returnen als true en anders is het false   
    def verglijk_nummer(self, kaart2, kaart3): 
        if self.a == kaart2.a == kaart3.a or (self.a != kaart2.a and self.a != kaart3.a and kaart2.a != kaart3.a):
            return True
        else:
            return False
        #door deze functie worden de symbolen van de kaarten met elkaar vergleken, als ze dezelfde zijn of ze zijn allemaal verschillend van elkaar dan gaat het returnen als true en anders is het false
    def verglijk_symbool(self, kaart2, kaart3):
        if self.b == kaart2.b == kaart3.b or (self.b != kaart2.b and self.b != kaart3.b and kaart2.b != kaart3.b):
            return True
        else:
            return False
    def verglijk_kleur(self, kaart2, kaart3):
        if self.c == kaart2.c == kaart3.c or (self.c != kaart2.c and self.c != kaart3.c and kaart2.c != kaart3.c):
            return True
        else: 
            return False
    
    def verglijk_shading(self, kaart2, kaart3):
        if self.d == kaart2.d == kaart3.d or (self.d != kaart2.d and self.d != kaart3.d and kaart2.d != kaart3.d):
            return True
        else:
            return False
        