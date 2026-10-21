import unittest
import numpy as np

from src.connect_four_solver import (
    create_board,
    drop_piece,
    is_valid_location,
    get_next_open_row,
    winning_move,
    get_valid_locations,
    is_terminal_node,
    score_position,
    minimax,
    ROW_COUNT,
    COLUMN_COUNT
)

class TestSolver(unittest.TestCase):

    def test_create_board(self):
        board = create_board()
        # Check shape
        self.assertEqual(board.shape, (ROW_COUNT, COLUMN_COUNT))
        # Check all zeroes
        self.assertTrue((board == 0).all())

    def test_drop_piece_and_is_valid_location(self):
        board = create_board()
        # Drop piece in column 0
        self.assertTrue(is_valid_location(board, 0))
        row = get_next_open_row(board, 0)
        drop_piece(board, row, 0, 1)
        # The top cell in row=0 col=0 should now be 1
        self.assertEqual(board[0][0], 1)
        # Fill up column 0 to see if it becomes invalid
        for _ in range(ROW_COUNT - 1):
            r = get_next_open_row(board, 0)
            drop_piece(board, r, 0, 1)
        # Now column 0 should not be valid
        self.assertFalse(is_valid_location(board, 0))

    def test_winning_move_horizontal(self):
        board = create_board()
        # Make a horizontal winning move for piece=1
        for col in range(4):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 1)
        self.assertTrue(winning_move(board, 1))

    def test_get_valid_locations(self):
        board = create_board()
        valid_cols = get_valid_locations(board)
        # Initially all columns are valid
        self.assertEqual(len(valid_cols), COLUMN_COUNT)

    def test_is_terminal_node(self):
        board = create_board()
        self.assertFalse(is_terminal_node(board))
        # Fill the board with no winner
        for col in range(COLUMN_COUNT):
            for _ in range(ROW_COUNT):
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, 1 if (col % 2 == 0) else 2)
        # Now the board is full, no winner (if we arranged carefully) => terminal
        self.assertTrue(is_terminal_node(board))

    def test_score_position_center_preference(self):
        board = create_board()
        # Place a piece in the center
        center_col = COLUMN_COUNT // 2
        row = get_next_open_row(board, center_col)
        drop_piece(board, row, center_col, 2)
        # Score should be > 0 for piece 2
        self.assertGreater(score_position(board, 2), 0)

    def test_minimax_return_type(self):
        board = create_board()
        col, value = minimax(board, depth=1, alpha=float('-inf'), beta=float('inf'), maximizingPlayer=True)
        # Minimax should return a tuple (column, value)
        self.assertIsInstance(col, (int, type(None)))
        self.assertIsInstance(value, (int, float))

if __name__ == '__main__':
    unittest.main()
