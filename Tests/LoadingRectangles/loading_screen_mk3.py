# TURNS OUT PYGAME HAS A DELAY FUNCTION AND I DIDN'T KNOW ABOUT IT SO MY IMPLEMENTATIONS ON WAITING FUNCTIONS
# WERE USELESS AFTER ALL >:)
import sys
import pygame
pygame.init()

# Variables storing the size of the window
width = 400
height = 400
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Loading Screen")

cell_size = 40
rows = height // cell_size
cols = width // cell_size

#Set a waiting time between screen updates so that the user can understand what is happening on the screen
#Waiting time in milliseconds
cooldown_time = 50

#Set the checking time so that the computer knows what the comparison is going to be with
last_update_time = pygame.time.get_ticks()

#Game Loop

window.fill((0, 0, 0))
pygame.display.update()

while True:
  window.fill((0, 0, 0))
  pygame.display.update()

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()


  # if current_time - last_update_time >= cooldown_time:
  for row in range(rows):
    for col in range(cols):
        rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
        pygame.draw.rect(window, (255, 255, 255), rect, 1)
        pygame.display.update()
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        pygame.time.delay(cooldown_time)


