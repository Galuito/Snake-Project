import pygame
pygame.init()
import sys
from pygame.locals import *

# Placeholder values
window = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Key Press Example")

# Found another and probably better way to handle waiting times!
clock = pygame.time.Clock()
FPS = 30
delay_time = 100
last_checked_time = pygame.time.get_ticks()
while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
  
  window.fill((0, 0, 0))
  pygame.display.update()

  # I am keeping this file only to document a bad implementation of a key press cool down, the difference is 
  # subtle, but, sometimes you'll be able to notice that even though you pressed one of the arrow keys it doesn't
  # get picked up and that's why this code does not achieve what I'm looking for
  current_time = pygame.time.get_ticks()
  key = pygame.key.get_pressed()
  if current_time - last_checked_time >= delay_time:
    if key[pygame.K_UP]:
      print("Up Key Pressed")
    if key[pygame.K_DOWN]:
      print("Down Key Pressed")
    if key[pygame.K_RIGHT]:
      print("Right Key Pressed")
    if key[pygame.K_LEFT]:
      print("Left Key Pressed")
    last_checked_time = current_time
  
  clock.tick(FPS)
  