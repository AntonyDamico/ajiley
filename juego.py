from Jugador import Jugador
from Mazo import Mazo

mazo = Mazo()

jugador1 = Jugador(mazo)

for carta in jugador1.getMano():
    print(carta.mostrarCarta())

print(jugador1.getPuntos())

jugador1.agarrarCarta(mazo)

for carta in jugador1.getMano():
    print(carta.mostrarCarta())

print(jugador1.getPuntos())