from Game import *
import math

NUMBER_OF_ROWS = 8
NUMBER_OF_COLS = 8

class ConnectFourGame(Game) :

    def __init__(self) :
        self.initial = [['.'] * NUMBER_OF_COLS for _ in range(NUMBER_OF_ROWS)]



    def display(self, state):
        """Print or otherwise display the state."""
        print()
        for row in range(NUMBER_OF_ROWS-1,-1,-1):
            print("|\t",end='')
            for col in range(NUMBER_OF_COLS):
                print(state[row][col],"\t", end="")
            print("|")

        print("-----------------------------------------------------------------")
        print("\t0\t1\t2\t3\t4\t5\t6 ")
        
    def drop_piece(self, state, row, col, piece):
        state[row][col] = piece

    def is_valid_location(self, state, col):
        if col <0 or col >= NUMBER_OF_COLS:
            return False
        else:
            return state[NUMBER_OF_ROWS - 1][col] == '.'

    def get_next_open_row(self, state, col):
        for r in range(NUMBER_OF_ROWS):
            if state[r][col] == '.':
                return r
        return NUMBER_OF_ROWS

    def winning_move(self, board, piece):
        # Check horizontal locations for win
        for c in range(NUMBER_OF_COLS - 3):
            for r in range(NUMBER_OF_ROWS):
                if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][
                    c + 3] == piece:
                    return True

        # Check vertical locations for win
        for c in range(NUMBER_OF_COLS):
            for r in range(NUMBER_OF_ROWS - 3):
                if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][
                    c] == piece:
                    return True

        # Check positively sloped diaganols
        for c in range(NUMBER_OF_COLS - 3):
            for r in range(NUMBER_OF_ROWS - 3):
                if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and \
                        board[r + 3][c + 3] == piece:
                    return True

        # Check negatively sloped diaganols
        for c in range(NUMBER_OF_COLS - 3):
            for r in range(3, NUMBER_OF_ROWS):
                if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and \
                        board[r - 3][c + 3] == piece:
                    return True
        return False

    def terminal_test(self, state):
        return self.winning_move(state, "x") or self.winning_move(state, "o") or len(self.actions(state)) == 0


    def getEnemyPlayer(self,player):
        # return the opposite of player
        if player == 'x':
            return 'o'
        else:
            return 'x'


    def undo(self, state, move):
        row = self.get_next_open_row(state, move)
        state[row-1][move] = '.'
        return state



    def actions(self, state):
        # returns list of numbers corresponding to possible moves        
        
        # TO DO        
        # YOUR CODE ...
        valid_locations = []
        for col in range(NUMBER_OF_COLS):
            #if self.get_next_open_row(state,col) < NUMBER_OF_COLS:
            if self.is_valid_location(state, col):
                valid_locations.append(col)
        return valid_locations


    def result(self, state, move, player):
        """Return the state that results from making a move from a state."""
        # TO DO
        # YOUR CODE ...
        row = self.get_next_open_row(state, move)        
        #self.drop_piece(self, state, row, move, player)
        state[row][move] = player
        return state


    def utility(self, state, player):
        """Return the value of this final state to player."""
        
        # TO DO
        # YOUR CODE ...
        if self.winning_move(state, 'o') == True:
            return +1
        elif self.winning_move(state, 'x') == True:
            return -1
        else:
            return 0



    def alphabeta(self, state, depth, alpha, beta, player, bestMove):
        
        if self.terminal_test(state) or depth == 0:
            return self.utility(state, player), bestMove
        

        if player == 'o':
            value = -10000
            for col in self.actions(state):
                # child = self.drop_piece(state, self.get_next_open_row(state,col),col,player)
                state = self.result(state, col, 'o')
                #value = max(value, self.alphabeta(state, depth-1, alpha, beta, 'o', bestMove)[0])
                cur_val, cur_move = self.alphabeta(state, depth-1, alpha, beta, 'x', bestMove)
                state = self.undo(state, col)
                
                if cur_val > value:
                    value    = cur_val
                    bestMove = col
                    

                if value > beta: 
                    return value, bestMove
                if value > alpha:
                    alpha = max(alpha, value)
                    bestMove = col
            return value, bestMove
        else:
            value = 10000
            for col in self.actions(state):
                # child = self.drop_piece(state, self.get_next_open_row(state,col),col,player)
                '''state = self.result(state, col, player)
                value = min(value, self.alphabeta(state, depth-1, alpha, beta, 'x', bestMove)[0])
                state = self.undo(state, col)'''
                
                state = self.result(state, col, 'x')
                cur_val, cur_move = self.alphabeta(state, depth-1, alpha, beta, 'o', bestMove)
                state = self.undo(state, col)
                
                if cur_val < value:
                    value = cur_val
                    bestMove = col

                
                
                
                
                if value < alpha:
                    return value, bestMove
                

                if value < beta:
                    beta = min(beta, value)
                    bestMove = col


            return value, bestMove       


    def play(self, state):
        game_over = False
        turn = 2
        while not game_over:
            self.display(state)
            if turn == 1:
                print("PLAYER 1")
                col = int(input("Where to drop a piece?"))
                if self.is_valid_location(state, col):
                    row = self.get_next_open_row(state, col)
                    self.drop_piece(state, row, col, 'x')
                    turn = 2
                else:
                    print('not a valid location; try again')

                if self.winning_move(state, 'x'):
                    print("Player 1 wins!")
                    game_over = True

            else:

                print("AI")
                #val, col = self.minimax(state, "o", 4)
                
                val, col = self.alphabeta(state, 4, -math.inf, math.inf, 'o', -1)
                if self.is_valid_location(state, col):
                    row = self.get_next_open_row(state, col)
                    self.drop_piece(state, row, col, 'o')
                    turn = 1
                else:
                    print('not a vaild location; try again')

                if self.winning_move(state, 'o'):
                    print("AI wins!")
                    game_over = True

            if self.terminal_test(state):
                game_over = True
        self.display(state)





# 2 player game
#play the game
game = ConnectFourGame()
game.play(game.initial)