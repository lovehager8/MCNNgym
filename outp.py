alfa = ["a", "b", "c", "d", "e", "f", "g", "h"]
libra = [
    "a1", "b1", "c1", "d1", "e1", "f1", "g1", "h1", "a2", "b2", "c2", "d2",
    "e2", "f2", "g2", "h2", "a3", "b3", "c3", "d3", "e3", "f3", "g3", "h3",
    "a4", "b4", "c4", "d4", "e4", "f4", "g4", "h4", "a5", "b5", "c5", "d5",
    "e5", "f5", "g5", "h5", "a6", "b6", "c6", "d6", "e6", "f6", "g6", "h6",
    "a7", "b7", "c7", "d7", "e7", "f7", "g7", "h7", "a8", "b8", "c8", "d8",
    "e8", "f8", "g8", "h8"
]


def outform(movenext):
  first = libra.index(movenext[:2])
  second = libra.index(movenext[2:4])
  firstl = int(alfa.index(movenext[0]))
  secondl = int(alfa.index(movenext[2]))
  a = 65
  if movenext[0] == movenext[2]:
    #up and down
    if first > second:
      a = -(int(movenext[3]) - int(movenext[1])) - 1
    else:
      a = 6 + int(movenext[3]) - int(movenext[1])
  elif movenext[1] == movenext[3]:
    # right and left
    if first > second:
      a = 13 + firstl - secondl
    else:
      a = 20 + secondl - firstl
  elif abs(firstl - secondl) == abs(int(movenext[1]) - int(movenext[3])):
    # diagonals
    if first > second:
      if firstl > secondl:
        a = 27 - (int(movenext[3]) - int(movenext[1]))
      else:
        a = 34 - (int(movenext[3]) - int(movenext[1]))
    else:
      if firstl > secondl:
        a = 41 + (int(movenext[3]) - int(movenext[1]))
      else:
        a = 48 + (int(movenext[3]) - int(movenext[1]))
  else:
    # knight moves
    if first > second:
      if firstl > secondl:
        a = 55 - (int(movenext[3]) - int(movenext[1]))
      else:
        a = 57 - (int(movenext[3]) - int(movenext[1]))
    else:
      if firstl > secondl:
        a = 59 + int(movenext[3]) - int(movenext[1])
      else:
        a = 61 + int(movenext[3]) - int(movenext[1])
  if a == 65:
    return "99999"
  a += first * 64
  return str(a)




def backform(a):
  a = int(a)
  first = libra[a // 64]
  for i in range(64):
    if int(outform(first + libra[i])) == a:
      return first + libra[i]

