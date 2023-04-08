"""
Rectangle that moves in a grid pattern
"""

import pygame
pygame.init()
# I'm not going to be using random because I need this case to be controlled
# And by controlled I mean that both the spot that you appear in and the speed is
# determined by the programmer so that everything goes right
import sys
from pygame.locals import *
import random

width = 400
height = 400
# This is assuming that the height and width are the same, it probably is a bad practice but let's see
rectangle_side = width*0.1 #40 I'd like to keep it 1/10 of the screen
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Grid Rectangle")

starting_x = random.randint(1, 9) * rectangle_side
starting_y = random.randint(1, 9) * rectangle_side
my_rect = pygame.Rect(starting_x, starting_y, rectangle_side, rectangle_side)
pygame.draw.rect(window, (255, 255, 255), my_rect, 0)
pygame.display.update()

# pygame.time.delay(50)

last_checked_time = pygame.time.get_ticks()
delay_time = 100

while True:
  for event in pygame.event.get():
    if event.type == QUIT: # This QUIT works because I imported pygame.locals
      pygame.quit()
      sys.exit()
  
  current_time = pygame.time.get_ticks()
  if current_time - last_checked_time > delay_time:
    last_checked_time = current_time
    rectangle_speed_x = random.randint(-1, 1) * rectangle_side
    rectangle_speed_y = random.randint(-1, 1) * rectangle_side

    if my_rect.bottom >= height:
      rectangle_speed_y = random.randint(-1, 0) * rectangle_side
    if my_rect.top <= 0:
      rectangle_speed_y = random.randint(0, 1) * rectangle_side

    if my_rect.right >=  width:
      rectangle_speed_x = random.randint(-1, 0) * rectangle_side
    if my_rect.left <= 0:
      rectangle_speed_x = random.randint(0, 1) * rectangle_side
    
    my_rect.move_ip(rectangle_speed_x, rectangle_speed_y)
    # This can be inside of the if so that it's not done when it's not necessary
    window.fill((0, 0, 0))
    pygame.draw.rect(window, (255, 255, 255), my_rect, 0)
    pygame.display.update()
  