import chess
import random
import time
import math
import tensorflow as tf

searchboard = chess.Board()

centerdistance = [0.0] * 64
for i in range(8):
    for j in range(8):
        centerdistance[8 * i + j] = 1 - 0.01 * (abs(i - 3.5) + abs(j - 3.5))

values = {
    "K": 2,
    "k": 2,
    "Q": 9,
    "q": -9,
    "R": 5,
    "r": -5,
    "N": 3,
    "n": -3,
    "B": 3,
    "b": -3,
    "P": 1,
    "p": -1,
    "None": 0
}


class node:
    visitcount = 0
    sum = 0

    def __init__(self, parent, move):
        global searchboard
        self.parent = parent
        self.move = move
        self.children = []


def evaluate(board):
    if board.is_game_over():

        winningplayer = board.outcome().winner
        if winningplayer is None:
            return 0
        elif winningplayer:
            return 11
        else:
            return -11

    s = sum(values[f"{board.piece_at(i)}"] for i in range(64)) + (2 * board.turn - 1) * 0.1 * len(
        list(board.legal_moves))
    return 0.5 * (abs(s + 10) - abs(s - 10))
    # return s


'''def evaluate(board):
  playoutboard = board.copy()

  while not playoutboard.is_game_over():

    randommove = random.choice(list(playoutboard.legal_moves))
    playoutboard.push(randommove)

  winningplayer = playoutboard.outcome().winner
  if winningplayer is None:
    return 0
  if winningplayer:
    return 1
  return -1'''


def score(node):
    if not node.visitcount:
        return node.parent.visitcount
    exploit = node.sum / node.visitcount

    explore = math.sqrt(2 * math.log(node.parent.visitcount) / node.visitcount)
    return explore + exploit


def montecarlo(startnode):
    global searchboard

    startnode.visitcount += 1

    if (startnode.visitcount == 1) or searchboard.is_game_over():
        x = evaluate(searchboard)

    else:
        if startnode.visitcount == 2:
            for i in searchboard.legal_moves:
                startnode.children.append(node(startnode, i))
                # skapa endast barn när de behövs

        best = startnode.children[0]
        for i in startnode.children:
            if score(i) > score(best):
                best = i

        searchboard.push(best.move)
        x = montecarlo(best)
        searchboard.pop()

    if searchboard.turn:
        startnode.sum -= x
    else:
        startnode.sum += x
    return x


def findmove(board, searchtime):
    global searchboard

    if board.is_game_over():
        return None

    searchboard = board.copy()
    root = node(None, None)
    starttime = time.time()

    count = 0
    while time.time() - starttime < searchtime:
        count += 1
        montecarlo(root)

    chosen = root.children[0]
    for candidate in root.children:
        if candidate.visitcount > chosen.visitcount:
            chosen = candidate

    print(count)

    return chosen.move


def playbot(board, searchtime, playercolour):
    while not board.is_game_over():

        if board.turn == playercolour:

            print("make a move")
            while True:
                try:
                    board.push_san(input())
                except Exception:
                    print("invalid move")
                else:
                    break

            print(board)
            print("")

        else:

            botmove = findmove(board, searchtime)
            board.push(botmove)
            print(board)
            print("")
            # print(f"bot played {board.san(botmove)}")

    print(board.outcome().termination)


board = chess.Board()
for i in range(0):
    board.push_san(input())
    print(board)

playbot(board, 5, True)






