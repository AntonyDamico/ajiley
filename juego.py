import pygame

anchoPantalla = 800
altoPantalla = 600

negro = (0, 0, 0)
blanco = (255, 255, 255)
rojo = (255, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)

anchoCarta = 100
altoCarta = 139

gameDisplay = pygame.display.set_mode((anchoPantalla, altoPantalla))
pygame.display.set_caption('Ajilei')
clock = pygame.time.Clock()

cardImg = pygame.image.load("12.jpg")