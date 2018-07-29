from Mazo import Mazo
from Carta import Carta
from Operador import calcularPuntosMano


class Jugador:

    def __init__(self, mazo):
        """
        Constructor de la clase Jugador que va a tener
        un array de objetos de la clase Carta con las cartas en su mano
        y un tupple _puntos para llevar los puntos de cada pinta

        Parametros
        -----------
        arg1: obj Mazo
            Mazo del juego
        """
        # Array que se va a llenar de objetos de la clase Carta
        self.__mano = []

        # Puntos por pinta del jugador
        self.__puntos = {
            "palos": 0,
            "espadas": 0,
            "oro": 0,
            "copa": 0
        }

        # 5 llamadas al metodo para agarrar 5 cartas
        for _ in range(0, 5):
            self.agarrarCarta(mazo)

    
    def agarrarCarta(self, mazo):
        """
        Metodo para que el objeto agarre una carta del
        mazo del juego y la agregue a su mano

        Parametros
        -----------
        arg1: obj Mazo
            Mazo del juego
        """
        nuevaCarta = mazo.agarrarCarta()
        # Agregando la carta al array __mano
        self.__mano.append(nuevaCarta)
        # Calculando los puntos que se deben agregar segun la carta sacada
        self.__puntos = calcularPuntosMano(
            nuevaCarta,
            True,
            self.__puntos
        )

    def cambiarCartas(self, cambioCartas, mazo):
        """
        Metodo para quitar una o más cartas del array __mano y 
        agregar una o más nuevas

        Parámetros
        -----------
        arg1: Array Carta
            Array de objetos Carta que se quieren cambiar
        arg2: Obj Mazo
            Mazo del juego
        """
        # Se buscan las cartas que se quieren cambiar en el array __mano y se quitan
        self.__mano = [x for x in self.__mano if x not in cambioCartas]
        # Por cada carta en el array de las que se quieren cambiar, se agrega una nueva
        for viejaCarta in cambioCartas:
            self.__puntos = calcularPuntosMano(
                viejaCarta,
                False,
                self.__puntos
            )
            self.agarrarCarta(mazo)

    def getMaxPuntos(self):
        """
        Método para obtener el máximo puntaje entre
        todas las pintas

        Returns
        -------
        int
            Puntaje máximo que tiene el jugador en alguna de las pintas
        """
        max = 0
        for pinta in self.__puntos:
            if(self.__puntos[pinta] > max):
                max = self.__puntos[pinta]
        return max

    def imprimirCartas(self):
        # Método de prueba en consola para imprimir todas las cartas del jugador
        for carta in self.__mano:
            print(str(carta.getValor()) + " de " + carta.getPinta())

    def getPuntos(self):
        """ Devuelve el array __puntos del jugador actual """
        return self.__puntos

    def getMano(self):
        """ Devuelve el array __mano del jugador actual """
        return self.__mano
