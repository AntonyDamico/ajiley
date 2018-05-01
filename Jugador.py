from Mazo import Mazo
from Carta import Carta

mazo = Mazo()


class Jugador:
    __mano = []
    __puntos = 0

    def __init__(self):
        for _ in range(0, 3):
            self.agarrarCarta()

    def __calcularPuntos(self):
        for carta in self.__mano:
            self.__puntos += carta.getValor()

    def agarrarCarta(self):
        nuevaCarta = mazo.agarrarCarta()
        self.__mano.append(nuevaCarta)
        self.__puntos += nuevaCarta.getValor()

    def getPuntos(self):
        return self.__puntos

    def getMano(self):
        return self.__mano

# =========================================

jugador1 = Jugador()

for carta in jugador1.getMano():
    print(carta.mostrarCarta())

print(jugador1.getPuntos())

jugador1.agarrarCarta()

for carta in jugador1.getMano():
    print(carta.mostrarCarta())

print(jugador1.getPuntos())
