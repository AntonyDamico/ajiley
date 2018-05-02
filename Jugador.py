from Mazo import Mazo

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

    def __init__(self, mazo):
        for _ in range(0, 3):
            self.agarrarCarta(mazo)

    def __agregarPuntos(self, carta):
        puntos = self.__calcularPuntosCarta(carta)

        if carta.getPinta() == "Oro" and carta.getValor == 7:
            print(0)

        self.__puntos[carta.getPinta()] += puntos
        

    def __calcularPuntosCarta(self, carta):
        valor = carta.getValor()
        if valor in self.__valoresCartas:
            return self.__valoresCartas[valor]
        return 10

    def agarrarCarta(self, mazo):
        nuevaCarta = mazo.agarrarCarta()
        self.__mano.append(nuevaCarta)
        self.__agregarPuntos(nuevaCarta)

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
