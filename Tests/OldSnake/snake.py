#Remember that python uses snake_case
import pygame
pygame.init()
from pygame.locals import *
import sys
import random

"""
REMEMBER 
ROWS ARE NORMALLY ASSOCIATED WITH HEIGHT, BECAUSE WITH MORE ROWS THE HEIGHT INCREASES, THEY ARE HORIZONTAL PLATES ON A PILE
COLUMNS ARE ASSOCIATED WITH WIDTH, BECAUSE WITH MORE COLUMNS THE WIDTH INCREASES, THEY ARE VERTICAL LINES PUT NEXT TO EACH OTHER
TL:DR
+ ROWS == + HEIGHT
+ COLS == + WIDTH
I got confused a while back
"""
pygame.display.set_caption("Snake Game by @Galuito")

window_width = 250
window_height = 250

snake_side = 25

cols = window_width // snake_side
rows = window_height // snake_side

grid = list()

for row in range(rows):
  grid.append([0] * cols)

for row in range(rows):
  for col in range(cols):
    grid[row][col] = (snake_side * row, snake_side * col)

# snake_start_x = random.randint(0, cols - 1)
snake_start_x = 5
# snake_start_y = random.randint(0, rows - 1)
snake_start_y = 5

# Grid done, it works with this size but later I'll try to make it work fo any size
# grid[y][x] = 1
# grid[snake_start_y][snake_start_x]
# print(snake_start_x, snake_start_y)
# print(grid[snake_start_y][snake_start_x])
# for i in grid:
#   print(i)


class Snake():
  def __init__(self, x, y, rectangle):
    self.x = x
    self.y = y
    self.rectangle = rectangle
    self.previous_movement = None
    self.current_movement = None
  def get_rectangle(self):
    return self.rectangle
  def get_x(self):
    return self.x
  def get_y(self):
    return self.y
  def get_previous_movement(self):
    return self.previous_movement
  def get_current_movement(self):
    return self.current_movement
  
  def move_down(self):
    self.previous_movement = self.current_movement
    self.current_movement = 'down'
    if self.rectangle.bottom < window_height:
      self.rectangle.move_ip(0, snake_side)
      self.y += snake_side
      return True

  def move_up(self):
    self.previous_movement = self.current_movement
    self.current_movement = 'up'
    if self.rectangle.top > 0:
      self.rectangle.move_ip(0, -snake_side)
      self.y -= snake_side
      return True


  def move_right(self):
    self.previous_movement = self.current_movement
    self.current_movement = 'right'
    if self.rectangle.right < window_height:
      self.rectangle.move_ip(snake_side, 0)
      self.x += snake_side
      return True


  def move_left(self):
    self.previous_movement = self.current_movement
    self.current_movement = 'left'
    if self.rectangle.left > 0:
      self.rectangle.move_ip(-snake_side, 0)
      self.x -= snake_side
      return True



  
def make_snake_rectangle(x, y):
  global snake_side
  return pygame.Rect(x, y, snake_side, snake_side)


"""
List of Things that I need to implement (Not necessarily in order, just a reminder)

* A grid in which the snake is going to be moving. (Hard)

* The mechanisms which will handle the information inside of that grid and tell where
the snake is. (Hard)

* The key inputs so that the user can move the snake in screen (Easy)

* A delay mechanism which makes the snake move after a certain amount of time has passed between key presses (Easy)

* A way to store the direction in which the snake was going, in case the user stops pressing the keys (Easy)
"""


#Delay Mechanism
"""
The other variable of the delay mechanism is going to be ↓
current_time 
Current time is going to be used to do a comparison between the last_time_checked and its value, after this is done
if the result is greater than the delay time then a command is going to be executed.
"""
last_time_checked = pygame.time.get_ticks()
delay_time = 250 # This feels like the waiting time between moves from the original snake game

#Framerate Mechanism
clock = pygame.time.Clock()
FPS = 30


window = pygame.display.set_mode((window_width, window_height))

snake_head = Snake(snake_start_x * snake_side, snake_start_y * snake_side, make_snake_rectangle(snake_start_x * snake_side, snake_start_y* snake_side))

pygame.draw.rect(window, (0, 200, 0), snake_head.get_rectangle())

snake = list()
snake.append(snake_head)
snake.append(Snake(snake_head.get_x() + snake_side, snake_head.get_y(), snake_head.get_rectangle().move(snake_side, 0)))
pygame.display.update()
next_move = snake_head.move_down

first_move = False

while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()

  key = pygame.key.get_pressed()

  current_time = pygame.time.get_ticks()
  movement_done = False
  if current_time - last_time_checked >= delay_time:
    if key[pygame.K_DOWN] and not movement_done:
      next_move = snake_head.move_down
      last_time_checked = current_time
      movement_done = True
      first_move = True
    if key[pygame.K_UP] and not movement_done:
      next_move = snake_head.move_up
      last_time_checked = current_time
      movement_done = True
      first_move = True
    if key[pygame.K_RIGHT] and not movement_done:
      next_move = snake_head.move_right
      last_time_checked = current_time
      movement_done = True
      first_move = True
    if key[pygame.K_LEFT] and not movement_done:
      next_move = snake_head.move_left
      last_time_checked = current_time
      movement_done = True
      first_move = True
    if first_move:
      if next_move():
        for i in range(1, len(snake)):
          move = snake[i - 1].get_previous_movement()
          if move == None:
            move = snake[i - 1].get_current_movement()
          # print(command)
          if move == 'left':
            snake[i].move_left()
          if move == 'right':
            snake[i].move_right()
          if move == 'up':
            snake[i].move_up()
          if move == 'down':
            snake[i].move_down()

    
  window.fill((0, 0, 0))
  for snake_part in snake:
    pygame.draw.rect(window, (0, 200, 0), snake_part.get_rectangle())

  # window.fill((225, 40, 80))
  pygame.display.update()
  clock.tick(15)