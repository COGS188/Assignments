# COGS 188 Winter 2025 Assignment 1: Maze Solvers (Graph-Based)

In this assignment, you will implement **five different** search algorithms to find a path in a **randomly generated maze**, **modeled as an undirected graph**. Specifically, you will:

1. **Parse** a 2D NumPy maze into a graph (where each open cell is a `Node`).
2. Implement the following search algorithms on that graph:
   - **A\*** (using the Manhattan distance as a heuristic)  
   - **Simulated Annealing**  
   - **Breadth-First Search (BFS)**  
   - **Depth-First Search (DFS)**  
   - **Bidirectional Search**  

You will write your code in `solver.py`, and you can use `visualizer.py` to visualize how your algorithm explores the maze.  

---

## 1. Installation & Setup

The code in this assignment requires:

- **Python 3.8+**
- **NumPy**
- **Pygame**

Install these libraries (if not already installed):

```bash
pip install numpy pygame
```

We recommend running the code on your local machine rather than DataHub because the Pygame GUI used for visualization won't work well on remote servers.

---

## 2. Repository Structure

The assignment looks like this:

```plaintext
.
├── solver.py        <-- Starter code for your search algorithms
├── visualizer.py    <-- Script for visualizing your maze and solution
├── README.md        <-- This document with instructions
```

### `solver.py` (Starter Code)

This file contains:

* A `Node` class for representing each open cell in the maze as a graph node.
* A function `parse_maze_to_graph(maze)` that converts a 2D NumPy array into a graph of Nodes.
* Five key algorithms you must implement:
  * `astar(start_node, goal_node)`
  * `simulated_annealing(start_node, goal_node, ...)`
  * `bfs(start_node, goal_node)`
  * `dfs(start_node, goal_node)`
  * `bidirectional_search(start_node, goal_node)`
* Each function has a detailed docstring specifying its input (graph `Node` objects) and output (a list of `(row, col)` tuples or `None`).

**Important:**

* Do not rename these functions or remove any of their required arguments/return formats.
* The autograder depends on these exact names/signatures.
* Within `solver.py`, you’ll see placeholder `# TODO:` comments for each function. Insert your implementation there. You may create helper functions if you wish.
* Do not use any external libraries, apart from those imported at the top of the file. You may use any standard Python library (e.g., `math`, `random`, etc.).

### `visualizer.py`

This file uses Pygame to:

* Generate a random maze (a 2D NumPy array) of shape `(GRID_SIZE, GRID_SIZE)`, where `0` = open and `1` = wall.
* Convert this maze into a graph using `parse_maze_to_graph`.
* Run one of the solver algorithms (`astar`, `bfs`, `dfs`, `bidirectional_search`, or `simulated_annealing`) based on a command-line argument (e.g., `python visualizer.py bfs`).
* Draw the maze and, if found, the solution path in blue.
* It also provides two buttons:
   * **New Map**: Generate a new random maze and re-run the solver.
   * **Try Again**: Only appears for Simulated Annealing, letting you re-run it on the same maze (since simulated annealing is stochastic).

You do not need to modify `visualizer.py`. It is only a tool for testing and will not be graded.

---

## 3. Task Summary

In `solver.py`, implement:

* `parse_maze_to_graph(maze)`
* `bfs(start_node, goal_node)`
* `dfs(start_node, goal_node)`
* `astar(start_node, goal_node)`
* `bidirectional_search(start_node, goal_node)`
* `simulated_annealing(start_node, goal_node, temperature=..., cooling_rate=..., min_temperature=...)`

Test Locally:

Use visualizer.py with each algorithm to see if a blue path appears.

For instance:

```
python visualizer.py bfs
```

or

```
python visualizer.py dfs
```

or

```
python visualizer.py astar
```

or

```
python visualizer.py simulated_annealing
```

or

```
python visualizer.py bidirectional
```

Try generating new mazes to confirm the solver still works.

---

## 4. Submitting to Gradescope

* Upload `solver.py` to Gradescope under the A1 assignment.
* **Make sure your filename is `solver.py`. All other filenames will be rejected by the autograder, and you will not receive a grade.**
* Ensure your implementations are inside the provided function stubs.
* Wait for the autograder to run.
* The autograder will run basic test cases and show partial results. Additional hidden tests will be revealed after the due date.

---

## 5. FAQ

Q: Do I need to change the Pygame code in `visualizer.py`?

A: No, you only need to add your logic to `solver.py`. The visualizer is for debugging and demonstration.

Q: My solver returns a path, but no blue squares appear.

A: Make sure you’re returning (row, col) tuples (not (col, row)), and that start and goal are included in your final path.

Q: How do I verify correctness besides the visual output?

A: You can manually check small mazes or rely on the autograder’s tests. A path is valid if each consecutive pair of coordinates is adjacent (differ by 1 in either row or column) and never traverses a wall cell.

Q: Can we add new helper functions or classes?

A: Absolutely. Just do not rename or remove the required five functions, and keep their parameters/returns the same.
