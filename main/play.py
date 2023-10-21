import sys
from termcolor import colored
from main import two_player_game
from main import bot_game

def instructions():
    print("INSTRUCTIONS")
    print("#TAKING A TURN")
    print(" Each player takes their turn by moving a piece. Pieces are always moved diagonally and can be moved in the following ways:")
    print("Diagonally in the forward direction (towards the opponent) to the next dark square.")
    print("If there is one of the opponent's pieces next to a piece and an empty space on the other side, you jump your opponent and remove their piece. You can do multiple jumps if they are lined up in the forward direction. *** note: if you have a jump, you have no choice but to take it.")
    print("KING PIECES")
    print("The last row is called the king row. If you get a piece across the board to the opponent's king row, that piece becomes a king. Another piece is placed onto that piece so it is now two pieces high. King pieces can move in both directions, forward and backward.")
    print("WINNING THE GAME")
    print("You win the game when the opponent has no more pieces or can't move (even if he/she still has pieces). If neither player can move then it is a draw or a tie.")
    print("")

def exit_game():
    sys.exit(0)


def about():
    print("THIS GAME IS CREATED BY ASHWIN WAGHMARE")  
    print("")
    
def play():
    print("")
    print(colored('WELCOME TO CHECKERS!!!       ', 'blue', 'on_cyan'))
    print(colored('                             ', 'blue', 'on_cyan'))
    ind = colored(' (1) ', 'dark_grey', 'on_white')
    text = colored(' HUMAN VS HUMAN         ', 'blue', 'on_cyan')
    print(ind, end="")
    print(text)
    ind = colored(' (2) ', 'dark_grey', 'on_white')
    text = colored(' HUMAN VS BOT           ', 'blue', 'on_cyan')
    print(ind, end="")
    print(text)
    ind = colored(' (3) ', 'dark_grey', 'on_white')
    text = colored(' HOW TO PLAY            ', 'blue', 'on_cyan')
    print(ind, end="")
    print(text)
    ind = colored(' (4) ', 'dark_grey', 'on_white')
    text = colored(' ABOUT                  ', 'blue', 'on_cyan')
    print(ind, end="")
    print(text)
    ind = colored(' (5) ', 'dark_grey', 'on_white')
    text = colored(' QUIT                   ', 'blue', 'on_cyan')
    print(ind, end="")
    print(text)

    c = input("CHOOSE INDEX : ")
    print("")
    match c:
        case '1':
            two_player_game.game()
        case '2':
            bot_game.game()
        case '3':
            instructions()
            play()
        case '4':
            about()
            play()
        case '5':
            print("THANKS FOR PLAYING CHECKERS!!")
            print("EXITING CHECKERS")
            exit_game()
        case _:
            print(colored("CHOOSE FROM GIVEN INDICES",'white', 'on_red'))
            play()
   