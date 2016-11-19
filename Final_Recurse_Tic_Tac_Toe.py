# prints instructions for the game
def printHeader():
  print """ The game board looks like this: 

    | 1 | 2 | 3 |
     -----------
    | 4 | 5 | 6 |
     -----------
    | 7 | 8 | 9 |
      
    On the board, player 1 will be "X" and player 2 is "O". 
    First player to get 3 in a row wins!
    """

# draws the game board
def drawBoard(board):
  print '|',board[1],'|', board[2],'|', board[3],'|'
  print '-------------'
  print '|',board[4],'|', board[5],'|', board[6],'|'
  print '-------------'
  print '|',board[7],'|', board[8],'|', board[9],'|'

def playAgain():
  print("Do you want to play again? (y/n)")
  userInput = raw_input()
  if userInput == "y": 
    ticTacToe()

def playerMove(board, playerNumber, playerMark):
  # player input
  move = raw_input("Player " + str(playerNumber) + ", Choose a number to make your next move: ")
  move = int(move)

  # checks if space is empty
  if board[move] == " ": 
    board[move] = playerMark
  else: 
    print "That space is already taken!"
    

  #check for player's win
  if(board[1] == playerMark and board[2] == playerMark and board[3] == playerMark) or \
    (board[4] == playerMark and board[5] == playerMark and board[6] == playerMark) or \
    (board[7] == playerMark and board[8] == playerMark and board[9] == playerMark) or \
    (board[1] == playerMark and board[4] == playerMark and board[7] == playerMark) or \
    (board[2] == playerMark and board[5] == playerMark and board[8] == playerMark) or \
    (board[3] == playerMark and board[6] == playerMark and board[9] == playerMark) or \
    (board[1] == playerMark and board[5] == playerMark and board[9] == playerMark) or \
    (board[3] == playerMark and board[5] == playerMark and board[7] == playerMark):
    printHeader()
    drawBoard(board)
    print "Player " + str(playerNumber) + " wins!"
    playAgain()
    # Indicates that player won the game. Showing the game should be over. 
    return True

  #check for tie
  if " " not in board:
    print "The game is a tie!" 
    return True
    
def ticTacToe(): 
  board = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

  gameOver = False
  while True: 
    printHeader() 
    drawBoard(board) 
    # Player 1's turn 
    gameOver = playerMove(board, 1, "X") 
    if gameOver:
      break
    # Player 2's turn
    gameOver = playerMove(board, 2, "O")
    if gameOver:
      break
    
if __name__ == "__main__":
  ticTacToe()