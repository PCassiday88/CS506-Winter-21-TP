import random #will be used when the AI is built

# board = []
# for square in range(10):
#     square = str(square) 
#     board.append(square)

class Board:
    def __init__(self, board):
        self.board = []
        for square in range(26):
            square = str(square) 
            board.append(square)
    
    def show_Board(self, board):
        print('-------------------------')
        print('  ' + board[ 1 ] + ' |  ' + board[ 2 ] + ' |  ' + board[ 3 ] + ' |  ' + board [ 4 ] + ' |  ' + board[ 5 ])
        print('-------------------------')
        print('  ' + board[ 6] + ' |  ' + board[ 7] + ' |  ' + board[ 8] + ' |  ' + board[ 9 ] + ' | ' + board[10])
        print('-------------------------')
        print(' ' + board[11] + ' | ' + board[12] + ' | ' + board[13] + ' | ' + board[14] + ' | ' + board[15])
        print('-------------------------')
        print(' ' + board[16] + ' | ' + board[17] + ' | ' + board[18] + ' | ' + board[19] + ' | ' + board[20])
        print('-------------------------')
        print(' ' + board[21] + ' | ' + board[22] + ' | ' + board[23] + ' | ' + board[24] + ' | ' + board[25])
        print('-------------------------')

class Human:
    def __init__(self):
        pass

    def makeMove(self, board):
        while True:
            turn = input("It's your move, human: ")
            
            try:
                pos = int(turn) #check for integer input
                while True:
                    try:
                        pos >= 1 and pos <= 25 #check if integer is a valid board space
                        # If you pick a number outside of the range, you are given a chance to pick the pos again
                        if (board[pos] == 'X' or board[pos] == 'O'): #Check to see if space is occupied 
                            print(" ")   #For appearance 
                            print("You skip your turn for trying to flip a taken square")
                        #Space isn't occupied and the pos is within rangebreak
                        if (pos > 10):# for formatting squares correctly when replacing 2 digit number
                            board[pos] = " X" 
                            
                        else:
                            board[pos] = "X" 
                        break
                    except:
                        print("Lets try that again. This time pick an open space between 1-25.")
                        print(" ")
                        self.makeMove(board)
                        break
                break        
            except ValueError:
                print("That's not a number, please try again: ")
        return board

class AI: #This class is controlled by the computer
    def __init__(self):
        pass
    #Used in selecting randomly when the computer has more than one
    # possible option
    def randomSelection(self, b, board):
        ln = len(b)
        r = random.randrange(1, ln)
        # return r
        board[r] = 'O'
        return

    def makeMove(self, board, movesMade):    
    #This checks to see if there is a spot where the AI can win and then checks to block a move where the human can win
        i = 0
        j = 0
        k = ' '
        AI_judge = Judge()
        posSquares = []
                
        for j in range(len(board)): #This loop checks for moves that makes the AI win
            if board[j] == 'X' or board[j] == 'O' or board[j] == '0':
                posSquares.append(k)
                continue #Prevents us from considering squares that have a token or are the zero index
            else: 
                posSquares.append(j) #filling container with all possible squares not filled with a player token
                board[j] = "O" #Temp set square
                if AI_judge.gamePlay("O", movesMade, board) == True: #Determine if that would make AI win
                    return #If true, return because this move makes AI win
                if AI_judge.gamePlay("O", movesMade, board) == False:
                    board[j] = str(j) #If move will not make AI win, set square to its previous value and keep looking        
    
        for i in range(len(board)):
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
                    
        print(len(posSquares))
        # #If a win or a block is not available, check to take a corner 
        # openCorners = []
        # for i in range(len(board)):
        #     if board[i] == "1" or board[i] == "5" or board[i] == "21" or board[i] == "25":
        #         openCorners.append(i)
        #     if len(openCorners) > 0:
        #         self.randomSelection(openCorners, board)
        #         # board[move] = "O"
        #         # return 
        # return
        
        # #If a win, block, or corner isn't available, take the center
        # if 13 in board:
        #     move = 13
        #     board[move] = "O"
        #     return

        #If none of the above options are available, take ant open edge
        # posEdges = [2,3,4,6,11,16,10,15,20,22,23,24]
        # openEdges = []
        # for i in range(len(posSquares)):
        #     # for j in range(len(posEdges)):
        #     if board[j] == ' ':
        #         continue
        #     else:
        #         openEdges.append(j)
        # if len(openEdges) > 0:
        #     self.randomSelection(openEdges, board)
            # board[move] = "O"
            # return
        #If no edge is available, take any random open square
        if len(posSquares) > 0:
            self.randomSelection(posSquares, board)
            # board[move] = "O"
            # return 

        return

class Judge: #This class will be called to determine is a win or tie has occured 
    def __init__(self):
        pass
    
    def gamePlay(self, t, movesMade, board):
        a = self.checkWinner(t, board)
        if (a == True):
            return True
        if (a == False):
            if (movesMade >= 25):
                return False
            else:
                return False

    def checkWinner(self, t, board): # t == player token
        for win in [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[1,6,11,16,21],[2,7,12,17,22],[3,8,13,18,23],[4,9,14,19,24],[5,10,15,20,25],[1,7,13,19,25],[5,9,13,17,21]]:
            result = True
            for b in win:
                if board[b] != t:
                    result = False
            if result == True:
                return True
        return False

def main():
    #Any move between 1-25 reflects moves made during game
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

    while (movesMade < 26):
        board = player1.makeMove(board)
        game.show_Board(board)
        movesMade += 1
        if (judge.gamePlay("X", movesMade, board) == True):
            print("The X's have won!")
            decision = input("Would you like to play again? <Y/N> ").upper()
            if (decision == "Y"): #If player wants to play again we clean the board
                movesMade = -1 #Skips the AI move
                for square in range(26): #Resets board to original values
                    board[square] = str(square)
            else:
                movesMade = -2
        if (judge.gamePlay("X", movesMade, board) == False):
            if (movesMade == 25):
                print("Tie Game!")
                decision = input("Would you like to play again? <Y/N> ").upper()
                if (decision == "Y"): #If player wants to play again we clean the board
                    for square in range(26):
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
        
        if (movesMade < 25 and movesMade >= 0): #Check to see if there are moves remaining
            player2.makeMove(board, movesMade)
            game.show_Board(board)
            movesMade +=1
            if (judge.gamePlay("O", movesMade, board) == True):
                print("I have defeated you human!")
                decision = input("Would you like to play again? <Y/N> ").upper()
                if (decision == "Y"): #If player wants to play again we clean the board
                    movesMade = 0
                    for square in range(26): #Resets board to original values
                        board[square] = str(square)
                else:
                    movesMade = -2
            if (judge.gamePlay("X", movesMade, board) == False):
                if (movesMade == 26):
                    decision = input("Would you like to play again? <Y/N> ").upper()
                    if (decision == "Y"): #If player wants to play again we clean the board
                        for square in range(26):
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
            movesMade = 26 # To end the game at the start of the while-loop

main()


