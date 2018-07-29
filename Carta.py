class Carta:

    def __init__(self, valor, pinta):
        """
        Constructor de la clase Carta con su pinta,
        valor y ruta de la imágen correspondiente

        Parametros
        -----------
        arg1: int
            Núemero de la carta
        arg2: str
            Pinta de la carta
        """
        self.__valor = valor
        self.__pinta = pinta
        self.__img = "imagenes/cartas/" + pinta + "/" + str(valor) + ".jpg"

    def __eq__(self, otra):
        """
        Metodo para establecer la comparación de dos objetos Carta

        Parametros
        ----------
        arg1: obj
            Objeto carta con el que se va a comparar la actual

        Returns
        -------
        boolean
            True si los dos objetos tienen la misma pinta y valor
            False en el caso contrario
        """
        return self.__valor == otra.getValor() and self.__pinta == otra.getPinta()

    def mostrarCarta(self):
        # Metodo para hacer pruebas en consola, no va a estar en la versión final
        return str(self.__valor) + " de " + self.__pinta

    def getValor(self):
        """ Devuelve el valor de la carta como int """
        return self.__valor

    def getPinta(self):
        """ Devuelve la pinta de la carta como str """
        return self.__pinta

    def getImg(self):
        """ Devuelve la ruta a la imagen de la carta como str """
        return self.__img
