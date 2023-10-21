#RANDOM BOT
import sys
import os
import random
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
from generic import movegen

def bot(board):
    coins = movegen.coinsToMove(board,"black")
    rcoin = random.choice(coins)
    ind = board.getCoinByPos(rcoin)
    coin = board.coins[ind]
    coinpos = coin.getPosition()
    moves = movegen.availableCoinMoves(board, coinpos)
    move = random.choice(moves)
    return coinpos, move