
# Tic Tac Toe Grid
theBoard = {'tl': '-', 'tm': '-', 'tr': '-',
            'ml': '-', 'mm': '-', 'mr': '-',
            'll': '-', 'lm': '-', 'lr': '-'}

keys = ['tl', 'tm', 'tr', 'ml', 'mm', 'mr', 'll', 'lm', 'lr']

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

turn = 'X'


# players enter moves
def playerTurn(move, turn, theBoard):

    i = 0

    while i < 9: #changed this from for to while loop. this prevents counter from counting invalid moves
        printBoard(theBoard)
        print(i)
        print(turn + ', it is your turn. Select a spot.')
        move = input()

        if move in keys and theBoard[move] == '-':
            theBoard[move] = turn
            i += 1
            
        else:
            print("Invalid move. Try again.")
            continue #this skips everthing below and goes back up to the beginning of the loop. player turn remains the same.

    # determinine and announce winner

        firstLetterCount = 0
        secondLetterCount = 0
        
        #This checks for row wins:
        for k in theBoard.keys():
            if (k[0] == move[0]) and (theBoard[k] == turn): #k[0] is the first letter of the key. move[0] is the first letter of the player's selection theBoard[k] is the key value. turn is the X or O.
                print("same in row:")
                print(k[0], move[0], theBoard[k], turn)
                firstLetterCount+=1       
            if firstLetterCount == 3: #There is only one instance when the first letters of three spots are the same. That is in either row t, m, or l.
                winMessage(turn)
            else:
                continue  
        
        #This checks for column wins:
        for k in theBoard.keys():
            if (k[1] == move[1]) and (theBoard[k] == turn):#k[1] is the second letter of the key. move[1] is the second letter of the player's selection theBoard[k] is the key value. turn is the X or O,
                print("same in column:")
                print(k[1], move[1], theBoard[k], turn)
                secondLetterCount+=1
            if secondLetterCount == 3: #There is only one instance when the second letters of three spots are the same. That is in either column l, m, or r.
                winMessage(turn)
            else:
                continue
        
        #These check for diagonal wins:
        if (theBoard['tl'] == turn) and (theBoard['mm'] == turn) and (theBoard['lr'] == turn):
            winMessage(turn)

        if (theBoard['tr'] == turn) and (theBoard['mm'] == turn) and (theBoard['ll'] == turn): 
            winMessage(turn)

        #This swaps the player after each turn:
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
        
        # Restarts game play if there is no winner.
            
    drawMessage()

# win announcement and game exit
def winMessage(turn):
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


playerTurn("move", turn, theBoard) #starts the game
