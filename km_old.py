from hw import *
from ion import *
#from grid import Grid

KEYS_PRESSED={}
LAST_KEYS={}

def updKey(key):
  global KEYS_PRESSED
  if keydown(key):
    KEYS_PRESSED|={key}
  else:
    KEYS_PRESSED-={key}


def keyon(key):  
  """
  if key in KEYS_PRESSED and not keydown(key):
    KEYS_PRESSED-={key}
    print("rm")
  if (not key in KEYS_PRESSED) and keydown(key):
    KEYS_PRESSED|={key}
    print("ad")
  """  
  #updKey(key)
  global KEYS_PRESSED
  KEYS_PRESSED[key]=keydown(key)
  return keydown(key)

def keyin(key):
  #print(key not in KEYS_PRESSED,keydown(key))
  out=key not in KEYS_PRESSED and keyon(key)
  keyon(key)
  return out

def keyout(key):
  out = key in KEYS_PRESSED and not keyon(key)
  keyon(key)
  return out

"""
while True:
  #print(KEYS_PRESSED,keyin(KEY_RIGHT),keyout(KEY_RIGHT))
  
  for e,event in enumerate([keyin,keyon,keyout]):
    if event(KEY_RIGHT):
      print(["in","on","out"][e])
      

"""