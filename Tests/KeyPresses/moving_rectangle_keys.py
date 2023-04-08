# This file is merging what I did in jumping_rectangle.py with what I made in key_press.py 

import pygame
import sys
pygame.init()
from pygame.locals import *

# I am going to try and make this not necessarily for the same height and width, I am going to first do it with
# the same height and width, but then I'll change them and check if the code still works, if it doesn't then
# I'll change it until this code works for any window width and height

#I'd like to make a snake that is completely set up by me, therefore, 
# This kinda works but it's not still what I'm looking for
# I think I'm going to shave the excess screen so that it looks better
window_width = 433
window_height = 305

#It's not LeviOsa, it's LeviosA

# percentage = 0.1 #10%
percentage = 0.15 #15% #This value breaks the screen
# percentage = 0.2 #20%

# A way to control how you determine the rectangle size, if it's true then by the use of the percentage it will
# be such size that you can put 10 rectangles inside of the dimension that is smaller be it the width or the height
percentage_size = True

if percentage_size:
  if window_height < window_width:
    rectangle_side = (window_height * percentage)
  else:
    rectangle_side = (window_width * percentage)
else:
  # Set Size
  rectangle_side = 100

rectangle_side = rectangle_side//1
# I have to create a grid
# Amount of rows that fit inside of the  
rows = window_height // rectangle_side
cols = window_width // rectangle_side

max_x = rectangle_side * cols
max_y = rectangle_side * rows

rectangle_x_speed = rectangle_side # Could be useful but in actuality do nothing.
rectangle_y_speed = rectangle_side # Could be useful but in actuality do nothing.

window = pygame.display.set_mode((max_x, max_y))
print(max_x, max_y)
print(rectangle_side)
print(rectangle_x_speed, rectangle_y_speed)
pygame.display.set_caption("Wingardium LeviOsa!")

# Rectangle that starts in (0, 0) and has width = rectangle_x_side and height = rectangle_y_side
my_rect = pygame.Rect(0, 0, rectangle_side, rectangle_side)
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
      if my_rect.bottom <= max_y - rectangle_side:
        my_rect.move_ip(0, rectangle_y_speed)
      last_time_checked = current_time
      action_made = True
    if key[pygame.K_UP] and not action_made:
      if my_rect.top > 0:
        my_rect.move_ip(0, -rectangle_y_speed)
      last_time_checked = current_time
      action_made = True
    if key[pygame.K_RIGHT] and not action_made:
      if my_rect.right <= max_x - rectangle_side:
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


