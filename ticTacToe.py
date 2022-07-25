# Tic Tac Toe Grid
theBoard = {'tl': '-', 'tm': '-', 'tr': '-',
            'ml': '-', 'mm': '-', 'mr': '-',
            'll': '-', 'lm': '-', 'lr': '-'}

# wecome message and directions
print('Welcome to Tic Tac Toe!')
print('Object of the game: To win, get three Xs or Os in a row, column, or diagonal.')
print('Game play: 1. Decide who is X and who is O. 2. Take turns typing the row and column codes of your selected spot.')
print('For example, the code for the top-left spot is tl, for the mid-middle spot it is mm, and for the lower-right spot it is lr.')

# printed board
def printBoard(board):
    print(' ')
    print('~~~~~')
    print(board['tl'] + ' ' + board['tm'] + ' ' + board['tr'])
    print(board['ml'] + ' ' + board['mm'] + ' ' + board['mr'])
    print(board['ll'] + ' ' + board['lm'] + ' ' + board['lr'])
    print('~~~~~')
    print(' ')

   
# players enter moves
def playerTurn():

    turn = 'X'

    for i in range(9):
        printBoard(theBoard)

        print(turn + ', it is your turn. Select a spot.')
        
        move = input()

        if theBoard[move] == '-':
            theBoard[move] = turn
        else:
            print("That space is already taken. Select an empty spot.")
            continue

        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
            
    winMessage()
    drawMessage()

# determinine and announce winner
def winner():

    firstLetterCount = 0
    secondLetterCount = 0
    for k in theBoard.keys():
        if (k[0] == move[0]) and (theBoard[k] == turn): 
            firstLetterCount+=1       
        if firstLetterCount == 3: 
            winMessage()
        else:
            continue  

    for k in theBoard.keys():
        if (k[1] == move[1]) and (theBoard[k] == turn):
            secondLetterCount+=1
        if secondLetterCount == 3:
            winMessage()
        else:
            continue
    
    if (theBoard['tl'] == turn) and (theBoard['mm'] == turn) and (theBoard['lr'] == turn):
        winMessage()

    if (theBoard['tr'] == turn) and (theBoard['mm'] == turn) and (theBoard['ll'] == turn): 
        winMessage()


# win announcement and game exit
def winMessage():
    printBoard(theBoard)
    print(turn + ' wins!')
    print(' ')
    exit()

# draw announcement and game exit
def drawMessage():   
    printBoard(theBoard)
    print('It is a draw!')
    print(' ')
    exit()

playerTurn()