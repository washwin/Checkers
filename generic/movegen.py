def checkKill(board,color):
    killcoins = []
    if color == 'red':
        for coin in board.coins:
            if coin.getColor() == color:
                loc = coin.getPosition()
                if not coin.isKing():
                    i = board.getCoinByPos((loc[0]+1,loc[1]+1))
                    if i != 26:
                        if board.coins[i].getColor() != color:
                            if (loc[0]+2,loc[1]+2) not in board.getAllCoins():
                                killcoins.append(loc)
                    i = board.getCoinByPos((loc[0]-1,loc[1]+1))
                    if i != 26:
                        if board.coins[i].getColor() != color:
                            if (loc[0]-2,loc[1]+2) not in board.getAllCoins():
                                killcoins.append(loc)
                else:
                    i = board.getCoinByPos((loc[0]+1,loc[1]+1))
                    if i != 26:
                        if board.coins[i].getColor() != color:
                            if (loc[0]+2,loc[1]+2) not in board.getAllCoins():
                                killcoins.append(loc)
                    i = board.getCoinByPos((loc[0]-1,loc[1]+1))
                    if i != 26:
                        if board.coins[i].getColor() != color:
                            if (loc[0]-2,loc[1]+2) not in board.getAllCoins():
                                killcoins.append(loc)
                    i = board.getCoinByPos((loc[0]+1,loc[1]-1))
                    if i != 26:
                        if board.coins[i].getColor() != color:
                            if (loc[0]+2,loc[1]-2) not in board.getAllCoins():
                                killcoins.append(loc)
                    i = board.getCoinByPos((loc[0]-1,loc[1]-1))
                    if i != 26:
                        if board.coins[i].getColor() != color:
                            if (loc[0]-2,loc[1]-2) not in board.getAllCoins():
                                killcoins.append(loc)
    else:
        for coin in board.coins:
            if coin.getColor() == color:
                loc = coin.getPosition()
                if not coin.isKing():
                    i = board.getCoinByPos((loc[0]+1,loc[1]-1))
                    if i != 26:
                        if board.coins[i].getColor() != color:
                            if (loc[0]+2,loc[1]-2) not in board.getAllCoins():
                                killcoins.append(loc)
                    i = board.getCoinByPos((loc[0]-1,loc[1]-1))
                    if i != 26:
                        if board.coins[i].getColor() != color:
                            if (loc[0]-2,loc[1]-2) not in board.getAllCoins():
                                killcoins.append(loc)
                else:
                    i = board.getCoinByPos((loc[0]+1,loc[1]+1))
                    if i != 26:
                        if board.coins[i].getColor() != color:
                            if (loc[0]+2,loc[1]+2) not in board.getAllCoins():
                                killcoins.append(loc)
                    i = board.getCoinByPos((loc[0]-1,loc[1]+1))
                    if i != 26:
                        if board.coins[i].getColor() != color:
                            if (loc[0]-2,loc[1]+2) not in board.getAllCoins():
                                killcoins.append(loc)
                    i = board.getCoinByPos((loc[0]+1,loc[1]-1))
                    if i != 26:
                        if board.coins[i].getColor() != color:
                            if (loc[0]+2,loc[1]-2) not in board.getAllCoins():
                                killcoins.append(loc)
                    i = board.getCoinByPos((loc[0]-1,loc[1]-1))
                    if i != 26:
                        if board.coins[i].getColor() != color:
                            if (loc[0]-2,loc[1]-2) not in board.getAllCoins():
                                killcoins.append(loc)
    t = set(killcoins)
    killcoins = (list(t))
    return killcoins

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

def isTile(loc):
    if loc[0] not in range(1,9) or loc[1] not in range(1,9):
        return False
    return True

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