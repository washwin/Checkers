import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
from generic import util
from generic import movegen
from generic import options
        
def convert(point):
    op = []
    match point[0].capitalize():
        case 'A':
            op.append(1)
        case 'B':
            op.append(2)
        case 'C':
            op.append(3)
        case 'D':
            op.append(4)
        case 'E':
            op.append(5)
        case 'F':
            op.append(6)
        case 'G':
            op.append(7)
        case 'H':
            op.append(8)
        case _:
            print("error")
    match point[1]:
        case '1':
            op.append(1)
        case '2':
            op.append(2)
        case '3':
            op.append(3)
        case '4':
            op.append(4)
        case '5':
            op.append(5)
        case '6':
            op.append(6)
        case '7':
            op.append(7)
        case '8':
            op.append(8)
        case _:
            print("error")
    op = tuple(op)
    return op
            
def convertback(point):
    op = ""
    match point[0]:
        case 1:
            op = "A"
        case 2:
            op = "B"
        case 3:
            op = "C"
        case 4:
            op = "D"
        case 5:
            op = "E"
        case 6:
            op = "F"
        case 7:
            op = "G"
        case 8:
            op = "H"
        case _:
            print("ERROR")
    match point[1]:
        case 1:
            op += "1"
        case 2:
            op += "2"
        case 3:
            op += "3"
        case 4:
            op += "4"
        case 5:
            op += "5"
        case 6:
            op += "6"
        case 7:
            op += "7"
        case 8:
            op += "8"
        case _:
            print("ERROR")   
    return op

def gameOver(board):
    player1 = True
    player2 = True
    for coin in board.coins:
        if coin.getColor() == "red":
            player1 = False
        else:
            player2 = False
    if player1:
        print("GAME OVER")
        print("PLAYER 2 WINS!!!")
        return True
    if player2:
        print("GAME OVER")
        print("PLAYER 1 WINS!!!")
        return True
    return False

def testing(board):
    board.eliminate((1,7))
    board.eliminate((3,7))
    board.eliminate((5,7))
    board.eliminate((7,7))
    board.eliminate((2,8))
    board.eliminate((4,8))
    board.eliminate((6,8))
    board.eliminate((8,8))
    board.eliminate((2,6))
    # board.eliminate((4,6))
    board.eliminate((6,6))
    board.eliminate((8,6))
    board.eliminate((1,1))
    board.eliminate((3,1))
    board.eliminate((5,1))
    board.eliminate((7,1))
    board.eliminate((2,2))
    board.eliminate((4,2))
    board.eliminate((6,2))
    board.eliminate((8,2))
    board.eliminate((1,3))
    board.eliminate((3,3))
    # board.eliminate((5,3))
    board.eliminate((7,3))

def game():
    board = util.Board()
    # testing(board)
    turn = 0
    while not gameOver(board):
        options.optionBar()
        board.display()
        if turn%2 == 0:
            print("PLAYER 1's TURN")
            color = "red"
        else:
            print("PLAYER 2's TURN")
            color = "black"
        initialflag = True
        finalflag = True
        while initialflag:
            initial = input("CHOOSE COIN: ")
            if initial.capitalize() == 'Q':
                print("THANKS FOR PLAYING CHECKERS!")
                print("EXITING CHECKERS")
                exit()
            if initial.capitalize() == 'O':
                options.displayOptions()
                continue
            if len(initial) != 2:
                print("INVALID INPUT")
                continue
            ip = convert(initial)
            mc = movegen.coinsToMove(board,color)
            if ip not in mc:
                print("INVALID COIN, CHOOSE FROM THE FOLLOWING")
                for m in mc:
                    print(convertback(m),end=" ")
                print("")
            else:
                initialflag = False       
        while finalflag:
            final = input("PLACE COIN TO: ")
            if len(final) != 2:
                print("INVALID INPUT")
                continue
            fp = convert(final)
            mc = movegen.availableCoinMoves(board,ip)
            if fp not in mc:
                print("INVALID MOVE, CHOOSE FROM THE FOLLOWING")
                for m in mc:
                    print(convertback(m),end=" ")
                print("")
            else:
                finalflag = False
        board.moveCoin(ip,fp)
        
        if color == "red":
            if fp[1] == ip[1] + 2 or fp[1] == ip[1] - 2:
                board.eliminate((int((ip[0]+fp[0])/2), int((ip[1]+fp[1])/2)))
            if fp[1] == 8:
                board.coins[board.getCoinByPos(fp)].setKing()
        else:
            if fp[1] == ip[1] - 2 or fp[1] == ip[1] + 2:
                board.eliminate((int((ip[0]+fp[0])/2), int((ip[1]+fp[1])/2)))
            if fp[1] == 1:
                board.coins[board.getCoinByPos(fp)].setKing()
        print("")
        print("")
        print("")
        turn = turn + 1


game()