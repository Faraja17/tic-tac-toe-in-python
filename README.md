# Tic Tac Toe in Python

Descripton: This is a modification and extension of the game presented as practice problem in Chapter 5 of Automate the Boring Stuff with Python by Al Sweigart.

## Table of contents

- [Overview](#overview)
  - [My Code](#my-code)
  - [Link(s) to Live Site](#links)
- [My process](#my-process)
  - [Built with](#built-with)
  - [What I learned](#what-i-learned)
  - [Continued development](#continued-development)
  - [Useful resources](#useful-resources)
- [Author](#author)
- [Acknowledgments](#acknowledgments)

## Overview

I selected Sweigart's model to begin with because I like his logic and his clean concise code. He guided me through setting up a grid by creating a library, setting up the printed board through a function, and allowing players to enter moves using a for in loop that iterates 9 times, regardless of a winner. My job is to write functions to determine and announce the winner and to end the game in the case of a winner. I am also interested in adding a human vs. computer option and eventually translating this game into JavaScript so that I can connect it to HTML and CSS to make it interactive.


### My Code

```python
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
    
```

### Links

- Live Site URL: [Visualize the Tic Tac Toe game on Python Tutor!](https://pythontutor.com/render.html#code=%23%20Tic%20Tac%20Toe%20Grid%0AtheBoard%20%3D%20%7B'tl'%3A%20'-',%20'tm'%3A%20'-',%20'tr'%3A%20'-',%0A%20%20%20%20%20%20%20%20%20%20%20%20'ml'%3A%20'-',%20'mm'%3A%20'-',%20'mr'%3A%20'-',%0A%20%20%20%20%20%20%20%20%20%20%20%20'll'%3A%20'-',%20'lm'%3A%20'-',%20'lr'%3A%20'-'%7D%0A%0A%23%20wecome%20message%20and%20directions%0Aprint%28'Welcome%20to%20Tic%20Tac%20Toe!'%29%0Aprint%28'Object%20of%20the%20game%3A%20To%20win,%20get%20three%20Xs%20or%20Os%20in%20a%20row,%20column,%20or%20diagonal.'%29%0Aprint%28'Game%20play%3A%201.%20Decide%20who%20is%20X%20and%20who%20is%20O.%202.%20Take%20turns%20typing%20the%20row%20and%20column%20codes%20of%20your%20selected%20spot.'%29%0Aprint%28'For%20example,%20the%20code%20for%20the%20top-left%20spot%20is%20tl,%20for%20the%20mid-middle%20spot%20it%20is%20mm,%20and%20for%20the%20lower-right%20spot%20it%20is%20lr.'%29%0A%0A%23%20printed%20board%20option%202%0Adef%20printBoard%28board%29%3A%0A%20%20%20%20print%28'%20'%29%0A%20%20%20%20print%28'~~~~~'%29%0A%20%20%20%20print%28board%5B'tl'%5D%20%2B%20'%20'%20%2B%20board%5B'tm'%5D%20%2B%20'%20'%20%2B%20board%5B'tr'%5D%29%0A%20%20%20%20print%28board%5B'ml'%5D%20%2B%20'%20'%20%2B%20board%5B'mm'%5D%20%2B%20'%20'%20%2B%20board%5B'mr'%5D%29%0A%20%20%20%20print%28board%5B'll'%5D%20%2B%20'%20'%20%2B%20board%5B'lm'%5D%20%2B%20'%20'%20%2B%20board%5B'lr'%5D%29%0A%20%20%20%20print%28'~~~~~'%29%0A%20%20%20%20print%28'%20'%29%0A%20%20%20%0A%23%20players%20enter%20moves%0Aturn%20%3D%20'X'%0Afor%20i%20in%20range%289%29%3A%0A%20%20%20%20printBoard%28theBoard%29%0A%20%20%20%20print%28turn%20%2B%20',%20it%20is%20your%20turn.%20Select%20a%20spot.'%29%0A%20%20%20%20move%20%3D%20input%28%29%0A%20%20%20%20theBoard%5Bmove%5D%20%3D%20turn%0A%0A%20%20%20%20%23%20determinine%20and%20announce%20winner%0A%20%20%20%20firstLetterCount%20%3D%200%0A%20%20%20%20secondLetterCount%20%3D%200%0A%20%20%20%20for%20k%20in%20theBoard.keys%28%29%3A%0A%20%20%20%20%20%20%20%20if%20%28k%5B0%5D%20%3D%3D%20move%5B0%5D%20and%20theBoard%5Bk%5D%20%3D%3D%20turn%29%3A%20%0A%20%20%20%20%20%20%20%20%20%20%20%20firstLetterCount%2B%3D1%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20if%20firstLetterCount%20%3D%3D%203%3A%20%0A%20%20%20%20%20%20%20%20%20%20%20%20printBoard%28theBoard%29%0A%20%20%20%20%20%20%20%20%20%20%20%20print%28turn%20%2B%20'%20wins!'%29%0A%20%20%20%20%20%20%20%20%20%20%20%20print%28'%20'%29%0A%20%20%20%20%20%20%20%20%20%20%20%20exit%28%29%0A%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20continue%20%20%0A%0A%20%20%20%20for%20k%20in%20theBoard.keys%28%29%3A%0A%20%20%20%20%20%20%20%20if%20%28k%5B1%5D%20%3D%3D%20move%5B1%5D%20and%20theBoard%5Bk%5D%20%3D%3D%20turn%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20secondLetterCount%2B%3D1%0A%20%20%20%20%20%20%20%20if%20secondLetterCount%20%3D%3D%203%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20printBoard%28theBoard%29%0A%20%20%20%20%20%20%20%20%20%20%20%20print%28turn%20%2B%20'%20wins!'%29%0A%20%20%20%20%20%20%20%20%20%20%20%20print%28'%20'%29%0A%20%20%20%20%20%20%20%20%20%20%20%20exit%28%29%0A%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20continue%0A%20%20%20%20%0A%20%20%20%20if%20%28theBoard%5B'tl'%5D%20%3D%3D%20turn%29%20and%20%28theBoard%5B'mm'%5D%20%3D%3D%20turn%29%20and%20%28theBoard%5B'lr'%5D%20%3D%3D%20turn%29%3A%0A%20%20%20%20%20%20%20%20printBoard%28theBoard%29%0A%20%20%20%20%20%20%20%20print%28turn%20%2B%20'%20wins!'%29%0A%20%20%20%20%20%20%20%20print%28'%20'%29%0A%20%20%20%20%20%20%20%20exit%28%29%0A%0A%20%20%20%20if%20%28theBoard%5B'tr'%5D%20%3D%3D%20turn%29%20and%20%28theBoard%5B'mm'%5D%20%3D%3D%20turn%29%20and%20%28theBoard%5B'll'%5D%20%3D%3D%20turn%29%3A%20%0A%20%20%20%20%20%20%20%20printBoard%28theBoard%29%0A%20%20%20%20%20%20%20%20print%28turn%20%2B%20'%20wins!'%29%0A%20%20%20%20%20%20%20%20print%28'%20'%29%0A%20%20%20%20%20%20%20%20exit%28%29%0A%0A%20%20%20%20if%20turn%20%3D%3D%20'X'%3A%0A%20%20%20%20%20%20%20%20turn%20%3D%20'O'%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20turn%20%3D%20'X'%0A%20%20%20%20%0AprintBoard%28theBoard%29%0Aprint%28'It%20is%20a%20draw!'%29%0Aprint%28'%20'%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)
## My process

5/11/22 - So far, I have successfully replicated Sweigart's game. I changed the look of the board, removing the lines and instead adding a top and a bottom border using `~~~~~`. I also added a welcome/directions section and modified the prompt text to be more natural and engaging. I added a print after 9 rounds: "It is a draw!' The next step for me to complete independently will be to add functions to determine and announce the winner and to end the game in the case of a winner.

### Built with

- Python 3

### What I learned



### Continued development



### Useful resources

- [*Automate the Boring Stuff with Python*](https://automatetheboringstuff.com/2e/chapter5/) - by Al Sweigart, Chapter 5

## Author

Faraja Thompson

- [My Personal Website](https://faraja17.github.io/my-website/)
- [My Blog: Teacher to Techie](https://faraja17.github.io/)
- [Faraja Thompson, M.Ed. on LinkedIn](https://www.linkedin.com/in/faraja-thompson-m-ed-70885b8/)

## Acknowledgments

I'd like to acknowledge my son and mentor [DeForestt Thompson](https://github.com/DeForestt).  His steadfast support and encouragement keep me motivated!  Thanks for forcing me to use the command-line, Son <3 <3 <3.
