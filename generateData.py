import chess
import chess.pgn
import numpy as np
import outp
import random

pgn = open('lichess_elite_2022-11.pgn')
file = open("failenhame.txt", "a")
w = 0

def gen_input():
  global w
  if w == 1:
    return False
  w+=1
  try:
    first_game = chess.pgn.read_game(pgn)
  except error:
    return False

  board = first_game.board()
  next = ''

  gamelen = len(list(first_game.mainline_moves()))
  gamethird = (gamelen) // 3
  firstmove = random.randint(0, gamethird)
  secondmove = random.randint(gamethird, 2 * gamethird)
  thirdmove = random.randint(gamethird * 2, gamethird * 3 + gamelen % 3)

  for i, move in enumerate(first_game.mainline_moves()):
    if (i != firstmove) and (i != secondmove) and (i != thirdmove):
      board.push(move)
      continue
    
    next = move

    black, white = board.occupied_co
    turn = str(int(board.turn)) * 64
    castling = board.castling_rights
    result = first_game.headers["Result"]
    enpassant = board.ep_square
    if enpassant is not None:
      enpassant = ('0' * (enpassant - 1)) + '1' + ('0' * (64 - enpassant))
    else:
      enpassant = '0' * 64

    bitboards = np.array([
        format(black & board.pawns, '064b'),
        format(black & board.knights, '064b'),
        format(black & board.bishops, '064b'),
        format(black & board.rooks, '064b'),
        format(black & board.queens, '064b'),
        format(black & board.kings, '064b'),
        format(white & board.pawns, '064b'),
        format(white & board.knights, '064b'),
        format(white & board.bishops, '064b'),
        format(white & board.rooks, '064b'),
        format(white & board.queens, '064b'),
        format(white & board.kings, '064b'),
        format(castling, '064b'),
        enpassant,
        turn,
    ],
                         dtype=str)

    result = result.split('-')
    if result[0] == "1/2":
      result = [0, 0]
    result = str(int(result[0]) - int(result[1]))
    inpstring = ''

    out = [[[0] * 15 for j in range(8)] for i in range(8)]
    for i in range(8):
      for j in range(8):
        for k in range(15):
          out[i][j][k] = int(bitboards[k][8 * i + j])
    for a in out:
      for b in a:
        for c in b:
          inpstring += str(c)

    print(str(move))
    outstring = outp.outform(str(next))
    print(outstring, first_game.headers["White"], first_game.headers["Black"])
    file.writelines([inpstring + "\n", outstring + "\n", result + "\n"])
    board.push(move)
    print("heyyy")
    continue

  return True


while gen_input():
  pass

file.close()
