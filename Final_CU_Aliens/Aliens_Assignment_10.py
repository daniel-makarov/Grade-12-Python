# Daniel Makarov
# Date: January 24, 2022
# Aliens Assignment 10

import pygame
import random
import math

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
    #print("Spaceships' x-coordinate:", self.x)
    #print("Spaceships' y-coordinate:", self.y)
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

# Alien image
alien = pygame.image.load("alien.png")
alien = pygame.transform.scale(alien, (100, 120))

# Stores each alien, its coordinates, and movement speed to draw them in our window
alien_images = []
alien_x_coor = []
alien_y_coor = []
alien_x_movement = []

for all_enemies in range(20):
  alien_images.append(alien)
  alien_x_coor.append(random.randint(1000, 2220))
  alien_y_coor.append(random.randint(0, 720))
  alien_x_movement.append(-5)

#print("All aliens images:", alien_images)
#print("All aliens initial x-coordinates:", alien_x_coor)
#print("All aliens initial y-coordinates:", alien_y_coor)

def alien(x_coor, y_coor, all_aliens):
  ### Displays aliens ingame ###
  #print("Alien x-coordinate:", x_coor)
  #print("Alien y-coordinate:", y_coor)
  screen.blit(alien_images[all_aliens], (x_coor,y_coor))

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

def enemy_hit(enemy_x_coor, enemy_y_coor, bullet_x_coor, bullet_y_coor):
  ### Uses distance formula to check if the bullet hit a alien. ###
  #print("Alien x-coordinate:", enemy_x_coor)
  #print("Alien y-coordinate:", enemy_y_coor)
  #print("Bullet x-coordinate:", bullet_x_coor)
  #print("Bullet y-coordinate:", bullet_y_coor)
  is_enemy_hit = math.sqrt(math.pow(enemy_x_coor-bullet_x_coor,2) + math.pow(enemy_y_coor-bullet_y_coor,2))
  #print(is_enemy_hit)
  if is_enemy_hit < 26:
    #print('Alien Hit!')
    return True


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
      game_running = False

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

  for every_alien in range(20):
    #print("Alien x-coordinates:", alien_x_coor[every_alien])
    #print("Alien y-coordinates:", alien_y_coor[every_alien])
    alien_x_coor[every_alien] += alien_x_movement[every_alien]

    alien(alien_x_coor[every_alien], alien_y_coor[every_alien], every_alien)

    if alien_x_coor[every_alien] <= -100:
      alien_x_coor[every_alien] = random.randint(1000, 2200)
      alien_y_coor[every_alien] = random.randint(0, 720)
      #print("Alien respawn x-coordinates:", alien_x_coor[every_alien])
      #print("Alien respawn y-coordinates:", alien_y_coor[every_alien])

    enemy_is_hit = enemy_hit(alien_x_coor[every_alien], alien_y_coor[every_alien], bullet_x_coor, bullet_y_coor)
    if enemy_is_hit:
      alien_x_coor[every_alien] = random.randint(1000, 2200)
      alien_y_coor[every_alien] = random.randint(0, 720)
      #print("Alien respawn x-coordinates:", alien_x_coor[every_alien])
      #print("Alien respawn y-coordinates:", alien_y_coor[every_alien])
      bullet_x_coor = -100
      bullet_y_coor = -100
      cooldown = "complete"

  clock.tick(fps)
  pygame.display.update()