class ServiceGame:
    def __init__(self, repo, user_input_val):
        self._repo = repo
        self._user_input_validator = user_input_val
        #self._user_move_validator = user_move_validator

    def display_board(self):
        return self._repo.display_board()

    def get_first_position_that_is_free_on_the_column(self, move):
        board = self._repo.get_board()
        for row in reversed(range(6)):
            if board[row][move] == "":
                return row

    def check_winner(self, current_player):
        positions_needed_to_win = 4
        board = self._repo.get_board()
        player = current_player
        computer = -current_player
        for row in range(6):
            for column in range(7):
                player_count = 0
                computer_count = 0
                directions = self._repo.get_directions()
                #Search for player win
                if board[row][column] == "X":
                    player_count += 1

                    #Search in all 8 directions for a similar piece

                    for element in range(len(directions)):
                        direction = directions[element]
                        position_to_check_row = row + direction[0]
                        position_to_check_column = column + direction[1]

                        if position_to_check_row < 6 and position_to_check_column < 7:
                            count = 1

                            while True:
                                position_to_check_row = row + direction[0] * count
                                position_to_check_column = column + direction[1] * count

                                count += 1

                                if 0 <= position_to_check_row < 6 and 0 <= position_to_check_column < 7:
                                    if board[position_to_check_row][position_to_check_column] == "X":
                                        player_count += 1
                                    else:
                                        break
                                else:
                                    break
                        if player_count >= positions_needed_to_win:
                            return 1
                        player_count = 1

                #Search for computer win
                if board[row][column] == "0":
                    computer_count = 1

                    for element in range(len(directions)):
                        direction = directions[element]
                        position_to_check_row = row + direction[0]
                        position_to_check_column = column + direction[1]

                        if position_to_check_row < 6 and position_to_check_column < 7:
                            count = 1

                            while True:
                                position_to_check_row = row + direction[0] * count
                                position_to_check_column = column + direction[1] * count

                                count += 1

                                if 0 <= position_to_check_row < 6 and 0 <= position_to_check_column < 7:
                                    if board[position_to_check_row][position_to_check_column] == "0":
                                        computer_count += 1
                                    else:
                                        break
                                else:
                                    break
                        if computer_count >= positions_needed_to_win:
                            return -1
                        computer_count = 1


        valid_moves = self._repo.get_valid_columns()
        if len(valid_moves) == 0:
            return 0

    def get_all_valid_moves(self):
        valid_moves = []
        board = self._repo.get_board
        for row in range(6):
            for column in range(7):
                if board[row][column] == "":
                    valid_moves.append([row,column])
        return valid_moves


    def computer_move(self):
        self._repo.computer_move()


    def player_move(self, move):
        self._user_input_validator.validate_command(move)
        self._repo.player_move(int(move))