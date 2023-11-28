from src.domain.board import ConnectFour
import random

class RepoException(Exception):
    pass
class RepoGame:
    def __init__(self):
        self._data = []
        self.rows = 6
        self.columns = 7
        self.directions = {
            0: (-1, -1),
            1: (-1, 0),
            2: (-1, 1),
            3: (0, -1),
            4: (0, 1),
            5: (1, -1),
            6: (1, 0),
            7: (1, 1)
        }
        for row in range(self.rows):
            self._data.append([""] * self.columns)

    def get_valid_columns(self):
        #return the list of all valid moves
        valid_columns = []
        for column in range(7):
            # is_at_least_one_valid_position_on_the_column = False
            for row in range(6):
                if self._data[row][column] == "":
                    if column not in valid_columns:
                        valid_columns.append(column)
        return valid_columns


    def display_board(self):
        board = ConnectFour(self.rows,self.columns,self._data)
        return board

    def get_board(self):
        return self._data


    def is_any_move_available_on_column(self, column):
        is_there_any_move_to_make_on_this_column = False
        for row in reversed(range(6)):
            if self._data[row][column - 1] == "":
                return row, column - 1
        if is_there_any_move_to_make_on_this_column == False:
            raise RepoException("There is no space on this column to make another move  ! ")


    def player_move(self, move):
        row, column = self.is_any_move_available_on_column(move)
        self._data[row][column] = "X"


    def is_player_close_to_winning(self):
        """
        This function determines if the player is close to winning(has three consecutive tokens
        horizontally, vertically, or diagonally
        :return: The position where the computer should place its token in order to prevent the player from winning
        """
        board = self.get_board()

        blocking_move = -1
        #CHECK ON COLUMN
        for column in range(7):
            for row in range(5,2,-1):
                if (board[row][column] == "X" and board[row-1][column] == "X" and board[row-2][column] == "X" and board[row-3][column] == ""):
                    blocking_move = column
                    return blocking_move

        #CHECK ON LINE
        for row in reversed(range(6)):
            for column in range(0,4):
                if (board[row][column] == "X" and board[row][column + 1] == "X" and board[row][column + 2] == "X" and board[row][column + 3] == ""): # XXX
                    if row != 5:
                        if board[row + 1][column + 3] != "":
                            blocking_move = column + 3
                            return blocking_move
                    else:
                        blocking_move = column + 3
                        return blocking_move

                elif (board[row][column] == "X" and board[row][column + 1] == "" and board[row][column + 2] == "X" and board[row][column + 3] == "X"): #X XX
                    if row != 5:
                        if board[row + 1][column + 1] != "":
                            blocking_move = column + 1
                            return blocking_move
                    else:
                        blocking_move = column + 1
                        return blocking_move
                elif (board[row][column] == "X" and board[row][column + 1] == "X" and board[row][column + 2] == "" and board[row][column + 3] == "X"): #xx x
                    if row != 5:
                        if board[row + 1][column + 2] != "":
                            blocking_move = column + 2
                            return blocking_move
                    else:
                        blocking_move = column + 2
                        return blocking_move

        #CHECK ON SESCOND DIAGONAL
        for row in range(5, 2, -1):
            for column in range(4):
                if (board[row][column] == "X" and board[row - 1][column + 1] == "X" and board[row - 2][column + 2] == "X" and board[row -3 ][column + 3] == "") :
                    if board[row - 2 ][column + 3] != "":
                        blocking_move = column + 3
                        return blocking_move
                elif (board[row][column] == "X" and board[row - 1][column + 1] == "" and board[row - 2][column + 2] == "X" and board[row -3 ][column + 3] == "X") :
                    if board[row][column + 1] != "":
                        blocking_move = column + 1
                        return blocking_move
                elif (board[row][column] == "X" and board[row - 1][column + 1] == "X" and board[row - 2][column + 2] == "" and board[row -3 ][column + 3] == "X") :
                    if board[row - 1 ][column + 2] != "":
                        blocking_move = column + 2
                        return blocking_move
        #CHECK ON MAIN DIAGONAL
        for row in range(5, 2, -1):
            for column in range(6, 2, -1):
                if (board[row][column] == "X" and board[row - 1][column - 1] == "X" and board[row - 2][column - 2] == "X" and board[row - 3][column - 3] == ""):
                    if board[row - 2][column - 3] != "":
                        blocking_move = column - 3
                        return blocking_move
                elif (board[row][column] == "X" and board[row - 1][column - 1] == "" and board[row - 2][column - 2] == "X" and board[row - 3][column - 3] == "X"):
                    if board[row][column - 1] != "":
                        blocking_move = column - 1
                        return blocking_move
                elif (board[row][column] == "X" and board[row - 1][column - 1] == "X" and board[row - 2][column - 2] == "" and board[row - 3][column - 3] == "X"):
                    if board[row - 1][column - 2] != "":
                        blocking_move = column - 2
                        return blocking_move


        return blocking_move

    def is_computer_close_to_winning(self):
        board = self.get_board()

        winning_move = -1
        #CHECK ON COLUMN
        for column in range(7):
            for row in range(5,2,-1):
                if (board[row][column] == "0" and board[row-1][column] == "0" and board[row-2][column] == "0" and board[row-3][column] == ""):
                    winning_move = column
                    return winning_move
        #CHECK ON LINE
        for row in reversed(range(6)):
            for column in range(0,4):
                if (board[row][column] == "0" and board[row][column + 1] == "0" and board[row][column + 2] == "0" and board[row][column + 3] == ""):
                    if row != 5:
                        if board[row + 1][column + 3] != "":
                            winning_move = column + 3
                            return winning_move
                    else:
                        winning_move = column + 3
                        return winning_move
                elif (board[row][column] == "0" and board[row][column + 1] == "" and board[row][column + 2] == "0" and board[row][column + 3] == "0"):
                    if row != 5:
                        if board[row + 1][column + 1] != "":
                            winning_move = column + 1
                            return winning_move
                    else:
                        winning_move = column + 1
                        return winning_move
                elif (board[row][column] == "0" and board[row][column + 1] == "0" and board[row][column + 2] == "" and board[row][column + 3] == "0"):
                    if row != 5:
                        if board[row + 1][column + 2] != "":
                            winning_move = column + 2
                            return winning_move
                    else:
                        winning_move = column + 2
                        return winning_move

        #CHECK ON SESCOND DIAGONAL
        for row in range(5, 2, -1):
            for column in range(4):
                if (board[row][column] == "0" and board[row - 1][column + 1] == "0" and board[row - 2][column + 2] == "0" and board[row -3 ][column + 3] == "") :
                    if board[row - 2 ][column + 3] != "":
                        winning_move = column + 3
                        return winning_move
                elif (board[row][column] == "0" and board[row - 1][column + 1] == "" and board[row - 2][column + 2] == "0" and board[row -3 ][column + 3] == "0") :
                    if board[row][column + 1] != "":
                        winning_move = column + 1
                        return winning_move
                elif (board[row][column] == "0" and board[row - 1][column + 1] == "0" and board[row - 2][column + 2] == "" and board[row -3 ][column + 3] == "0") :
                    if board[row - 1 ][column + 2] != "":
                        winning_move = column + 2
                        return winning_move
        #CHECK ON MAIN DIAGONAL
        for row in range(5, 2, -1):
            for column in range(6, 2, -1):
                if (board[row][column] == "0" and board[row - 1][column - 1] == "0" and board[row - 2][column - 2] == "0" and board[row - 3][column - 3] == ""):
                    if board[row - 2][column - 3] != "":
                        winning_move = column - 3
                        return winning_move
                elif (board[row][column] == "0" and board[row - 1][column - 1] == "" and board[row - 2][column - 2] == "0" and board[row - 3][column - 3] == "0"):
                    if board[row][column - 1] != "":
                        winning_move = column - 1
                        return winning_move
                elif (board[row][column] == "0" and board[row - 1][column - 1] == "0" and board[row - 2][column - 2] == "" and board[row - 3][column - 3] == "0"):
                    if board[row - 1][column - 2] != "":
                        winning_move = column - 2
                        return winning_move

        return winning_move

    def computer_move(self):
        board = self.get_board()

        blocking_player_move = self.is_player_close_to_winning()
        winning_move_for_computer = self.is_computer_close_to_winning()

        if blocking_player_move != -1:
            row, column = self.is_any_move_available_on_column(blocking_player_move + 1) #in functia is any move scad -1 din coloana
            self._data[row][column] = "0"
        elif winning_move_for_computer != -1:
            row, column = self.is_any_move_available_on_column(winning_move_for_computer + 1)
            self._data[row][column] = "0"
        else:
            # IF THERE IS NOT ANY WINNING POSSIBLITY FOR THE HUMAN PLAYER OR THE COMPUTER
            valid_columns = self.get_valid_columns()
            move = random.choice(valid_columns)
            row, column = self.is_any_move_available_on_column(move + 1)
            self._data[row][column] = "0"

    def get_directions(self):
        return self.directions