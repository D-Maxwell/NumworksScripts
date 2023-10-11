def deco(file_name:str):
  file=open(file_name+".py","rw")
  print(file.readable())
  file.writelines([" hello there ;"]+file.readlines())