# Tic Tac Toe Grid
theBoard = {'tl': '-', 'tm': '-', 'tr': '-',
            'ml': '-', 'mm': '-', 'mr': '-',
            'll': '-', 'lm': '-', 'lr': '-'}

# wecome message and directions
print('Welcome to Tic Tac Toe!')
print('Object of the game: To win, get three Xs or Os in a row, column, or diagonal.')
print('Game play: 1. Decide who is X and who is O. 2. Take turns typing the row and column codes of your selected spot.')
print('For example, the code for the top-left spot is tl, for the mid-middle spot it is mm, and for the lower-right spot it is lr.')

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

    # determinine and announce winner
    firstLetterCount = 0
    secondLetterCount = 0
    for k in theBoard.keys():
        if (k[0] == move[0]) and (theBoard[k] == turn): 
            firstLetterCount+=1       
        if firstLetterCount == 3: 
            printBoard(theBoard)
            print(turn + ' wins!')
            print(' ')
            exit()
        else:
            continue  

    for k in theBoard.keys():
        if (k[1] == move[1]) and (theBoard[k] == turn):
            secondLetterCount+=1
        if secondLetterCount == 3:
            printBoard(theBoard)
            print(turn + ' wins!')
            print(' ')
            exit()
        else:
            continue
    
    if (theBoard['tl'] == turn) and (theBoard['mm'] == turn) and (theBoard['lr'] == turn):
        printBoard(theBoard)
        print(turn + ' wins!')
        print(' ')
        exit()

    if (theBoard['tr'] == turn) and (theBoard['mm'] == turn) and (theBoard['ll'] == turn): 
        printBoard(theBoard)
        print(turn + ' wins!')
        print(' ')
        exit()

    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
    
printBoard(theBoard)
print('It is a draw!')
print(' ')
