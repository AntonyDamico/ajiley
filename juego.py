import pygame
from Mazo import Mazo
from Jugador import Jugador

mazo = Mazo()
jugador1 = Jugador(mazo)

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
for carta in jugador1.getMano():
    cartasImagenes.append(carta.getImg())



# cardImg = pygame.image.load("imagenes/cartas/copa/1.jpg")

def card(x, y, img):
    img = pygame.image.load(img)
    gameDisplay.blit(img, (x, y))

def gameLoop():

    x = (anchoPantalla*0.1)
    y = (altoPantalla*0.7)

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(verde)

        for i in range(0, len(cartasImagenes)):
            card(x * (i + 1), y, cartasImagenes[i])

        pygame.display.update()
        clock.tick(30)

gameLoop()