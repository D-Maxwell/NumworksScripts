from math import *
from kandinsky import *

n=2
for x in range(128):
  for y in range(128):
    if x%(n*2)<n and y%(n*2)<n:
      set_pixel(x,y,[255]*3)
