""" Tic Tac Toe Game
    Lets two people play a game of tic tac toe in a terminal.
    The program should let the players take turns to input 
    their moves.
    The program should report the outcome of the game.
"""        

def ticTacToe(): 

  # define the board
  board = ["", " ", " ", " ", " ", " ", " ", " ", " ", " "] 

  # print the header
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
  def drawBoard():
    print "   |   |   "
    print " "+board[1]+" | "+board[2]+" | "+board[3]+"  "
    print "   |   |   "
    print "---|---|---"
    print "   |   |   "
    print " "+board[4]+" | "+board[5]+" | "+board[6]+"  "
    print "   |   |   "
    print "---|---|---"
    print "   |   |   "     
    print " "+board[7]+" | "+board[8]+" | "+board[9]+"  "
    print "   |   |   "

  while True: 
    printHeader() # prints instructions for the game
    drawBoard() # draws the game board

    # gets player 1's input
    move = raw_input("Player 1, Choose a number to make your next move: ")
    move = int(move)

    # checks to see if the space is empty
    if board[move] == " ": 
      board[move] = "X"

    else: 
      print "That space is already taken!"
      

    # check for player 1's win
    if (board[1] == "X" and board[2] == "X" and board[3] == "X") or \
      (board[4] == "X" and board[5] == "X" and board[6] == "X") or \
      (board[7] == "X" and board[8] == "X" and board[9] == "X") or \
      (board[1] == "X" and board[4] == "X" and board[7] == "X") or \
      (board[2] == "X" and board[5] == "X" and board[8] == "X") or \
      (board[3] == "X" and board[6] == "X" and board[9] == "X") or \
      (board[1] == "X" and board[5] == "X" and board[9] == "X") or \
      (board[3] == "X" and board[5] == "X" and board[7] == "X"):
      printHeader()
      drawBoard()
      print "Player 1 wins!"
      break

      printHeader()
      drawBoard()

    #check for tie
    isFull = True
    if " " in board: 
      isFull = False

    if isFull == True: 
      print "The game is a tie!"
      break

    # player o input
    move = raw_input("Player 2, Choose a number to make your next move: ")
    move = int(move)

    # checks if space is empty
    if board[move] == " ": 
      board[move] = "O" 

    else: 
      print "That space is already taken!"
      

    #check for player 2's win
    if (board[1] == "O" and board[2] == "O" and board[3] == "O") or \
      (board[4] == "O" and board[5] == "O" and board[6] == "O") or \
      (board[7] == "O" and board[8] == "O" and board[9] == "O") or \
      (board[1] == "O" and board[4] == "O" and board[7] == "O") or \
      (board[2] == "O" and board[5] == "O" and board[8] == "O") or \
      (board[3] == "O" and board[6] == "O" and board[9] == "O") or \
      (board[1] == "O" and board[5] == "O" and board[9] == "O") or \
      (board[3] == "O" and board[5] == "O" and board[7] == "O"):
      printHeader()
      drawBoard()
      print "Player 2 wins!"
      break

 # ask if players want to play again
def playAgain(): 
  print("Do you want to play again? (y/n)")
  userInput = raw_input()
  if userInput == "y": 
    ticTacToe()

if __name__ == "__main__":
  ticTacToe()
  playAgain()  
