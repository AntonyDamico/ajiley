"""
Funciones necesarias para el cálculo de los puntos de cada carta
"""


from Carta import Carta

# Puntos que proporcionan el 1, 6 y 7 ya que
# las demás cartas dan 10 puntos
valoresCartas = {
    1: 11,
    6: 6,
    7: 7
}

# Objeto comodín, da 7 puntos en todas las pintas
# Es usado para comparar con la mano del jugador y así saber
# si posee un comodín
comodin = Carta(7, "oro")


def calcularPuntosMano(carta, operacion, puntosJugador):
    """
    Función para calcular los puntos actuales del jugador
    con las cartas en su mano
    
    Parámetros
    ----------
    arg1: obj Carta
        Carta de la cuál se quieren agregar o quitar los puntos
    arg2: boolean
        Operación que se desea realizar True para suma y False para resta
    arg3: array
        Array de los puntso actuales del jugador

    Returns
    -------
    array
        nuevo array de puntos del jugador, con las nuevas cartas agregadas
        o quitadas
    """
    # Se obtiene los puntos que da la carta
    puntos = calcularPuntosCarta(carta)
    # Se comprueba si la carta es un comodin
    if carta == comodin:
        # Se agregan los puntos de comodin a todas las pintas
        for pinta in puntosJugador:
            puntosJugador[pinta] += realizarOperacionComodin(operacion)
        return puntosJugador
    # Si no es comodín, se agregan los puntos a la pinta de la carta original
    puntosJugador[carta.getPinta()] += realizarOperacionPuntos(operacion, puntos)
    return puntosJugador


def calcularPuntosCarta(carta):
    """
    Busca la carta actual en el array, si la consigue
    devuelve el valor especificado en el array 
    sino devuelve 10

    Parámetros
    -----------
    arg1: obj Carta
        Objeto Carta la cual se quiere obtener los puntos

    Returns 1
    ---------
    int
        Los puntos que da la carta si se consigue en el array

    Returns 2
    ---------
    int
        Si no se consigue, devuelve 10
    """
    if carta.getValor() in valoresCartas:
        return valoresCartas[carta.getValor()]
    return 10


def realizarOperacionPuntos(operacion, puntos):
    """
    Determina si los puntos se deben sumar o restar
    según se agarren o se quiten cartas

    Parámetros
    ----------
    arg1: boolean
        True si se quiere sumar la carta a los puntos, False si se
        quiere restar
    arg2: int
        Los puntos que da la carta

    Returns 1
    ---------
    El valor positivo de los puntos que da la carta

    Returns 2
    ---------
    El valor negativo de los puntos que da la carta
    """
    if(operacion):
        return puntos
    return -puntos


def realizarOperacionComodin(operacion):
    """
    Determina si los puntos del comodin se deben sumar o restar
    según se agarren o se quiten cartas

    Parámetros
    ----------
    arg1: boolean
        True si se quiere sumar la carta a los puntos, False si se
        quiere restar

    Returns 1
    ---------
    El valor positivo de los puntos del comodín (10pts)

    Returns 2
    ---------
    El valor negativo de los puntos del comodín (-10pts)
    """
    if(operacion):
        return 10
    return -10
