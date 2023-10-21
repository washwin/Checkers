from termcolor import colored
import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
from main import play
from main import two_player_game
from main import bot_game

def optionBar():
    bar = colored('                          OPTIONS(O) QUIT(Q)', 'black', 'on_white')
    print(bar)

def displayOptions(i):
    print("")
    ind = colored(' (1) ', 'dark_grey', 'on_white')
    text = colored(' RESUME GAME        ', 'blue', 'on_cyan')
    print(ind, end="")
    print(text)
    ind = colored(' (2) ', 'dark_grey', 'on_white')
    text = colored(' RESTART GAME       ', 'blue', 'on_cyan')
    print(ind, end="")
    print(text)
    ind = colored(' (3) ', 'dark_grey', 'on_white')
    text = colored(' HOW TO PLAY        ', 'blue', 'on_cyan')
    print(ind, end="")
    print(text)
    ind = colored(' (4) ', 'dark_grey', 'on_white')
    text = colored(' BACK TO MAIN MENU  ', 'blue', 'on_cyan')
    print(ind, end="")
    print(text)
    ind = colored(' (5) ', 'dark_grey', 'on_white')
    text = colored(' QUIT               ', 'blue', 'on_cyan')
    print(ind, end="")
    print(text)

    c = input("CHOOSE INDEX : ")
    print("")
    match c:
        case '1':
            return
        case '2':
            if i == 0:
                two_player_game.game()
            else:
                bot_game.game()
        case '3':
            play.instructions()
            return
        case '4':
            play.play()
        case '5':
            print("THANKS FOR PLAYING CHECKERS!!")
            print("EXITING CHECKERS")
            play.exit_game()
        case _:
            print(colored("CHOOSE FROM GIVEN INDICES", 'white','on_red'))
            displayOptions()
