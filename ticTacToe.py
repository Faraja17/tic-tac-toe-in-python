
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

turn = 'X'


# players enter moves
def playerTurn(move, turn):

    i = 0

    while i < 9:
        printBoard(theBoard)
        print(i)
        print(turn + ', it is your turn. Select a spot.')
        move = input()

        # j = 0

        # while True: 
        #     try:
        #         for j in range(9):
        #             if move == keys[j]:
        #                 break
        #             else:    
        #                 j += 1
        #     except KeyError:
        #         print("Invalid move. Try again.")
        #         continue
        #     else:
        #         break  
        

        if theBoard[move] == '-':
            theBoard[move] = turn
            i += 1
        
        else:
            print("That space is already taken. Select an empty spot.")
            continue
             

    #     if turn == 'X':
    #         turn = 'O'
    #     else:
    #         turn = 'X'
            
    # drawMessage()

    # determinine and announce winner

        firstLetterCount = 0
        secondLetterCount = 0
        for k in theBoard.keys():
            if (k[0] == move[0]) and (theBoard[k] == turn): 
                print(k[0], move[0], theBoard[k], turn)
                firstLetterCount+=1       
            if firstLetterCount == 3: 
                winMessage(turn)
            else:
                continue  

        for k in theBoard.keys():
            if (k[1] == move[1]) and (theBoard[k] == turn):
                print(k[1], move[1], theBoard[k], turn)
                secondLetterCount+=1
            if secondLetterCount == 3:
                winMessage(turn)
            else:
                continue
        
        if (theBoard['tl'] == turn) and (theBoard['mm'] == turn) and (theBoard['lr'] == turn):
            winMessage(turn)

        if (theBoard['tr'] == turn) and (theBoard['mm'] == turn) and (theBoard['ll'] == turn): 
            winMessage(turn)

        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
        
        playerTurn("move", turn) # takes back into game play if there is no winner.
            
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
    

playerTurn("move", turn) #starts the game