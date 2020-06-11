# Python_Games

To play a game, type
```
python games.py --game <game-to-play>
``` 
where `<game-to-play>` can be replaced with one of the following: `guess_num`, `rps`, `cows_n_bulls`, `ttt`, or `hangman`.
To exit any of the games, type `exit` in the input.

Below are the types of games and their instructions.

## Guess the Number

### Instructions
You try to guess a number that the computer has generated. First, choose a difficulty. Easy will be a number between 1-9, medium will be a number between 1-50, and hard will be a number between 1-100. When you guess a number, the computer will tell you if your guess is too high or too low. The computer will track your lowest number of guesses for each difficulty.

## Rock Paper Scissors

### Instructions
The computer has chosen either rock, paper, or scissors. You type rock, paper, or scissors and either win, lose, or tie with the computer. The computer will keep track of the score for each session. (You can also type r, p, s in place of the words)

## Cows and Bulls

### Instructions
You try to guess a four digit number that the computer has created. If you guessed a digit in the right placeholder, the computer will print bull (Ex: the number is 1234, you guessed 1677. Computer will print 1 bull). If you guessed a digit correctly but in the wrong placeholder, the computer will print cow (Ex: the number is 1234. you guessed 3467. Computer will print 2 cows (for 3 and 4)). 
If you choose easy mode, the number will have no repeated digits. 
If you choose hard mode, the number might have two of the same digit. If there is a repeated number in the answer and you guess the number once, there will only be one cow (or bull) (Ex. Answer is 7111, you guess 1246. There will only be one cow).  You only have 10 attempts to guess the number before you lose.                      

## Tic Tac Toe

### Instructions
A two player game. When the computer prompts you for your move, you type a coordinate based on the board (1,1 is top left corner, 2,2 is the middle square, 3,3 is the bottom right corner). The computer will place your symbol (Player 1 is X, Player 2 is O) on the board and show it. Your score will be kept track of for each session.

## Hangman 

### Instructions
The computer will choose a word that you have guess. You can choose a difficulty (easy, medium, hard) which affects the number of wrong guesses you can have. 