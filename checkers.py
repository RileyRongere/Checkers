from Game import *
import math
import copy

import pdb

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

    def is_valid_location(self, state, row, col):
        if col < 0 or col >= NUMBER_OF_COLS:
            return False
        elif row < 0 or row >= NUMBER_OF_ROWS:
            return False
        else:
            return True

    def winning_move(self, player):
        if player == 'r' and self.b_pieces == 0:
            return True
        
        if player == 'b' and self.r_pieces == 0:
            return True
        
        else:
            return False
        
    def terminal_test(self, state, player):
        return self.winning_move(player) or self.winning_move(self.getEnemyPlayer(player)) or len(self.all_actions(state,player)) == 0 

    def all_actions(self,state,player):
        all_actions = []
        for row in range(NUMBER_OF_ROWS):
            for col in range(NUMBER_OF_COLS):
                if state[row][col] == player:
                    for move in self.actions(state,(row,col)):
                        all_actions.append(move)
        
        return all_actions

    def getEnemyPlayer(self,player):
        if player == 'r':
            return 'b'
        else:
            return 'r'
    
    # returns a list of tuples that describe possible locations to move a piece
    def actions(self, state, piece_loc): # piece_loc should be a tuple containing 2 ints
        valid_moves = []
        team = state[piece_loc[0]][piece_loc[1]]
        # if piece is red
        if team == 'r':
            # up-right diagnal jump
            if  self.is_valid_location(state, piece_loc[0]+2, piece_loc[1]+2) and \
                    state[piece_loc[0]+1][piece_loc[1]+1] == self.getEnemyPlayer(team) and \
                    state[piece_loc[0]+2][piece_loc[1]+2] == '.': # next space is enemy, double is in bounds, double is empty
                valid_moves.append((piece_loc[0],piece_loc[1],piece_loc[0]+2, piece_loc[1]+2))

            # up-left diagnal jump
            if self.is_valid_location(state, piece_loc[0]+2, piece_loc[1]-2) and \
                    state[piece_loc[0]+1][piece_loc[1]-1] == self.getEnemyPlayer(team) and \
                    state[piece_loc[0]+2][piece_loc[1]-2] == '.': # next space is enemy, double is in bounds, double is empty
                valid_moves.append((piece_loc[0],piece_loc[1],piece_loc[0]+2, piece_loc[1]-2))

            # if king
            if state[piece_loc[0]][piece_loc[1]] == team.upper():
                # down-right diagnal jump
                if self.is_valid_location(state, piece_loc[0]-2, piece_loc[1]+2) and \
                        state[piece_loc[0]-1][piece_loc[1]+1] == self.getEnemyPlayer(team) and \
                        state[piece_loc[0]-2][piece_loc[1]+2] == '.': # next space is enemy, double is in bounds, double is empty
                    valid_moves.append((piece_loc[0],piece_loc[1],piece_loc[0]-2, piece_loc[1]+2))

                # down-left diagnal jump
                if self.is_valid_location(state, piece_loc[0]-2, piece_loc[1]-2) and \
                        state[piece_loc[0]-1][piece_loc[1]-1] == self.getEnemyPlayer(team) and \
                        state[piece_loc[0]-2][piece_loc[1]-2] == '.': # next space is enemy, double is in bounds, double is empty
                    valid_moves.append((piece_loc[0],piece_loc[1],piece_loc[0]-2, piece_loc[1]-2))

            # if there are jump moves, return just jump moves, otherwise continue
            if valid_moves:
                return valid_moves
            

            # up-right diagnal
            if self.is_valid_location(state, piece_loc[0]+1, piece_loc[1]+1) and \
                    state[piece_loc[0]+1][piece_loc[1]+1] == '.': # in bounds and empty
                valid_moves.append((piece_loc[0],piece_loc[1],piece_loc[0]+1, piece_loc[1]+1))

            # up-left diagnal
            if self.is_valid_location(state, piece_loc[0]+1, piece_loc[1]-1) and \
                    state[piece_loc[0]+1][piece_loc[1]-1] == '.': # in bounds and empty
                valid_moves.append((piece_loc[0],piece_loc[1],piece_loc[0]+1, piece_loc[1]-1))

            # if king
            if state[piece_loc[0]][piece_loc[1]] == team.upper():
                # down-right diagnal
                if self.is_valid_location(state, piece_loc[0]-1, piece_loc[1]+1) and \
                        state[piece_loc[0]-1][piece_loc[1]+1] == '.': # in bounds and empty
                    valid_moves.append((piece_loc[0],piece_loc[1],piece_loc[0]-1, piece_loc[1]+1))

                # down-left diagnal
                if self.is_valid_location(state, piece_loc[0]-1, piece_loc[1]-1) and \
                        state[piece_loc[0]-1][piece_loc[1]-1] == '.': # in bounds and empty
                    valid_moves.append((piece_loc[0],piece_loc[1],piece_loc[0]-1, piece_loc[1]-1))    


        # if piece is black  
        else:
            # down-right diagnal jump
            if self.is_valid_location(state, piece_loc[0]-2, piece_loc[1]+2) and \
                    state[piece_loc[0]-1][piece_loc[1]+1] == self.getEnemyPlayer(team) and \
                    state[piece_loc[0]-2][piece_loc[1]+2] == '.': # next space is enemy, double is in bounds, double is empty
                valid_moves.append((piece_loc[0],piece_loc[1],piece_loc[0]-2, piece_loc[1]+2))

            # down-left diagnal jump
            if self.is_valid_location(state, piece_loc[0]-2, piece_loc[1]-2) and \
                    state[piece_loc[0]-1][piece_loc[1]-1] == self.getEnemyPlayer(team) and \
                    state[piece_loc[0]-2][piece_loc[1]-2] == '.': # next space is enemy, double is in bounds, double is empty
                valid_moves.append((piece_loc[0],piece_loc[1],piece_loc[0]-2, piece_loc[1]-2))

            # if king
            if state[piece_loc[0]][piece_loc[1]] == team.upper():
                # up-right diagnal jump
                if self.is_valid_location(state, piece_loc[0]+2, piece_loc[1]+2) and \
                        state[piece_loc[0]+1][piece_loc[1]+1] == self.getEnemyPlayer(team) and \
                        state[piece_loc[0]+2][piece_loc[1]+2] == '.': # next space is enemy, double is in bounds, double is empty
                    valid_moves.append((piece_loc[0],piece_loc[1],piece_loc[0]+2, piece_loc[1]+2))

                # up-left diagnal jump
                if self.is_valid_location(state, piece_loc[0]+2, piece_loc[1]-2) and \
                        state[piece_loc[0]+1][piece_loc[1]-1] == self.getEnemyPlayer(team) and \
                        state[piece_loc[0]+2][piece_loc[1]-2] == '.': # next space is enemy, double is in bounds, double is empty
                    valid_moves.append((piece_loc[0],piece_loc[1],piece_loc[0]+2, piece_loc[1]-2))
        
            # if there are jump moves, return just jump moves, otherwise continue
            if valid_moves:
                return valid_moves
            
            # down-right diagnal
            if self.is_valid_location(state, piece_loc[0]-1, piece_loc[1]+1) and \
                    state[piece_loc[0]-1][piece_loc[1]+1] == '.': # in bounds and empty
                valid_moves.append((piece_loc[0],piece_loc[1],piece_loc[0]-1, piece_loc[1]+1))

            # down-left diagnal
            if self.is_valid_location(state, piece_loc[0]-1, piece_loc[1]-1) and \
                    state[piece_loc[0]-1][piece_loc[1]-1] == '.': # in bounds and empty
                valid_moves.append((piece_loc[0],piece_loc[1],piece_loc[0]-1, piece_loc[1]-1))

            # if king
            if state[piece_loc[0]][piece_loc[1]] == team.upper():
                # up-right diagnal
                if self.is_valid_location(state, piece_loc[0]+1, piece_loc[1]+1) and \
                        state[piece_loc[0]+1][piece_loc[1]+1] == '.': # in bounds and empty
                    valid_moves.append((piece_loc[0],piece_loc[1],piece_loc[0]+1, piece_loc[1]+1))

                # up-left diagnal
                if self.is_valid_location(state, piece_loc[0]+1, piece_loc[1]-1) and \
                        state[piece_loc[0]+1][piece_loc[1]-1] == '.': # in bounds and empty
                    valid_moves.append((piece_loc[0],piece_loc[1],piece_loc[0]+1, piece_loc[1]-1))

        return valid_moves

    def jump_move(self, state, move):
        if state[move[0]][move[1]] == 'r':
            if move[2] == (move[0] + 1):
                return False
            else:
                return True

        elif state[move[0]][move[1]] == 'b':
            if move[2] == (move[0] - 1):
                return False
            else:
                return True
            
        elif state[move[0]][move[1]] == 'R' or state[move[0]][move[1]] == 'B':
            if move[2] == (move[0] - 1) or  move[2] == (move[0] + 1):
                return False
            else:
                return True

    def make_move(self, state, move):
        if state[move[0]][move[1]] == 'r':
            if move[2] == (move[0] + 1):
                if move[2] == 7:
                    state[move[2]][move[3]] = 'R'
                else:
                    state[move[2]][move[3]] = 'r'                    
                state[move[0]][move[1]] = '.'
            else:
                if move[2] == 7:
                    state[move[2]][move[3]] = 'R'
                else:
                    state[move[2]][move[3]] = 'r'
                state[move[0]][move[1]] = '.'
                state[move[2] - 1][(move[1] + move[3]) // 2] = '.'
                self.b_pieces -= 1

        elif state[move[0]][move[1]] == 'R':
            if move[2] == (move[0] - 1) or  move[2] == (move[0] + 1):
                state[move[2]][move[3]] = 'R'
                state[move[0]][move[1]] = '.'
            elif move[2] > move[0]:
                state[move[2]][move[3]] = 'R'
                state[move[0]][move[1]] = '.'
                state[move[2] - 1][(move[1] + move[3]) // 2] = '.'
                self.b_pieces -= 1
            else:
                state[move[2]][move[3]] = 'R'
                state[move[0]][move[1]] = '.'
                state[move[2] + 1][(move[1] + move [3]) // 2] = '.'
                self.b_pieces -= 1

        elif state[move[0]][move[1]] == 'b':
            if move[2] == (move[0] - 1):
                if move[2] == 0:
                    state[move[2]][move[3]] = 'B'
                else:
                    state[move[2]][move[3]] = 'b'
                state[move[0]][move[1]] = '.'
            else:
                if move[2] == 0:
                    state[move[2]][move[3]] = 'B'
                else:
                    state[move[2]][move[3]] = 'b'
                state[move[0]][move[1]] = '.'
                state[move[2] + 1][(move[1] + move [3]) // 2] = '.'
                self.r_pieces -= 1

        elif state[move[0]][move[1]] == 'B':
            if move[2] == (move[0] - 1) or  move[2] == (move[0] + 1):
                state[move[2]][move[3]] = 'B'
                state[move[0]][move[1]] = '.'
            elif move[2] > move[0]:
                state[move[2]][move[3]] = 'B'
                state[move[0]][move[1]] = '.'
                state[move[2] - 1][(move[1] + move[3]) // 2] = '.'
                self.r_pieces -= 1
            else:
                state[move[2]][move[3]] = 'B'
                state[move[0]][move[1]] = '.'
                state[move[2] + 1][(move[1] + move [3]) // 2] = '.'
                self.r_pieces -= 1
        
        return state
    
    def result_make_move(self, state, move):
        if state[move[0]][move[1]] == 'r':
            if move[2] == (move[0] + 1):
                if move[2] == 7:
                    state[move[2]][move[3]] = 'R'
                else:
                    state[move[2]][move[3]] = 'r'                    
                state[move[0]][move[1]] = '.'
            else:
                if move[2] == 7:
                    state[move[2]][move[3]] = 'R'
                else:
                    state[move[2]][move[3]] = 'r'
                state[move[0]][move[1]] = '.'
                state[move[2] - 1][(move[1] + move[3]) // 2] = '.'

        elif state[move[0]][move[1]] == 'R':
            if move[2] == (move[0] - 1) or  move[2] == (move[0] + 1):
                state[move[2]][move[3]] = 'R'
                state[move[0]][move[1]] = '.'
            elif move[2] > move[0]:
                state[move[2]][move[3]] = 'R'
                state[move[0]][move[1]] = '.'
                state[move[2] - 1][(move[1] + move[3]) // 2] = '.'
            else:
                state[move[2]][move[3]] = 'R'
                state[move[0]][move[1]] = '.'
                state[move[2] + 1][(move[1] + move [3]) // 2] = '.'

        elif state[move[0]][move[1]] == 'b':
            if move[2] == (move[0] - 1):
                if move[2] == 0:
                    state[move[2]][move[3]] = 'B'
                else:
                    state[move[2]][move[3]] = 'b'
                state[move[0]][move[1]] = '.'
            else:
                if move[2] == 0:
                    state[move[2]][move[3]] = 'B'
                else:
                    state[move[2]][move[3]] = 'b'
                state[move[0]][move[1]] = '.'
                state[move[2] + 1][(move[1] + move [3]) // 2] = '.'

        elif state[move[0]][move[1]] == 'B':
            if move[2] == (move[0] - 1) or  move[2] == (move[0] + 1):
                state[move[2]][move[3]] = 'B'
                state[move[0]][move[1]] = '.'
            elif move[2] > move[0]:
                state[move[2]][move[3]] = 'B'
                state[move[0]][move[1]] = '.'
                state[move[2] - 1][(move[1] + move[3]) // 2] = '.'
            else:
                state[move[2]][move[3]] = 'B'
                state[move[0]][move[1]] = '.'
                state[move[2] + 1][(move[1] + move [3]) // 2] = '.'
        
        return state


    def result(self, state, move, player):
        """Return the state that results from making a move from a state."""
        
        #imported copy so that this function wouldn't change the state when returning the move
        workingState = copy.deepcopy(state)

        workingState = self.result_make_move(workingState, move)

        return workingState

    def utility(self, state, player):
        """Return the value of this final state to player."""
            
        if self.winning_move(player):
            return 5000
        
        elif self.winning_move(self.getEnemyPlayer(player)):
            return -5000
        
        else:
            return 0


    def minimax(self, state, player, depth=0, maxi=-math.inf, mini=math.inf):
        best = -1
        bestMove = (-1,-1,-1,-1)
        runningMax = maxi
        runningMin = mini
        if not depth > 0:
            return self.utility(state,player), bestMove

        if self.terminal_test(state, player):
            return self.utility(state,player), bestMove

        if player == 'r':
            best = math.inf
            for child in self.all_actions(state,player):
                childScore = self.minimax(self.result(state,child,player), self.getEnemyPlayer(player), depth-1, runningMax,runningMin)[0] - 1
                if childScore < best:
                    best = childScore
                    bestMove = child

                runningMin = min(runningMin, childScore)
                if childScore <= runningMax:
                    break

        else:
            best = -(math.inf)
            for child in self.all_actions(state,player):
                childScore = self.minimax(self.result(state,child,player), self.getEnemyPlayer(player), depth-1,runningMax,runningMin)[0] + 1
                if childScore > best:
                    best = childScore
                    bestMove = child

                runningMax = max(runningMax,childScore)
                if childScore >= runningMin:
                    break
                
        
        return best, bestMove

    def play(self, state):
        game_over = False
        turn = 1
        while not game_over:
            self.display(state)
            if turn == 1:

                print("PLAYER 1")

                move_text = input("Which piece would you like to move where?")

                move = tuple(map(int, move_text.split(',')))
                
                if move in self.actions(state, (move[0], move[1])):
                    self.make_move(state, move)

                    while len(self.actions(state, (move[2], move[3]))) > 0 and self.jump_move(state, move) and self.jump_move(state, self.actions(state, (move[2], move[3]))[0]):
                        jump = tuple(input("Which jump would you like to make?"))
                
                        if jump in self.actions(state, (move[2], move[3])):
                            self.make_move(state, move)
                            move = jump
                        else:
                            print('you must jump with the piece at (', move[2], ',', move[3], ')')

                    turn = 2
                else:
                    print('not a valid move; try again')

                if self.winning_move('r'):
                    print("Player 1 wins!")
                    game_over = True

            else:

                print("AI")
                val, move = self.minimax(state, 'b', 10)
                if move in self.actions(state, (move[0], move[1])):
                    self.make_move(state, move)

                    while len(self.actions(state, (move[2], move[3]))) > 0 and self.jump_move(state, move) and self.jump_move(state, self.actions(state, (move[2], move[3]))[0]):
                        val, jump = self.minimax(state, 'b', 10)

                        if jump in self.actions(state, (move[2], move[3])):
                            self.make_move(state, move)
                            move = jump
                        else:
                            print('you must jump with the piece at (', move[2], ',', move[3], ')')

                    turn = 1
                else:
                    print('not a vaild move; try again')

                if self.winning_move('b'):
                    print("AI wins!")
                    game_over = True

            if self.terminal_test(state,'b'):
                game_over = True
        self.display(state)

game = CheckersGame()
game.play(game.initial)