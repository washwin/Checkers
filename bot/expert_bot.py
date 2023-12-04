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

def alphaBeta()