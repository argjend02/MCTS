import random
import math

class Node:
    """
    Represents a single state (node) in the Tic-Tac-Toe game tree.
    """
    def __init__(self, state, parent=None):
        self.state = state  # Current board state
        self.parent = parent  # Parent node
        self.children = []  # List of child nodes
        self.visits = 0  # Number of times this node has been visited
        self.value = 0  # Value of the node (win/loss score)

    def is_fully_expanded(self):
        """Checks if all possible moves have been explored from this node."""
        return len(self.children) == len(get_legal_moves(self.state))

    def best_child(self, exploration_weight=1.41):
        """
        Selects the best child node using the Upper Confidence Bound (UCT) formula:
        UCT = (win_score / visits) + exploration_weight * sqrt(log(parent.visits) / visits)
        """
        return max(self.children, key=lambda x: x.value / (x.visits + 1e-6) +
                   exploration_weight * math.sqrt(math.log(self.visits + 1) / (x.visits + 1e-6)))

# Monte Carlo Tree Search (MCTS) Implementation

def MCTS(root, iterations=1000):
    """
    Runs the MCTS algorithm for a given number of iterations to determine the best move.
    """
    for _ in range(iterations):
        node = selection(root)  # Step 1: Selection
        new_node = expansion(node)  # Step 2: Expansion
        result = simulation(new_node)  # Step 3: Simulation (Rollout)
        backpropagation(new_node, result)  # Step 4: Backpropagation
    return best_move(root)

def selection(node):
    """Traverses the tree using the UCT formula to find the best node to expand."""
    while node.children and node.is_fully_expanded():
        node = node.best_child()
    return node

def expansion(node):
    """
    Expands the node by creating a new child node for an unexplored move.
    """
    legal_moves = get_legal_moves(node.state)
    for move in legal_moves:
        if not any(child.state == move for child in node.children):  # Ensure unique moves
            new_state = apply_move(node.state, move)
            new_node = Node(new_state, parent=node)
            node.children.append(new_node)
            return new_node
    return node  # If no new move is possible, return the same node

def simulation(node):
    """
    Simulates a random playout from the given node until the game ends.
    Returns the result (1 for win, 0 for draw, -1 for loss).
    """
    current_state = node.state.copy()
    while not is_terminal(current_state):
        move = random.choice(get_legal_moves(current_state))  # Play a random move
        current_state = apply_move(current_state, move)
    return get_result(current_state)

def backpropagation(node, result):
    """
    Updates the node and its ancestors with the simulation result.
    """
    while node:
        node.visits += 1
        node.value += result  # 1 for win, 0 for draw, -1 for loss
        node = node.parent

def best_move(root):
    """
    Selects the move with the highest visit count after MCTS iterations.
    """
    return max(root.children, key=lambda x: x.visits).state