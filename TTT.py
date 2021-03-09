import random #will be used when the AI is built

# board = []
# for square in range(10):
#     square = str(square) 
#     board.append(square)

class Board:
    def __init__(self, board):
        self.board = []
        for square in range(10):
            square = str(square) 
            board.append(square)
    
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

    def makeMove(self, position, board):
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

class AI: #This class is controlled by the computer
    def __init__(self):
        pass
    #Used in selecting randomly when the computer has more than one
    # possible option
    def randomSelection(self, b):
        ln = len(b)
        r = random.randrange(0, ln)
        return b[r]

    def makeMove(self, board, movesMade):    
    #This checks to see if there is a spot where the AI can win and then checks to block a move where the human can win
        i = 0
        j = 0
        AI_judge = Judge()
                
        for i in range(len(board)):
            if j < len(board): #This allows the for loop to be nested without duplicated efforts
                for j in range(len(board)): #This loop checks for moves that makes the AI win
                    if board[j] == 'X' or board[j] == 'O' or board[j] == '0':
                        continue #Prevents us from considering squares that have a token or are the zero index
                    else: 
                        board[j] = "O" #Temp set square
                        if AI_judge.gamePlay("O", movesMade, board) == True: #Determine if that would make AI win
                            return #If true, return because this move makes AI win
                        if AI_judge.gamePlay("O", movesMade, board) == False:
                            board[j] = str(j) #If move will not make AI win, set square to its previous value and keep looking
                            continue
            #After checking for winning moves, check for moves that the AI needs to block or the human will win
            if board[i] == 'X' or board[i] == 'O' or board[i] == '0':
                continue
            else: 
                board[i] = "X"
                if AI_judge.gamePlay("X", movesMade, board) == True:
                    board[i] = "O" #If the move will result in a human win, mark the square with AI token
                    return
                if AI_judge.gamePlay("X", movesMade, board) == False:
                    board[i] = str(i)
                else: #Likely inaccessible code but acts as a catch all if no if statement is entered somehow
                    board[i] = str(i)
                    

        #If a win or a block is not available, check to take a corner 
        openCorners = []
        for i in range(len(board)):
            if board[i] == "1" or board[i] == "3" or board[i] == "7" or board[i] == "9":
                openCorners.append(i)
            if len(openCorners) > 0:
                move = self.randomSelection(openCorners)
                board[move] = "O"
                return 
        return
        
        #If a win, block, or corner isn't available, take the center
        if 5 in board:
            move = 5
            board[move] = "O"
            return

        #If none of the above options are available, take ant open edge
        openEdges = []
        for i in range(len(board)):
            if board[i] == '2' or board[i] == '4' or board[i] == '6' or board[i] == '8':
                openEdges.append(i)
            if len(openEdges) > 0:
                move = (randomSelection(openEdges))
                board[move] = "O"
                return 
        return

class Judge: #This class will be called to determine is a win or tie has occured 
    def __init__(self):
        pass
    
    def gamePlay(self, t, movesMade, board):
        a = self.checkWinner(t, board)
        if (a == True):
            return True
        if (a == False):
            if (movesMade >= 9):
                return False
            else:
                return False

    def checkWinner(self, t, board): # t == player token
        for win in [[1,2,3], [4,5,6], [7,8,9], [1,4,7], [2,5,8], [3,6,9], [1,5,9], [3,5,7]]:
            result = True
            for b in win:
                if board[b] != t:
                    result = False
            if result == True:
                return True
        return False

def main():
    #Any move between 0-9 reflects moves made during game
    # movesMade values of -1 and -2 are used to dictate messages and reset game play
    # before resetting movesMade back to zero and a new game begins with the human
    movesMade = 0 

    #Creating the board and player objects for game play
    board = []
    game = Board(board)
    player1 = Human()
    player2 = AI()
    judge = Judge()
    game.show_Board(board)

    while (movesMade < 9):
        move = input("Human Move ")
        player1.makeMove(move, board)
        game.show_Board(board)
        movesMade += 1
        if (judge.gamePlay("X", movesMade, board) == True):
            print("The X's have won!")
            decision = input("Would you like to play again? <Y/N> ").upper()
            if (decision == "Y"): #If player wants to play again we clean the board
                movesMade = -1 #Skips the AI move
                for square in range(10): #Resets board to original values
                    board[square] = str(square)
            else:
                movesMade = -2
        if (judge.gamePlay("X", movesMade, board) == False):
            if (movesMade == 9):
                print("Tie Game!")
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
            player2.makeMove(board, movesMade)
            game.show_Board(board)
            movesMade +=1
            if (judge.gamePlay("O", movesMade, board) == True):
                print("I have defeated you human!")
                decision = input("Would you like to play again? <Y/N> ").upper()
                if (decision == "Y"): #If player wants to play again we clean the board
                    movesMade = 0
                    for square in range(10): #Resets board to original values
                        board[square] = str(square)
                else:
                    movesMade = -2
            if (judge.gamePlay("X", movesMade, board) == False):
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
            print("AI Moves Made: " + str(movesMade))
        print(" ")
            
        if (movesMade == -1):
            movesMade = 0 #Resets moves to zero and human starts new game
        if (movesMade == -2):
            movesMade = 10 # To end the game at the start of the while-loop

main()


