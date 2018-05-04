from Mazo import Mazo
from Carta import Carta
from Operador import Operador


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
        # self.__calcularPuntosMano(nuevaCarta, True)
        self.__puntos[nuevaCarta.getPinta()] += Operador.calcularPuntosMano(nuevaCarta, True)

    # la operacion es True para suma y False para resta
    # def __calcularPuntosMano(self, carta, operacion):
    #     puntos = self.__calcularPuntosCarta(carta)
    #     if carta == self.__comodin:
    #         self.__realizarOperacionComodin(operacion)
    #         return
    #     self.__realizarOperacion(carta, operacion, puntos)

    # def __realizarOperacion(self, carta, operacion, puntos):
    #     if(operacion):
    #         self.__puntos[carta.getPinta()] += puntos
    #         return
    #     self.__puntos[carta.getPinta()] -= puntos

    # def __realizarOperacionComodin(self, operacion):
    #     for pinta in self.__puntos:
    #         if(operacion):
    #             self.__puntos[pinta] += 10
    #         else:
    #             self.__puntos[pinta] -= 10

    # def __calcularPuntosCarta(self, carta):
    #     if carta.getValor() in self.__valoresCartas:
    #         return self.__valoresCartas[carta.getValor()]
    #     return 10

    def cambiarCartas(self, cambioCartas, mazo):
        self.__mano = [x for x in self.__mano if x not in cambioCartas]
        for viejaCarta in cambioCartas:
            self.__puntos[viejaCarta.getPinta()] += Operador.calcularPuntosMano(viejaCarta, False)
            self.agarrarCarta(mazo)

    def imprimirCartas(self):
        for carta in self.__mano:
            print(str(carta.getValor()) + " de " + carta.getPinta())

    def getPuntos(self):
        return self.__puntos

    def getMano(self):
        return self.__mano


mazo = Mazo()
jugador1 = Jugador(mazo)

print(jugador1.getPuntos())
jugador1.imprimirCartas()

remover = [jugador1.getMano()[0]]
jugador1.cambiarCartas(remover, mazo)

print(jugador1.getPuntos())
jugador1.imprimirCartas()
