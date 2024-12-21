from collections import deque

STARTING_POINT = '0'
ENDING_POINT = '9'


def find_total_score_part1():
    with open("part1-input.txt", "r") as input_file:
        topographic_map = input_file.read().strip().split("\n")

    rows = len(topographic_map)
    cols = len(topographic_map[0])

    score = 0
    for row in range(rows):
        for col in range(cols):
            if topographic_map[row][col] == STARTING_POINT:
                # we have to store visited cells with distance separately for each starting point
                queue = deque([(0, row, col)]) # queue -> (distance, row, col)
                seen = set() # visited cells
                while queue:
                    distance, prev_row, prev_col = queue.popleft()
                    if (prev_row, prev_col) in seen:
                        continue
                    seen.add((prev_row, prev_col))
                    if topographic_map[prev_row][prev_col] == ENDING_POINT:
                        score += 1
                    # directions        up      down    left     right
                    for direction in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        next_row, next_col = prev_row + direction[0], prev_col + direction[1]
                        if 0 <= next_row < rows and 0 <= next_col < cols and int(topographic_map[next_row][next_col]) == int(topographic_map[prev_row][prev_col]) + 1:
                            queue.append((distance + 1, next_row, next_col))
    return score


def find_total_score_part2():
    with open("part2-input.txt", "r") as input_file:
        topographic_map = input_file.read().strip().split("\n")

    rows = len(topographic_map)
    cols = len(topographic_map[0])

    cached = {}
    def find_ways(row, col):
        if topographic_map[row][col] == STARTING_POINT:
            return 1
        if (row, col) in cached:
            return cached[(row, col)]
        answer = 0
        # directions         up     down    left    right
        for direction in [(-1, 0), (0, 1), (1, 0), (0, -1)]: # (row, col)
            new_row = row + direction[0]
            new_col = col + direction[1]
            if 0 <= new_row < rows and 0 <= new_col < cols and int(topographic_map[new_row][new_col]) == int(topographic_map[row][col]) - 1:
                answer += find_ways(new_row, new_col)
        cached[(row, col)] = answer
        return answer

    score = 0
    for row in range(rows):
        for col in range(cols):
            # we calculate score with iterating from end ('9') to start ('0')
            if topographic_map[row][col] == ENDING_POINT:
                score += find_ways(row, col)

    return score


if __name__ == "__main__":
    print(find_total_score_part2())
