import unittest
from src.sudoku_solver import (
    find_empty_cell,
    is_valid,
    solve_sudoku,
    is_solved_correctly
)

class TestSudokuSolver(unittest.TestCase):

    def setUp(self):
        # An example puzzle with a known solution
        self.board = [
            [7, 8, 0, 4, 0, 0, 1, 2, 0],
            [6, 0, 0, 0, 7, 5, 0, 0, 9],
            [0, 0, 0, 6, 0, 1, 0, 7, 8],
            [0, 0, 7, 0, 4, 0, 2, 6, 0],
            [0, 0, 1, 0, 5, 0, 9, 3, 0],
            [9, 0, 4, 0, 6, 0, 0, 0, 5],
            [0, 7, 0, 3, 0, 0, 0, 1, 2],
            [1, 2, 0, 0, 0, 7, 4, 0, 0],
            [0, 4, 9, 2, 0, 6, 0, 0, 7],
        ]

    def test_find_empty_cell(self):
        # We expect at least one empty cell
        row_col = find_empty_cell(self.board)
        self.assertIsNotNone(row_col, "There should be at least one empty cell")

    def test_is_valid(self):
        # Testing a simple scenario
        # Let's check row=0, col=2 (which is 0) => is it valid to put 3 there?
        self.assertTrue(is_valid(self.board, 0, 2, 3), "3 should be valid at (0,2) in the sample puzzle")
        # Let's check if 7 is valid at (0,2) => it's in the row already
        self.assertFalse(is_valid(self.board, 0, 2, 7), "7 should not be valid at (0,2) in the sample puzzle")

    def test_solve_sudoku(self):
        solved = solve_sudoku(self.board)
        self.assertTrue(solved, "The puzzle should be solvable.")
        self.assertTrue(is_solved_correctly(self.board), "After solve_sudoku, the board should be valid.")

if __name__ == "__main__":
    unittest.main()
