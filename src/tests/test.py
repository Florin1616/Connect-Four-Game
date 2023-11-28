import unittest
from src.domain.board import ConnectFour
from src.repository.repository import RepoGame, RepoException
import random

class TestRepoGame(unittest.TestCase):
    def setUp(self):
        self.repo = RepoGame()


    def test_get_valid_columns(self):
        # Test that the function returns the expected list of valid columns
        valid_columns = self.repo.get_valid_columns()
        self.assertEqual(valid_columns, list(range(7)))


    def test_display_board(self):
        # Test that the display_board() function returns an instance of the ConnectFour class
        board = self.repo.display_board()
        self.assertIsInstance(board, ConnectFour)

    def test_get_board(self):
        # Test that the get_board() function returns the expected list of lists
        board = self.repo.get_board()
        self.assertEqual(board, [[""] * 7 for _ in range(6)])

    def test_is_any_move_available_on_column(self):
        # Test that the function returns the expected tuple when there is a move available on the column
        move = random.randint(1, 7)
        row, column = self.repo.is_any_move_available_on_column(move)
        self.assertEqual((row, column), (5, move - 1))

        # Test that the function raises a RepoException when there is no move available on the column
        for i in range(6):
            self.repo.player_move(1)
        self.assertRaises(RepoException, self.repo.is_any_move_available_on_column, 1)

    def test_player_move(self):
        # Test that the player_move() function correctly updates the board
        move = random.randint(1, 7)
        self.repo.player_move(move)
        board = self.repo.get_board()
        self.assertEqual(board[5][move - 1], "X")

    def test_is_player_close_to_winning(self):
        # Test that the function returns the expected blocking move when the player is close to winning
        # vertically
        self.repo._data[2][2] = "X"
        self.repo._data[3][2] = "X"
        self.repo._data[4][2] = "X"
        self.assertEqual(self.repo.is_player_close_to_winning(), 2)


