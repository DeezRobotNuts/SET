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

(erg naar dat als je deze anders dan README noemt hij niet meer automatisch op de homepagina staat)

# Create custom events for adding a new enemy and a cloud
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)
ADDCLOUD = pygame.USEREVENT + 2
pygame.time.set_timer(ADDCLOUD, 1000)
