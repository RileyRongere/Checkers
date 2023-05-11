    # returns a list of tuples that describe possible locations to move a piece
    def actions(self, state, piece_loc): # piece_loc should be a touple containing 2 ints
        valid_moves = []
        team = state[piece_loc[0]][piece_loc[1]]
        # if piece is red
        if team == 'r':
            # up-right diagnal jump
            if  self.is_valid_location(state, piece_loc[0]+2, piece_loc[1]+2) and \
                    state[piece_loc[0]+1][piece_loc[1]+1] == self.getEnemyPlayer and \
                    state[piece_loc[0]+2][piece_loc[1]+2] == '.': # next space is enemy, double is in bounds, double is empty
                valid_moves.append((piece_loc[0]+2, piece_loc[1]+2))

            # up-left diagnal jump
            if self.is_valid_location(state, piece_loc[0]+2, piece_loc[1]-2) and \
                    state[piece_loc[0]+1][piece_loc[1]-1] == self.getEnemyPlayer and \
                    state[piece_loc[0]+2][piece_loc[1]-2] == '.': # next space is enemy, double is in bounds, double is empty
                valid_moves.append((piece_loc[0]+2, piece_loc[1]-2))

            # if king
            if state[piece_loc[0]][piece_loc[1]] == team.upper():
                # down-right diagnal jump
                if self.is_valid_location(state, piece_loc[0]-2, piece_loc[1]+2) and \
                        state[piece_loc[0]-1][piece_loc[1]+1] == self.getEnemyPlayer and \
                        state[piece_loc[0]-2][piece_loc[1]+2] == '.': # next space is enemy, double is in bounds, double is empty
                    valid_moves.append((piece_loc[0]-2, piece_loc[1]+2))

                # down-left diagnal jump
                if self.is_valid_location(state, piece_loc[0]-2, piece_loc[1]-2) and \
                        state[piece_loc[0]-1][piece_loc[1]-1] == self.getEnemyPlayer and \
                        state[piece_loc[0]-2][piece_loc[1]-2] == '.': # next space is enemy, double is in bounds, double is empty
                    valid_moves.append((piece_loc[0]-2, piece_loc[1]-2))

            # if there are jump moves, return just jump moves, otherwise continue
            if valid_moves:
                return valid_moves
            

            # up-right diagnal
            if self.is_valid_location(state, piece_loc[0]+1, piece_loc[1]+1) and \
                    state[piece_loc[0]+1][piece_loc[1]+1] == '.': # in bounds and empty
                valid_moves.append((piece_loc[0]+1, piece_loc[1]+1))

            # up-left diagnal
            if self.is_valid_location(state, piece_loc[0]+1, piece_loc[1]-1) and \
                    state[piece_loc[0]+1][piece_loc[1]-1] == '.': # in bounds and empty
                valid_moves.append((piece_loc[0]+1, piece_loc[1]-1))

            # if king
            if state[piece_loc[0]][piece_loc[1]] == team.upper():
                # down-right diagnal
                if self.is_valid_location(state, piece_loc[0]-1, piece_loc[1]+1) and \
                        state[piece_loc[0]-1][piece_loc[1]+1] == '.': # in bounds and empty
                    valid_moves.append((piece_loc[0]-1, piece_loc[1]+1))

                # down-left diagnal
                if self.is_valid_location(state, piece_loc[0]-1, piece_loc[1]-1) and \
                        state[piece_loc[0]-1][piece_loc[1]-1] == '.': # in bounds and empty
                    valid_moves.append((piece_loc[0]-1, piece_loc[1]-1))    


        # if piece is black  
        else:
            # down-right diagnal jump
            if self.is_valid_location(state, piece_loc[0]-2, piece_loc[1]+2) and \
                    state[piece_loc[0]-1][piece_loc[1]+1] == self.getEnemyPlayer and \
                    state[piece_loc[0]-2][piece_loc[1]+2] == '.': # next space is enemy, double is in bounds, double is empty
                valid_moves.append((piece_loc[0]-2, piece_loc[1]+2))

            # down-left diagnal jump
            if self.is_valid_location(state, piece_loc[0]-2, piece_loc[1]-2) and \
                    state[piece_loc[0]-1][piece_loc[1]-1] == self.getEnemyPlayer and \
                    state[piece_loc[0]-2][piece_loc[1]-2] == '.': # next space is enemy, double is in bounds, double is empty
                valid_moves.append((piece_loc[0]-2, piece_loc[1]-2))

            # if king
            if state[piece_loc[0]][piece_loc[1]] == team.upper():
                # up-right diagnal jump
                if self.is_valid_location(state, piece_loc[0]+2, piece_loc[1]+2) and \
                        state[piece_loc[0]+1][piece_loc[1]+1] == self.getEnemyPlayer and \
                        state[piece_loc[0]+2][piece_loc[1]+2] == '.': # next space is enemy, double is in bounds, double is empty
                    valid_moves.append((piece_loc[0]+2, piece_loc[1]+2))

                # up-left diagnal jump
                if self.is_valid_location(state, piece_loc[0]+2, piece_loc[1]-2) and \
                        state[piece_loc[0]+1][piece_loc[1]-1] == self.getEnemyPlayer and \
                        state[piece_loc[0]+2][piece_loc[1]-2] == '.': # next space is enemy, double is in bounds, double is empty
                    valid_moves.append((piece_loc[0]+2, piece_loc[1]-2))
        
            # if there are jump moves, return just jump moves, otherwise continue
            if valid_moves:
                return valid_moves
            
            # down-right diagnal
            if self.is_valid_location(state, piece_loc[0]-1, piece_loc[1]+1) and \
                    state[piece_loc[0]-1][piece_loc[1]+1] == '.': # in bounds and empty
                valid_moves.append((piece_loc[0]-1, piece_loc[1]+1))

            # down-left diagnal
            if self.is_valid_location(state, piece_loc[0]-1, piece_loc[1]-1) and \
                    state[piece_loc[0]-1][piece_loc[1]-1] == '.': # in bounds and empty
                valid_moves.append((piece_loc[0]-1, piece_loc[1]-1))

            # if king
            if state[piece_loc[0]][piece_loc[1]] == team.upper():
                # up-right diagnal
                if self.is_valid_location(state, piece_loc[0]+1, piece_loc[1]+1) and \
                        state[piece_loc[0]+1][piece_loc[1]+1] == '.': # in bounds and empty
                    valid_moves.append((piece_loc[0]+1, piece_loc[1]+1))

                # up-left diagnal
                if self.is_valid_location(state, piece_loc[0]+1, piece_loc[1]-1) and \
                        state[piece_loc[0]+1][piece_loc[1]-1] == '.': # in bounds and empty
                    valid_moves.append((piece_loc[0]+1, piece_loc[1]-1))

        return valid_moves