import math
import heapq

goal = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]

def precompute_goal_positions(goal):
    positions = {}
    for index, value in enumerate(goal):
        row = index // 4
        col = index % 4
        positions[value] = (row, col)
    return positions

def is_within_range(number, n):
    return 0 <= number < n*n  # Fixed range condition

def get_manhattan_distance(current, positions):
    sum = 0
    for i in range(len(current)):
        if current[i] != 0:
            current_row, current_col = i // 4, i % 4
            target_row, target_col = positions[current[i]]
            sum += abs(current_row - target_row) + abs(current_col - target_col)
    return sum

class Node:
    def __init__(self, current_state, parent_node, current_step, total_cost, switcher_index):
        self.current_state = current_state
        self.parent_node = parent_node
        self.current_step = current_step
        self.total_cost = total_cost  # Ensure this is an integer
        self.switcher_index = switcher_index

    def __lt__(self, other):
        return self.total_cost < other.total_cost

    def __repr__(self):
        return f"Node(current_state={self.current_state}, current_step={self.current_step}, total_cost={self.total_cost})"

def generate_states(current, n):
    i = current.index(0)
    result = []
    possible_moves = []

    if i % n > 0:  # Left
        possible_moves.append(i - 1)
    if i % n < n - 1:  # Right
        possible_moves.append(i + 1)
    if i - n >= 0:  # Up
        possible_moves.append(i - n)
    if i + n < n * n:  # Down
        possible_moves.append(i + n)

    for pos in possible_moves:
        new_state = current.copy()
        new_state[i], new_state[pos] = new_state[pos], new_state[i]
        result.append({
            'state': new_state,
            'switcher_index': pos
        })

    return result

def get_a_star_result(start, goal):
    step = 0
    check_set = set()
    queue = []
    goal_positions = precompute_goal_positions(goal)

    initial_node = Node(start, None, step, get_manhattan_distance(start, goal_positions), None)
    heapq.heappush(queue, initial_node)
    check_set.add(tuple(start))

    while queue:
        next_node = heapq.heappop(queue)
        next_state = next_node.current_state

        if next_state == goal:
            print("done")
            return construct_backwards(next_node, [])

        state_objs = generate_states(next_state, 4)

        for obj in state_objs:
            state_tuple = tuple(obj['state'])
            if state_tuple not in check_set:
                check_set.add(state_tuple)
                distance = get_manhattan_distance(obj['state'], goal_positions)
                total_cost = next_node.current_step + 1 + distance
                new_node = Node(obj['state'], next_node, next_node.current_step + 1, total_cost, obj['switcher_index'])
                heapq.heappush(queue, new_node)

    return None

def construct_backwards(node, final_list):
    if node.current_step == 0:
        return final_list[::-1]
    final_list.append(node.switcher_index)
    return construct_backwards(node.parent_node, final_list)

def solution(position):
    return get_a_star_result(position, goal)

print(solution([5, 1, 4, 8, 9, 6, 3, 11, 10, 2, 15, 7, 13, 14, 12, 0]))
