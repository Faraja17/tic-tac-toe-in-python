# Tic Tac Toe in Python

Descripton: This is a modification and extension of the partial game presented as a practice problem in Chapter 5 of [*Automate the Boring Stuff with Python* by Al Sweigart.](https://automatetheboringstuff.com/2e/chapter5/)

## Table of contents

- [Overview](#overview)
  - [My Code](#my-code)
  - [Links to Live Sites](#links)
- [My process](#my-process)
  - [Built with](#built-with)
  - [What I learned](#what-i-learned)
  - [Continued development](#continued-development)
  - [Useful resources](#useful-resources)
- [Author](#author)
- [Acknowledgments](#acknowledgments)

## Overview

I selected Sweigart's model to begin with because I like his logic and his clean concise code. He guided me through setting up a grid by creating a dictionary, setting up the printed board through a function, and allowing players to enter moves using a for in loop that iterates 9 times, regardless of a winner. 

My job was to write functions to determine and announce the winner and to end the game in the case of a winner. I am also interested in adding a human vs. computer option and eventually [translating this game into JavaScript](https://github.com/Faraja17/tic-tac-toe-in-js) so that I can connect it to HTML and CSS to make it interactive.


### My Code

```python
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

# win announcement and game exit
def winMessage():
    printBoard(theBoard)
    print(turn + ' wins!')
    print(' ')
    exit()
   
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

    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
    
printBoard(theBoard)
print('It is a draw!')
print(' ')    
```

### Links

- Live Site URL: [Play Tic Tac Toe using the Online Python IDE!](https://www.online-python.com/TId0EfS2Wn)
- [Visualize the Tic Tac Toe game on Python Tutor!](https://pythontutor.com/render.html#code=%23%20Tic%20Tac%20Toe%20Grid%0AtheBoard%20%3D%20%7B'tl'%3A%20'-',%20'tm'%3A%20'-',%20'tr'%3A%20'-',%0A%20%20%20%20%20%20%20%20%20%20%20%20'ml'%3A%20'-',%20'mm'%3A%20'-',%20'mr'%3A%20'-',%0A%20%20%20%20%20%20%20%20%20%20%20%20'll'%3A%20'-',%20'lm'%3A%20'-',%20'lr'%3A%20'-'%7D%0A%0A%23%20wecome%20message%20and%20directions%0Aprint%28'Welcome%20to%20Tic%20Tac%20Toe!'%29%0Aprint%28'Object%20of%20the%20game%3A%20To%20win,%20get%20three%20Xs%20or%20Os%20in%20a%20row,%20column,%20or%20diagonal.'%29%0Aprint%28'Game%20play%3A%201.%20Decide%20who%20is%20X%20and%20who%20is%20O.%202.%20Take%20turns%20typing%20the%20row%20and%20column%20codes%20of%20your%20selected%20spot.'%29%0Aprint%28'For%20example,%20the%20code%20for%20the%20top-left%20spot%20is%20tl,%20for%20the%20mid-middle%20spot%20it%20is%20mm,%20and%20for%20the%20lower-right%20spot%20it%20is%20lr.'%29%0A%0A%23%20printed%20board%20option%202%0Adef%20printBoard%28board%29%3A%0A%20%20%20%20print%28'%20'%29%0A%20%20%20%20print%28'~~~~~'%29%0A%20%20%20%20print%28board%5B'tl'%5D%20%2B%20'%20'%20%2B%20board%5B'tm'%5D%20%2B%20'%20'%20%2B%20board%5B'tr'%5D%29%0A%20%20%20%20print%28board%5B'ml'%5D%20%2B%20'%20'%20%2B%20board%5B'mm'%5D%20%2B%20'%20'%20%2B%20board%5B'mr'%5D%29%0A%20%20%20%20print%28board%5B'll'%5D%20%2B%20'%20'%20%2B%20board%5B'lm'%5D%20%2B%20'%20'%20%2B%20board%5B'lr'%5D%29%0A%20%20%20%20print%28'~~~~~'%29%0A%20%20%20%20print%28'%20'%29%0A%0A%23%20win%20announcement%20and%20game%20exit%0Adef%20winMessage%28%29%3A%0A%20%20%20%20printBoard%28theBoard%29%0A%20%20%20%20print%28turn%20%2B%20'%20wins!'%29%0A%20%20%20%20print%28'%20'%29%0A%20%20%20%20exit%28%29%0A%20%20%20%0A%23%20players%20enter%20moves%0Aturn%20%3D%20'X'%0Afor%20i%20in%20range%289%29%3A%0A%20%20%20%20printBoard%28theBoard%29%0A%20%20%20%20print%28turn%20%2B%20',%20it%20is%20your%20turn.%20Select%20a%20spot.'%29%0A%20%20%20%20move%20%3D%20input%28%29%0A%20%20%20%20theBoard%5Bmove%5D%20%3D%20turn%0A%0A%20%20%20%20%23%20determinine%20and%20announce%20winner%0A%20%20%20%20firstLetterCount%20%3D%200%0A%20%20%20%20secondLetterCount%20%3D%200%0A%20%20%20%20for%20k%20in%20theBoard.keys%28%29%3A%0A%20%20%20%20%20%20%20%20if%20%28k%5B0%5D%20%3D%3D%20move%5B0%5D%29%20and%20%28theBoard%5Bk%5D%20%3D%3D%20turn%29%3A%20%0A%20%20%20%20%20%20%20%20%20%20%20%20firstLetterCount%2B%3D1%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20if%20firstLetterCount%20%3D%3D%203%3A%20%0A%20%20%20%20%20%20%20%20%20%20%20%20winMessage%28%29%0A%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20continue%20%20%0A%0A%20%20%20%20for%20k%20in%20theBoard.keys%28%29%3A%0A%20%20%20%20%20%20%20%20if%20%28k%5B1%5D%20%3D%3D%20move%5B1%5D%29%20and%20%28theBoard%5Bk%5D%20%3D%3D%20turn%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20secondLetterCount%2B%3D1%0A%20%20%20%20%20%20%20%20if%20secondLetterCount%20%3D%3D%203%3A%0A%20%20%20%20%20%20%20%20%20%20%20winMessage%28%29%0A%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20continue%0A%20%20%20%20%0A%20%20%20%20if%20%28theBoard%5B'tl'%5D%20%3D%3D%20turn%29%20and%20%28theBoard%5B'mm'%5D%20%3D%3D%20turn%29%20and%20%28theBoard%5B'lr'%5D%20%3D%3D%20turn%29%3A%0A%20%20%20%20%20%20%20%20winMessage%28%29%0A%0A%20%20%20%20if%20%28theBoard%5B'tr'%5D%20%3D%3D%20turn%29%20and%20%28theBoard%5B'mm'%5D%20%3D%3D%20turn%29%20and%20%28theBoard%5B'll'%5D%20%3D%3D%20turn%29%3A%20%0A%20%20%20%20%20%20%20%20winMessage%28%29%0A%0A%20%20%20%20if%20turn%20%3D%3D%20'X'%3A%0A%20%20%20%20%20%20%20%20turn%20%3D%20'O'%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20turn%20%3D%20'X'%0A%20%20%20%20%0AprintBoard%28theBoard%29%0Aprint%28'It%20is%20a%20draw!'%29%0Aprint%28'%20'%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)

## My process

5/11/22 

So far, I have successfully replicated Sweigart's game. I changed the look of the board, removing the lines and instead adding a top and a bottom border using `~~~~~`. I also added a welcome/directions section and modified the prompt text to be more natural and engaging. I condensed the names of the keys to two characters each. I added a print function after 9 rounds: "It is a draw!' The next step for me to complete independently will be to add functions to determine and announce the winner and to end the game in the case of a winner.

5/12/22

Wow, this was a very educational project for me! For the first time, I was able to come up with my own clever logic that works! Here is how it went: In order to determine winners, I knew that I had to figure out a way to analyze the game board for the instance of three in a row or column. This took A LOT of thinking away from the screen. I spent time talking my way through different scenarios and jotting ideas on notepaper. 

A key moment was when I noticed some patterns in the keys that might help. Each row and column had a unique set of first letters. For example, the top row keys all had 't' for their first letter, and the right column keys all had 'r' for their second letter. I had by chance renamed all of the keys to just two letters in order to make input easier. Sweigart had named his keys more elaborately, e.g. top-L, mid-M, which I found to be tedious to input. I did not realize at the time how much my change would help later! 

So, after noticing the pattern, I remembered learning in chapter 5 about being able create list-like values of a dictionary's keys, values, and items. I also remembered learning in JavaScript how to slice characters of a string through their indices. I went back and reread Chapter 5, and I did some searching for how to return the first letter of a string in Python. Then I started thinking of a plan to create a function to make a list of the keys, loop through each to get the first/second letters, then see if there was an instance of Xs or Os, three in a row or a column. On my note paper, I brainstormed the following functions and loops:

```python
def winner(turn, firstLetter):
  for i in range of 3:
    turn == board(value w/first letter)
    
def firstLetter(turn):
  for i in range 3:
    key starts with t and key starts with t's value == turn
    i+=1
```
But I got stuck. I didn't want to write multiple lines of repetitive code to cover each possible first and second letter. As I have been learning lately, the whole point of coding is to make life easier. I also did not want to hard code the first and second letter variables. I wanted my code to have flexibility incase I ever needed to add more rows and columnts. And I wanted my code to be more sophisticated and on par with what I have been learning. So I tried to think of a creative way to determine which specific first/second letter to test for. I wrote out my plan and how to achieve it in words:

```
If turn is the value of 3 keys that start withthe same letter, print turn + ' wins!'
Count how many turns are == to the value of keys beginning with the same letter.
If any count == 3, turn wins, else, keep playing.
```

I read my plan over and broke down the steps part by part. Suddenly, it struck me! I had been confusing `turn` with `move`. `turn` was the X or O that the program would place into the correct key value, but `move` was the key itself, inputted by the player. This was the answer to determining which specific first and second letters to test for! Each time the player entered their move, the program could look at the the letters and find out if any other keys with the same letters had the value of `turn`. Since each row shares a unique first letter, and each column shares a unique second letter, if the program finds three keys in a row with the same first letter AND all three of those keys contain a value of `turn` it means that the player had won. The same is true for the last letter in a column. So that is how I came up with the following loop:

```python
firstLetterCount = 0
secondLetterCount = 0
    for k in theBoard.keys():
        if (k[0] == move[0]) and (theBoard[k] == turn): 
            firstLetterCount+=1       
        if firstLetterCount == 3: 
            winMessage()
        else:
            continue
```
To my sheer delight, my program WORKED! I tried combining the second letter value, but instead I wound up just making a separate for in loop for it. These two loops saved me from having to write six separate hard-coded if statements, one for each column and one for each row. For such a simple game, this wouldn't have been a big deal, but if I were to add more rows, the number of separate hard-coded if statements would also increase. This way, no matter how many rows or columns are added, the same function can be used with the minor adjustment of changing the `if firstLetterCount ===` value. It wasn't so bad only having to hard-code each of the diagonals:

```python
if (theBoard['tl'] == turn) and (theBoard['mm'] == turn) and (theBoard['lr'] == turn):
        winMessage()

if (theBoard['tr'] == turn) and (theBoard['mm'] == turn) and (theBoard['ll'] == turn): 
        winMessage()
```

Finally, I needed to exit both the inner loop and the outer loop so that the game would end in case of a winner. I did a lot of research on the topic, but I still haven't been able to create a workable solution. For now, my son suggested using `exit()`, but he warned me that it is not ideal, especially if I want to add a prompt giving a choice of either playing again or quitting. He said that I should avoid using loops within loops.

### Built with

- Python 3

### What I learned

- the Dictionary Data Structure
- Key, Value, and Item Methods
- Review of String Indexing


### Continued development

My next project is to [translate this game into JavaScript](https://github.com/Faraja17/tic-tac-toe-in-js) and then modify it to manipulate the DOM. I also am considering the following ways to improve my program:

- Randomize the first player.
- Get rid of the loops within loops.
- Ask player if they wish to continue playing or to quit.
- Make the game human vs. computer.
- Address when wrong input is entered.
- Keep track of spots already filled.
- Remove case sensitivity. 

### Useful resources

- [*Automate the Boring Stuff with Python*](https://automatetheboringstuff.com/2e/chapter5/) - by Al Sweigart, Chapter 5

## Author

Faraja Thompson

- [My Personal Website](https://faraja17.github.io/my-website/)
- [My Blog: Teacher to Techie](https://faraja17.github.io/)
- [Faraja Thompson, M.Ed. on LinkedIn](https://www.linkedin.com/in/faraja-thompson-m-ed-70885b8/)

## Acknowledgments

I'd like to acknowledge my son and mentor [DeForestt Thompson](https://github.com/DeForestt).  His steadfast support and encouragement keep me motivated!  Thanks for forcing me to use the command-line, Son <3 <3 <3.
