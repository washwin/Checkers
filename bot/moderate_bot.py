#SIMPLE HEURISTIC BOT
import sys
import os
import numpy as np
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
from generic import movegen
from generic import util

#DEFINING PARAMETERS
home_coin_score = 2
border_coin_score = 1
king_coin_score = 3
chaining_score = 1
multi_kill_score = 3

def homeCoinScore(cp):
    if cp[1] == 8:
        return home_coin_score
    return 0

def borderCoinScore(cp):
    if cp[0] == 1 or cp[0] == 8:
        return border_coin_score
    return 0

def kingCoinScore(cp):
    if cp[1] == 1:
        return king_coin_score
    return 0

def chainingScore(coins, cp):
    chain = 0
    i = 1
    while (cp[0]+i, cp[1]+i) in coins:
        chain = chain + chaining_score
        i = i + 1
    i = 1
    while (cp[0]-i, cp[1]-i) in coins:
        chain = chain + chaining_score
        i = i + 1
    i = 1
    while (cp[0]-i, cp[1]+i) in coins:
        chain = chain + chaining_score
        i = i + 1
    i = 1
    while (cp[0]+i, cp[1]-i) in coins:
        chain = chain + chaining_score
        i = i + 1 
    return chain

def multiKillScore(board, move):
    while movegen.checkMultiKill(board, move):
        print("hello")
    return 0

def killPositionScore(move):
    return homeCoinScore(move) + borderCoinScore(move) + kingCoinScore(move)
    
def bot(board):
    move_coins = movegen.coinsToMove(board,"black")
    heuristic = np.zeros((len(move_coins),), dtype=int)
    black_coins = board.getAllBlackCoins()
    i = 0
    for coin in move_coins:
        heuristic[i] = homeCoinScore(coin) + borderCoinScore(coin) + chainingScore(black_coins, coin) + kingCoinScore(coin)
        moves = movegen.availableCoinMoves(board, coin)
        for move in moves:
            board.moveCoin(coin,move)
            heuristic[i] = heuristic[i] + chainingScore(board.getAllBlackCoins(), move) + multiKillScore(board, move) + killPositionScore(move)
            board.moveCoin(move,coin)
        i = i + 1
    board.display()
    print(heuristic)

def test():
    board = util.Board()
    util.testing(board)
    bot(board)
test()