"""
Tic Tac Toe Game
Name: Ziva Hirsch

This program lets two people play a game of tic tac toe.
It lets the players take turns to input their moves. Player 1 is "X" and Player 2 is "O". 
The two possible outcomes of the game are: (1) one of the players wins by getting 3 spaces 
in a row (horizontally, diagonally, or vertically) (2) a tie game.
"""


""" 
Function: printHeader
Prints game instructions and a visual of the game board. 
"""
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
  print "On the board, player 1 is 'X' and player 2 is 'O'."
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
Function: playerMove
Given a board, playerNumber, and playerMark, this function prompts the user to enter
a valid number to mark the board. After the mark is entered, there are three cases:
1. Tells the users that the game is a tie, asks them if they want to play again, and returns True
2. Announces the winner, asks the users if they want to play again, and returns True
3. Neither player has won and there is no tie, so the function returns False 
"""
def playerMove(board, playerNumber, playerMark):
  move = raw_input("Player " + str(playerNumber) + ", Choose a number to make your next move: ")
  move = int(move)

  # Checks if space is empty and places player's mark if free
  while (board[move] != " "):
    print "That space is already taken! Choose another space"
    move = raw_input("Player " + str(playerNumber) + ", Choose a number to make your next move: ")
    move = int(move)  
  board[move] = playerMark

  # Checks for tie 
  if " " not in board:
    print "Game is a tie!"
    playAgain()
    return True

  # Check for player's win
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

  # If there is not a tie or a win, the function returns False
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
    gameOver = playerMove(board, 1, "X") 
    if gameOver:
      break

    # Player 2's turn
    printHeader() 
    drawBoard(board)
    gameOver = playerMove(board, 2, "O")
    if gameOver:
      break
    
if __name__ == "__main__":
  ticTacToe()