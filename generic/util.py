from termcolor import colored
# import movegen

class coin:
    def __init__(self, x, y, color, alive=True, king=False):
        self.x = x
        self.y = y
        self.color = color
        self.king = king
        self.alive = alive

    def setKing(self):
        self.king = True

    def setPosition(self,loc):
        if loc[0] not in range(1,9) or loc[1] not in range(1,9) or (loc[0]+loc[1])%2 == 1:
            return 1            #invalid position
        self.x = loc[0]
        self.y = loc[1]
        return 0

    def getPosition(self):
        return self.x , self.y
    
    def getColor(self):
        return self.color
    
    def isKing(self):
        return self.king
    
    def killed(self):
        self.alive = False

    def isAlive(self):
        return self.alive


class Board:
    def __init__(self):
        self.coins = []
        self.coins.append(coin(1,7,'dark_grey'))
        self.coins.append(coin(3,7,'dark_grey'))
        self.coins.append(coin(5,7,'dark_grey'))
        self.coins.append(coin(7,7,'dark_grey'))
        self.coins.append(coin(2,8,'dark_grey'))
        self.coins.append(coin(4,8,'dark_grey'))
        self.coins.append(coin(6,8,'dark_grey'))
        self.coins.append(coin(8,8,'dark_grey'))
        self.coins.append(coin(2,6,'dark_grey'))
        self.coins.append(coin(4,6,'dark_grey'))
        self.coins.append(coin(6,6,'dark_grey'))
        self.coins.append(coin(8,6,'dark_grey'))
        self.coins.append(coin(1,1,'red'))
        self.coins.append(coin(3,1,'red'))
        self.coins.append(coin(5,1,'red'))
        self.coins.append(coin(7,1,'red'))
        self.coins.append(coin(2,2,'red'))
        self.coins.append(coin(4,2,'red'))
        self.coins.append(coin(6,2,'red'))
        self.coins.append(coin(8,2,'red'))
        self.coins.append(coin(1,3,'red'))
        self.coins.append(coin(3,3,'red'))
        self.coins.append(coin(5,3,'red'))
        self.coins.append(coin(7,3,'red'))

    def display(self):
        wtile = colored('   ', 'light_grey', 'on_light_grey', attrs=['dark'])
        print("    A  B  C  D  E  F  G  H    ")
        for i in range(1, 9):
            row = " {} ".format(9-i)
            for j in range(1, 9):
                if (i+j)%2 == 0:
                    row += wtile
                else:
                    if (j, 9-i) in self.getAllCoins():
                        c = self.coins[self.getCoinByPos((j, 9-i))]                       
                        if c.isKing():
                            state = ' 0 '
                        else:
                            state = ' o '
                        color = c.getColor()
                        btile = colored(state, color, 'on_dark_grey', attrs=['bold','dark'])
                    else:
                        btile = colored('   ', 'red', 'on_dark_grey', attrs=['bold','dark'])
                    row += btile
            row += " {} ".format(9-i)
            print(row)
        print("    A  B  C  D  E  F  G  H    ")

    def getAllCoins(self):
        positions = []
        for coin in self.coins:
            positions.append(coin.getPosition())
        return positions
    
    def getCoinByPos(self, loc):
        i = 0
        for pos in self.getAllCoins():
            if loc==pos:
                return i
            i = i+1
        return 26
    
    def moveCoin(self, initial, final):
        i = self.getCoinByPos(initial)
        if i == 26:             #invalid initial position
            return 1
        c  = self.coins[i]
        if c.setPosition(final) == 1:       #invalid final position
            return 1
        return 0

    def eliminate(self, loc):
        i = self.getCoinByPos(loc)
        del self.coins[i]

def testing(board):
    board.eliminate((3,7,))
    board.eliminate((5,7,))
    board.eliminate((7,7,))
    board.eliminate((2,8,))
    board.eliminate((4,8,))
    board.eliminate((6,8,))
    board.eliminate((8,8,))
    board.eliminate((2,6,))
    board.eliminate((4,6,))
    board.eliminate((6,6,))
    board.eliminate((8,6,))
    board.eliminate((1,1,))
    board.eliminate((3,1,))
    board.eliminate((5,1,))
    board.eliminate((7,1,))
    board.eliminate((2,2,))
    board.eliminate((4,2,))
    board.eliminate((6,2,))
    board.eliminate((8,2,))
    board.eliminate((1,3,))
    board.eliminate((3,3,))
    board.eliminate((5,3,))


# b = Board()
# testing(b)
# print(movegen.availableCoinMoves(b,(7,3)))