# This file is merging what I did in jumping_rectangle.py with what I made in key_press.py 

import pygame
import sys
pygame.init()
from pygame.locals import *

# I am going to try and make this not necessarily for the same height and width, I am going to first do it with
# the same height and width, but then I'll change them and check if the code still works, if it doesn't then
# I'll change it until this code works for any window width and height

#This works, only that I don't like the stretched out snake

window_height = 400
window_width = 800
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Wingardium LeviOsa!")
#It's not LeviOsa, it's LeviosA

percentage = 0.1 #10%
# percentage = 0.15 #15% #This value breaks the screen
# percentage = 0.2 #20%

rectangle_x_side = window_width * percentage
rectangle_y_side = window_height * percentage

speed_reducer = 10 * percentage #This allows for the square to move less but kinda break the grid pattern
rectangle_x_speed = rectangle_x_side //speed_reducer
rectangle_y_speed = rectangle_y_side //speed_reducer

# Rectangle that starts in (0, 0) and has width = rectangle_x_side and height = rectangle_y_side
my_rect = pygame.Rect(0, 0, rectangle_x_side, rectangle_y_side)
pygame.draw.rect(window, (255, 255, 255), my_rect, 0)
pygame.display.update()

last_time_checked = pygame.time.get_ticks()
key_cool_down = 250 

while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
  
  key = pygame.key.get_pressed()
  current_time = pygame.time.get_ticks()
  
  # Checks if the square has already moved
  action_made = False
  # If you don't implement this the square will be able to move diagonally 

  if current_time - last_time_checked >= key_cool_down:
    if key[pygame.K_DOWN] and not action_made:
      if my_rect.bottom < window_height:
        my_rect.move_ip(0, rectangle_y_speed)
      last_time_checked = current_time
      action_made = True
    if key[pygame.K_UP] and not action_made:
      if my_rect.top > 0:
        my_rect.move_ip(0, -rectangle_y_speed)
      last_time_checked = current_time
      action_made = True
    if key[pygame.K_RIGHT] and not action_made:
      if my_rect.right < window_width:
        my_rect.move_ip(rectangle_x_speed, 0)
      last_time_checked = current_time
      action_made = True
    if key[pygame.K_LEFT] and not action_made:
      if my_rect.left > 0:
        my_rect.move_ip(-rectangle_x_speed, 0)
      last_time_checked = current_time
      action_made = True
  
  window.fill((0, 0, 0))
  pygame.draw.rect(window, (255, 255, 255), my_rect, 0)
  pygame.display.update()


