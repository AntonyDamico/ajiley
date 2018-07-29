import random
from Carta import *


class Mazo:
    # attr privado: Valores posibles en una baraja francesa
    __valores = (1, 2, 3, 4, 5, 6, 7, 10, 11, 12)
    # attr privado: Pintas posibles en una baraja francesa
    __pintas = ("palos", "espadas", "oro", "copa")

    def __init__(self):
        """
        Constructor de la clase Mazo que va a ser un array
        lleno de objetos de la clase Carta
        """
        self.__cartas = []
        self.__armarMazo()

    def __armarMazo(self):
        """
        Metodo privado que llena el array _cartas de la clase de objetos de la
        clase Carta usando todas las combinaciones de pintas
        y valores posibles
        """
        for pinta in self.__pintas:
            for valor in self.__valores:
                self.__cartas.append(Carta(valor, pinta))

    # agarrar una carta al azar del mazo
    def agarrarCarta(self):
        """
        Devuelve una carta del array y la quita, si está
        vacío, lo llena de nuevo

        Returns
        -------
        obj Carta
            Objeto de la clase Carta perteneciente al array _cartas
        """
        # Comprobando si _cartas está vacío
        if not self.__cartas:
            self.__armarMazo()
        # número al azar entre 0 y 39 para el index del array
        return self.__cartas.pop(
            random.randint(0, len(self.__cartas)-1)
        )

    def getCartas(self):
        """ Devuelve el array _cartas completo """
        return self.__cartas

    def getCarta(self, i):
        """ Devuelve un objeto Carta del array dado un indice """
        return self.__cartas[i]


# PRUEBAS DE CONSOLA

# mazo1 = Mazo()

# for i in range(1, 100):
#     print(str(i) + " :" + str(mazo1.agarrarCarta().mostrarCarta()))
