# -------------- Hardware --------------- #

scrWH = scrW, scrH = 320, 222
cliWH = cliW, cliH = 6, 10
chrWH = chrW, chrH = 10, 18


def sgn(signed_val):
  #return signed_val/abs(signed_val)
  return +1 if signed_val >= 0 else -1








"""
for var,val in {
  "scr": (320,222),
  "cli": (6,10),
  "chr": (10,18),
}.items():
  for dim in ["W","H","WH"]:
    exec(f"{var}={val}")
"""








#fill_rect(W//2-1,H//2,1,chrH,[255]*3)
#fill_rect(W//2,H//2-1,chrW,1,[255]*3)
#draw_string("0",W//2,H//2,[0]*3,[255,0,0])

#draw_string("0",W//2,H//2+chrH,[0]*3,[0,255,0])
