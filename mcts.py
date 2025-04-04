import random
import math
import time

class Node:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent
        self.children = []
        self.visits = 0
        self.value = 0

    def is_fully_expanded(self):
        return len(self.children) == len(get_legal_moves(self.state))

    def best_child(self, exploration_weight=1.41):
        return max(
            self.children,
            key=lambda x: x.value / (x.visits + 1e-6) +
                          exploration_weight * math.sqrt(math.log(self.visits + 1) / (x.visits + 1e-6))
        )

def MCTS(root, iterations=1000):
    for _ in range(iterations):
        node = selection(root)
        new_node = expansion(node)
        result = simulation(new_node)
        backpropagation(new_node, result)
    return best_move(root)

def selection(node):
    while node.children and node.is_fully_expanded():
        node = node.best_child()
    return node

def expansion(node):
    legal_moves = get_legal_moves(node.state)
    for move in legal_moves:
        if not any(child.state == apply_move(node.state, move) for child in node.children):
            new_state = apply_move(node.state, move)
            new_node = Node(new_state, parent=node)
            node.children.append(new_node)
            return new_node
    return node

def simulation(node):
    current_state = node.state[:]
    while not is_terminal(current_state):
        move = random.choice(get_legal_moves(current_state))
        current_state = apply_move(current_state, move)
    return get_result(current_state)

def backpropagation(node, result):
    while node:
        node.visits += 1
        node.value += result
        node = node.parent

def best_move(root):
    return max(root.children, key=lambda x: x.visits).state

# Game logic functions
def get_legal_moves(state):
    return [i for i in range(9) if state[i] == ' ']

def apply_move(state, move):
    new_state = state[:]
    player = 'X' if new_state.count('X') <= new_state.count('O') else 'O'
    new_state[move] = player
    return new_state

def is_terminal(state):
    return get_result(state) is not None

def get_result(state):
    winning_combos = [(0,1,2), (3,4,5), (6,7,8),
                      (0,3,6), (1,4,7), (2,5,8),
                      (0,4,8), (2,4,6)]
    for a, b, c in winning_combos:
        if state[a] == state[b] == state[c] and state[a] != ' ':
            return 1 if state[a] == 'X' else -1
    if ' ' not in state:
        return 0
    return None

def print_board(state):
    for i in range(0, 9, 3):
        print(state[i], '|', state[i+1], '|', state[i+2])
    print("----------------")

# Human vs AI
def play_game():
    state = [' '] * 9
    while not is_terminal(state):
        print_board(state)
        if state.count('X') <= state.count('O'):
            move = int(input("Enter your move (0-8): "))
        else:
            root = Node(state)
            state = MCTS(root, iterations=1000)
            continue
        state = apply_move(state, move)
    print_board(state)
    result = get_result(state)
    if result == 1:
        print("X wins!")
    elif result == -1:
        print("O wins!")
    else:
        print("It's a draw!")

# AI vs AI
def play_game_ai_vs_ai():
    state = [' '] * 9
    while not is_terminal(state):
        print_board(state)
        root = Node(state)
        state = MCTS(root, iterations=1000)
    print_board(state)
    result = get_result(state)
    if result == 1:
        print("X wins!")
    elif result == -1:
        print("O wins!")
    else:
        print("It's a draw!")

# Edge Case Testing
def edge_case_tests():
    print("----- Edge Case 1: Only One Move Left -----")
    state1 = ['X', 'O', 'X',
              'X', 'O', 'O',
              'O', 'X', ' ']  # Only index 8 left
    root1 = Node(state1)
    move1 = MCTS(root1, iterations=500)
    print("Selected move:")
    print_board(move1)

    print("----- Edge Case 2: Immediate Winning Move -----")
    state2 = ['X', 'X', ' ',
              'O', 'O', ' ',
              ' ', ' ', ' ']  # X can win at index 2
    root2 = Node(state2)
    move2 = MCTS(root2, iterations=500)
    print("Selected move:")
    print_board(move2)

    print("----- Edge Case 3: Already Terminal State -----")
    state3 = ['X', 'X', 'X',
              'O', 'O', ' ',
              ' ', ' ', ' ']
    print("Is terminal:", is_terminal(state3))
    print("Result:", get_result(state3))  # Should return 1 (X wins)
def performance_test():
    test_iterations = [100, 500, 1000, 5000]
    state = [' '] * 9  # Start with an empty board

    for iterations in test_iterations:
        print(f"Running MCTS with {iterations} iterations...")
        root = Node(state)
        
        start_time = time.time()
        best_state = MCTS(root, iterations=iterations)
        end_time = time.time()
        
        elapsed_time = end_time - start_time
        print(f"Time taken for {iterations} iterations: {elapsed_time:.4f} seconds")
        print_board(best_state)
        print("-" * 30) 

# ===========================
# Testing Cases 
# ===========================

# Uncomment the one you want to run

# play_game()            # Human vs AI
#  play_game_ai_vs_ai()   # AI vs AI
# edge_case_tests()      # Run edge case test suite

# ===========================
# Uncomment to run the test
# ===========================
performance_test()   
