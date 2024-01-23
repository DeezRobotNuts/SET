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
        #door deze functie worden de kleur van de kaarten met elkaar vergleken, als ze dezelfde zijn of ze zijn allemaal verschillend van elkaar dan gaat het returnen als true en anders is het false
    def verglijk_kleur(self, kaart2, kaart3):
        if self.c == kaart2.c == kaart3.c or (self.c != kaart2.c and self.c != kaart3.c and kaart2.c != kaart3.c):
            return True
        else: 
            return False
    
    #door deze functie worden de shading van de kaarten met elkaar vergleken, als ze dezelfde zijn of ze zijn allemaal verschillend van elkaar dan gaat het returnen als true en anders is het false
    def verglijk_shading(self, kaart2, kaart3):
        if self.d == kaart2.d == kaart3.d or (self.d != kaart2.d and self.d != kaart3.d and kaart2.d != kaart3.d):
            return True
        else:
            return False
    #hier checken we de 3kaarten en kijken of het uiteindelijke waarde true of false is, dit hebben we gedaan doormiddel van de functies met elkaar te verglijken, als alle 4 de functies waarde true geeft dan geeft deze functie ook de waarde true aan en anders geeft het false aan.
    def verglijk(self, kaart2, kaart3):
        if verglijk_nummer(self, kaart2 ,kaart3) and self.verglijk_symbool(kaart2, kaart3) and self.verglijk_kleur(kaart2, kaart3) and self.verglijk_shading(kaart2, kaart3):
            return True
        else:
            return False


#zo kan je het testen
#card1 = Kaart(0,0,0,0)
#card2 = Kaart(1,1,1,1)
#card3 = Kaart(2,2,2,2)

#print(card1.verglijk(card2, card3))
  
  
 #we doen dit aan het einde als we tijd hebben en willen veranderen, we halen de functies uit class zelf en voegen __eq__ toe aan de class en alle 4 functies gaan uit de class, later gaan we met __eq__ de true en false doen, dit is aangeraden door een leeraar de andere leeraar zegt dat wat wij aan het doen zijn ook goed is.
#def verglijk_nummer(kaart1, kaart2, kaart3): 
     #if kaart1.a == kaart2.a == kaart3.a or (kaart1.a != kaart2.a and kaart1.a != kaart3.a and kaart2.a != kaart3.a):
        #return True
     #else:
        #return False
        