#RANDOM BOT
import sys
import os
import random
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
from generic import movegen

def multikill(board, coin):
    moves = movegen.availableCoinMoves(board, coin)
    move = random.choice(moves)
    board.moveCoin(coin,move)
    if move[1] == coin[1] - 2 or move[1] == coin[1] + 2:
        board.eliminate((int((coin[0]+move[0])/2), int((coin[1]+move[1])/2)))
    if move[1] == 1:
        board.coins[board.getCoinByPos(move)].setKing()
    if movegen.checkMultiKill(board, move):
        multikill(board, move)

def bot(board):
    coins = movegen.coinsToMove(board,"black")
    rcoin = random.choice(coins)
    ind = board.getCoinByPos(rcoin)
    coin = board.coins[ind]
    coinpos = coin.getPosition()
    moves = movegen.availableCoinMoves(board, coinpos)
    move = random.choice(moves)
    board.moveCoin(coinpos,move)
    if move[1] == coinpos[1] - 2 or move[1] == coinpos[1] + 2:
        board.eliminate((int((coinpos[0]+move[0])/2), int((coinpos[1]+move[1])/2)))
    if move[1] == 1:
        board.coins[board.getCoinByPos(move)].setKing()
    if movegen.checkMultiKill(board, move):
        multikill(board, move)
    # print(move,type(move))
    # return coinpos, move