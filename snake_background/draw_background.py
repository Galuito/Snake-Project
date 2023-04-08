"""
In here I'll be making a function which you can import to generate a background without having to worry about setting
everything up, of course you'll need to pass a lot of variables to the function but it'll work nicely so that you
don't have to repeat code over and over again

The objective of this is making a reusable component

I am honestly happy that it worked on my first try, it needs to follow some parameters but it really is amazing
"""


def draw_background(pygame: object, colors: tuple, cols: int, rows: int, grid_size: int, window: object):
  """
  Generates a grid background for a pygame window

  This functions takes all of the arguments that are used inside of a pygame module, they are listed below

  Args:
    pygame (module): The pygame instance of the file
    colors (tuple): A tuple containing two tuples which must contain an rgb value stored like the following (R, G, B)
    cols (integer): The amount of columns found in the window
    rows (integer): The amount of rows found in the window
    window (object): The window in which the background is going to be drawn

  Returns:
    None
  
  Raises:
    TBD
  """

  bg_colors = {True: colors[0], False: colors[1]}
  for row in range(rows):
    for col in range(cols):
      rect = pygame.Rect(col * grid_size, row * grid_size, grid_size, grid_size)
      color = bg_colors[not (col % 2)]
      if row % 2 == 0:
        color = bg_colors[col % 2]
      pygame.draw.rect(window, color, rect, 0)