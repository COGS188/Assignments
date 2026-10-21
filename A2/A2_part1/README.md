# COGS 188 Winter 2025 Assignment 2: Constraint Satisfaction Problems

In this assignment, you will implement two classic constraint satisfaction problems:

* A Connect Four solver using Minimax with Alpha-Beta pruning.
* A Sudoku solver using backtracking.

You will fill in the incomplete starter code for each solver, focusing on the core logic of the puzzle’s constraints.

---

## 1. Installation & Setup

The code in this assignment requires:

- **Python 3.8 or later**
- **NumPy**
- **Pygame**
- **Argparse**

Install these libraries (if not already installed):

```bash
pip install numpy pygame argparse
```

We recommend running the code on your local machine rather than DataHub because the Pygame GUI used for visualization won't work well on remote servers.

---

## 2. Repository Structure

The assignment looks like this:

```plaintext
└── src
    ├── __init__.py
    ├── connect_four_solver.py (Starter Code) 
    └── sudoku_solver.py (Starter Code) 
└── tests
    ├── test_connect_four_solver.py
    └── test_sudoku_solver.py
├── connect_four_gui.py 
└── README.md (this file)
```

### `connect_four_solver.py` (Starter Code)

This file contains skeletons of several functions needed to implement a Connect Four solver using the Minimax algorithm. You must fill in each `TODO`-marked function with your logic. The file also provides constants for row count and column count.

You will find functions such as:

* `create_board`
* `drop_piece`
* `is_valid_location`
* `get_next_open_row`
* `winning_move`
* `get_valid_locations`
* `is_terminal_node`
* `score_position` (ALREADY IMPLEMENTED FOR YOU)
* `minimax`

Each function’s docstring states the expected input and output format. For instance, `create_board` returns a numpy 2D array, while `drop_piece` modifies the board in-place.

**Important**: Do not rename these functions or remove any required arguments or change the return types. The autograder relies on these exact names and signatures.

### `sudoku_solver.py` (Starter Code)

This file contains skeletons of functions for solving a 9x9 Sudoku puzzle using backtracking. You will see placeholder (`# TODO:`) comments instructing you to fill in:

* `find_empty_cell`
* `is_valid`
* `solve_sudoku`
* `is_solved_correctly`

The function `print_board` is already implemented as an example of how you might display a Sudoku board. You may create any additional helper functions if needed, but do not modify the function signatures of the required methods. The autograder will look for them specifically by name.

### `connect_four_gui.py`
This file uses Pygame to provide a GUI for testing your Connect Four solver. It allows you to play Connect Four either against another human or against the AI (which calls your minimax function). You do not need to modify `connect_four_gui.py`, and it will not be graded directly. It is only for local testing.

To run the GUI:

```
python connect_four_gui.py human
```

(for human vs. human play) or

```
python connect_four_gui.py ai
```

(for human vs. AI play).

You can also specify an optional command-line argument --depth if you want to control the AI’s search depth for the minimax algorithm. For example:

```bash
python connect_four_gui.py ai --depth 4
```

Note that a larger depth will make the AI stronger but slower.

---

## 3. Task Summary

### Connect Four Solver

In `connect_four_solver.py`, implement these core functions (where marked with `TODO`):

1. `create_board`: Returns a numpy 2D array of shape (`ROW_COUNT`, `COLUMN_COUNT`) initialized to 0.
2. `drop_piece`: Modifies the board in-place by putting the given piece (1 or 2) into the specified row and column.
3. `is_valid_location`: Checks whether a piece can be dropped in the given column (i.e., the top cell of that column is still 0).
4. `get_next_open_row`: Returns the lowest row index (0-based from the top in the array) where a piece can be placed in that column.
5. `winning_move`: Returns `True` if the given piece (1 or 2) has four in a row horizontally, vertically, or diagonally.
6. `get_valid_locations`: Returns a list of columns where the player can still drop a piece.
7. `is_terminal_node`: Returns `True` if the game has ended (either someone has won or the board is full).
8. `score_position` (ALREADY IMPLEMENTED): A simple scoring heuristic that rewards having pieces in the center column.
9. `minimax`: Implements the Minimax algorithm with alpha-beta pruning. Returns the best column to drop a piece and the corresponding score.

**Inputs**

For each function, read the docstring carefully to see what parameters are provided and in what format. Typically, you’ll receive a numpy array for the board and integer parameters for rows, columns, or piece identifiers.

**Outputs**

Some functions return a Boolean (e.g., `winning_move`), others return list of valid columns, and others modify the board in-place with no return. Make sure you return exactly what the docstring specifies.

### Sudoku Solver

In `sudoku_solver.py`, fill in the four key functions:

* `find_empty_cell`: Scans the 9x9 board (list of lists) for a cell containing 0. Returns (row, col) or None if there is no empty cell.
* `is_valid`: Checks if a given number can be placed at (row, col) without violating the row, column, or 3x3 sub-grid constraints.
* `solve_sudoku`: Uses backtracking. Searches for an empty cell, tries the digits 1–9 in that cell, and recurses. Returns True if the puzzle is solvable.
* `is_solved_correctly`: Verifies that the board is a valid, fully solved Sudoku (each row, column, and 3x3 box contains numbers 1 through 9 exactly once).

**Inputs**

The board is a list of lists of integers, where 0 represents an empty cell.

**Outputs**

Each function’s docstring clarifies whether it returns a boolean, tuple, or modifies the board in-place.

---

## 4. Testing Locally

This section provides guidance on how to test your implementations locally before submitting to Gradescope.

### Connect Four Testing

1. You can test your functions by running `connect_four_gui.py`:

```bash
python connect_four_gui.py ai
```

2. Observe if the AI (your minimax) makes valid moves and eventually wins or loses as expected.
   
3. You can also add print statements or test your functions directly in a separate Python file.

### Sudoku Testing

1. A debugging scenario is included in the `if __name__ == __"main"__` block of `sudoku_solver.py`. After implementing your functions, enter the `src` directory and run:

```
python sudoku_solver.py
```

2. It will print an example Sudoku, try to solve it, then check if the solution is correct.

3. You may also create your own Sudoku puzzles or test partial progress to confirm correctness.

4. Feel free to modify the example sudoku in the `sudoku_solver.py` file to test your solver on different puzzles.

### Running Test Cases

We have provided test cases in the `tests` directory. You can run them using the following command:

```bash
python -m unittest discover -s tests
```

Just like what you've seen in previous labs, this command will run all the test cases in the `tests` directory. These tests are mainly sanity checks that ensure that the functions give the right output format and do not crash. You should also write your own test cases to ensure that your functions are working as expected.

---

## 5. Submitting to Gradescope

* Upload `connect_four_solver.py` AND `sudoku_solver.py` to Gradescope under the A2 assignment.
* Ensure your implementations are inside the provided function stubs and that you have not modified the function signatures.
* Wait for the autograder to run.
* The autograder will run basic test cases and show partial results. Additional hidden tests will be revealed after the due date.