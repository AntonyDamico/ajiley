from Mazo import Mazo
from Carta import Carta
from Operador import calcularPuntosMano


class Jugador:
    __mano = []

    __puntos = {
        "Palos": 0,
        "Espadas": 0,
        "Oro": 0,
        "Copa": 0
    }

    def __init__(self, mazo):
        for _ in range(0, 2):
            self.agarrarCarta(mazo)
        
    def agarrarCarta(self, mazo):
        nuevaCarta = mazo.agarrarCarta()
        self.__mano.append(nuevaCarta)
        self.__puntos = calcularPuntosMano(nuevaCarta, True, self.__puntos)

    def cambiarCartas(self, cambioCartas, mazo):
        self.__mano = [x for x in self.__mano if x not in cambioCartas]
        for viejaCarta in cambioCartas:
            self.__puntos = calcularPuntosMano(viejaCarta, False, self.__puntos)
            self.agarrarCarta(mazo)

    # def imprimirCartas(self):
    #     for carta in self.__mano:
    #         print(str(carta.getValor()) + " de " + carta.getPinta())

    def getPuntos(self):
        return self.__puntos

    def getMano(self):
        return self.__mano


# mazo = Mazo()
# jugador1 = Jugador(mazo)

# print(jugador1.getPuntos())
# jugador1.imprimirCartas()

# remover = [jugador1.getMano()[0]]
# jugador1.cambiarCartas(remover, mazo)

# print(jugador1.getPuntos())
# jugador1.imprimirCartas()
