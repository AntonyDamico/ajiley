class Carta:

    def __init__(self, valor, pinta):
        self.__valor = valor
        self.__pinta = pinta
        self.__img = "imagenes/cartas/" + pinta + "/" + str(valor) + ".jpg"

    # hace que la comparacion de los campos de dos objetos funcione
    def __eq__(self, otra):
        return self.__valor == otra.getValor() and self.__pinta == otra.getPinta()

    def mostrarCarta(self):
        return str(self.__valor) + " de " + self.__pinta

    def getValor(self):
        return self.__valor

    def getPinta(self):
        return self.__pinta

    def getImg(self):
        return self.__img
