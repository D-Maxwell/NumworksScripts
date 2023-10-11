from hw import *
from km import *
from grid import *
import time

Board=Grid(
  #width=3,
  #height=3,
  #default=Grid(width=3,height=3,default=None),
  [
    [Grid(
      width=3,
      height=3,
      default=None
    ) for i in range(3)]
    for j in range(3)
  ]
)
  #([Grid(3,3)]*3*3)[idx] for idx in range(3*3)




def display(array:grid,pos=[0,0],cell_size=1,margin=0,color=get_palette()["HomeBackground"]):
  
  for y,row in enumerate(array):
    for x,elm in enumerate(row):
      highlight=False
      
      screen_pos=[
        pos[0] + x*(cell_size+margin),
        pos[1] + y*(cell_size+margin),
        
      ]
      
      #if array[y][x]==True:
      #  color=[0,255,0]
      
      
      if type(array.parent) is Grid:
        highlight = (
          [x,y] == [CURSOR_POS[0]%len(array),
                    CURSOR_POS[1]%len(array)]
          and
          array.cell_pos == [CURSOR_POS[0]//array.parent.width,
                             CURSOR_POS[1]//array.parent.height]
        )
      
      
      #print(get_pixel(screen_pos[0],screen_pos[1]),color)
      #if get_pixel(screen_pos[0],screen_pos[1])!=color:
      if type(array.parent) is Grid:
        fill_rect(
          screen_pos[0], screen_pos[1],
          cell_size, cell_size,
          color if array[y][x] is None else [[255,0,0],[0,255,0]][array[y][x]],
        )
        if highlight:
          fill_rect(
            screen_pos[0]+cell_size//4,
            screen_pos[1]+cell_size//4,
            cell_size//2,
            cell_size//2,
            [0,0,255],
          )
      
      #if type(array[y][x]) is Grid:
      if type(array.parent) is not Grid:
        array[y][x].cell_pos=[x,y]
        array[y][x].parent=array
        display(array[y][x],
          pos=screen_pos,
          margin=(margin:=1),
          cell_size=cell_size//len(array) - margin,
          color=[128]*3,
        )
        
        #if not highlight: continue
        #if array.parent is not None: continue
        #if [x,y]!=CURSOR_POS: continue
        #highlight_color=[0,0,255]
        for axis in range(2):
          if (
            [x,y]!=[CURSOR_POS[0]//3,CURSOR_POS[1]//3]
            or get_pixel(screen_pos[0],screen_pos[1])!=get_palette()["Toolbar"]
          ):
            
            fill_rect(
              pos[0]+[x,0][axis]*(cell_size+margin)-4*[0,margin][axis],
              pos[1]+[0,y][axis]*(cell_size+margin)-4*[margin,0][axis],
              [cell_size,margin][axis],
              [margin,cell_size][axis],
              get_palette()["Toolbar"] if [x,y]==[CURSOR_POS[0]//3,CURSOR_POS[1]//3] else color,
            )
        
      #else:
      #  if keyin(KEY_OK):
      #    array[y][x]=True
        
        #fill_rect(,,,,)
        
        

CONTROLS={
  0 : {
    "-" : KEY_LEFT,
    "+" : KEY_RIGHT,
  },
  1 : {
    "-" : KEY_UP,
    "+" : KEY_DOWN,
  },
}

CURSOR_POS=[0]*2
Player_Turn=False
while True:
  
  """CURSOR_POS=[
    CURSOR_POS[axis] +
    [keyin(KEY_RIGHT),keyin(KEY_DOWN)][axis] -
    [keyin(KEY_LEFT), keyin(KEY_UP)  ][axis]
    for axis in range(len(CURSOR_POS))
  ]"""
  
  #draw_string(str(CURSOR_POS),scrW-len(str(CURSOR_POS))*chrW,0)
  
  for axis in range(len(CURSOR_POS)):
    CURSOR_POS[axis] += (
      + keyin(CONTROLS[axis]["+"])
      - keyin(CONTROLS[axis]["-"])
    )

  
  #fill_rect(CURSOR_POS[0],CURSOR_POS[1],1,1,[255]*3)
  
  display(Board,
    cell_size=(cell_size:=min(scrWH)//Board.width - (margin:=4)),
    pos=[round(scrW/2 - (Board.width*(cell_size+margin)-margin)/2),scrH-(Board.height*(cell_size+margin)-margin)],
    margin=margin,
#    color=None,
  )
  
  
  if keyin(KEY_OK):
    print(Board[0][0])
    Board[CURSOR_POS[1]//3][CURSOR_POS[0]//3][CURSOR_POS[1]%3][CURSOR_POS[0]%3] = Player_Turn
    Player_Turn^=True
    print(Board[0][0])
  
  
  #time.sleep(1/60)
  