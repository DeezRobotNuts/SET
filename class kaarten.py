import math, sys
class Kaart:
    def __init__(self, nummer, symbool, kleur, shading):
        self.nummer = nummer
        self.symbool = symbool
        self.kleur = kleur
        self.shading = shading
        
    def verglijk_nummer(self, kaart2, kaart3):
        if self.nummer == kaart2.nummer == kaart3.nummer or (self.nummer != kaart2.nummer and self.nummer != kaart3.nummer and kaart2.nummer != kaart3.nummer):
            return True
        else:
            return False
    def verglijk_symbool(self, kaart2, kaart3):
        if self.symbool == kaart2.symbool == kaart3.symbool or (self.symbool != kaart2.symbool and self.symbool != kaart3.symbool and kaart2.symbool != kaart3.symbool):
            return True
        else:
            return False
    def verglijk_kleur(self, kaart2, kaart3):
        if self.kleur == kaart2.kleur == kaart3.kleur or (self.kleur != kaart2.kleur and self.kleur != kaart3.kleur and kaart2.kleur != kaart3.kleur):
            return True
        else: 
            return False
    
    def verglijk_shading(self, kaart2, kaart3):
        self.shading == kaart2.shading == kaart3.shading or (self.shading != kaart2.shading and self.shading != kaart3.shading and kaart2.shading != kaart3.shading)
        