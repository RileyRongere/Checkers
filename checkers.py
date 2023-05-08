from Game import *
import math

NUMBER_OF_ROWS = 8
NUMBER_OF_COLS = 8

class ConnectFourGame(Game) :

    def __init__(self) :
        self.initial = [['.'] * NUMBER_OF_COLS for _ in range(NUMBER_OF_ROWS)]
        self.pervious_state = self.initial
        self.red_pieces = [(1,1),(1,3),(1,5),(1,7),(2,2),(2,4),(2,6),(2,8),(3,1),(3,3),(3,5),(3,7)]
        self.black_pieces = [(6,2),(6,4),(6,6),(6,8),(7,1),(7,3),(7,5),(7,7),(8,2),(8,4),(8,6),(8,8)]

        for piece in self.red_pieces:
            self.initial[piece[0]-1][piece[1]-1] = 'r'

        for piece in self.black_pieces:
            self.initial[piece[0]-1][piece[1]-1] = 'b'

    def display(self, state):
        """Print or otherwise display the state."""
        print()
        for row in range(NUMBER_OF_ROWS-1,-1,-1):
            print(row,"|\t",end='')
            for col in range(NUMBER_OF_COLS):
                print(state[row][col],"\t", end="")
            print("|")

        print("-------------------------------------------------------------------------")
        print("\t0\t1\t2\t3\t4\t5\t6\t7 ")
    
    def move_piece(self, state, row, col, piece):
        state[row][col] = piece


    def jump_piece(self, state, move_row, move_col, jump_row, jump_col, piece):
        row_dif = move_row-jump_row
        col_dif = move_col-jump_col
        
        state[move_row][move_col]=='.'
        state[jump_row][jump_col]=='.'

        # jump up right
        if row_dif > 0 and col_dif > 0:
            state[move_row+2][move_col+2] = piece

        # jump up left
        elif row_dif > 0 and col_dif < 0:
            state[move_row+2][move_col-2] = piece

        # jump down right
        elif row_dif < 0 and col_dif > 0:
            state[move_row-2][move_col+2] = piece

        # jump down left
        else: # row_dif < 0 and col_dif < 0:
            state[move_row-2][move_col-2] = piece


    def is_valid_location(self, state, row, col):
        if col < 0 or col >= NUMBER_OF_COLS:
            return False
        elif row < 0 or row >= NUMBER_OF_ROWS:
            return False
        else:
            # TODO: NEED TO CHECK/FIX
            return state[NUMBER_OF_ROWS - 1][col] == '.'
        
    def winning_move(self, board, piece):
        # Check if all of one color are gone.
        for c in range(NUMBER_OF_COLS ):
            for r in range(NUMBER_OF_ROWS):
                if board[r][c] == self.getEnemyPlayer(piece):
                    return False
            return True
        
    def terminal_test(self, state):
        return self.winning_move(state, "r") or self.winning_move(state, "b") or len(self.actions(state)) == 0
    
    def getEnemyPlayer(self,player):
        # return the opposite of player
        if player == 'r':
            return 'b'
        else:
            return 'r'
        
    def undo(self):
        return self.pervious_state
    
    def get_moves_for_piece(self, state, team, piece_index):
        valid_moves = []
        # if piece is red
        if team == 'r':
            # piece = self.red_pieces[piece_index]
            # if king
            if state[piece_index[0]][piece_index[1]] == team.upper():
                # up-right diagnal
                if self.is_valid_location(state, piece_index[0]+1, piece_index[1]+1) and \
                        state[piece_index[0]+1][piece_index[1]+1] != team: # in bounds and not same team
                    valid_moves.append((piece_index[0]+1, piece_index[1]+1))
                    # see if you can jump
                if state[piece_index[0]+1][piece_index[1]+1] == self.getEnemyPlayer and \
                        self.is_valid_location(state, piece_index[0]+2, piece_index[1]+2) and \
                        state[piece_index[0]+2][piece_index[1]+2] == '.': # next space is enemy, double is in bounds, double is empty
                    valid_moves.append((piece_index[0]+2, piece_index[1]+2))



                    self.move_piece(state, piece_index[0]+1, piece_index[1]+1,team)


        # if piece is black  
        else:
            # piece = self.black_pieces[piece_index]
            # if king
            if state[piece_index[0]][piece_index[1]] == piece_index.upper():
                for pie in self.red_pieces:
                    pass


        # for r in range(NUMBER_OF_ROWS):
        #     if state[r][col] == '.':
        #         return r
        # return NUMBER_OF_ROWS

    def actions(self, state, team, piece):
        # returns list of numbers corresponding to possible moves
        valid_locations = []
        for col in range(NUMBER_OF_COLS):
            #if self.get_next_open_row(state,col) < NUMBER_OF_COLS:
            if self.is_valid_location(state, col):
                valid_locations.append(col)
        return valid_locations
        
        # valid_locations = []
        # for col in range(NUMBER_OF_COLS):

    
