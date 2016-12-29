"""
1. Replace Player 2 with AI Player
2. AI player needs to be able to: 
  a. generate a random number between 0-8
  b. test if the space is already taken
  c. if the space is taken, choose a different number
  d. if it's not taken, place it's marker on that number on the board

  Code that stays the same between current player move and computer move:  
  - checks for tie
  - if player won
  pull out these two sections of code and create helper functions so they can be 
  called in both playerMove and aiMove.

  in ticTacToe function: 
  - replace player 2 function playerMove with the new AI function and pass the same arguments. 


"""
 
"""
Tic Tac Toe Game
Name: Ziva Hirsch

This program lets a person play a game of tic tac toe against an AI Player.
It lets the players take turns to input their moves. Player 1 is "X" and the AI Player is "O". 
The two possible outcomes of the game are: (1) one of the players wins by getting 3 spaces 
in a row (horizontally, diagonally, or vertically) (2) a tie game.
"""


""" 
Function: printHeader
Prints game instructions and a visual of the game board. 
"""
import random

def printHeader():
  print "\n"
  print "The game board for Tic Tac Toe looks like this:" 
  print "\n"
  print "| 0 | 1 | 2 |"
  print " ----------- "
  print "| 3 | 4 | 5 |"
  print " ----------- "
  print "| 6 | 7 | 8 |" 
  print "\n"
  print "On the board, player 1 is 'X' and the AI Player is 'O'."
  print "The first player to get 3 in a row wins!"
  print "\n"


"""
Function: drawBoard
Given a board, this function prints the game board
"""
def drawBoard(board):
  print '|',board[0],'|', board[1],'|', board[2],'|'
  print '-------------'
  print '|',board[3],'|', board[4],'|', board[5],'|'
  print '-------------'
  print '|',board[6],'|', board[7],'|', board[8],'|'
  print "\n"


"""
Function: playAgain
Asks the user if they want to play again and starts another game if yes. 
"""
def playAgain():
  userInput = raw_input("Do you want to play again? (y/n): ")
  if userInput == "y": 
    ticTacToe()
  else: 
    print "Thanks for playing!"

"""
Function: checkForTie 
Checks for tie
"""
def checkForTie(board): 
  if " " not in board:
    print "Game is a tie!"
    playAgain()
    return True

"""
Function: checkForWin
Checks for win
"""

def checkForWin(board, playerMark, playerNumber): 
  if(board[0] == playerMark and board[1] == playerMark and board[2] == playerMark) or \
    (board[3] == playerMark and board[4] == playerMark and board[5] == playerMark) or \
    (board[6] == playerMark and board[7] == playerMark and board[8] == playerMark) or \
    (board[0] == playerMark and board[3] == playerMark and board[6] == playerMark) or \
    (board[1] == playerMark and board[4] == playerMark and board[7] == playerMark) or \
    (board[2] == playerMark and board[5] == playerMark and board[8] == playerMark) or \
    (board[0] == playerMark and board[4] == playerMark and board[8] == playerMark) or \
    (board[2] == playerMark and board[4] == playerMark and board[6] == playerMark):
    printHeader()
    drawBoard(board)
    print "Player " + str(playerNumber) + " wins!"
    playAgain() 
    return True

"""
Function: playerMove
Given a board, playerNumber, and playerMark, this function prompts the user to enter
a valid number to mark the board. After the mark is entered, there are three cases:
1. Tells the users that the game is a tie, asks them if they want to play again, and returns True
2. Announces the winner, asks the users if they want to play again, and returns True
3. Neither player has won and there is no tie, so the function returns False 
"""
## TODO: when player 1 choses the middle space (4), half the board gets filled with numbers
def playerMove(board, playerMark):
  move = raw_input("Player 1, Choose a number to make your next move: ")
  move = int(move)

  # Checks if space is empty and places player's mark if free
  while (board[move] != " "):
    print "That space is already taken! Choose another space"
    move = raw_input("Player 1, Choose a number to make your next move: ")
    move = int(move)  
  board[move] = playerMark

  checkForTie(board)
  checkForWin(board, "X", 1)

  # If there is not a tie or a win, the function returns False
  return False 

def aiMove(board, playerNumber, playerMark):

  while True:
    move = random.randint(0,8)
    #if the space is blank: place the AI's turn, otherwise try again
    if board[move] == " ":
      board[move] = playerMark
      break

    checkForTie(board)
    checkForWin(board, "O", 2)
    return True

  return False


"""
Function: ticTacToe
Keeps prompting Player 1 and Player 2 for their moves until either one user wins or there is a tie. 
"""
def ticTacToe(): 
  board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
  gameOver = False
  while True: 
    # Player 1's turn
    printHeader() 
    drawBoard(board)
    gameOver = playerMove(board, "X") 
    if gameOver:
      break

    # Player 2's turn
    printHeader() 
    drawBoard(board)
    gameOver = aiMove(board, 2, "O")
    if gameOver:
      break
    
if __name__ == "__main__":
  ticTacToe()