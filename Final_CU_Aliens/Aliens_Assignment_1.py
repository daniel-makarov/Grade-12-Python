# Daniel Makarov
# Date: January 24, 2022
# Aliens Assignment 1

import pygame

# Window settings
screen = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("Alien")
clock = pygame.time.Clock()
fps = 60

game_running = True
while game_running:

    screen.fill((0,191,255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

    clock.tick(fps)
    pygame.display.update()