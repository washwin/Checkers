from termcolor import colored
import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
from generic import util
from generic import movegen
from generic import options
from bot import beginner_bot
from bot import moderate_bot
from bot import expert_bot
import two_player_game
from main import play

def gameOver(board):
    human = True
    bot = True
    for coin in board.coins:
        if coin.getColor() == "red":
            human = False
        else:
            bot = False
    if human:
        board.display()
        print("GAME OVER")
        print("I WIN!!!")
        return True
    if bot:
        board.display()
        print("GAME OVER")
        print("YOU WIN!!!")
        return True
    return False

def human(board):
    initialflag = True
    finalflag = True
    while initialflag:
        initial = input("CHOOSE COIN: ")
        if initial.capitalize() == 'Q':
            print("THANKS FOR PLAYING CHECKERS!")
            print("EXITING CHECKERS")
            exit()
        if initial.capitalize() == 'O':
            options.displayOptions(1)
            options.optionBar()
            board.display()
            continue
        if len(initial) != 2:
            print("INVALID INPUT")
            continue
        ip = two_player_game.convert(initial)
        mc = movegen.coinsToMove(board,"red")
        if ip not in mc:
            print("INVALID COIN, CHOOSE FROM THE FOLLOWING")
            for m in mc:
                print(two_player_game.convertback(m),end=" ")
            print("")
        else:
            initialflag = False       
    while finalflag:
        final = input("PLACE COIN TO: ")
        if final.capitalize() == 'Q':
            print("THANKS FOR PLAYING CHECKERS!")
            print("EXITING CHECKERS")
            exit()
        if final.capitalize() == 'O':
            options.displayOptions(1)
            options.optionBar()
            board.display()
            continue
        if len(final) != 2:
            print("INVALID INPUT")
            continue
        fp = two_player_game.convert(final)
        mc = movegen.availableCoinMoves(board,ip)
        if fp not in mc:
            print("INVALID MOVE, CHOOSE FROM THE FOLLOWING")
            for m in mc:
                print(two_player_game.convertback(m),end=" ")
            print("")
        else:
            finalflag = False
    board.moveCoin(ip,fp) 
    if fp[1] == ip[1] + 2 or fp[1] == ip[1] - 2:
        board.eliminate((int((ip[0]+fp[0])/2), int((ip[1]+fp[1])/2)))
    if fp[1] == 8:
        board.coins[board.getCoinByPos(fp)].setKing()


def game():
    print(colored(' CHOOSE DIFFICULTY        ', 'blue', 'on_cyan'))
    ind = colored(' (1) ', 'dark_grey', 'on_white')
    text = colored(' BEGINNER                ', 'blue', 'on_cyan')
    print(ind, end="")
    print(text)
    ind = colored(' (2) ', 'dark_grey', 'on_white')
    text = colored(' MODERATE                ', 'blue', 'on_cyan')
    print(ind, end="")
    print(text)
    ind = colored(' (1) ', 'dark_grey', 'on_white')
    text = colored(' EXPERT                  ', 'blue', 'on_cyan')
    print(ind, end="")
    print(text)
    c = input("CHOOSE INDEX : ")
    print("")
    match c:
        case '1':
            bot = beginner_bot
        case '2':
            bot = moderate_bot
        case '3':
            bot = expert_bot
        case _:
            print(colored("CHOOSE FROM GIVEN INDICES", 'white','on_red'))
            print("")
            game()

    board = util.Board()
    turn = 0
    while not gameOver(board):
        options.optionBar()
        board.display()
        if turn%2 == 0:
            print("YOUR TURN (RED)")
            human(board)
        else:
            print("MY TURN (BLACK)")
            coin, move = bot.bot(board)
            board.moveCoin(coin,move)
            if move[1] == coin[1] - 2 or move[1] == coin[1] + 2:
                board.eliminate((int((coin[0]+move[0])/2), int((coin[1]+move[1])/2)))
            if move[1] == 1:
                board.coins[board.getCoinByPos(move)].setKing()
        turn = turn + 1
        print("")
        print("")
        print("")
    print("RETURNING TO MAIN MENU")
    play.play()