import random
import math
import time
import matplotlib.pyplot as plt

class Node:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent
        self.children = []
        self.visits = 0
        self.value = 0

    def is_fully_expanded(self):
        return len(self.children) == len(get_legal_moves(self.state))

    def best_child(self, exploration_weight=0.5):  # Adjusted exploration weight for balance
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
        new_state = apply_move(node.state, move)
        if not any(child.state == new_state for child in node.children):
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
    best_child = max(root.children, key=lambda x: x.visits)
    for i in range(9):
        if root.state[i] != best_child.state[i]:
            return i

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
            move = MCTS(root, iterations=1000)
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
        move = MCTS(root, iterations=1000)
        state = apply_move(state, move)
    print_board(state)
    result = get_result(state)
    if result == 1:
        print("X wins!")
    elif result == -1:
        print("O wins!")
    else:
        print("It's a draw!")

iterations = [100, 500, 1000, 5000]
times = [0.1, 0.25, 0.35, 1.2]  # Example times in seconds for each iteration count

plt.plot(iterations, times, marker='o')
plt.xlabel('Number of Simulations')
plt.ylabel('Time Taken (s)')
plt.title('Runtime vs. Number of Simulations')
plt.grid(True)
plt.show()        

# Edge Case Testing
def edge_case_tests():
    # print("----- Edge Case 1: Only One Move Left -----")
    # state1 = ['X', 'O', 'X',
    #           'X', 'O', 'O',
    #           'O', 'X', ' ']  # Only index 8 left
    # root1 = Node(state1)
    # move1 = MCTS(root1, iterations=500)
    # final_state1 = apply_move(state1, move1)
    # print_board(final_state1)

    print("----- Edge Case 2: Immediate Winning Move -----")
    state2 = ['X', 'X', ' ',
              'O', 'O', ' ',
              ' ', ' ', ' ']  # X can win at index 2
    root2 = Node(state2)
    move2 = MCTS(root2, iterations=500)
    final_state2 = apply_move(state2, move2)
    print_board(final_state2)

    # print("----- Edge Case 3: Already Terminal State -----")
    # state3 = ['X', 'X', 'X',
    #           'O', 'O', ' ',
    #           ' ', ' ', ' ']
    # print("Is terminal:", is_terminal(state3))
    # print("Result:", get_result(state3))

def performance_test():
    test_iterations = [100, 500, 1000, 5000]
    state = [' '] * 9
    for iterations in test_iterations:
        print(f"Running MCTS with {iterations} iterations...")
        root = Node(state)
        start_time = time.time()
        move = MCTS(root, iterations=iterations)
        end_time = time.time()
        elapsed_time = end_time - start_time
        result_state = apply_move(state, move)
        print(f"Time taken for {iterations} iterations: {elapsed_time:.4f} seconds")
        print_board(result_state)
        print("-" * 30)

def win_rate_test_flip_roles(games=30, low_iter=100, high_iter=1000):
    x_wins = 0
    o_wins = 0
    draws = 0
    for game in range(games):
        state = [' '] * 9
        while not is_terminal(state):
            current_player = 'X' if state.count('X') <= state.count('O') else 'O'
            iter_count = high_iter if (game < games // 2 and current_player == 'X') or (game >= games // 2 and current_player == 'O') else low_iter
            root = Node(state)
            move = MCTS(root, iterations=iter_count)
            state = apply_move(state, move)
        result = get_result(state)
        if result == 1:
            x_wins += 1
        elif result == -1:
            o_wins += 1
        else:
            draws += 1
    print("Games Played:", games)
    print(f"Player X Wins: {x_wins}")
    print(f"Player O Wins: {o_wins}")
    print(f"Draws: {draws}")

# ===========================
# Uncomment one test at a time
# ===========================
# win_rate_test_flip_roles(games=30, low_iter=100, high_iter=1000)

# play_game()
# play_game_ai_vs_ai()
# edge_case_tests()
# performance_test()