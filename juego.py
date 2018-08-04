# pylint: disable=E1101
# pylint: disable=E1121
"""
Archivo principal del juego, este es el que se debe correr en consola

---------------------
python juego.py
---------------------
"""

import pygame
from Mazo import Mazo
from Jugador import Jugador

"""
Variables Globales
"""

# Objeto mazo para el juego
mazo = Mazo()
# Array que se va a llenar de objetos Jugador
jugadores = []
# Array que se usa para almacenar las cartas que un jugador desea cambiar
cartasSeleccionadas = []


intro = True
jugando = True
pantallaPuntos = False
puedeCambiarCartas = True

# El array se llena de 4 jugadores
# for i in range(0, 4):
#     jugadores.append(Jugador(mazo))

"""
Iniciando pygame
"""
pygame.init()
global gameDisplay
# Dimensiones del juego
anchoPantalla = 1000
altoPantalla = 500

# Index del array de jugadores del que tiene el turno actual
turnoActual = 0

# Colores comunes
negro = (0, 0, 0)
blanco = (255, 255, 255)
gris = (200, 200, 200)
rojo = (255, 0, 0)
verde = (40, 150, 40)
azul = (0, 0, 255)

# Dimensiones de las imágenes de las cartas
anchoCarta = 100
altoCarta = 139
# Ruta a la imágen de la parte de atras de las cartas
cartaAtras = "imagenes/cartas/atras/vertical.jpg"
# Ruta a la imágen del fondo del tablero
fondo = "imagenes/fondo.jpg"

# Haciendo el juego visible con las dimensiones dadas
gameDisplay = pygame.display.set_mode((anchoPantalla, altoPantalla))
# Nombre de la ventana del juego
pygame.display.set_caption('Ajilei')
clock = pygame.time.Clock()

# Llenando array con las imágenes de las cartas del jugador actual
cartasImagenes = []
# for carta in jugadores[0].getMano():
#     cartasImagenes.append(carta.getImg())


def boton(msg, x, y, w, h, ic, ac, action=None, parameters=[], fuenteTam=20):
    """
    Función para crear un botón
    Parámetros
    ----------
    arg1 str msg: Mensaje del botón
    arg2 int x: posición x del botón
    arg3 int y: posición y del botón 
    arg4 int w: ancho del botón
    arg5 int h: alto del botón
    arg6 array ic: color del botón cuando no tiene el cursor encima
    arg7 array ac: color del botón cuando tiene el cursor encima
    arg8 function action: función que va a realizar el botón
    arg9 array parameters: parametrós para la función del botón
    
    """

    # Posición del cursor
    mouse = pygame.mouse.get_pos()
    # Dice si el boton ha sido presionado o no
    click = pygame.mouse.get_pressed()
     
    if x+w > mouse[0] > x and y + h > mouse[1] > y:
        # Si el cursor está encima del botón, cambia a su color activo (ac)
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        # Comprueba si el botón fue presionado y posee alguna opción
        if click[0] == 1 and action != None:
            if parameters:
                action(parameters[0])
            else:
                action()
    else:
        # Dibuja el botón con su color inactivo
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

    # Fuente y tamano del texto del botón
    textButton = pygame.font.Font('freesansbold.ttf', fuenteTam)
    TextSurf, TextRect = text_objects(msg, textButton)
    # Posicionando el botón
    TextRect.center = ((x+(w/2)), (y+(h/2)))
    # Poniendo el botón en pantalla
    gameDisplay.blit(TextSurf, TextRect)

def fondoPantalla(imagen):
    
    """
    Agrega la imágen de fondo a la ventana

    Parametros
    ----------
    arg1 str: Ruta de la imágen de fondo
    """
    imagen = pygame.image.load(imagen)
    rect = imagen.get_rect()
    rect.left, rect.top = [0,0]
    gameDisplay.fill([255, 255, 255])
    gameDisplay.blit(imagen, rect)


def imprimirTexto(texto, x, y, tam = 25):
    """
    Imprime un texto en la pantalla dada una posición

    Parámetros
    ----------
    arg1 str texto: Texto que se desea imprimir
    arg2 int x: posición x del texto
    arg2 int y: posición y del texo
    """
    font = pygame.font.SysFont(None, tam)
    texto = font.render(texto, True, negro)
    gameDisplay.blit(texto, (x, y))

def imprimirImagen(x, y, img):
    """
    Imprime una imágen en la pantalla dada una posición

    Parámetros
    ----------
    arg1 int x: posición x del texto
    arg2 int y: posición y del texo
    arg3 str img: ruta a la imágen
    """
    img = pygame.image.load(img)
    gameDisplay.blit(img, (x, y))


def mostrarPuntos(puntos):
    """
    Muestra los puntos actuales de cada pinta de la mano
    del jugador

    Parámetros
    ----------
    arg1 array puntos: Puntos que se van a imprimir 
    """
    # Modificador de la posición en y
    i = 0
    for pinta in puntos:
        imprimirTexto(
            pinta + ": " + str(puntos[pinta]), 
            anchoPantalla*0.90, 
            (altoPantalla * 0.70) + i
        )
        # Se aumenta para hacer que cada putno se imprima más abajo
        i += 40


def text_objects(text, font):
    textSurface = font.render(text, True, negro)
    return textSurface, textSurface.get_rect()

def pasarTurno():
    """
    Función para cambiar el valor de turnoActual
    y así cambiar el jugador
    """
    global turnoActual
    global cartasSeleccionadas
    # Si el valor es 3, lo devuelve al principio
    if turnoActual < 3:
        turnoActual += 1
    else:
        turnoActual = 0
    # Vacía el array del jugador actual
    cartasSeleccionadas = []

def cambiarCartas(jug):
    """
    Función para cambiar las cartas seleccionadas
    y quitar las imágenes de las viejas

    Parámetros
    ----------
    arg1 obj Jugador jug: Jugador del turno actual
    """
    global cartasSeleccionadas
    global puedeCambiarCartas
    if cartasImagenes and puedeCambiarCartas:
        jugadores[jug].cambiarCartas(cartasSeleccionadas, mazo)
        # Borra las imágenes actuales para que se impriman las nuevas
        # en el siguiente ciclo
        cartasSeleccionadas = []
    
    puedeCambiarCartas = False
    

def botonCarta(x, y, w, h, carta):
    """
    Dibuja un botón especial encima de cada carta
    para saber si están seleccionadas o no

    Parámetros
    ----------
    arg1 int x: Posición x del botón
    arg2 int y: Posición y del botón
    arg3 int w: ancho del botón
    arg4 int h: alto del botón
    arg5 obj Carta: carta sobre la cual se imprime el boton
    """
    # Posición del mouse
    mouse = pygame.mouse.get_pos()
    # Ve si se ha hecho click
    click = pygame.mouse.get_pressed()
    # Crea una superficie blanca detrás de la carta
    s = pygame.Surface((w, h))
    # Llena la parte de atrás de blanco para que cuando se pase
    # el cursor encima parezca que la imagen brilla
    s.fill(blanco)

    # Comprueba si el cursor está encima de la carta
    if x+w > mouse[0] > x and y + h > mouse[1] > y:
        # Establece la transparencia de la superficie para que
        # se vea cuando el cursor está encima
        s.set_alpha(80)
        # Imprime la superficie
        gameDisplay.blit(s, (x, y))
        if click[0] == 1:
            if puedeCambiarCartas:
                # Agrega o quita la carta que se le hizo click del array
                # de cartas seleccionadas para cambiar
                if carta not in cartasSeleccionadas:
                    cartasSeleccionadas.append(carta)
                else:
                    cartasSeleccionadas.remove(carta)
        elif not puedeCambiarCartas:
            imprimirTexto("No puede cambiar más cartas", anchoPantalla * 0.3, altoPantalla * 0.6)
    else:
        # Vuelve la superficie invisible cuando no está el cursor encima
        s.set_alpha(0)
        gameDisplay.blit(s, (x, y))


def imprimirCartas(jugadorCont):
    """
    Imprime las cartas del jugador actual
puntos
    Parámetros
    ----------
    arg1 int jugadorCont: Index del jugador actual en el 
        array de jugadores 
    """
    # Posiciones de la primera carta a la izquierda
    x = (anchoPantalla * 0.1)
    y = (altoPantalla * 0.7)
    # Modificador de la posición en x
    i = 1
    # Imprime todas las cartas en la mano
    for carta in jugadores[jugadorCont].getMano():
        # Si una de las cartas está en el array de las cartas seleccionadas
        # se sube un poco cambiando su posici'on en y para demostrarlo
        if carta in cartasSeleccionadas:
            y = y - 20

        imprimirImagen(x + (i * anchoCarta), y, carta.getImg())
        # Imprime el bot'on de cadda carta probando si es la primera
        # Si no lo es, se reduce el tamano del bot'on para evitar pulsar
        # el bot'on de dos cartas al mismo tiempo
        # if(i < len(cartasImagenes) - 1):
        #     botonCarta(
        #         x * (i + 1), 
        #         y, 
        #         anchoCarta -anchoCarta * 0.2, 
        #         altoCarta, 
        #         carta
        #     )
        # else:
        botonCarta(
            x + (i * anchoCarta), 
            y, 
            anchoCarta, 
            altoCarta, 
            carta
        )
        # Se aumenta para cambiar la posici'on en x de cada carta
        i += 1
        y = (altoPantalla*0.7)


def salirJuego():
    """"
    Funci'on para cerrar el juego si se presiona la 
    tecla de salir o se cambia el tipo de evento a quit
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

def inicio(ini):
    imagen_inicio = pygame.image.load(ini)
    rect = imagen_inicio.get_rect()
    rect.left, rect.top = [300,200]
    gameDisplay.fill([255, 255, 255])
    gameDisplay.blit(imagen_inicio, rect)
    """
    iniciar = imagen("imagen/inicio.png",True)      
    iniciar= pygame.transform.scale(iniciar, (300, 200))
    Mesa.blit(iniciar,(565,365))
    pygame.display.flip()
"""
def pantallaIntro():
    #importo la imagen del titulo
    fondoPantalla("imagenes/global/principal.jpg")
    imprimirImagen(450, 400, "imagenes/global/inicio.png")
    

    #inicio("inicio.jpg")
    global intro
    
    while intro:
        salirJuego()

        # Fondo verde
        #gameDisplay.fill(verde)
        
        # Titulo
        #imprimirTexto("Ajilei", (anchoPantalla / 2) - 200, (altoPantalla/2) - 200, 200)
        # Botón para empezar
        
        boton (
            "Empezar", 
            (anchoPantalla / 2) - 120,
            (altoPantalla / 2) + 150, 
            300, 60, blanco,
            gris,
            cambiarEstadoIntro,
            [],
            40
        )
        
        # Autores

        imprimirTexto("Autores:", anchoPantalla - 200, altoPantalla - 170, 30)
        imprimirTexto("Antony D'Amico", anchoPantalla - 200, altoPantalla - 140, 30)
        imprimirTexto("Mariano Landaeta", anchoPantalla - 200, altoPantalla - 110, 30)
        
        # refrescando el juego
        pygame.display.update()
        clock.tick(15)


def cambiarEstadoIntro():
    global intro
    intro = not intro

def cambiarEstadoJugando():
    global jugando
    jugando = not jugando

def cambiarEstadoPantallaPuntos():
    global pantallaPuntos
    pantallaPuntos = not pantallaPuntos

def volverAJugar():
    cambiarEstadoJugando()
    cambiarEstadoPantallaPuntos()
    

def juegoPrincipal():
    while jugando:
        fondoPantalla("imagenes/global/juego_inicial.png")
        salirJuego()
        # Dibuja el fondo
        #gameDisplay.fill(verde)
        # Imprime las im'agenes de los jugadores no activos
        imprimirImagen(anchoPantalla*0.80 - anchoCarta, altoPantalla * 0.4, cartaAtras)
        imprimirImagen(anchoPantalla*0.05, altoPantalla * 0.3, cartaAtras)
        imprimirImagen(anchoPantalla*0.4 - anchoCarta/2, altoPantalla*0.01, cartaAtras)

        # Se imprimen las cartas del jugador actual
        imprimirCartas(turnoActual)
        # Se imprimen los puntos del jugador actual
        mostrarPuntos(jugadores[turnoActual].getPuntos())

        # Bot'on para cambiar las cartas seleccionadas
        boton(
            "Cambiar Carta", 
            anchoPantalla * 0.80,
            altoPantalla * 0.05, 
            150, 30, blanco,
            gris, 
            cambiarCartas, 
            [turnoActual]
        )

        # Bot'on para pasar al siguiente turno
        boton(
            "Finalizar", 
            anchoPantalla * 0.80,
            altoPantalla * 0.17, 
            150, 
            30, 
            blanco, 
            gris, 
            volverAJugar
        )

        # Refresca la pantalla
        pygame.display.update()
        # fps del juego, se ponen 15 porque con más los
        # botones de las cartas actuan como si se presionaran 2 veces
        clock.tick(30)
        
def pantallaVictoria():
    while pantallaPuntos:
        salirJuego()
        fondoPantalla("imagenes/global/juego_inicial.png")
        mayorPunto = 0
        jugadorGanador = 0
        for i in range(len(jugadores)):
            if jugadores[i].getMaxPuntos() > mayorPunto:
                jugadorGanador = i + 1
                mayorPunto = jugadores[i].getMaxPuntos()

        mensaje = "Ha gando el jugador " + str(jugadorGanador)  
        imprimirTexto(
            mensaje, 
            anchoPantalla * 0.3, 
            altoPantalla * 0.3, 
            60
        )

        boton(
            "Nuevo Juego",
            anchoPantalla * 0.2,
            altoPantalla*0.7,
            150,
            30,
            blanco,
            gris,
            volverAJugar
        )

        pygame.display.update()
        clock.tick(15)

def repartirCartas():
    global jugadores
    global puedeCambiarCartas
    puedeCambiarCartas = True
    jugadores = []
    for _ in range(0, 4):
        jugadores.append(Jugador(mazo))
    
    global cartasImagenes
    cartasImagenes = []
    for carta in jugadores[0].getMano():
        cartasImagenes.append(carta.getImg())


"""
=============================
| Ciclo principal del juego  |
=============================
"""
def gameLoop():

    while True:

        salirJuego()
        pantallaIntro()
        repartirCartas()
        juegoPrincipal()
        pantallaVictoria()

        
gameLoop()
