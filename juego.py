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
actual = 0

negro = (0, 0, 0)
blanco = (255, 255, 255)
gris = (200, 200, 200)
rojo = (255, 0, 0)
verde = (0, 100, 0)
azul = (0, 0, 255)

anchoCarta = 100
altoCarta = 139
cartaAtras = "imagenes/cartas/atras/vertical.jpg"
fondo = "imagenes/fondo.jpg"

gameDisplay = pygame.display.set_mode((anchoPantalla, altoPantalla))
pygame.display.set_caption('Ajilei')
clock = pygame.time.Clock()

cartasImagenes = []
for carta in jugadores[0].getMano():
    cartasImagenes.append(carta.getImg())


def boton(msg, x, y, w, h, ic, ac, action=None, parameters=[]):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            if parameters:
                action(parameters[0])
            else:
                action()
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

    smallText = pygame.font.Font('freesansbold.ttf', 20)
    TextSurf, TextRect = text_objects(msg, smallText)
    TextRect.center = ((x+(w/2)), (y+(h/2)))
    gameDisplay.blit(TextSurf, TextRect)

def fondoPantalla(imagen):
    imagen = pygame.image.load(imagen)
    rect = imagen.get_rect()
    rect.left, rect.top = [0,0]
    gameDisplay.fill([255, 255, 255])
    gameDisplay.blit(imagen, rect)


def imprimirTexto(texto, x, y):
    font = pygame.font.SysFont(None, 25)
    texto = font.render(texto, True, blanco)
    gameDisplay.blit(texto, (x, y))


def imprimirImagen(x, y, img):
    img = pygame.image.load(img)
    gameDisplay.blit(img, (x, y))


def mostrarPuntos(puntos):
    i = 0
    for pinta in puntos:
        imprimirTexto(
            pinta + ": " + str(puntos[pinta]), anchoPantalla*0.65, (altoPantalla * 0.75) + i)
        i += 20


def text_objects(text, font):
    textSurface = font.render(text, True, negro)
    return textSurface, textSurface.get_rect()


def pasarTurno():
    global actual
    if actual < 3:
        actual += 1
    else:
        actual = 0
    cartasSeleccionadas.clear()


def cambiarCartas(jug):
    if cartasImagenes:
        jugadores[jug].cambiarCartas(cartasSeleccionadas, mazo)
        cartasSeleccionadas.clear()


def botonCarta(x, y, w, h, carta):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    s = pygame.Surface((w, h))
    s.fill(blanco)

    if x+w > mouse[0] > x and y + h > mouse[1] > y:
        s.set_alpha(80)
        gameDisplay.blit(s, (x, y))
        if click[0] == 1:
            if carta not in cartasSeleccionadas:
                cartasSeleccionadas.append(carta)
            else:
                cartasSeleccionadas.remove(carta)
    else:
        s.set_alpha(0)
        gameDisplay.blit(s, (x, y))


def imprimirCartas(jugadorCont):
    x = (anchoPantalla*0.1)
    y = (altoPantalla*0.7)
    i = 0
    for carta in jugadores[jugadorCont].getMano():
        if carta in cartasSeleccionadas:
            y = y - 20

        imprimirImagen(x * (i + 1), y, carta.getImg())
        if(i < len(cartasImagenes) - 1):
            botonCarta(x * (i + 1), y, anchoCarta -
                       anchoCarta * 0.2, 139, carta)
        else:
            botonCarta(x * (i + 1), y, 100, 139, carta)
        i += 1
        y = (altoPantalla*0.7)


def salirJuego():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()


def gameLoop():

    while True:

        salirJuego()

        # Dibujando
        # fondo
        gameDisplay.fill(verde)

        imprimirImagen(anchoPantalla*0.95 - anchoCarta, altoPantalla * 0.3, cartaAtras)
        imprimirImagen(anchoPantalla*0.05, altoPantalla * 0.3, cartaAtras)
        imprimirImagen(anchoPantalla*0.5 - anchoCarta/2, altoPantalla*0.01, cartaAtras)

        imprimirCartas(actual)

        mostrarPuntos(jugadores[actual].getPuntos())

        boton("Cambiar Carta", anchoPantalla * 0.80,
              altoPantalla * 0.75, 150, 30, blanco,
              gris, cambiarCartas, [actual])

        boton("Pasar Turno", anchoPantalla * 0.80,
              altoPantalla * 0.85, 150, 30, blanco, 
              gris, pasarTurno)

        # refrescando
        pygame.display.update()
        clock.tick(15)


gameLoop()
