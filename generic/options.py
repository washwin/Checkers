from termcolor import colored

def optionBar():
    bar = colored('                          OPTIONS(O) QUIT(Q)', 'black', 'on_white')
    print(bar)

def displayOptions():
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
    match c:
        case '1':
            return
        case '2':
            return
        case '3':
            instructions()
            return
        case '4':
            return
        case '5':
            return
            
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


displayOptions()
