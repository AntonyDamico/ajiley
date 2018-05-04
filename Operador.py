from Carta import Carta


class Operador:

    __valoresCartas = {
        1: 11,
        6: 6,
        7: 7
    }

    __comodin = Carta(7, "Oro")

    @classmethod
    def calcularPuntosMano(cls, carta, operacion, puntosJugador):
        puntos = cls.__calcularPuntosCarta(carta)
        if carta == cls.__comodin:
            for pinta in puntosJugador:
                puntosJugador[pinta] += cls.__realizarOperacionComodin(operacion)
            return puntosJugador
        puntosJugador[carta.getPinta()] += cls.__realizarOperacionPuntos(operacion, puntos)
        return puntosJugador

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

    @classmethod
    def __realizarOperacionComodin(cls, operacion):
        if(operacion):
            return 10
        else:
            return -10
