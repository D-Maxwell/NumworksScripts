# ------------- BoxLayout --------------- #

from math import *
from kandinsky import *
from hw import *
from ms import *
from km import *
from ion import *


UPDATES=[]



class Box:
  """
  properties={
    "width": 0,
    "height": 0,
    "parent": None,
    "children":[],
  }
  """
  def __init__(self,**kwargs):
    """
    for prop,value in Box.properties.items():
      exec(f"self.{prop}={value}")
    """
    self.pos = kwargs.get("pos", [0]*2)
    self.dim = kwargs.get("dim", [0]*2)
    
    self.origin = kwargs.get("origin", [-1]*2)
    
    self.abspos = self.pos
    self.absdim = self.dim
    
    self.margin = kwargs.get("margin", [0]*2)
    self.padout = kwargs.get("padout", [0]*2)
    self.padin  = kwargs.get("padin",  [0]*2)
    
    self.is_focused = False
    
    self.parent = kwargs.get("parent", None)
    self.children = kwargs.get("children", [])
    
    for child in self.children:
      child.parent=self
    
    self.idx=self.setIdx()
    
    
    self.bg=kwargs.get("bg", [])
    
  def __postinit__(self):
    if self.parent is None:
      self[0].is_focused=True
    
    
  def setIdx(self, length=0):
    
    length+=1
    #print(self,self.children,self.idx)

    for child in self:
      length = child.setIdx(length)

    self.idx=length
    return self.idx
  
  """
  def getElement(self, idx:int,scroll=0):
    print(self.children)
    if self.idx==idx:
      return self
    
    for child in self.children:
      scroll+=1
      
      print("me:",scroll,child.length)
      
      if scroll+child.length < idx:
        scroll+=child.length
      
      if idx==scroll:
        return child
      
      if idx<scroll+child.length:
        print("c->"+str(scroll))
        return child.getElement(idx,scroll)
  """

  
  def absPos(self):
    self.abspos=self.pos
    if self.parent is not None:
      """
      self.abspos=lmap(ADD,
        lmap(ADD,
          lmap(ADD,
            self.abspos, self.parent.padin),
          self.parent.absPos()),
        self.parent.padout)
      """
      
      self.abspos=[
        self_abspos#+self_padout
        +
        parent_abspos+parent_padout+parent_padin
        for self_abspos,parent_abspos,parent_padout,parent_padin
        in zip(
          self.abspos,
          self.parent.abspos,
          self.parent.padout,
          self.parent.padin,
        )
      ]
      
      self.abspos = [
        self_abspos
        +
        (parent_dim - 2*parent_padin - self_absdim)
        *
        (origin+1)//2
        for self_abspos,parent_dim,parent_padin,self_absdim,origin
        in zip(
          self.abspos,
          self.parent.dim,
          self.parent.padin,
          self.absdim,
          self.origin,
        )
      ]
      
    return self.abspos
  
  def absDim(self):
    self.absdim=lmap(ADD,
      self.dim, lmap(MUL,
        self.padout, 2))
    if False:
      self.absdim=[
        self_absdim + parent_absdim
        for self_absdim, parent_absdim
        in zip(
          self.absdim,
          self.parent.absDim()
        )
      ]
    return self.absdim
    
  #def absIdx(self):
    #for c,child in enumerate(self.parent.children):
    #  child.absidx=c
  #  if self.parent is not None:
  #    self.absidx+=self.parent.absIdx()
  #  return self.absidx
    #if self.parent is not None:
    #  self.absidx+=self.parent.absidx
  
    
  def __draw__(self):
    if self.bg==[]: return
    fill_rect(
      self.absPos()[0],
      self.absPos()[1],
      self.absDim()[0],
      self.absDim()[1],
      self.bg,
    )
  
  def __erase__(self):
    pass
    
  
  def __upd__(self):
    #if SELECTION_INDEX != self.idx:
      #print(self.idx)
      #return
    """
    if self.is_focused:
      self.isFocused()
    """
    """
    fill_rect(
      self.absPos()[0],
      self.absPos()[1],
      self.absDim()[0],
      self.absDim()[1],
      [255]*3,
    )
    """
    """
    draw_string(str(self.is_focused),*self.absPos())
    """
    
  def __tick__(self, cascade=False):
    
    self.__erase__()
    self.__upd__()
    self.__draw__()
    
    if not cascade: #and self not in UPDATES:
      return
    
    for child in self.children:
      child.__tick__(cascade=cascade)
  
  def __getitem__(self,idx:int):
    return self.children[idx]
    
  
  def isFocused(self):
    gyro=[
      keyin(KEY_LEFT) - keyin(KEY_RIGHT),
      keyin(KEY_DOWN) - keyin(KEY_UP),
    ]
    #self.is_focused=False
    
    if self.parent is None:
      parent_idx=0
    else:
      parent_idx=self.parent.idx
    
    if gyro[0] == 0 and gyro[1] != 0:
      
      [draw_string(
        info,
        scrW-len(info)*chrW,
        i*chrH,
      ) for i,info in enumerate([
        f"{gyro[1]=}",
        f"{self.idx=}",
        f"{parent_idx=}",
      ])]
      
      if self.parent is None: return
      
      self.parent[gyro[1]
        + self.idx
        - parent_idx
        ].is_focused = True
      
    elif gyro[1] == 0:
      pass
    else:
      self.is_focused=True


from rc import Squircle


TREE=(
  Box(
  dim=[128]*2,
  padin=[8]*2,
  padout=[4]*2,
  bg=[0,0,255],
  children=[
    
    Box(
    dim=[8]*2,
    bg=[0,255,0],
    ),
    Box(
    pos=[16]*2,
    dim=[8]*2,
    bg=[0,255,0],
    children=[
      Box(
      dim=[4]*2,
      bg=[255,0,0],
      ),
    ]),
    Squircle(
    origin=[0]*2,
    dim=[64]*2,
    bg=get_palette()["HomeBackground"],
    radius=2,
    ),
    
  ])
)
#UPDATES+=[TREE]


#SELECTION_INDEX=1

#TREE.getLength()
TREE.__postinit__()
TREE.is_focused=True
TREE.__tick__(cascade=True)

# init renderer
set_pixel(-1,-1,[0]*3)

f=0
while f<666:
  #[e.__tick__() for e in UPDATES]
  #TREE.__tick__(cascade=True)
  
  #SELECTION_INDEX += (
  #  keyin(KEY_DOWN) - keyin(KEY_UP)
  #)
  
  #draw_string(
  #  string:=f" {SELECTION_INDEX}",
  #  scrW - len(string)*chrW,
  #  0,
  #)
  
  #TREE.getElement(SELECTION_INDEX).__tick__()
  
  
  f+=1

