import pygame
pygame.init()
import sys
from pygame.locals import *

# Placeholder values
window = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Key Press Demo")

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
  

  # Rather than doing a general cool down for everything I should do a cool down for key presses, so that whenever
  # a key is pressed a cool down starts in which the user will have to wait a certain amount of milliseconds until
  # they can do their next action, this makes sense so that the program doesn't get overloaded with a big number of
  # key presses and that the user immediately feels that the command they just inputted on the game is felt.
  current_time = pygame.time.get_ticks()
  key = pygame.key.get_pressed()
  # With this, you can give cool downs not only to one thing but to many things, only that you'd have to use different
  # variables to keep track of the different elapsed times.
  if current_time - last_checked_time >= delay_time:
    if key[pygame.K_UP]:
      print("Up Key Pressed")
      window.fill((255, 255, 255))
      last_checked_time = current_time
    if key[pygame.K_DOWN]:
      print("Down Key Pressed")
      window.fill((0, 0, 255))
      last_checked_time = current_time
    if key[pygame.K_RIGHT]:
      print("Right Key Pressed")
      window.fill((255, 0, 0))
      last_checked_time = current_time
    if key[pygame.K_LEFT]:
      print("Left Key Pressed")
      window.fill((0, 255, 0))
      last_checked_time = current_time
  pygame.display.update()
  
  clock.tick(FPS)
  