import sys

EMPTY = '.'
GUARD = "^"
OBSTACLE = "#"
VISITED = "X"


def find_visited_area_by_guard_part1():
    with open("part1-input.txt", "r") as input_file:
        area = [list(line) for line in input_file.read().splitlines()]

    rows = len(area)
    cols = len(area[0])
    sys.setrecursionlimit(rows * cols)

    guard_pos = None
    for row in range(rows):
        for col in range(cols):
            if area[row][col] == GUARD:
                guard_pos = (row, col)

    # directions -> up     right    down    left
    directions: list[tuple[int, int]] = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    def mark_visited_area(curr_row, curr_col, direction: tuple):
        if curr_row < 0 or curr_row >= rows or curr_col < 0 or curr_col >= cols:
            return
        if area[curr_row][curr_col] == VISITED:
            mark_visited_area(curr_row + direction[0], curr_col + direction[1], direction)
            return
        if area[curr_row][curr_col] == OBSTACLE:
            # if the current cell contains '#' character (obstacle), then we go back to the previous cell
            # after we change direction
            curr_row -= direction[0]
            curr_col -= direction[1]
            direction = directions[(directions.index(direction) + 1) % len(directions)]

        area[curr_row][curr_col] = VISITED
        mark_visited_area(curr_row + direction[0], curr_col + direction[1], direction)

    mark_visited_area(guard_pos[0], guard_pos[1], directions[0])
    visited_count = sum(1 for row in area for col in row if col == VISITED)
    return visited_count


def find_visited_area_by_guard_part2():
    with open("part2-input.txt", "r") as input_file:
        area = [list(line) for line in input_file.read().splitlines()]

    rows = len(area)
    cols = len(area[0])
    sys.setrecursionlimit(rows * cols)

    guard_pos = None
    for row in range(rows):
        for col in range(cols):
            if area[row][col] == GUARD:
                guard_pos = (row, col)

    # directions -> up     right    down    left
    directions: list[tuple[int, int]] = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    def mark_visited_area(curr_row, curr_col, direction: tuple):
        if curr_row < 0 or curr_row >= rows or curr_col < 0 or curr_col >= cols:
            return
        if area[curr_row][curr_col] == VISITED:
            mark_visited_area(curr_row + direction[0], curr_col + direction[1], direction)
            return
        if area[curr_row][curr_col] == OBSTACLE:
            # if the current cell contains '#' character (obstacle), then we go back to the previous cell
            # after we change direction
            curr_row -= direction[0]
            curr_col -= direction[1]
            direction = directions[(directions.index(direction) + 1) % len(directions)]

        area[curr_row][curr_col] = VISITED
        mark_visited_area(curr_row + direction[0], curr_col + direction[1], direction)

    def patrol_loop(curr_pos: tuple[int, int], next_pos: tuple[int, int]) -> bool:
        curr_row, curr_col = curr_pos
        next_row, next_col = next_pos
        visited = set()
        while True:
            visited.add((curr_row, curr_col, next_row, next_col))
            if curr_row + next_row < 0 or curr_row + next_row >= rows or curr_col + next_col < 0 or curr_col + next_col >= cols:
                break
            if area[curr_row + next_row][curr_col + next_col] == OBSTACLE:
                # we change direction to the right
                next_row, next_col = next_col, -next_row
            else:
                curr_row += next_row
                curr_col += next_col
            if (curr_row, curr_col, next_row, next_col) in visited:
                return True
        return False

    mark_visited_area(guard_pos[0], guard_pos[1], directions[0])
    visited_positions = [(row, col) for row in range(len(area)) for col in range(len(area[row])) if area[row][col] == VISITED]
    next_row, next_col = -1, 0
    adding_obstacles = 0
    for row, col in visited_positions:
        area[row][col] = OBSTACLE
        # we always start from the first position of the guard
        if patrol_loop(guard_pos, (next_row, next_col)):
            adding_obstacles += 1
        area[row][col] = EMPTY
    return adding_obstacles


if __name__ == '__main__':
    print(find_visited_area_by_guard_part2())
