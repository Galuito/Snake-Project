# This iteration of the rainbow_window module uses a color iterator which I find not useful.
# I find cooler doing this module with only a while loop. But this version may be better because it works
# precisely without the use of said while loop, so that it's not inside a circle that cannot access other 
# functions outside.

import sys
import pygame
pygame.init()

#Function to go from Hex to Rgb
def hex_to_rgb(hex_color):
    """Converts a hexadecimal color code to an RGB tuple"""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

flashing_lights = ['#ff0000', '##ffee00', '#00ff00', '#00ffee', '#0000ff', '#8800ff', '#ff00ff']

# Variables storing the size of the window
width = 400
height = 400
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Rainbow Window")

#Set a waiting time between screen updates so that the user can understand what is happening on the screen
#Waiting time in milliseconds
cooldown_time = 1000

#Set the checking time so that the computer knows what the comparison is going to be with
last_update_time = pygame.time.get_ticks()
color_picker = 1

#Game Loop

window.fill((255, 0, 0))
pygame.display.update()

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
  
  
  current_time = pygame.time.get_ticks()
  if current_time - last_update_time >= cooldown_time:
    window.fill(hex_to_rgb(flashing_lights[color_picker]))
    pygame.display.update()
    last_update_time = current_time
    if color_picker == 6:
      color_picker = -1
    color_picker += 1


