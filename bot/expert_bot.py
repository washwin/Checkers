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
MIN = -100
MAX = 100
home_coin_score = 2
border_coin_score = 1
king_coin_score = 3
chaining_score = 1

def alphaBeta(depth, nodeIndex, maximizingPlayer, values, alpha, beta):
    if depth == 3:
        return values[nodeIndex]
    
    if maximizingPlayer:
        best = MIN
        for i in range(0, 2):
            val = alphaBeta(depth + 1, nodeIndex*2 + i, False, values, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    
    else:
        best = MAX
        for i in range(0, 2):
            val = alphaBeta(depth + 1, nodeIndex*2 + i, False, values, alpha, beta)
            best = max(best, val)
            beta = max(alpha, best)
            if beta <= alpha:
                break
        return best
