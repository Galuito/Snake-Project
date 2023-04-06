import pygame
pygame.init()
import sys

width = 400
height = 400
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Loading Screen MK2")
# Programa hecho realmente de manera toche
# Rectangle is going to occupy 1/10 of the total size from the original window
percentage = 0.1 # 10%
cooldown_time = 100

last_check_time = pygame.time.get_ticks()
current_time = pygame.time.get_ticks()


for i in range(1, 401, 40):
  for j in range (1, 401, 40):
    while current_time - last_check_time < cooldown_time:
      current_time = pygame.time.get_ticks()
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()

    rect = pygame.Rect(j, i, width*percentage, height*percentage)
    pygame.draw.rect(window, (255, 255, 255), rect, 1)
    pygame.display.update()
    last_check_time = current_time
    



while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
