# Tic Tac Toe in Python

Descripton: This is a modification and extension of the game presented as practice problem in Chapter 5 of Automate the Boring Stuff with Python by Al Sweigart.

## Table of contents

- [Overview](#overview)
  - [My Code](#my-code)
  - [Links](#links)
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

- Live Site URL coming soon!: [name of site](URL)

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
