

import numpy as np
import tensorflow as tf
from tensorflow import keras
from keras import datasets, layers, models
import random
import chess



libra = ["a1", "b1","c1", "d1", "e1", "f1", "g1", "h1", "a2", "b2", "c2", "d2", "e2", "f2", "g2", "h2", "a3", "b3", "c3", "d3", "e3", "f3", "g3", "h3", "a4", "b4", "c4", "d4", "e4", "f4", "g4", "h4", "a5", "b5", "c5", "d5", "e5", "f5", "g5", "h5", "a6", "b6", "c6", "d6", "e6", "f6", "g6", "h6", "a7", "b7", "c7", "d7", "e7", "f7", "g7", "h7", "a8", "b8", "c8", "d8", "e8", "f8", "g8", "h8"]
  
def tomove(num):
  
  return str(libra[num//64]) + str(libra[num%64])

def outform(movenext):
  
  first = libra.index(movenext[:2])
  second = libra.index(movenext[2:4])

  return (first * 64 + second)


def tobit(board):
    black, white = board.occupied_co
    turn = str(int(board.turn)) * 64
    castling = board.castling_rights
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

    

    out = [[[0] * 15 for j in range(8)] for i in range(8)]
    for i in range(8):
      for j in range(8):
        for k in range(15):
          out[i][j][k] = int(bitboards[k][8 * i + j])
    return out