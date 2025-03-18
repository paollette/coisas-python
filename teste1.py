# importando pygame
import pygame
from pygame.locals import *
from sys import exit

# iniciando
pygame.init()

# tela 
largura = 640
altura = 480

tela = pygame.display.set_mode((largura, altura))

#nome na tela
pygame.display.set_caption('Jogo de teste')

# loop jogo

while True: 
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.display.update()