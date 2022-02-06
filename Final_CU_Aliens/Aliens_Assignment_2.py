# Daniel Makarov
# Date: January 24, 2022
# Aliens Assignment 2

import pygame

# Window settings
screen = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("Alien")
clock = pygame.time.Clock()
fps = 60

class Spaceship:
  def __init__(self, x_coor, y_coor):
    self.x = x_coor
    self.y = y_coor
    #print("Initial spaceship x-coordinate:", self.x)
    #print("Initial spaceship y-coordinate:", self.y)

  def draw(self, screen):
    #print("Spaceship x-coordinate:", self.x)
    #print("Spaceship y-coordinate:", self.y)
    screen.blit(self.character_image, (self.x, self.y))

class Player(Spaceship):
  def __init__(self, x_coor, y_coor):
    #print("Initial spaceship x-coordinate:", x_coor)
    #print("Initial spaceship y-coordinate:", y_coor)
    super().__init__(x_coor, y_coor)
    self.character_image = player

  def draw(self, screen):
    super().draw(screen)

# Player image 
player = pygame.image.load("ship.png")
player = pygame.transform.scale(player, (100, 120))

# Player's inital coordinates
player = Player(430, 350)

game_running = True
while game_running:

  screen.fill((0,191,255))

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      quit()

  player.draw(screen)
  
  clock.tick(fps)
  pygame.display.update()