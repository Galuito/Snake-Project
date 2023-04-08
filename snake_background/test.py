import pygame
pygame.init()
from pygame.locals import *
import sys
from draw_background import draw_background

window_width = 500
window_height = 500
grid_size = 50

cols = window_width // grid_size
rows = window_height // grid_size

window = pygame.display.set_mode((window_width, window_height))

# Light Blue and Dark Blue Combination
sea_colors = ((0, 0, 220), (0, 0, 130))
inverse_sea_colors = ((0, 0, 130), (0, 0, 220))

# Light Green and Dark Green Combination
forest_colors = ((0, 220, 0), (0, 130, 0))
inverse_forest_colors = ((0, 130, 0), (0, 220, 0))

# Light Red and Dark Red Combination
volcano_colors = ((220, 0, 0), (130, 0, 0))
inverse_volcano_colors = ((130, 0, 0), (220, 0, 0))

# Chess Board Pattern
chess_board = ((0, 0, 0), (230, 230, 230))



last_update_time = pygame.time.get_ticks()
delay_time = 500

flag = 0

# Set Background once
# draw_background(pygame, colors, cols, rows, grid_size, window)
# pygame.display.update()

while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
  
  current_time = pygame.time.get_ticks()
  if current_time - last_update_time > delay_time:
    last_update_time = current_time
    # Changing Background
    if flag == 0:
      draw_background(pygame, volcano_colors, cols, rows, grid_size, window)
      flag = 1
    else:
      draw_background(pygame, inverse_volcano_colors, cols, rows, grid_size, window)
      flag = 0

    # Restore a single background
    # draw_background(pygame, chess_board, cols, rows, grid_size, window)
    pygame.display.update()