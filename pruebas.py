from Jugador import Jugador
from Mazo import Mazo

mazo = Mazo()

jugadores = []

for i in range(0, 4):
    jugadores.append(Jugador(mazo))


# jugador1 = Jugador(mazo)

print(jugadores[0].getPuntos())
jugadores[0].imprimirCartas()

print(jugadores[1].getPuntos())
jugadores[1].imprimirCartas()
# remover = [jugador1.getMano()[0]]
# jugador1.cambiarCartas(remover, mazo)

# print(jugador1.getPuntos())
# print(jugador1.getMaxPuntos())

# print(jugador1.getMano()[0].getImg())
