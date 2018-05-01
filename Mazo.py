import random
from Carta import *


class Mazo:
    __valores = (1, 2, 3, 4, 5, 6, 7, 10, 11, 12)
    __pintas = ("Palos", "Espadas", "Oro", "Copa")
    __cartas = []

    def __init__(self):
        self.__armarMazo()

    #llena el array __cartas de todas las cartas
    def __armarMazo(self):
        for pinta in self.__pintas:
            for valor in self.__valores:
                self.__cartas.append(Carta(valor, pinta))

    #agarrar una carta al azar del mazo
    def agarrarCarta(self):
        # si __cartas está vacío, se llena otra vez
        if not self.__cartas:
            self.__armarMazo()
        # número al azar entre 0 y 39 cartas
        return self.__cartas.pop(random.randint(0, len(self.__cartas)-1))

    #devuelve el array de carts
    def getCartas(self):
        return self.__cartas

    #devuelve una solo carta al dar un índice
    def getCarta(self, i):
        return self.__cartas[i]


# mazo1 = Mazo()

# for i in range(1, 100):
#     print(str(i) + " :" + str(mazo1.agarrarCarta().mostrarCarta()))
