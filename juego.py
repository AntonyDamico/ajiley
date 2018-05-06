import pygame
from Mazo import Mazo
from Jugador import Jugador

mazo = Mazo()
jugadores = []

for i in range(0, 4):
    jugadores.append(Jugador(mazo))

pygame.init()

anchoPantalla = 800
altoPantalla = 600

negro = (0, 0, 0)
blanco = (255, 255, 255)
rojo = (255, 0, 0)
verde = (0, 100, 0)
azul = (0, 0, 255)

anchoCarta = 100
altoCarta = 139

gameDisplay = pygame.display.set_mode((anchoPantalla, altoPantalla))
pygame.display.set_caption('Ajilei')
clock = pygame.time.Clock()

cartasImagenes = []
for carta in jugadores[0].getMano():
    cartasImagenes.append(carta.getImg())


# cardImg = pygame.image.load("imagenes/cartas/copa/1.jpg")

def card(x, y, img):
    img = pygame.image.load(img)
    gameDisplay.blit(img, (x, y))

def mostrarPuntos(puntos):
    font = pygame.font.SysFont(None, 25)
    i = 0
    for pinta in puntos:
        texto = font.render(pinta + ": " + str(puntos[pinta]), True, blanco)
        gameDisplay.blit(texto, (anchoPantalla*0.65, (altoPantalla *0.75) + i))
        i += 20

def gameLoop():

    x = (anchoPantalla*0.1)
    y = (altoPantalla*0.7)

    # gameExit = False

    while True:
        # Cerrando el juego
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Dibujando
        # fondo
        gameDisplay.fill(verde)

        for i in range(0, len(cartasImagenes)):
            card(x * (i + 1), y, cartasImagenes[i])
            
        mostrarPuntos(jugadores[0].getPuntos())
        
        # refrescando
        pygame.display.update()
        clock.tick(30)

gameLoop()