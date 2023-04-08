import pygame
pygame.init()
from pygame.locals import *
import sys

"""
From now on I am going to be working with set values for the dimensions of a screen, this is because there are some
times in which the user shouldn't be able to set things and that options are unnecessary.
"""

soft_green = (0, 160, 0)
dark_green = (0, 80, 0)
greens = {True: soft_green, False: dark_green}

window_width = 500
window_height = 500

grid_size = 50 # 10 for each column and having 10 rows

window = pygame.display.set_mode((window_width, window_height))
# my_rect = pygame.Rect()


cols = window_width // grid_size # Integer, 10 in this case
rows = window_height // grid_size # Integer, 10 in this case

for row in range(rows):
  for col in range(cols):
    rect = pygame.Rect(col * grid_size, row * grid_size, grid_size, grid_size)
    if row % 2 == 0:
      color = greens[col % 2]
    else:
      color = greens[not (col % 2)]
    pygame.draw.rect(window, color, rect, 0)

pygame.display.update()

while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()