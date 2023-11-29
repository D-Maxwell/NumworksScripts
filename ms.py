# ----------- MapShorthands ------------- #

def lmap(func,*args):
  args=list(args)
  max_length=max([
    len(arg) for arg in args
    if type(arg) is list
  ])
  for n,number in enumerate(args):
    if type(number) in [list,tuple]: continue
    args[n]=[number]*max_length
  return list(map(func,*args))

ADD=lambda *args: sum(args)

def mul(args:[]):
  out=1
  for arg in args:
    out*=arg
  return out
MUL=lambda *args: mul(args)
