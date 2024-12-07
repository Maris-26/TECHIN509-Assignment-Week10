import unittest
from models.board import Board

class TestCheckWinner(unittest.TestCase):
    def test_row_winner(self): # 3X in one row
        board = Board()
        board.grid = [['X', 'X', 'X'], ['O', 'O', ' '], [' ', ' ', ' ']]
        self.assertEqual(board.check_winner(), 'X')

    def test_column_winner(self): # 3X in one colum
        board = Board()
        board.grid = [['X', 'O', ' '], ['X', 'O', ' '], ['X', ' ', ' ']]
        self.assertEqual(board.check_winner(), 'X')

    def test_diagonal_winner(self): # 3X in one diagonal
        board = Board()
        board.grid = [['X', 'O', ' '], [' ', 'X', 'O'], [' ', ' ', 'X']]
        self.assertEqual(board.check_winner(), 'X')

    def test_no_winner(self): # no winner, game not finish yet
        board = Board()
        board.grid = [['X', 'O', ' '], [' ', 'X', ' '], ['X', ' ', 'O']]
        self.assertEqual(board.check_winner(), '')

    def test_full_board_draw(self): # no winner, game finish
        board = Board()
        board.grid = [['X', 'O', 'X'], ['O', 'X', 'O'], ['O', 'X', 'O']]
        self.assertEqual(board.check_winner(), '')

if __name__ == '__main__':
    unittest.main()