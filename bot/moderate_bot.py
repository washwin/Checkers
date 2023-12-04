#SIMPLE HEURISTIC BOT
import sys
import os
import numpy as np
import random
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

def killPositionScore(move):
    return homeCoinScore(move) + borderCoinScore(move) + kingCoinScore(move)

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
    move_coins = movegen.coinsToMove(board,"black")
    coin_heuristic = np.zeros((len(move_coins),), dtype=int)
    move_heuristic = np.zeros((len(2*move_coins),), dtype=int)
    black_coins = board.getAllBlackCoins()
    i = 0
    j = 0
    all_moves = []
    all_coins = []
    for coin in move_coins:
        coin_heuristic[i] = -homeCoinScore(coin) - borderCoinScore(coin) - chainingScore(black_coins, coin)
        moves = movegen.availableCoinMoves(board, coin)
        for move in moves:
            board.moveCoin(coin,move)
            move_heuristic[j] = coin_heuristic[i] + chainingScore(board.getAllBlackCoins(), move) + killPositionScore(move)
            board.moveCoin(move,coin)
            all_moves.append(move)
            all_coins.append(coin)
            if movegen.checkMultiKill(board, coin):
                multikill(board, coin)
                return
            j = j + 1
        i = i + 1
    
    i = np.where(move_heuristic == move_heuristic.max(axis=0))[0][0]
    board.moveCoin(all_coins[i], all_moves[i])
    if all_moves[i][1] == 8:
        board.coins[board.getCoinByPos(all_moves[i])].setKing()
    if all_moves[i][1] == all_coins[i][1] + 2 or all_moves[i][1] == all_coins[i][1] - 2:
        board.eliminate((int((all_coins[i][0]+all_moves[i][0])/2), int((all_coins[i][1]+all_moves[i][1])/2)))