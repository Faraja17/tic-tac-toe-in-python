
# Tic Tac Toe Grid
theBoard = {'tl': '-', 'tm': '-', 'tr': '-',
            'ml': '-', 'mm': '-', 'mr': '-',
            'll': '-', 'lm': '-', 'lr': '-'}

keys = ['tl', 'tm', 'tr', 'ml', 'mm', 'mr', 'll', 'lm', 'lr']

# wecome message and directions
print(' ')
print('WELCOME TO TIC TAC TOE!')
print(' ')
print('OBJECT OF THE GAME: To win, get three Xs or Os in a row, column, or diagonal.')
print(' ')
print('GAME PLAY: First, decide who is X and who is O. Then, take turns typing the row and column code of your selected spot.')
print(' ')
print('FOR EXAMPLE: The code for the top-left spot is tl, for the mid-middle spot it is mm, and for the lower-right spot it is lr.')

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
        print(turn + ", it's your turn. Select a spot.")
        move = input()

        if move in keys and theBoard[move] == '-':
            theBoard[move] = turn
            i += 1
            
        else:
            print(" \nInvalid move. Try again, " + turn + ".")
            continue #this skips everthing below and goes back up to the beginning of the loop. player turn remains the same.

    # determinine and announce winner

        firstLetterCount = 0
        secondLetterCount = 0
        
        #This checks for row wins:
        for k in theBoard.keys():
            if (k[0] == move[0]) and (theBoard[k] == turn): #k[0] is the first letter of the key. move[0] is the first letter of the player's selection theBoard[k] is the key value. turn is the X or O.
                firstLetterCount+=1       
            if firstLetterCount == 3: #There is only one instance when the first letters of three spots are the same. That is in either row t, m, or l.
                winMessage(turn)
            else:
                continue  
        
        #This checks for column wins:
        for k in theBoard.keys():
            if (k[1] == move[1]) and (theBoard[k] == turn):#k[1] is the second letter of the key. move[1] is the second letter of the player's selection theBoard[k] is the key value. turn is the X or O.
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
    playAgain()

# draw announcement and game exit
def drawMessage():   
    printBoard(theBoard)
    print("It's a draw!")
    print(' ')
    playAgain()

#play again choice
def playAgain():
    choice = input('Play again? y or n \n')
    if choice == 'y':
        for key in theBoard:
            theBoard[key] = '-' # this resets the gameboard.
        playerTurn("move", turn, theBoard) #this restarts the game
    else:
        print(" \nThank you for playing!\n ")
        exit()

playerTurn("move", turn, theBoard) #starts the game
