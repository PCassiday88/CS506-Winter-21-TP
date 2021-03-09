#This version wis complete without AI

board = []
for square in range(10):
    square = str(square) 
    board.append(square)

class Board:
    def __init__(self):
        pass
    
    def show_Board(self, board):
        print('-----------')
        print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
        print('-----------')
        print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
        print('-----------')
        print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
        print('-----------')

class Human:
    def __init__(self):
        pass

    def makeMove(self, position):
        pos = int(position)
        if pos >= 1 and pos <= 9:
            if (board[pos] == 'X' or board[pos] == 'O'): #Check to see if space is occupied 
                print(" ")   #For appearance 
                print("You skip your turn for trying to flip a taken square")
            else:
                board[pos] = "X" #Space isn't occupied and the pos is within range
        else: # If you pick a number outside of the range, you are given a chance to pick the pos again
            print("Lets try that again")
            pos = input("This time pick an open space between 1-9 ")
            print(" ")
            self.makeMove(pos) # Calls itself with new pos and game continues

class AI: #This class will eventually get the AI built in but at this stage we will control it
    def __init__(self):
        pass
    
    def makeMove(self, position):
        pos = int(position)
        if pos >= 1 and pos <= 9:
            if (board[pos] == 'X' or board[pos] == 'O'):   
                print("You skip your turn for trying to flip a taken square")
            else:
                board[pos] = "O"
        else: # If you pick a number outside of the range, you are given a chance to pick the pos again
            print("Lets try that again")
            pos = input("This time pick an open space between 1-9 ")
            print(" ")
            self.makeMove(pos) # Calls itself with new pos and game continues

class Judge: #This class will be called to determine is a win or tie has occured 
    def __init__(self):
        pass
    
    def gamePlay(self, t, movesMade):
        a = self.checkWinner(t)
        if (a == True):
            print(t + "'s have Won!!")
            return True
        if (a == False):
            if (movesMade >= 9):
                print("Tie Game!")
                return False
            else:
                return False

    def checkWinner(self, t): # t == player token
        #rows going across
        if (board[1] == t and board[2] == t and board[3] == t):  
            return True
        if (board[4] == t and board[5] == t and board[6] == t):
            return True
        if (board[7] == t and board[8] == t and board[9] == t):
            return True
        #columns
        if (board[1] == t and board[4] == t and board[7] == t):
            return True
        if (board[2] == t and board[5] == t and board[8] == t):
            return True
        if (board[3] == t and board[6] == t and board[9] == t):
            return True
        #diagonal
        if (board[1] == t and board[5] == t and board[9] == t): 
            return True
        if (board[3] == t and board[5] == t and board[7] == t):
            return True
        else:
            return False
        

def main():
    #Any move between 0-9 reflects moves made during game
    # movesMade values of -1 and -2 are used to dictate messages and reset game play
    # before resetting movesMade back to zero and a new game begins with the human
    movesMade = 0 

    #Creating the board and player objects for game play
    game = Board()
    player1 = Human()
    player2 = AI()
    judge = Judge()
    game.show_Board(board)

    while (movesMade < 9):
        move = input("Human Move ")
        player1.makeMove(move)
        game.show_Board(board)
        movesMade += 1
        if (judge.gamePlay("X", movesMade) == True):
            decision = input("Would you like to play again? <Y/N> ").upper()
            if (decision == "Y"): #If player wants to play again we clean the board
                movesMade = -1 #Skips the AI move
                for square in range(10): #Resets board to original values
                    board[square] = str(square)
            else:
                movesMade = -2
        if (judge.gamePlay("X", movesMade) == False):
            if (movesMade == 9):
                decision = input("Would you like to play again? <Y/N> ").upper()
                if (decision == "Y"): #If player wants to play again we clean the board
                    for square in range(10):
                        board[square] = str(square)
                    movesMade = -1 #To skip the AI move
                else:
                    movesMade = -2 #To prompt the I am done with the game message
        print(" ")
        if (movesMade < 0):
            if (movesMade == -2):
                print("Thank you! Come play again weak human!") #Done with the game message
        else:
            print("Moves Made is: " + str(movesMade))
        print(" ")
        
        if (movesMade < 9 and movesMade >= 0): #Check to see if there are moves remaining
            move = input("AI Move ")
            player2.makeMove(move)
            game.show_Board(board)
            movesMade += 1
            if (judge.gamePlay("O", movesMade) == True):
                decision = input("Would you like to play again? <Y/N> ").upper()
                if (decision == "Y"): #If player wants to play again we clean the board
                    movesMade = 0
                    for square in range(10): #Resets board to original values
                        board[square] = str(square)
                else:
                    movesMade = -2
            if (judge.gamePlay("X", movesMade) == False):
                if (movesMade == 9):
                    decision = input("Would you like to play again? <Y/N> ").upper()
                    if (decision == "Y"): #If player wants to play again we clean the board
                        for square in range(10):
                            board[square] = str(square)
                        movesMade = 0 
                    else:
                        movesMade = -2 #To prompt the I am done with the game message
            print(" ")
            if (movesMade < 0):
                if (movesMade == -2):
                    print("Thank you! Come play again weak human!") #Done with the game message
            else:
                print("Moves Made is: " + str(movesMade))
            print(" ")
            
        if (movesMade == -1):
            movesMade = 0 #Resets moves to zero and human starts new game

main()
