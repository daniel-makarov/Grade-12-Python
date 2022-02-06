# Daniel Makarov
# Date: January 24, 2022
# Aliens Assignment 8

import pygame

# Window settings
screen = pygame.display.set_mode((1000,500))
pygame.display.set_caption("Raindrop")
clock = pygame.time.Clock()
fps = 60

# Raindrop image
raindrop = pygame.image.load("raindrop.png")
raindrop = pygame.transform.scale(raindrop, (100, 100))

# Stores each raindrop, its coordinates, and movement speed to draw them in our window
raindrop_images = []
raindrop_x_coor = []
raindrop_y_coor = []
raindrop_y_movement = []

# Incrementing x and y values to position raindrops
incr_x = 0
incr_y = 0

# Raindrops' number to create a new row
new_row = [9, 19, 29, 39, 49]

for raindrops in range(50):
  raindrop_images.append(raindrop)
  raindrop_x_coor.append(incr_x)
  raindrop_y_coor.append(incr_y)
  raindrop_y_movement.append(-5)

  incr_x += 100
  #print("Increment in x-coordinate:", incr_x)
  if raindrops in new_row:
    incr_x = 0
    incr_y += 100
  #print("Increment in y-coordinate:", incr_y)

#print("All raindrop images:", raindrop_images)
#print("All raindrop x-coordinates:", raindrop_x_coor)
#print("All raindrop y-coordinates:", raindrop_y_coor)
#print("Every raindrops' y-coordinate movement:", raindrop_y_movement)

def raindrop(x_coor, y_coor, all_raindrops):
  ### Displays raindrops in our window. ###
  #print("All raindrop x-coordinates:", x_coor)
  #print("All raindrop y-coordinates:", y_coor)
  screen.blit(raindrop_images[all_raindrops], (x_coor, y_coor))


# Game loop
game_running = True
while game_running:

  screen.fill((255,255,255))

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      game_running = False

  for every_raindrop in range(50):
    #print("Raindrops' y-coordinate:", raindrop_y_coor[every_raindrop])
    raindrop_y_coor[every_raindrop] -= raindrop_y_movement[every_raindrop]
    #print("Raindrops' y-coordinate:", raindrop_y_coor[every_raindrop])
    #print("Raindrops' x-coordinate:", raindrop_x_coor[every_raindrop])
    raindrop(raindrop_x_coor[every_raindrop], raindrop_y_coor[every_raindrop], every_raindrop)

    if raindrop_y_coor[every_raindrop] == 1280:
      game_running = False

  clock.tick(fps)
  pygame.display.update()