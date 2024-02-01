# SET
Ik ga een class proberen te maken voor de 12 plekken op "tafel" die geselecteerd kunnen worden, en die zelf een eigenschap hebben waar ze de Kaart-class in bewaren, misschien kan je ook kijken naar hoe je daar de plaatjes in krijgt?

De main file is nu alleen nog
  SET+kaartclass.py

Het fractions bestand zit er alleen in om weer even een idee te hebben van dingen die je met een class kan doen.
Het Pygame bestand is niet van ons, maar gewoon een vb van internet, nu om een idee te krijgen van dingen die je met pygame kan.

donzo:
  class voor kaarten;
  vergelijkingsmethode voor drie kaarten;
  algoritme voor het vinden van elke SET;
  meer #opmerkingen in de code;
  willekeurig één set kiezen

todo:
  verslag;
  getallen koppelen aan eigenschappen, of direct omschrijvingen invoeren, bijv kaart(1,~,rd,0),
  afbeeldingen koppelen aan vector/kaart;
  nog meer (praktische) #opmerkingen

gebruik dit om een class voor je timer te maken: de namen zijn natuurlijk van mijn Grid class dus kies dingen die voor de timer logisch zijn

van hier:

class Grid(pygame.sprite.Sprite):
    def __init__(self, positie, kleur):
        pygame.sprite.Sprite.__init__(self)
    #hier kunnen we de kaartafbeeldingen doen
        self.positie = positie
        self.kleur = kleur

        self.plek = self.plaatje.get_rect(left=(95 + 90*self.positie)
                                       ,top = (20 + 240*(self.positie % 3)))

        self.vlak = pygame.Surface([90, 160])
        self.vlak.fill(self.kleur)

        
  grid = [Grid(i, (rd1, gr1, bl1)) for i in range(12)]
  
  scherm.blit(grid[n].plaatje, grid[n].plek)

tot hier 
(erg naar dat als je deze anders dan README noemt hij niet meer automatisch op de homepagina staat)

