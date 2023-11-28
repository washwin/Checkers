#Function parameters: current board object, color of the player for which we need to find available kill moves
#Return value: killcoins-> contains location of coins that have available kill
#Return datatype: list
def checkKill(board,color):
    killcoins = []
    if color == 'red':
        for coin in board.coins:
            if coin.getColor() == color:
                loc = coin.getPosition()
                if not coin.isKing():
                    i = board.getCoinByPos((loc[0]+1,loc[1]+1))
                    if i != 26 and isTile((loc[0]+2,loc[1]+2)):
                        if board.coins[i].getColor() != color:
                            if (loc[0]+2,loc[1]+2) not in board.getAllCoins():
                                killcoins.append(loc)
                    i = board.getCoinByPos((loc[0]-1,loc[1]+1))
                    if i != 26 and isTile((loc[0]-2,loc[1]+2)):
                        if board.coins[i].getColor() != color:
                            if (loc[0]-2,loc[1]+2) not in board.getAllCoins():
                                killcoins.append(loc)
                else:
                    i = board.getCoinByPos((loc[0]+1,loc[1]+1))
                    if i != 26 and isTile((loc[0]+2,loc[1]+2)):
                        if board.coins[i].getColor() != color:
                            if (loc[0]+2,loc[1]+2) not in board.getAllCoins():
                                killcoins.append(loc)
                    i = board.getCoinByPos((loc[0]-1,loc[1]+1))
                    if i != 26 and isTile((loc[0]-2,loc[1]+2)):
                        if board.coins[i].getColor() != color:
                            if (loc[0]-2,loc[1]+2) not in board.getAllCoins():
                                killcoins.append(loc)
                    i = board.getCoinByPos((loc[0]+1,loc[1]-1))
                    if i != 26 and isTile((loc[0]+2,loc[1]-2)):
                        if board.coins[i].getColor() != color:
                            if (loc[0]+2,loc[1]-2) not in board.getAllCoins():
                                killcoins.append(loc)
                    i = board.getCoinByPos((loc[0]-1,loc[1]-1))
                    if i != 26 and isTile((loc[0]-2,loc[1]-2)):
                        if board.coins[i].getColor() != color:
                            if (loc[0]-2,loc[1]-2) not in board.getAllCoins():
                                killcoins.append(loc)
    else:
        for coin in board.coins:
            if coin.getColor() == color:
                loc = coin.getPosition()
                if not coin.isKing():
                    i = board.getCoinByPos((loc[0]+1,loc[1]-1))
                    if i != 26 and isTile((loc[0]+2,loc[1]-2)):
                        if board.coins[i].getColor() != color:
                            if (loc[0]+2,loc[1]-2) not in board.getAllCoins():
                                killcoins.append(loc)
                    i = board.getCoinByPos((loc[0]-1,loc[1]-1))
                    if i != 26 and isTile((loc[0]-2,loc[1]-2)):
                        if board.coins[i].getColor() != color:
                            if (loc[0]-2,loc[1]-2) not in board.getAllCoins():
                                killcoins.append(loc)
                else:
                    i = board.getCoinByPos((loc[0]+1,loc[1]+1))
                    if i != 26 and isTile((loc[0]+2,loc[1]+2)):
                        if board.coins[i].getColor() != color:
                            if (loc[0]+2,loc[1]+2) not in board.getAllCoins():
                                killcoins.append(loc)
                    i = board.getCoinByPos((loc[0]-1,loc[1]+1))
                    if i != 26 and isTile((loc[0]-2,loc[1]+2)):
                        if board.coins[i].getColor() != color:
                            if (loc[0]-2,loc[1]+2) not in board.getAllCoins():
                                killcoins.append(loc)
                    i = board.getCoinByPos((loc[0]+1,loc[1]-1))
                    if i != 26 and isTile((loc[0]+2,loc[1]-2)):
                        if board.coins[i].getColor() != color:
                            if (loc[0]+2,loc[1]-2) not in board.getAllCoins():
                                killcoins.append(loc)
                    i = board.getCoinByPos((loc[0]-1,loc[1]-1))
                    if i != 26 and isTile((loc[0]-2,loc[1]-2)):
                        if board.coins[i].getColor() != color:
                            if (loc[0]-2,loc[1]-2) not in board.getAllCoins():
                                killcoins.append(loc)
    t = set(killcoins)
    killcoins = (list(t))
    return killcoins

#Function parameters: current board object, color of the player for which we need to find all available moves
#Return value: movecoins-> contains location of coins that are allowed to move
#Return datatype: list
def coinsToMove(board, color):
    movecoins = checkKill(board,color)
    if len(movecoins) > 0:
        return movecoins        #must take the kill
    else:
        movecoins = []
        if color == 'red':
            for coin in board.coins:
                if coin.getColor() == color:
                    loc = coin.getPosition()
                    if not coin.isKing():
                        i = board.getCoinByPos((loc[0]+1,loc[1]+1))
                        if i == 26 and isTile((loc[0]+1,loc[1]+1)):
                            movecoins.append(loc)
                        i = board.getCoinByPos((loc[0]-1,loc[1]+1))
                        if i == 26 and isTile((loc[0]-1,loc[1]+1)):
                            movecoins.append(loc)
                    else:
                        i = board.getCoinByPos((loc[0]+1,loc[1]+1))
                        if i == 26 and isTile((loc[0]+1,loc[1]+1)):
                            movecoins.append(loc)
                        i = board.getCoinByPos((loc[0]-1,loc[1]+1))
                        if i == 26 and isTile((loc[0]-1,loc[1]+1)):
                            movecoins.append(loc)
                        i = board.getCoinByPos((loc[0]+1,loc[1]-1))
                        if i == 26 and isTile((loc[0]+1,loc[1]-1)):
                            movecoins.append(loc)
                        i = board.getCoinByPos((loc[0]-1,loc[1]-1))
                        if i == 26 and isTile((loc[0]-1,loc[1]-1)):
                            movecoins.append(loc)
        else:
            for coin in board.coins:
                if coin.getColor() == color:
                    loc = coin.getPosition()
                    if not coin.isKing():
                        i = board.getCoinByPos((loc[0]+1,loc[1]-1))
                        if i == 26 and isTile((loc[0]+1,loc[1]-1)):
                            movecoins.append(loc)
                        i = board.getCoinByPos((loc[0]-1,loc[1]-1))
                        if i == 26 and isTile((loc[0]-1,loc[1]-1)):
                            movecoins.append(loc)
                    else:
                        i = board.getCoinByPos((loc[0]+1,loc[1]+1))
                        if i == 26 and isTile((loc[0]+1,loc[1]+1)):
                            movecoins.append(loc)
                        i = board.getCoinByPos((loc[0]-1,loc[1]+1))
                        if i == 26 and isTile((loc[0]-1,loc[1]+1)):
                            movecoins.append(loc)
                        i = board.getCoinByPos((loc[0]+1,loc[1]-1))
                        if i == 26 and isTile((loc[0]+1,loc[1]-1)):
                            movecoins.append(loc)
                        i = board.getCoinByPos((loc[0]-1,loc[1]-1))
                        if i == 26 and isTile((loc[0]-1,loc[1]-1)):
                            movecoins.append(loc)
        t = set(movecoins)
        movecoins = list(t)
        return movecoins
    

#finds whether or not a tile exists
def isTile(loc):
    if loc[0] not in range(1,9) or loc[1] not in range(1,9):
        return False
    return True

#Function parameters: current board object, location of coin that we intend to move
#Return value: moves->contains loctions where that particular coin can move to
#Return datatype: list
def availableCoinMoves(board, loc):
    i = board.getCoinByPos(loc)
    coin = board.coins[i]
    moves = []
    killcoins = checkKill(board,coin.getColor())
    if loc in killcoins:
        if not coin.isKing():
            if coin.getColor() == "red":
                i = board.getCoinByPos((loc[0]+2,loc[1]+2))
                i1 = board.getCoinByPos((loc[0]+1,loc[1]+1))
                if i==26 and isTile((loc[0]+2,loc[1]+2)) and i1!=26:
                    moves.append((loc[0]+2,loc[1]+2))
                i = board.getCoinByPos((loc[0]-2,loc[1]+2))
                i1 = board.getCoinByPos((loc[0]-1,loc[1]+1))
                if i==26 and isTile((loc[0]-2,loc[1]+2)) and i1!=26:
                    moves.append((loc[0]-2,loc[1]+2))
            else:
                i = board.getCoinByPos((loc[0]+2,loc[1]-2))
                i1 = board.getCoinByPos((loc[0]+1,loc[1]-1))
                if i==26 and isTile((loc[0]+2,loc[1]-2)) and i1!=26:
                    moves.append((loc[0]+2,loc[1]-2))
                i = board.getCoinByPos((loc[0]-2,loc[1]-2))
                i1 = board.getCoinByPos((loc[0]-1,loc[1]-1))
                if i==26 and isTile((loc[0]-2,loc[1]-2)) and i1!=26:
                    moves.append((loc[0]-2,loc[1]-2))
        else:
            i = board.getCoinByPos((loc[0]+2,loc[1]-2))
            i1 = board.getCoinByPos((loc[0]+1,loc[1]-1))
            if i==26 and isTile((loc[0]+2,loc[1]-2)) and i1!=26:
                moves.append((loc[0]+2,loc[1]-2))
            i = board.getCoinByPos((loc[0]-2,loc[1]-2))
            i1 = board.getCoinByPos((loc[0]-1,loc[1]-1))
            if i==26 and isTile((loc[0]-2,loc[1]-2)) and i1!=26:
                moves.append((loc[0]-2,loc[1]-2))
            i = board.getCoinByPos((loc[0]+2,loc[1]+2))
            i1 = board.getCoinByPos((loc[0]+1,loc[1]+1))
            if i==26 and isTile((loc[0]+2,loc[1]+2)) and i1!=26:
                moves.append((loc[0]+2,loc[1]+2))
            i = board.getCoinByPos((loc[0]-2,loc[1]+2))
            i1 = board.getCoinByPos((loc[0]-1,loc[1]+1))
            if i==26 and isTile((loc[0]-2,loc[1]+2)) and i1!=26:
                moves.append((loc[0]-2,loc[1]+2))
        return moves
    else:
        if not coin.isKing():
            if coin.getColor() == "red":
                i = board.getCoinByPos((loc[0]+1,loc[1]+1))
                if i==26 and isTile((loc[0]+1,loc[1]+1)):
                    moves.append((loc[0]+1,loc[1]+1))
                i = board.getCoinByPos((loc[0]-1,loc[1]+1))
                if i==26 and isTile((loc[0]-1,loc[1]+1)):
                    moves.append((loc[0]-1,loc[1]+1))
            else:
                i = board.getCoinByPos((loc[0]+1,loc[1]-1))
                if i==26 and isTile((loc[0]+1,loc[1]-1)):
                    moves.append((loc[0]+1,loc[1]-1))
                i = board.getCoinByPos((loc[0]-1,loc[1]-1))
                if i==26 and isTile((loc[0]-1,loc[1]-1)):
                    moves.append((loc[0]-1,loc[1]-1))
        else:
            i = board.getCoinByPos((loc[0]+1,loc[1]-1))
            if i==26 and isTile((loc[0]+1,loc[1]-1)):
                moves.append((loc[0]+1,loc[1]-1))
            i = board.getCoinByPos((loc[0]-1,loc[1]-1))
            if i==26 and isTile((loc[0]-1,loc[1]-1)):
                moves.append((loc[0]-1,loc[1]-1))
            i = board.getCoinByPos((loc[0]+1,loc[1]+1))
            if i==26 and isTile((loc[0]+1,loc[1]+1)):
                moves.append((loc[0]+1,loc[1]+1))
            i = board.getCoinByPos((loc[0]-1,loc[1]+1))
            if i==26 and isTile((loc[0]-1,loc[1]+1)):
                moves.append((loc[0]-1,loc[1]+1))
        return moves

#Function parameters: current board object, location of the coin which we want to check for available multikill moves
#Return value: True/False
#Return datatype: boolean 
def checkMultiKill(board, loc):
    coin = board.coins[board.getCoinByPos(loc)]
    if loc in checkKill(board, coin.getColor()):
        return True
    else:
        return False