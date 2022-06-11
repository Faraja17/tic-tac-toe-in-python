# Tic Tac Toe Grid
theBoard = {'tl': '-', 'tm': '-', 'tr': '-',
            'ml': '-', 'mm': '-', 'mr': '-',
            'll': '-', 'lm': '-', 'lr': '-'}

# tester
# theBoard = {'tl': 'O', 'tm': 'O', 'tr': 'O',
#             'ml': 'X', 'mm': 'X', 'mr': '-',
#             'll': '-', 'lm': '-', 'lr': 'X'}

# wecome message and directions
print('Welcome to Tic Tac Toe!')
print('Object of the game: To win, get three Xs or Os in a row, column, or diagonal.')
print('Game play: 1. Decide who is X and who is O. 2. Take turns typing the row and column codes of your selected spot.')
print('For example, the code for the top-left spot is tl, for the mid-middle spot it is mm, and for the lower-right spot it is lr.')

# printed board option 1
# def printBoard(board):
#     print(board['tl'] + '|' + board['tm'] + '|' + board['tr'])
#     print('-+-+-')
#     print(board['ml'] + '|' + board['mm'] + '|' + board['mr'])
#     print('-+-+-')
#     print(board['ll'] + '|' + board['lm'] + '|' + board['lr'])
# printBoard(theBoard)

# printed board option 2
def printBoard(board):
    print(' ')
    print('~~~~~')
    print(board['tl'] + ' ' + board['tm'] + ' ' + board['tr'])
    print(board['ml'] + ' ' + board['mm'] + ' ' + board['mr'])
    print(board['ll'] + ' ' + board['lm'] + ' ' + board['lr'])
    print('~~~~~')
    print(' ')
   
# players enter moves
turn = 'X'
for i in range(9):
    printBoard(theBoard)
    print(turn + ', it is your turn. Select a spot.')
    move = input()
    theBoard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
print('It is a draw!')

printBoard(theBoard)
    