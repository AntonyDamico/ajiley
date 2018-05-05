from Jugador import Jugador
from Mazo import Mazo

mazo = Mazo()
jugador1 = Jugador(mazo)

print(jugador1.getPuntos())

remover = [jugador1.getMano()[0]]
jugador1.cambiarCartas(remover, mazo)

print(jugador1.getPuntos())
print(jugador1.getMaxPuntos())