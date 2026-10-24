# 8 Puzzle Problem using DFS and IDS

GOAL = ()


def display(state):
    for i in range(0, 9, 3):
        print("  ", state[i], state[i + 1], state[i + 2])


def get_moves(state):
    moves = []
    zero = state.index(0)
    row, col = divmod(zero, 3)

    directions = [
        (-1, 0, "UP"),
        (1, 0, "DOWN"),
        (0, -1, "LEFT"),
        (0, 1, "RIGHT")
    ]

    for dr, dc, direction in directions:
        r, c = row + dr, col + dc

        if 0 <= r < 3 and 0 <= c < 3:
            pos = r * 3 + c
            new_state = list(state)

            new_state[zero], new_state[pos] = (
                new_state[pos], new_state[zero]
            )

            moves.append((tuple(new_state), direction))

    return moves


# Depth First Search
def dfs(start, limit=20):
    stack = [(start, [start], [])]
    visited = {start}

    while stack:
        state, path, directions = stack.pop()

        if state == GOAL:
            return path, directions

        if len(directions) < limit:
            for next_state, move in get_moves(state):
                if next_state not in visited:
                    visited.add(next_state)

                    stack.append((
                        next_state,
                        path + [next_state],
                        directions + [move]
                    ))

    return None, None


# Depth Limited Search for IDS
def dls(state, path, directions, limit):
    if state == GOAL:
        return path, directions

    if len(directions) == limit:
        return None, None

    for next_state, move in get_moves(state):
        if next_state not in path:
            result = dls(
                next_state,
                path + [next_state],
                directions + [move],
                limit
            )

            if result[0] is not None:
                return result

    return None, None


# Iterative Deepening Search
def ids(start, max_limit=30):
    for limit in range(max_limit + 1):
        path, directions = dls(start, [start], [], limit)

        if path is not None:
            return path, directions

    return None, None


# Check whether the puzzle can reach the goal
def solvable(start, goal):
    def inversions(state):
        nums = [n for n in state if n != 0]
        count = 0

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] > nums[j]:
                    count += 1

        return count

    return inversions(start) % 2 == inversions(goal) % 2


# Main Program
print("=" * 40)
print("       8 PUZZLE PROBLEM")
print("          DFS AND IDS")
print("=" * 40)

print("\nEnter INITIAL state (0 = blank tile)")
start = tuple(map(int, input("Enter 9 numbers: ").split()))

print("\nEnter GOAL state (0 = blank tile)")
goal = tuple(map(int, input("Enter 9 numbers: ").split()))

if (len(start) != 9 or sorted(start) != list(range(9))
        or len(goal) != 9 or sorted(goal) != list(range(9))):

    print("\nInvalid input!")
    print("Enter numbers 0 to 8 exactly once in each state.")

elif not solvable(start, goal):
    print("\nNo solution exists for these initial and goal states.")

else:
    GOAL = goal

    print("\nChoose Algorithm")
    print("1. Depth First Search (DFS)")
    print("2. Iterative Deepening Search (IDS)")

    choice = input("Enter choice (1/2): ")

    if choice == "1":
        path, directions = dfs(start)
        name = "DFS"

    elif choice == "2":
        path, directions = ids(start)
        name = "IDS"

    else:
        path, directions = None, None
        name = ""

    if not name:
        print("Invalid choice!")

    elif path is None:
        print("\nSolution not found within the depth limit.")

    else:
        print("\nSolution using", name)
        print("Total moves:", len(directions))

        for i, state in enumerate(path):
            if i == 0:
                print("\nInitial State:")
            else:
                print("\nMove", i, ":", directions[i - 1])

            display(state)

        print("\nGoal State Reached!")
