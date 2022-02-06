# Daniel Makarov
# Date: January 24, 2022
# Aliens Assignment 7

import pygame
from random import randint

# Window settings 
screen = pygame.display.set_mode((1000, 900))
pygame.display.set_caption("star")
clock = pygame.time.Clock()
fps = 60

# Image of the star
star = pygame.image.load("star.png")
star = pygame.transform.scale(star, (100, 100))

# Stores all the stars and their coordinates to draw them in our window
star_images = []
star_x_coor = []
star_y_coor = []

# Incrementing x and y values to position stars
incr_x = 0
incr_y = 0

for stars in range(10):
    star_images.append(star)
    star_x_coor.append(incr_x)
    star_y_coor.append(0)
    incr_x += 100
    #print("X-coordinates value incremented by:", incr_x)

#print("Stars images:", star_images)
#print("Stars x-coordinates:", star_x_coor)
#print("Stars y-coordinates:", star_y_coor)

def star(x_coor, y_coor, all_stars):
  ### Displays stars in our window. ###
  #print("Stars' x-coordinate:", x_coor)
  #print("Stars' y-coordinate:", y_coor)
  screen.blit(star_images[all_stars], (x_coor,y_coor))

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    while incr_y <= 800:
        for every_star in range(10):
            #print("Every stars' x-coordinate per row:", star_x_coor[every_star])
            #print("Every stars' y-coordinate per row without increment or random number:", star_y_coor[every_star])
            star(star_x_coor[every_star] + randint(-20,20), star_y_coor[every_star] + incr_y + randint(-20,20), every_star)
        incr_y += 100
        #print("Y-coordinates value incremented by:", incr_y)

    clock.tick(fps)
    pygame.display.update()