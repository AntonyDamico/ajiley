import pygame
from Mazo import Mazo
from Jugador import Jugador

mazo = Mazo()
jugadores = []
cartasSeleccionadas = []

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


def imprimitCarta(x, y, img):
    img = pygame.image.load(img)
    gameDisplay.blit(img, (x, y))

def mostrarPuntos(puntos):
    font = pygame.font.SysFont(None, 25)
    i = 0
    for pinta in puntos:
        texto = font.render(pinta + ": " + str(puntos[pinta]), True, blanco)
        gameDisplay.blit(texto, (anchoPantalla*0.65, (altoPantalla *0.75) + i))
        i += 20

def text_objects(text, font):
    textSurface = font.render(text, True, negro)
    return textSurface, textSurface.get_rect()


def botonCarta(msg, x, y, w, h, carta):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    s = pygame.Surface((w,h))
    s.fill((255,255,255))           

    if x+w > mouse[0] > x and y + h > mouse[1] > y:
        s.set_alpha(80)
        gameDisplay.blit(s, (x,y))
        if click[0] == 1:
            if carta not in cartasSeleccionadas:
                cartasSeleccionadas.append(carta)
    else:
        s.set_alpha(0)
        gameDisplay.blit(s, (x,y))

    smallText = pygame.font.Font('freesansbold.ttf', 20)
    TextSurf, TextRect = text_objects(msg, smallText)
    TextRect.center = ((x+(w/2)), (y+(h/2)))
    gameDisplay.blit(TextSurf, TextRect)

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
            imprimitCarta(x * (i + 1), y, cartasImagenes[i])
            if(i < len(cartasImagenes) - 1):
                botonCarta("", x * (i + 1), y, 100 - (20), 139, jugadores[0].getMano()[i])
            else:
                botonCarta("", x * (i + 1), y, 100, 139, jugadores[0].getMano()[i])

        for i in range(0, len(cartasSeleccionadas)):
            print(cartasSeleccionadas[i].mostrarCarta())
         
            
        mostrarPuntos(jugadores[0].getPuntos())
        
        # refrescando
        pygame.display.update()
        clock.tick(30)

gameLoop()