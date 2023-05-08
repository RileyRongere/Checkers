from Game import *
import math
import copy

NUMBER_OF_ROWS = 8
NUMBER_OF_COLS = 8

class CheckersGame(Game):

    def __init__(self) :
        self.initial = [['.'] * NUMBER_OF_COLS for _ in range(NUMBER_OF_ROWS)]

        player = ''

        for row in range(NUMBER_OF_ROWS):
            for col in range(NUMBER_OF_COLS):
                if row <= 2 or row >= 5:
                    if row <= 2:
                        player = 'r'
                    else:
                        player = 'b'

                    if row % 2 == 0 and col % 2 == 0:
                        self.initial[row][col] = player
                    elif row % 2 == 1 and col % 2 == 1:
                        self.initial[row][col] = player                 

        self.r_pieces = 12
        self.b_pieces = 12

    def display(self, state):
        """Print or otherwise display the state."""
        print()
        for row in range(NUMBER_OF_ROWS-1,-1,-1):
            print(row,"|\t",end='')
            for col in range(NUMBER_OF_COLS):
                print(state[row][col],"\t", end="")
            print("|")

        print("-----------------------------------------------------------------")
        print("\t0\t1\t2\t3\t4\t5\t6\t7 ")

    def is_valid_location(self, state, col):
        if col <0 or col >= NUMBER_OF_COLS:
            return False
        else:
            return state[NUMBER_OF_ROWS - 1][col] == '.'

    def winning_move(self, board, player):
        if player == 'r' and self.b_pieces == 0:
            return True
        
        if player == 'b' and self.r_pieces == 0:
            return True
        
        else:
            return False
        
    def terminal_test(self, state):
        return self.winning_move(state, 'r') or self.winning_move(state, 'b') or len(self.actions(state)) == 0 
    
    def getEnemyPlayer(self,player):
        if player == 'r':
            return 'b'
        else:
            return 'r'
        


game = CheckersGame()
game.display(game.initial)