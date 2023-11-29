# ------------ FileManager -------------- #

from hw import *
from bl import *
import bl



HELLO:str="hello there ;"



bl.TREE=(Box(
dim=scrWH,
padin=[16]*2,
children=[
  
  Label( id="hello",
  #pos=[0,-4],
  origin=[0,-1],
  label=lambda:[HELLO],
  dim=[64,0],
  bg=[0,0,255],
  ),
  
  Box(
  pos=[0,24],
  dim=[128,64],
  origin=[0,-1],
  bg=[0,255,0],
  ),

  Squircle(
  dim=[32]*2,
  origin=[0]*2,
  bg=[128]*3,
  ),
 
]))



init()

while 1:
  tick()
  if keyin(KEY_OK):
    HELLO="".join(list(reversed(HELLO)))
    draw_string(str(HELLO),0,scrH-chrH)
    
    #TREE.hook("#hello").__upd__()

