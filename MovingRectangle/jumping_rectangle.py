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

width = 400
height = 400
# This is assuming that the height and width are the same, it probably is a bad practice but let's see
rectangle_side = width*0.1 #40 I'd like to keep it 1/10 of the screen
rectangle_speed_x = rectangle_side #In this case they're going to be the same... because I want it to move in a grid pattern
rectangle_speed_y = rectangle_speed_x
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Grid Rectangle")

starting_x = 40
starting_y = 0
my_rect = pygame.Rect(starting_x, starting_y, rectangle_side, rectangle_side)
pygame.draw.rect(window, (255, 255, 255), my_rect, 0)
pygame.display.update()

pygame.time.delay(50)

while True:
  for event in pygame.event.get():
    if event.type == QUIT: # This QUIT works because I imported pygame.locals
      pygame.quit()
      sys.exit()
  my_rect.move_ip(rectangle_speed_x, rectangle_speed_y)
  if my_rect.bottom >= height:
    rectangle_speed_y *= -1
  if my_rect.right >=  width:
    rectangle_speed_x *= -1
  if my_rect.left <= 0:
    rectangle_speed_x *= -1
  if my_rect.top <= 0:
    rectangle_speed_y *= -1
  window.fill((0, 0, 0))
  pygame.draw.rect(window, (255, 255, 255), my_rect, 0)
  pygame.display.update()
  pygame.time.delay(500)
  