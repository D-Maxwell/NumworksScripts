from hw import *
import cmd
import time
from kandinsky import *
from math import floor,ceil


class Grid(list):
  def __init__(self,grid=None,**kwargs):
    self.parent=None
    self.width=kwargs.get("width",len(grid[0]) if grid is not None else 0)
    self.height=kwargs.get("height",len(grid) if grid is not None else 0)
    self.default=kwargs.get("default",grid[0][0] if grid is not None else None)

    
    if grid is None:
      super().__init__(self.gen(
        self.width,
        self.height,
        self.default,
      ))
    else:
      super().__init__(grid)
  
  def gen(self,width,height,default=None):
    return [
      [default for x in range(width)]
      for y in range(height)
    ]


  def __str__(self):
    return "\n".join(
      [" ".join(
        [f"{str(type(each)).split(' ')[1][1]}{str(each)[0]}" for each in row]
      ) for row in self]
    )
  def __repr__(self):
    return self.__str__()


def display(canvas:Grid):
  cell_size=max(chrWH)

  for y,row in enumerate(canvas):
    for x,col in enumerate(row):

      if canvas[y][x] is None:
        continue

      fill_rect(
        x*cell_size,
        y*cell_size,
        cell_size,
        cell_size,
        [canvas[y][x]*255]*3
      )


#g=Grid(ceil(scrW/chrW),ceil(scrH/chrH))
#for y,row in enumerate(g):
#  g[y]=[[False,None,True][(x+y)%3] for x in range(len(row))]

#display(g)