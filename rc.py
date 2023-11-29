# ----------- RoundedCorners ------------ #

from hw import *
from kandinsky import *
from bl import *

from math import pi
tau   = pi * 2
gamma = pi / 2


class Squircle(Box):
  
  def __init__(self,**kwargs):
    super().__init__(**kwargs)
    self.radius=kwargs.get("radius", 0)
    #self.absPos(); self.absDim()
  
  def __draw__(self):
    
    super().__draw__()
    
    [fill_rect(
      self.absPos()[0]+[0,self.radius][axis],
      self.absPos()[1]+[self.radius,0][axis],
      self.absDim()[0]-[0,2*self.radius][axis],
      self.absDim()[1]-[2*self.radius,0][axis],
      self.bg,
    ) for axis in range(2)]
    
    [fill_rect(
      round( self.absPos()[0] + self.absDim()[0]*(axis%2) + [1,-1][axis%2]*self.radius ),
      round( self.absPos()[1] + self.absDim()[1]*(axis%2 ^ axis>=2) + [1,-1][axis%2 ^ axis>=2]*self.radius ),
      round( sin(gamma/2) * self.radius ) * [-1,1][axis%2],
      round( sin(gamma/2) * self.radius ) * [-1,1][axis%2 ^ axis>=2],
      self.bg,
    ) for axis in range(4)]


"""
TREE=(
  Box(
  dim=[scrW,scrH],
  children=[
    Squircle(
    dim=[48]*2,
    origin=[0,0],
    radius=6,
    bg=[0,255,255],
    ),
  ])
)


# init renderer
set_pixel(-1,-1,[0]*3)

TREE.getLength()

FRAME=0
while FRAME<666:
  TREE.__tick__(cascade=True)
  
  
  
  
  
  
  
  
  FRAME+=1
  
  
  
  
"""