from hw import *

def echo(*strings,wrap=False,sep=""):
  out = "\n".join(
    [string[:len(string) if wrap else scrW//cliW] for string in sep.join(
      [str(string) for string in strings]
    ).split("\n")]
  )
  
  print(out,sep="")


class ls:
  def __type__(self):
    print("c")
  def __new__(self):
    print("ht")