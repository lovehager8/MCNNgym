import numpy as np
import positions
import tensorflow as tf
from tensorflow import keras
from keras import datasets, layers, models
import random
import chess
import outp

import util

model = keras.models.load_model("v2.keras")

def predict(board):


    bb = np.array([util.tobit(board)])


    y, z = model.predict(bb)

    y = list(y[0])
    best = 0
    bestmove = None
    for  move in board.legal_moves:
        ind = int(outp.outform(str(move)))
        print(move)
        print(ind)
        print(y[ind])
        if y[ind] > best:
            best = y[ind]
            bestmove = move
    print(y.index(max(y)))
    print(max(y))
    return bestmove


board = chess.Board()

print(predict(board))