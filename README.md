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