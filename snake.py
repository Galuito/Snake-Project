#Remember that python uses snake_case
import sys
import pygame
pygame.init()

#Function to go from Hex to Rgb


colors = {'white' : (255, 255, 255), 'black': (0, 0, 0)}

# Variables storing the size of the window
width = 400
height = 400
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake")

cell_size = 40
rows = height // cell_size
cols = width // cell_size

grid = list()

for i in range(rows):
  grid.append([0]*cols)

grid[rows//2][cols//2] = 1
#Set a waiting time between screen updates so that the user can understand what is happening on the screen
#Waiting time in milliseconds
cooldown_time = 1000

#Set the checking time so that the computer knows what the comparison is going to be with
last_update_time = pygame.time.get_ticks()

#Game Loop

window.fill(colors['black'])
pygame.display.update()

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()

  current_time = pygame.time.get_ticks()
  if current_time - last_update_time >= cooldown_time:
    for row in range(rows):
      for col in range(cols):
          rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
          pygame.draw.rect(window, (255, 255, 255), rect, 1)
          pygame.display.update()
    last_update_time = current_time




     