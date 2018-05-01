class Carta:
    __valor = None
    __pinta = None

    def __init__(self, valor, pinta):
        self.__valor = valor
        self.__pinta = pinta

    def mostrarCarta(self):
        return str(self.__valor) + " de " + self.__pinta

    def getValor(self):
        return self.__valor

    def getPinta(self):
        return self.__pinta
