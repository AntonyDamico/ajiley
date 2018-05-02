from Mazo import Mazo
from Carta import Carta


class Jugador:
    __mano = []

    __puntos = {
        "Palos": 0,
        "Espadas": 0,
        "Oro": 0,
        "Copa": 0
    }

    __valoresCartas = {
        1: 11,
        6: 6,
        7: 7
    }

    __comodin = Carta(7, "Oro")

    def __init__(self, mazo):
        for _ in range(0, 2):
            self.agarrarCarta(mazo)

    def agarrarCarta(self, mazo):
        nuevaCarta = mazo.agarrarCarta()
        self.__mano.append(nuevaCarta)
        self.__agregarPuntos(nuevaCarta)

    def __agregarPuntos(self, carta):
        puntos = self.__calcularPuntosCarta(carta)
        if carta == self.__comodin:
            self.__sumarComodin()
            return
        self.__puntos[carta.getPinta()] += puntos

    def __calcularPuntosCarta(self, carta):
        if carta.getValor() in self.__valoresCartas:
            return self.__valoresCartas[carta.getValor()]
        return 10

    def __sumarComodin(self):
        for pinta in self.__puntos:
            self.__puntos[pinta] += 10

    def imprimirCartas(self):
        for carta in self.__mano:
            print(str(carta.getValor()) + " de " + carta.getPinta())

    def getPuntos(self):
        return self.__puntos

    def getMano(self):
        return self.__mano


mazo = Mazo()
jugador1 = Jugador(mazo)
puntosActuales = jugador1.getPuntos()
jugador1.agarrarCarta(mazo)

print(puntosActuales)
jugador1.imprimirCartas()
