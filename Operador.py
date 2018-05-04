from Carta import Carta


class Operador:

    __valoresCartas = {
        1: 11,
        6: 6,
        7: 7
    }

    __comodin = Carta(7, "Oro")

    @classmethod
    def calcularPuntosMano(cls, carta, operacion):
        puntos = cls.__calcularPuntosCarta(carta)
        # if carta == cls.__comodin:
            # return cls.__realizarOperacionComodin(operacion)
        return cls.__realizarOperacionPuntos(operacion, puntos)

    @classmethod
    def __calcularPuntosCarta(cls, carta):
        if carta.getValor() in cls.__valoresCartas:
            return cls.__valoresCartas[carta.getValor()]
        return 10

    @classmethod
    def __realizarOperacionPuntos(cls, operacion, puntos):
        if(operacion):
            return puntos
        return -puntos

    # @classmethod
    # def __realizarOperacionComodin(cls, operacion):
    #     for pinta in self.__puntos:
    #         if(operacion):
    #             self.__puntos[pinta] += 10
    #         else:
    #             self.__puntos[pinta] -= 10
