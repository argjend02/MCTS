class Node(state, parent=None):
    # Represents a single state in the game tree.
    # Each node corresponds to a game state in Tic-Tac-Toe.
    
    - state: Current board configuration
    - parent: Reference to the parent node (None for root)
    - children: List of child nodes (initially empty)
    - visits: Number of times this node was visited (initially 0)
    - value: Total score accumulated from simulations (initially 0)

    function is_fully_expanded():
        # A node is fully expanded if all possible moves have been explored.
        return number of children == number of legal moves from state

    function best_child(exploration_weight):
        # Selects the best child node using the Upper Confidence Bound (UCT) formula:
        # UCT = (win_score / visits) + exploration_weight * sqrt(log(parent.visits) / child.visits)
        return child with highest value based on:
            (child.value / child.visits) + exploration_weight * sqrt(log(parent.visits) / child.visits)


function MCTS(root, iterations):
    # Runs Monte Carlo Tree Search for a given number of iterations.
    # The goal is to determine the best move from the current game state.

    for i = 1 to iterations:
        node = selection(root)  // Step 1: Select the best node to expand
        new_node = expansion(node)  // Step 2: Expand the node by adding a new child
        result = simulation(new_node)  // Step 3: Simulate a random game from the new node
        backpropagation(new_node, result)  // Step 4: Backpropagate the result up the tree

    return best_move(root)  // After iterations, return the best move based on visit count


function selection(node):
    # Selects the most promising node to expand using UCT formula.
    
    while node has children and node is fully expanded:
        node = best_child(node, exploration_weight)  // Traverse tree using UCT formula

    return node  // Return the best node to expand


function expansion(node):
    # Expands the current node by adding a new child for an unexplored move.

    legal_moves = get_legal_moves(node.state)  // Get all possible moves from current state
    for each move in legal_moves:
        if move is not in node’s children:
            new_state = apply_move(node.state, move)  // Apply move to get a new board state
            new_node = new Node(new_state, parent=node)  // Create a new node for this state
            add new_node to node.children  // Attach new node to current node
            return new_node  // Return the newly created node

    return node  // If all moves are already expanded, return the same node


function simulation(node):
    # Simulates a random playout (game) starting from the given node.
    # Random moves are played until the game ends (win/loss/draw).

    current_state = copy(node.state)  // Copy board state to avoid modifying original
    while game is not over:
        move = random move from get_legal_moves(current_state)  // Pick a random legal move
        current_state = apply_move(current_state, move)  // Apply the move to update state

    return get_result(current_state)  // Return outcome of simulation (1 for win, 0 for draw, -1 for loss)


function backpropagation(node, result):
    # Updates node statistics after a simulation result is obtained.
    # The result is backpropagated up the tree to inform parent nodes.

    while node is not NULL:
        node.visits += 1  // Increment visit count
        node.value += result  // Update value with simulation result (1, 0, or -1)
        node = node.parent  // Move to the parent node


function best_move(root):
    # After all MCTS iterations, return the best move.
    # The best move is the child with the highest visit count.

    return child of root with highest visit count


# Utility Functions (Game-Specific Logic)

function get_legal_moves(state):
    # Returns a list of valid moves for the given board state.
    return list of all possible empty positions on the board

function apply_move(state, move):
    # Applies a move to the board and returns the new state.
    return new state after placing X or O at the given position

function is_terminal(state):
    # Checks if the game has ended.
    return True if there is a win, loss, or draw; False otherwise

function get_result(state):
    # Determines the result of the game.
    # Returns 1 if the AI wins, 0 for a draw, -1 if the opponent wins.
    return 1 if win, 0 if draw, -1 if loss
