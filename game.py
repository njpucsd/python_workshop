# TIC-TAC-TOE

board = []
playerOneTurn = True

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

if playerOneTurn:
    print("Player 1:")
else:
    print("Player 2:")

choice = int(input())

board[choice-1] = "X"
