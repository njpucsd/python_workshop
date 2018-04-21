# TIC-TAC-TOE

board = []
playerOneTurn = True
winner = False

for x in range(0,9) :
    board.append(" ")

def display_instructions():
    print("""Welcome to Tic-Tac-Toe!
       To play please select a number from 1-9 that corresponds
       to the location where you want to place your move

       1 | 2 | 3
       4 | 5 | 6
       7 | 8 | 9

       """)

def drawBoard(board):
    print('\n -----')
    print('|' + board[0] + '|' + board[1] + '|' + board[2] + '|')
    print( ' -----')
    print('|' + board[3] + '|' + board[4] + '|' + board[5] + '|')
    print( ' -----')
    print('|' + board[6] + '|' + board[7] + '|' + board[8] + '|')
    print( ' -----\n')

#def winner(board):
    
#def validMove(choice):

display_instructions()

while not winner:
    if playerOneTurn:
        print("Player 1:")
    else:
        print("Player 2:")

    choice = int(input())

    if playerOneTurn:
        board[choice-1] = "X"
    else:
        board[choice-1] = "O"

    drawBoard(board)

    playerOneTurn = not playerOneTurn

    
    
