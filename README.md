# MCTS
# Monte Carlo Tree Search (MCTS) for Tic-Tac-Toe AI

# Project Overview

This project implements a Monte Carlo Tree Search (MCTS) algorithm to create an AI that plays Tic-Tac-Toe efficiently. MCTS is a decision-making algorithm widely used in games like Chess, Go, and other AI-driven applications. The goal of this project is to explore how MCTS can be applied to Tic-Tac-Toe and evaluate its performance.

# What is Monte Carlo Tree Search (MCTS)?

MCTS is a probabilistic search algorithm used for decision-making in games and planning problems. It works by simulating multiple possible moves and selecting the one with the highest expected success rate. MCTS consists of four main steps:

Selection: Start from the root node and traverse the tree using the Upper Confidence Bound (UCT) formula.

Expansion: If the current node is not a terminal state, expand by adding a new child node.

Simulation (Rollout): Perform random simulations from the new node until the game ends.

Backpropagation: Update node statistics based on the result of the simulation.

MCTS is useful because it does not require predefined heuristics and can adapt to different game states dynamically.

# Why Use MCTS for Tic-Tac-Toe?

While Tic-Tac-Toe is a relatively simple game, using MCTS allows us to:

Explore AI decision-making in a controlled environment.

Understand how MCTS performs in small-scale games.

Compare MCTS-based AI to traditional rule-based or minimax AI strategies.

# Complexity Analysis

# Time Complexity

The time complexity of MCTS depends on four key steps: Selection, Expansion, Simulation, and Backpropagation.

Selection:

The selection process involves traversing the tree using the UCT formula.

In a balanced tree with N nodes, the traversal depth is proportional to log N.

Time Complexity: O(log N) per iteration

Expansion:

In the worst case, we expand all possible child nodes.

Tic-Tac-Toe has at most 9 possible moves, reducing as the game progresses.

Time Complexity: O(1) per expansion (since the branching factor is small).

Simulation:

Each simulation plays a random game until a terminal state is reached.

The maximum number of moves in Tic-Tac-Toe is 9.

Time Complexity: O(1) per simulation (bounded by the game's move limit).

Backpropagation:

Updates the values of all nodes along the selection path.

In a balanced tree, this is proportional to the depth: O(log N).

 Overall Time Complexity:

Since MCTS runs for M iterations, each requiring O(log N) for selection and backpropagation, the total complexity is:

O(M log N)

Best-Case Complexity:

If an immediate winning move is found, MCTS can terminate early.

Best case: O(1) (constant time if the game ends quickly).

Worst-Case Complexity:

In cases where MCTS explores a large number of moves before convergence, the complexity is O(M log N).

Average-Case Complexity:

MCTS typically converges to a good move before reaching all nodes, so practical performance is closer to O(M log N) but often much faster than exhaustive search.

# Space Complexity

MCTS stores a tree of visited states, requiring memory proportional to the number of stored nodes.

Node Storage: Each node stores board state, visit count, value, and child nodes.

Max Possible Nodes: Tic-Tac-Toe has at most 9! ≈ 362880 board states (far fewer with pruning).

Typical Case: Since MCTS does not store all possible states, practical space usage is much lower.

Overall Space Complexity:

O(N), where N is the number of stored nodes.

Optimizations:

Pruning: Removing unpromising branches to reduce N.

Transposition Tables: Reusing states to avoid duplicate storage.

# Comparative Analysis: MCTS vs. Minimax

3.1 Minimax Algorithm

Time Complexity: O(b^d), where b is the branching factor and d is depth.

Space Complexity: O(d), as it only stores the current path.


![Screenshot 2025-03-23 at 3 27 27 PM](https://github.com/user-attachments/assets/7997e442-4d1a-4985-9d6a-21342df63f7c)

# Refined Design

The following changes aim to improve the efficiency and effectiveness of the Monte Carlo Tree Search (MCTS) algorithm for the Tic-Tac-Toe AI:

 # Optimized Selection Strategy

To strike a better balance between exploration and exploitation, we propose dynamically adjusting the exploration weight during the algorithm's execution. Early in the search, we increase the exploration weight to explore the tree more thoroughly, while later, we reduce it to focus on the most promising moves. This adaptation will ensure the algorithm explores enough of the search space while avoiding excessive computation on less relevant paths.

 # Improved Simulation Strategy

Instead of relying on completely random rollouts, we suggest incorporating heuristics that can guide the simulation phase more intelligently. By using simple strategies such as center control, blocking the opponent's moves, and detecting winning moves, we can make the rollouts more reflective of good decision-making. This refinement ensures that simulations are more accurate, which will ultimately help the algorithm make better decisions.

 #  Efficient Data Structures

To enhance the efficiency of the algorithm, we recommend using hash tables to store previously encountered states. This will prevent redundant calculations and unnecessary recomputations, improving both time and space efficiency. Storing computed states will allow for faster lookups and reduce memory usage, making the algorithm more scalable for larger search spaces.

These refined strategies will optimize the MCTS algorithm's performance, particularly in terms of execution time and decision quality.

# Control Flow Graph for MCTS


![CFG](https://github.com/user-attachments/assets/2baab250-ee0e-4f9a-9489-3423423500e4)

Start: MCTS begins.
Selection: Traverses the tree using the UCT formula.
Expansion: Adds a new node if possible.
Simulation: Runs a random playout to estimate the outcome.
Backpropagation: Updates values from the simulation back to the root.
Loop: If more iterations are needed, it returns to Selection.
Best Move: When all iterations are completed, it selects the best move.
End: The process stops.
