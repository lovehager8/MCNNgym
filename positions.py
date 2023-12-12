import util

import numpy as np
def a(n):
  
  file = open("failenhame.txt", "r")
  inparrarr = []
  outparrarr = []
  resultarr = []
  try:
    for i in range(n):
      
      inp = file.readline()
      
      outp = file.readline()
  
      result = file.readline()
      inparr = np.zeros((8,8,15), int)
      for i in range(15):
        for j in range(8):
          for k in range(8):
            inparr[k][j][i] = int(inp[k*15*8 + j*15 + i])

      outarr = [0]* int(outp[:-1])
      outarr += [1]
      outarr += [0] * (4096-len(outarr))
      outarr = np.array(outarr)
      inparrarr.append(inparr)
      outparrarr.append(outarr)
      resultarr.append(int(result[:-1]))

      
    return [np.array(inparrarr), np.array(outparrarr), np.array(resultarr)]
  except Exception as error:
    return [np.array(inparrarr), np.array(outparrarr), np.array(resultarr)]
  

