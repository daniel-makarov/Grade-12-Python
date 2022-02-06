# Daniel Makarov
# Date: January 24, 2022
# Aliens Assignment 5

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
player = pygame.transform.rotate(player, -90)

# Player moves at a speed of 5 pixels per keystroke
player_movement_change = 5

# Player's inital coordinates
player = Player(30, 350)

# Bullet's image
bullet = pygame.image.load("bullet.png")
bullet = pygame.transform.scale(bullet, (20, 10))

# Bullet moves at a speed of 5 pixels per display update
bullet_movement_change = -10

# When cooldown is "complete", the player can fire a bullet. Otherwise, the player has to wait for the cooldown to complete
cooldown = "complete"

# Bullet's inital coordinates
bullet_x_coor = -100
bullet_y_coor = -100

def player_bullet(x_coor, y_coor):
  ### Starts cooldown process, and displays a picture of the bullet. ###
  global cooldown
  #print("Bullet's image x-coordinate in the air when fired:", x_coor)
  #print("Bullet's image y-coordinate in the air when fired:", y_coor)
  screen.blit(bullet, (x_coor + 100, y_coor + 45))
  cooldown = "cooling_down"


# Game loop
game_running = True
while game_running:

  screen.fill((0,191,255))

  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        if cooldown == "complete":
          #print("Players' x-coordinate when bullet is fired:", player.x)
          #print("Players' y-coordinate when bullet is fired:", player.y)
          bullet_x_coor = player.x
          bullet_y_coor = player.y
          #print("Bullets' x-coordinate when fired:", bullet_x_coor)
          #print("Bullets' y-coordinate when fired:", bullet_y_coor)
          player_bullet(bullet_x_coor, bullet_y_coor)
    if event.type == pygame.QUIT:
      quit()

  key_input = pygame.key.get_pressed()
  # Movement Up
  if key_input[pygame.K_UP]:
    #print("y-coor:", player.y)
    if player.y == 0:
      #print("Spaceship hit the wall!")
      player.y = 0
    else:
      player.y -= player_movement_change
  # Movement down
  if key_input[pygame.K_DOWN]:
    #print("y-coor:", player.y)
    if player.y == 700:
      #print("Spaceship hit the wall!")
      player.y = 700
    else:
      player.y += player_movement_change

  #print("Bullets' x-coordinate:", bullet_x_coor)
  #print("Bullets' y-coordinate:", bullet_y_coor)
  
  if bullet_x_coor >= 1000:
    bullet_x_coor = -100
    bullet_y_coor = -100
    cooldown = "complete"
  
  #print("Cooldown status:", cooldown)

  if cooldown == "cooling_down":
    #print("Bullets' x-coordinate:", bullet_x_coor)
    #print("Bullets' y-coordinate", bullet_y_coor)
    player_bullet(bullet_x_coor, bullet_y_coor)
    bullet_x_coor -= bullet_movement_change

  player.draw(screen)

  clock.tick(fps)
  pygame.display.update()