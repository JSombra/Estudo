import sys
import pygame

pygame.init()

tam = width, height = 320, 240
vel = [2, 2]
pet = 0, 0, 0

tela = pygame.display.set_mode(tam)
bola = pygame.image.load("image.png")
bolarc = bola.get_rect()

tela.fill(pet)
tela.blit(bola, bolarc)
pygame.display.flip()
