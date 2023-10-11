from hw import *
from kandinsky import *
from ion import *
from math import ceil,floor
from random import randint
import time


SETTINGS={
  "CHARACTERS": "".join([
    (alphabet:="ABCDEFGHIJKLMNOPQRSTUVWXYZ")+alphabet.lower(),
    #"".join([str(e) for e in list(range(10))]),
    " " * 20,
  ]),
  "FIZZLE": False,
  "SPEED": 1/2,
  "COLOR": [96]*3,
}

FIELDS={
  (1,2):{
    "name": "Time",
    "data": time.monotonic(),
  },
  (2,3):{
    "name": "Battery",
    "data": str(
      floor(battery_level()*10**3)/10
    )[:4]+"%",
  },
  #():{
  #  "name": "Memory",
  #  "data": str(),
  #},
}


def genLine(chars:"",length:int):
  return "".join([
    chars[randint(0,len(chars)-1)]
    for x in range(length)
  ])

str_array = [
  genLine(SETTINGS["CHARACTERS"], ceil(scrW/chrW))
  for y in range(scrH//chrH+2)
]


def settings():
  pass


scroll=0

def upd():
  global str_array,scroll
  
  scroll += SETTINGS["SPEED"]
  if scroll%chrH==0:
    scroll=0
    str_array=[genLine(
      SETTINGS["CHARACTERS"],
      ceil(scrW/chrW),
    )] + str_array[scroll//chrH:]
  
  for y,string in enumerate(str_array):
    if SETTINGS["FIZZLE"]: y-=1
    
    str_pos=randint(0,len(string)-1)
    str_array[y] = (
      string[:str_pos] +
      SETTINGS["CHARACTERS"][randint(0,len(SETTINGS["CHARACTERS"])-1)] +
      string[str_pos+1:]
    )
    
    if not SETTINGS["FIZZLE"]: y-=1
        
    abs_pos=y * chrH + scroll
    
    print(string)
    for x,chr in enumerate(string):
      field=FIELDS.get((x,y),None)
      if field is None: continue
      string=[
        string[:x],
        [(bit:=f" {field["name"]}: {field["data"]} ")],
        string[x+len(bit):len(string)],
        #print(len(string),len(bit))
      ]
    if type(string) is str: string=[string]
    
    print(string)
    
    str_width=0
    for b,bit in enumerate(string):
      escape_fade=False
      if type(bit) is list:
        bit=bit[0]
        string[b]=bit
        escape_fade=True
      str_width+=len(bit)
      #print(sum([len(s) for s in string[:b]]))
      draw_string(
        bit,
        chrW*(sum([len(s) for s in string[:b]])),
        floor(abs_pos),
        get_palette()["PrimaryText"] if escape_fade else [max(channel,
          SETTINGS["COLOR"][idx] - ceil(
            max(abs_pos,0)/scrH*(
              SETTINGS["COLOR"][idx] - channel
            )
          ))
        for idx,channel in enumerate(get_palette()["HomeBackground"])],
      )
    y+=1
  
  """
  for field in FIELDS:
    draw_string(
      f"{field["name"]}: {field["data"]}",
      field["pos"][0],
      field["pos"][1],#+floor(scroll),
    )
  """
  

FPS_CAP=70
while True:
  upd()
  #draw_string(str(FPS_CAP),0,0)
  #FPS_CAP+=keydown(KEY_RIGHT)-keydown(KEY_LEFT)
  time.sleep(1/FPS_CAP)
  
