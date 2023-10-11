# ------------- KeyManager -------------- #

from math import *
from ion import *


LAST_KEYS={}
KEYS_IN={}

def keyin(key):
  
  out=False
  
  if keydown(key):
    
    if not LAST_KEYS.get(key):
      out=True
    
    #KEYS_IN[key]=True
    LAST_KEYS[key]=True
  else:
    LAST_KEYS[key]=False
    #KEYS_IN[key]=False
  
  global KEYS_IN
  if out:
    KEYS_IN[key]=True
  elif KEYS_IN.get(key) is not None:
    del KEYS_IN[key]
  
  return out

def keyout(key):
  out=False
  
  if not keydown(key):
    
    if LAST_KEYS.get(key):
      out=True
    
    LAST_KEYS[key]=False
  else:
    LAST_KEYS[key]=True

  return out


def keyon(key):
  out=False
  if keydown(key):
    if LAST_KEYS[key]:
      out=True
    LAST_KEYS[key]=True
  else:
    LAST_KEYS[key]=False

  return out


"""
def keyheld(key,time=0):
  yield
  if time==0:
    return keyin(key)
"""

"""
while True:
  keyin(KEY_DOWN)
  print(KEYS_IN)
"""
"""
  for key in [KEY_UP,KEY_DOWN,KEY_LEFT,KEY_RIGHT]:
    if keyin(key):
      print(key)
"""
"""
  if keydown(key):
    
    if not LAST_KEYS[key]:
      print("in")
    else:
      print("hold")
    
    LAST_KEYS[key]=True

  else:
    
    if LAST_KEYS.get(key):
      print("out")
    
    LAST_KEYS[key]=False
"""
  
  #print(keyin(key))
  
  #LAST_KEYS[key]=False
  
