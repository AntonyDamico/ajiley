class Jugador:
    __mano = []
    __puntos = 0

    def __init__(self, mazo):
        for _ in range(0, 3):
            self.agarrarCarta(mazo)

    def __calcularPuntos(self):
        for carta in self.__mano:
            self.__puntos += carta.getValor()

    def agarrarCarta(self, mazo):
        nuevaCarta = mazo.agarrarCarta()
        self.__mano.append(nuevaCarta)
        self.__puntos += nuevaCarta.getValor()

    def imprimirCartas(self):
        for carta in self.__mano:
            print(str(carta.getValor()) + " de " + carta.getPinta())

    def getPuntos(self):
        return self.__puntos

    def getMano(self):
        return self.__mano
