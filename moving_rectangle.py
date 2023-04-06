"""
In this file I would like to do the moving rectangle from DVD players which was moving from side to side with 
xv (x velocities) and yv (y velocities), to be honest, this module and all the things that I have implemented up to
this moment couldn't have been possible without me watching the videos from Coding Train. Thank You Daniel Shiffman
"""

import pygame
import sys
import random
from pygame.locals import *

pygame.init()

screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
colors = [(255, 255, 255), (255, 0, 0), (0, 255, 0), (0, 0, 255)]
color_picker = 0
pygame.display.set_caption("Cuadrado DVD")

def next_color():
  global color_picker
  if color_picker == 3:
      color_picker = -1
  color_picker += 1
rect_width = 40
rect_height = 40
rect_x = 0
rect_y = screen_height // 2 - rect_height // 2
xv = round(random.uniform(0.00, 10), 2)
yv = round(random.uniform(0.00, 10), 2)
my_rect = pygame.Rect(rect_x, rect_y, rect_width, rect_height)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    my_rect.move_ip(xv, yv)
    if(my_rect.bottom == screen_height):
        yv *= -1
        next_color()
    if(my_rect.right == screen_width):
        xv *= -1
        next_color()
    if(my_rect.left == 0):
        xv *= -1
        next_color()
    if(my_rect.top == 0):
        yv *= -1
        next_color()

    screen.fill((0, 0, 0))
    # The problem that I was having previously was that I was not drawing the rectangle again, I was only updating
    # my rectangle which made a change to the item but not to the item.
    # draw rectangle on screen with white color using the attributes found inside of my_rect
    # the 0 is not necessary but if you make it a 1 the rectangle becomes hollow inside.
    pygame.draw.rect(screen, colors[color_picker], my_rect, 0)
    pygame.display.update()
    pygame.time.delay(50)