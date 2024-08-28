import heapq
import math

goal = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]


def is_within_range(number, n):
    return 0 <= number <= n * n - 1


def get_manhattan_distance(current, target):
    sum = 0
    n = len(target)

    for i in range(0, n):
        if current[i] != 0:
            current_row = math.floor(i / 4)
            current_column = i % 4
            goal_index = target.index(current[i])
            target_row = math.floor(goal_index / 4)
            target_column = goal_index % 4
            sum = sum + abs(current_row - target_row) + abs(current_column - target_column)

    return sum


class Node:
    def __init__(self, current_state, parent_node, current_step, total_cost, switcher_index):
        self.current_state = current_state
        self.parent_node = parent_node
        self.current_step = current_step
        self.total_cost = total_cost
        self.switcher_index = switcher_index

    def __lt__(self, other):
        return self.total_cost < other.total_cost

    def __eq__(self, other):
        return self.current_state == other.current_state

    def __gt__(self, other):
        return self.total_cost > other.total_cost

    def __hash__(self):
        return hash(tuple(self.current_state))

    def __repr__(self):
        return f"Node(current_state={self.current_state}, current_step={self.current_step}, parent_state={self.parent_node}, total_cost={self.total_cost}, switcher_index={self.switcher_index})"


def generate_states(current, n):
    i = current.index(0)
    possible_indexes = []
    result = []

    is_top_left_corner = False
    is_bottom_left_corner = False
    is_top_right_corner = False
    is_bottom_right_corner = False
    is_left_edge = False
    is_right_edge = False

    if i == 0:
        is_top_left_corner = True
    if i == n * n - n:
        is_bottom_left_corner = True
    if i == n - 1:
        is_top_right_corner = True
    if i == n * n - 1:
        is_bottom_right_corner = True
    if i % n == 0:
        is_left_edge = True
    if i % n == n - 1:
        is_right_edge = True

    if is_top_left_corner:
        possible_indexes = [i + 1, i + n]
    elif is_bottom_left_corner:
        possible_indexes = [i + 1, i - n]
    elif is_top_right_corner:
        possible_indexes = [i - 1, i + n]
    elif is_bottom_right_corner:
        possible_indexes = [i - 1, i - n]
    elif is_left_edge:
        possible_indexes = [i + 1, i - n, i + n]
    elif is_right_edge:
        possible_indexes = [i - 1, i - n, i + n]
    else:
        possible_indexes = list(filter(lambda number: is_within_range(number, n), [i + 1, i - 1, i - n, i + n]))

    for pos in possible_indexes:
        temp_state = current.copy()
        temp = temp_state[i]
        temp_state[i] = temp_state[pos]
        temp_state[pos] = temp
        obj = {
            'state': temp_state,
            'switcher_index': pos
        }
        result.append(obj)

    return result


def get_a_star_result(start, goal):
    step = 0
    check_set = set()
    queue = []

    initial_node = Node(start, None, step, get_manhattan_distance(start, goal), None)
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
            if tuple(obj['state']) not in check_set:
                check_set.add(tuple(obj['state']))
                distance = get_manhattan_distance(obj['state'], goal)
                new_node = Node(obj['state'], next_node, next_node.current_step + 1,
                                next_node.current_step + 1 + distance, obj['switcher_index'])
                heapq.heappush(queue, new_node)

    return None


def construct_backwards(node, final_list):
    if node.current_step == 0:
        return final_list

    final_list.insert(0, node.switcher_index)
    return construct_backwards(node.parent_node, final_list)


def solution(position):
    return get_a_star_result(position, goal)


print(solution([5, 1, 4, 8, 9, 6, 3, 11, 10, 2, 15, 7, 13, 14, 12, 0]))
