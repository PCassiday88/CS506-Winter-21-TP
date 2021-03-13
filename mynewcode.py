""" 
This is the classic game of Tic-Tac-Toe between
two users
"""

import random 

WAYS_TO_WIN = ((1,2,3,4,5),(6,7,8,9,10),(11,12,13,14,15),(16,17,18,19,20),
              (1,6,11,16,21),(2,7,12,17,22),(3,8,13,18,23),(4,9,14,19,24),
              (5,10,15,20,25),(1,7,13,19,25),(5,9,13,17,21))
board = []
for square in range(26):
    square = str(square) 
    board.append(square)

def introduction():
    """Introduce the game to the user"""  
    print(
    """
    Welcome to Tic-Tac-Toe against me, the Mighty Computer.
    If you don't know how to play, you are in the wrong place. 
    When I ask your move, please tell me a space number between
    1 and 25, from top to bottom, left to right... Like this:
    
                  
                    1 |  2 |  3 |  4 |  5
                  -------------------------
                    6 |  7 |  8 |  9 | 10
                  -------------------------
                   11 | 12 | 13 | 14 | 15
                  -------------------------
                   16 | 17 | 18 | 19 | 20
                  -------------------------
                   21 | 22 | 23 | 24 | 25
                  
    I will even give you the advantage of making the first move.

                Let's see what you've got human!

    """
    )
    
class Board:
    def __init__(self):
        pass
        
    
    def show_Board(self):
        print("\n",' ' + board[1] + ' |  ' + board[2] + ' |  ' + board[3] + ' |  ' + board [4] + ' |  ' + board[5])
        print('-------------------------')
        print('  ' + board[6] + ' |  ' + board[7] + ' |  ' + board[8] + ' |  ' + board[9] + ' | ' + board[10])
        print('-------------------------')
        print(' ' + board[11] + ' | ' + board[12] + ' | ' + board[13] + ' | ' + board[14] + ' | ' + board[15])
        print('-------------------------')
        print(' ' + board[16] + ' | ' + board[17] + ' | ' + board[18] + ' | ' + board[19] + ' | ' + board[20])
        print('-------------------------')
        print(' ' + board[21] + ' | ' + board[22] + ' | ' + board[23] + ' | ' + board[24] + ' | ' + board[25])

class Human:
    def __init__(self):
        pass

    def makeMove(self):
        while True:
            turn = input("\nIt's your move, human: ")
            
            try:
                pos = int(turn) #check for integer input
                while True:
                    try:
                        pos >= 1 and pos <= 25 #check if integer is a valid board space
                        # If you pick a number outside of the range, you are given a chance to pick the pos again
                        if (board[pos] == 'X' or board[pos] == 'O'): #Check to see if space is occupied 
                            print("\nYou skip your turn for trying to flip a taken square")
                            break
                        #Space isn't occupied and the pos is within rangebreak
                        if (pos <= 10):# for formatting squares correctly when replacing 2 digit number
                            board[pos] = "X"
                            break 
                            
                        else:
                            board[pos] = " X" 
                        break
                    except:
                        print("Lets try that again. This time pick an open space between 1-25.\n")
                        self.makeMove()
                        break
                break        
            except ValueError:
                print("That's not a number, please try again: ")
        return

class AI: #This class is controlled by the computer
    def __init__(self):
        pass
    
    def randomSelection(self, board):
        """Randomly selects a square for the computer. 
        (Not the best AI.)"""
        
        ln = len(board)
        r = random.randrange(0, ln)

        # pick a new space if occupied
        while (board[r] == 'X' or board[r] == ' X' or board[r] == 'O' or board[r] == '0'):
            r = random.randrange(0, ln)
        return r  
        
        

    def makeMove(self):    
        """Selects the computer's move. There was a lot of AI attempted here and 
        shown in other submission material, but unfortunately, we had to reduce this
        to calling randomSelection"""
        r = self.randomSelection(board)
        board[r] = 'O'
                


class Judge:
    """Determines if a win or tie has occurred."""

    def __init__(self):
        pass
    
    """ def gamePlay(self, t):
        a = self.checkWinner(t)
        if (a == True):
            return True
        else:
            return False """

    def checkWinner(self, t): # t == player token
        for win in WAYS_To_WIN:
            result = True
            for b in win:
                if board[b] != t:
                    result = False
            if result == True:
                return True
        return False

def main():
    # Any move between 1-25 reflects moves made during game
    # movesMade values of -1 and -2 are used to dictate messages and reset game play
    # before resetting movesMade back to zero and a new game begins with the human
    movesMade = 0 


    #Creating the board and player objects for game play
    #board = []
    game = Board()
    player1 = Human()
    player2 = AI()
    judge = Judge()
    
    introduction() # welcome user and display instructions
    game.show_Board()

    while (movesMade < 26):
        #game.show_Board(board)
        player1.makeMove()
        game.show_Board()
        movesMade += 1
        if (judge.checkWinner("X") == True):
            print("\nUnbelievable! Somehow you have beat me...")
            decision = input("\nWould you like to play again? <Y/N> ").upper()
            if (decision == "Y"): #If player wants to play again we clean the board
                movesMade = -1 #Skips the AI move
                for square in range(26): #Resets board to original values
                    board[square] = str(square)
            else:
                movesMade = -2
        if (judge.checkWinner("X") == False):
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

        #Begins the AI move
        if (movesMade < 25 and movesMade >= 0): #Check to see if there are moves remaining
            player2.makeMove()
            game.show_Board()
            movesMade +=1
            if (judge.gamePlay("O") == True):
                print("I have defeated you human!")
                decision = input("Would you like to play again? <Y/N> ").upper()
                if (decision == "Y"): #If player wants to play again we clean the board
                    movesMade = 0
                    for square in range(26): #Resets board to original values
                        board[square] = str(square)
                else:
                    movesMade = -2
            if (judge.gamePlay("X") == False):
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


