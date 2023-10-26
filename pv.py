# ---------- PaletteVisualizer ---------- #

from math import ceil
from kandinsky import *
from hw import *
from km import *


def alphaCheckerBoard(dim=[24]*2):
  for x in range(ceil(scrW/dim[0])):
    for y in range(ceil(scrH/dim[1])):
      fill_rect(
        x*dim[0],
        y*dim[1],
        dim[0],
        dim[1],
        [ [100]*3,[200]*3 ][(x+y)%2]
      )



def pv():
  
  box_width=3
  
  for c,color in enumerate(get_palette().items()):
    
    fill_rect(
      x:=ceil(scrW/box_width)*(c%box_width),
      y:=(scrH//(len(get_palette())%box_width)) * (c//box_width),
      w:=ceil(scrW/box_width),
      h:=scrH//ceil(len(get_palette())/box_width),
      color[1],
    )
    
    def contrast(clr1,clr2,bg=[0]*3):
      diffs = [abs(sum([
        [clr1,clr2][i][c] - bg[c]
        for c in range(len(bg))
      ]))
      for i in range(2)]
      
      return [clr1,clr2][max(diffs)==diffs[1]]
      
    def caseSplit(text):
      out=[]
      idx=-1
      for chr in text:
        idx+=1
        if idx==0 or not chr.isalpha(): continue
        
        if idx==len(text)-1:
          idx+=1
              
        if chr.isupper() or idx==len(text):
          out+=[text[:idx]]
          text=text[idx:]
          idx=0
        
      return out
        
    [draw_string(
      bit,
      x + w//2 - chrW*len(bit)//2,
      y + h//2 - len(lines)*chrH//2 + b*chrH,
      contrast(
        get_palette()["PrimaryText"],
        [0]*3,
        bg=color[1]
      ),
      color[1],
    ) for b,bit in enumerate(
      lines:=caseSplit(str(color[0]))
      + (
        ["#"+"".join([hex(channel)[2:] for channel in color[1]])]
        if not COLOR_FORMAT else
        [f"{'rgb'[c]}: {channel:3}" for c,channel in enumerate(color[1])]
      )
    )]


COLOR_FORMAT=False

alphaCheckerBoard()
pv()

while True:
  
  if keyin(KEY_OK):
    COLOR_FORMAT^=True
    pv()
  


