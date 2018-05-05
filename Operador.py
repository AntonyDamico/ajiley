from Carta import Carta

valoresCartas = {
    1: 11,
    6: 6,
    7: 7
}

comodin = Carta(7, "Oro")


def calcularPuntosMano(carta, operacion, puntosJugador):
    puntos = calcularPuntosCarta(carta)
    if carta == comodin:
        for pinta in puntosJugador:
            puntosJugador[pinta] += realizarOperacionComodin(operacion)
        return puntosJugador
    puntosJugador[
        carta.getPinta()] += realizarOperacionPuntos(operacion, puntos)
    return puntosJugador


def calcularPuntosCarta(carta):
    if carta.getValor() in valoresCartas:
        return valoresCartas[carta.getValor()]
    return 10


def realizarOperacionPuntos(operacion, puntos):
    if(operacion):
        return puntos
    return -puntos


def realizarOperacionComodin(operacion):
    if(operacion):
        return 10
    return -10
