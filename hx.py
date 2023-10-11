from math import *
from kandinsky import *
from hw import *
from turtle import *


ORIGIN=(-scrW/2,-scrH/2)

def tp(x,y):
  penup()
  goto(ORIGIN[0]+x,ORIGIN[1]+y)
  pendown()


speed(0)

color(*get_palette()["Toolbar"])
n=16

for x in range(ceil(
  scrW/( 2*n )
)+1):
  for y in range(ceil(
    scrH/( 3**(1/2)*n )
  )+1):
  
    tp(
      #x*2*n - x%2*(sin(pi/2/3)*n),
      #x*2*n - y%2*(sin(pi/2/3)*n),
      #x*2*n - 2*(sin(pi/2/3)*n),
      x*(2*n - (sin(pi/2/3)*n)),
      y*3**(1/2)*n - x%2*(cos(pi/2/3)*n),
    )
  
    for side in range(6):
      forward(n)
      right(60)
        
    """
    draw_line(
      x1:= floor( x*2*n + n*sin(pi/2/3) ),
      x2:= floor( x1+n ),
      y1:= floor( y*3**(1/2)*n / 2 ),
      y2:= floor( y1+ ),
      ,
    )
    """
  
# canvas is not flushed,
# both modules are compatible !
#fill_rect(0,0,24,128,[255]*3)
