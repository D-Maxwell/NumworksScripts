# ------------- BoxLayout --------------- #

from math import *
from kandinsky import *
from hw import *
from ms import *
from km import *
from ion import *


UPDATES=[]



class Box:
  properties={
    "pos":[0]*2,
    "dim":[0]*2,
    "origin":[-1]*2,
    
    "abspos":[0]*2,
    "absdim":[0]*2,
    
    "margin":[0]*2,
    "padout":[0]*2,
    "padin":[0]*2,
    
    "bg":[],
    
    
    "is_focused":False,
    
    "parent":None,
    "children":[],
    
    "dyns":{},
  }
  def __init__(self,**kwargs):
    
    LOCALS={"self":self}
    
    for attr,value in self.properties.items():
      value=kwargs.get(attr, value)
      
      if type(value) is type(lambda:None):
        self.dyns[attr]=value
        value=value()
      
      LOCALS["attr"]=attr
      LOCALS["value"]=value
      
      exec(f"self.{attr}=value", LOCALS)
      
    
    
    """
    self.pos = kwargs.get("pos", [0]*2)
    self.dim = kwargs.get("dim", [0]*2)
    
    self.origin = kwargs.get("origin", [-1]*2)
    """
    
    self.absPos()
    self.absDim()
    
    """
    self.margin = kwargs.get("margin", [0]*2)
    self.padout = kwargs.get("padout", [0]*2)
    self.padin  = kwargs.get("padin",  [0]*2)
    
    self.is_focused = False
    
    self.parent = kwargs.get("parent", None)
    self.children = kwargs.get("children", [])
    """
    
    for child in self.children:
      child.parent=self
      
    """
    #self.idx=self.setIdx()
    
    
    self.bg=kwargs.get("bg", [])
    
    
    self.dynvars={}
    
    self.data=kwargs.get("data",{})
    """
    
  
  def __postinit__(self):
    if self.parent is None:
      self.setIdx()
      self.is_focused=True
    
    self.__draw__()
    
    for child in self.children:
      child.__postinit__()
      
    
  
  def setIdx(self, prevlength=0):
    
    self.idx=prevlength
    
    length=1
    
    #print(self,self.children,self.idx)
    
    for child in self:
      length += child.setIdx(prevlength+length)
      
    print(self.idx)
    
    return length
  
  
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
    
    if self.outline != [0,0]:
      fill_rect(
        *[pos - outline
        for pos,outline in
        zip(absPos(),self.outline)],
        *[dim + 2*outline
        for dim,outline in
        zip(absDim(),self.outline)],
        ,
      )
    
    
    fill_rect(
      self.absPos()[0],
      self.absPos()[1],
      self.absDim()[0],
      self.absDim()[1],
      [255]*3 if self.is_focused else self.bg,
    )
    
    focus_stroke = 1
    
    if self.is_focused:
      draw_string(
        str(self),
        scrW-len(str(self))*chrW,
        0,
      )
      
      fill_rect(
        self.absPos()[0]+focus_stroke,
        self.absPos()[1]+focus_stroke,
        self.absDim()[0]-focus_stroke*2,
        self.absDim()[1]-focus_stroke*2,
        self.bg,
      )

  
  def __erase__(self):
    pass
    
  
  def __upd__(self):
    #if SELECTION_INDEX != self.idx:
      #print(self.idx)
      #return
    
    LOCALS={"self":self}
    for attr,getter in self.dyns.items():
      LOCALS["getter"]=getter
      exec(f"self.{attr}=getter()", LOCALS)
    
    
    
    self.isFocused()
    
    if self.is_focused:
      
      draw_string(
        str(self.idx),
        self.absPos()[0],
        self.absPos()[1],
        [255]*3,
        self.bg if self.bg!=[] else get_palette()["HomeBackground"],
      )
      
      return
      
      [draw_string(
          info,
          scrW-len(info)*chrW,
          (i+1)*chrH,
        ) for i,info in enumerate([
          f"{self.idx=}",
          #f"{parent_idx=}",
        ])]
    
  
  def __tick__(self, cascade=False):
    
    if self.is_focused:
      self.__erase__()
      self.__upd__()
      self.__draw__()
    
    """
    draw_string(
      f"{self.idx}",
      *self.absPos(),
      [255]*3,
      self.bg,
    )
    """
    
    if not cascade: #and self not in UPDATES:
      return
    
    for child in self.children:
      child.__tick__(cascade=cascade)
  
  def __getitem__(self, idx):
    if type(idx) is int:
      return self.children[idx]
    if type(idx) is str:
      return self.data[idx]
    
  
  def old_isFocused(self):
    gyro=[
      keyin(KEY_LEFT) - keyin(KEY_RIGHT),
      keyin(KEY_DOWN) - keyin(KEY_UP),
    ]
    
    flow=1
    
    try:
      offset = self.idx - self.parent.idx - 1
      parent_offset = self.parent.parent.idx - self.parent.idx - 1
      
    except:
      offset = 0
      parent_offset = 0
      
    finally: pass
    
    
    if gyro != [0]*2:
      self.is_focused=False
      
    #else:
    #  return
    
    if self.parent is not None:
      if offset+gyro[flow] < 0:
        self.parent.is_focused=True
        
      elif offset+gyro[flow] >= len(self.parent.children):
        self.parent.parent[self.parent.parent.index(self.parent)+1].is_focused=True
        
      elif gyro[flow] != 0:
        print(f"{self.idx=} {offset=} {gyro=}")
        self.parent[offset+gyro[flow]].is_focused=True
      
    
    if gyro[1-flow] < 0:
      if self.parent is not None:
        self.parent.is_focused=True
      
    elif gyro[1-flow] > 0 or (
      offset<=0 and gyro[flow]>0
    ):
      if self.children != []:
        self[0].is_focused=True
    
    
    """
    if self.parent is None:
      parent_idx=0
    else:
      parent_idx=self.parent.idx
    """
    
    """
    if self.is_focused:
      self.parent.isFocused()
    else:
      self[0].isFocused()
    """
    
    """
    if gyro!=[0]*2:
      self.is_focused=False
    
    if self.parent is not None:
      if not (
        0 <= self.idx - self.parent.idx
        + gyro[1] - 1 < len(self.parent.children)
      ):
        self.parent.is_focused=True
      else:
        self.parent[
          self.idx
          - self.parent.idx
          + gyro[1] - 1
        ].is_focused = True
        
    if gyro[0]<0 and self.parent is not None:
      self.parent.is_focused=True
    elif gyro[0]>0:
      self[0].is_focused=True
    """
    
    """
    if gyro[0] == 0 and gyro[1] != 0:
      
      if self.parent is None and gyro[1]<0: return
      
      self.parent[gyro[1]
        + self.idx
        - parent_idx
        ].is_focused = True
      
    if gyro[0] != 0 and gyro[1] == 0:
      
      if (
        gyro[0]<0 and self.parent is None
        or( gyro[0]>0 and self.children==[] )
      ): return
      #self.parent.is_focused = False
      
      if gyro[0]<0:
        self.parent.is_focused=True
      else:
        self[0].is_focused=True
    
    
    self.is_focused=False
    
    if gyro == [0]*2:
      self.is_focused=True
    """
    
  
  def isFocused(self):
    gyro = [
      keyin(KEY_RIGHT) - keyin(KEY_LEFT),
      keyin(KEY_DOWN) - keyin(KEY_UP),
    ]
    
    draw_string(
      str(gyro),
      scrW  -  chrW * len( str(gyro) ),
      chrH,
    )
    
    flow = 1
    
    if gyro != [0,0]:
      self.is_focused=False
    else:
      return
    
    try:
      offset=self.idx-self.parent.idx-1
    except:
      offset=0
    
    
    if ( False
      or ( self.parent is None )
      or not ( 0 <= offset+gyro[flow] < len(self.parent.children) )
    ):
      gyro[1-flow]=sgn(gyro[flow])
      gyro[flow]=0
    elif gyro[flow] != 0:
      if self.parent is not None:
        self.parent[offset+gyro[flow]].is_focused=True
    
    if gyro[1-flow] < 0:
      if self.parent is not None:
        self.parent.is_focused=True
    elif gyro[1-flow] > 0:
      print(len(self.children))
      if len(self.children) > 0:
        self[0].is_focused=True
        print(gyro)
      else:
        if self.parent is None: return
        parent=self.parent
        while parent[-1].idx<=self.idx:
          parent=parent.parent
        for child in parent:
          if child.idx>self.idx:
            child.is_focused=True
            break
          
    #except:
    #  self.is_focused=True


class Label(Box):
  
  properties={
    "label":[""],
    "fg":[],
  }
  
  def __init__(self,**kwargs):
    self.properties.update(**super().properties)
    
    super().__init__(**kwargs)
        
    #if self.dim[0] == 0 and self.label != "":
    #  if self.parent is not None:
    #    self.dim[0] = self.parent.dim[0]
    
    if self.dim[0] != 0:
      #self.label = 
      pass
    
    self.dim[0] = min(
      self.dim[0],
      chrW * max([
        len(string)
        for string in self.label
      ]),
    )
    
    self.dim[1] = max(
      self.dim[1],
      chrH * len(self.label)
    )
  
  
  
  def __draw__(self):
    super().__draw__()
    
    for s,string in enumerate(self.label):
      draw_string(
        string[:self.dim[0]//chrW],
        self.absPos()[0],
        self.absPos()[1] + s*chrH,
        [255]*3,
        self.bg,
      )
    
  
  def __upd__(self):
    if type(self.label) is str:
      self.label = [self.label]
    
    super().__upd__()


from rc import Squircle


TREE=(
  Box(
  dim=[196]*2,
  padin=[16]*2,
  padout=[4]*2,
  bg=[0,0,255],
  children=[
    
    Box(
    dim=[32]*2,
    bg=[0,255,0],
    ),
    
    Box(
    pos=[64]*2,
    dim=[80]*2,
    padin=[16]*2,
    bg=[0,255,0],
    children=[
      Box(
      dim=[24]*2,
      bg=[255,0,0],
      origin=[1,1],
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


def init():
  global TREE

  #UPDATES+=[TREE]


  #SELECTION_INDEX=1

  #TREE.getLength()
  TREE.__postinit__()
  #TREE[0].is_focused=True
  TREE.__tick__(cascade=True)

  # init renderer
  set_pixel(-1,-1,[0]*3)


def tick():
  global TREE
  
  #[e.__tick__() for e in UPDATES]
  TREE.__tick__(cascade=True)
  
  #SELECTION_INDEX += (
  #  keyin(KEY_DOWN) - keyin(KEY_UP)
  #)
  
  #draw_string(
  #  string:=f" {SELECTION_INDEX}",
  #  scrW - len(string)*chrW,
  #  0,
  #)
  
  #TREE.getElement(SELECTION_INDEX).__tick__()
  
  
"""
init()
f=0
while f<666:
  tick()
  f+=1
"""