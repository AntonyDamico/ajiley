from Jugador import Jugador
from Mazo import Mazo

mazo = Mazo()

jugadores = []

for i in range(0, 4):
    jugadores.append(Jugador(mazo))


# jugador1 = Jugador(mazo)

print(jugadores[0].getPuntos())
# jugadores[0].imprimirCartas()

print(jugadores[1].getPuntos())
jugadores[0].imprimirCartas()
remover = [jugadores[0].getMano()[0], jugadores[0].getMano()[1]]
jugadores[0].cambiarCartas(remover, mazo)

print(jugadores[0].getPuntos())
jugadores[0].imprimirCartas()
# print(jugador1.getMaxPuntos())

# print(jugador1.getMano()[0].getImg())
