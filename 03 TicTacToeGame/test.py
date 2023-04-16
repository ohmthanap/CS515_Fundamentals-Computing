def instructions():
    # this function prints the instructions
    print("""
        Welcome to the greatest intellectual challenge of all time: Tic-Tac-Toe.
        This will be a showdown between your human brain and my silicon processor.

        You will make your move known by entering a number, 0 - 8. The number
        will correspond to the board position as illustrated:

        0 | 1 | 2
        ---------
        3 | 4 | 5
        ---------
        6 | 7 | 8

        Prepare yourself, human. The ultimate battle is about to begin. \n
        """)

# main list / global variable
board = [' '] * 9

def printBoard():
    # this function prints the board before and after every move
    print("******")
    print(" " + board[0] + "| " + board[1] + "| " + board[2])
    print("---------")
    print(" " + board[3] + "| " + board[4] + "| " + board[5])
    print("---------")
    print(" " + board[6] + "| " + board[7] + "| " + board[8])
    print("******")
#printBoard(board)

def insertMove(letter, position):
    # this function insert the letter x or o depending on whose move it is and assigns to the given value in the board
    board[position] = letter

def checkSpace(position):
    # this function checks for remaining spaces in the board
    return board[position] == " "

def win(letter):
    # this function takes in the board and letter and checks for possible win combinations
    # first, all rows. second, all columns. third diagonals
    return ((board[0] == letter and board[1] == letter and board[2] == letter) or (board[3] == letter and board[4] == letter and board[5] == letter) or
            (board[6] == letter and board[7] == letter and board[8] == letter) or
            (board[0] == letter and board[3] == letter and board[6] == letter) or(board[1] == letter and board[4] == letter and board[7] == letter) or
            (board[2] == letter and board[5] == letter and board[8] == letter) or
            (board[0] == letter and board[4] == letter and board[8] == letter) or (board[2] == letter and board[4] == letter and board[6] == letter))

def randomizeMove(list1):
    # this function randomizes input index for the computer move
    import random
    n = len(list1)
    r = random.randrange(0, n)
    return list1[r]

def playerMove():
    # get input, check if empty or not
    # change state of board
    # check win condition
    rem_spaces = [i for i, j in enumerate(board) if j == ' ']

    while True:
        #check for try catch
        n = int(input("Enter you position for move: "))
        if n not in rem_spaces:
            print("enter another move")
        else:
            break

    insertMove('x', n)
    printBoard()
    return win('x')

def compMove():
    # check for ' ' values and add to list
    rem_spaces = [i for i,j in enumerate(board) if j == ' ']
    m = randomizeMove(rem_spaces)
    #insert 'o' at index m
    insertMove('o', m)
    printBoard()
    # check win
    return win('o')

def game():
    # starts the game by turn values if turn even it is human chance, if odd computer's chance
    turn = 0
    while True:
        if turn % 2 == 0:
            a = playerMove()
            turn += 1
            if a:
                print("you win!")
                break

        else:
            b = compMove()
            turn += 1
            if b:
                print("computer wins!")
                break
        # if turn becomes 9 and there is no winner the game is a draw
        if turn == 9:
            print("Draw")
            break

def main():
    # main function to call game
    instructions()
    printBoard()
    game()

main()