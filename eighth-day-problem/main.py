def find_antinodes_part1():
    with open('part1-input.txt', "r") as input_file:
        lines = input_file.read().splitlines()

    board = [list(line) for line in lines]
    antennas = []  # (row, column, frequency)
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] != ".":
                antennas.append((row, col, board[row][col]))

    antinodes = set()
    rows = len(board)
    cols = len(board[0])

    # Process all pairs of antennas
    for i, (row1, col1, freq1) in enumerate(antennas):
        for j, (row2, col2, freq2) in enumerate(antennas):
            if i <= j or freq1 != freq2:
                continue  # Skip self-pairs and different frequencies

            dist_row = row2 - row1
            dist_col = col2 - col1

            # Add middle antinode (if evenly divisible distances)
            if abs(dist_row) % 2 == 0 and abs(dist_col) % 2 == 0:
                mid_row = row1 + dist_row // 2
                mid_col = col1 + dist_col // 2
                antinodes.add((mid_row, mid_col))

            if 0 <= row1 - dist_row < rows and 0 <= col1 - dist_col < cols:
                antinodes.add((row1 - dist_row, col1 - dist_col))
            if 0 <= row2 + dist_row < rows and 0 <= col2 + dist_col < cols:
                antinodes.add((row2 + dist_row, col2 + dist_col))

    return len(antinodes)

def find_antinodes_part2():
    with open('part2-input.txt', "r") as input_file:
        lines = input_file.read().splitlines()

    board = [list(line) for line in lines]
    antennas = []  # (row, column, frequency)
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] != ".":
                antennas.append((row, col, board[row][col]))

    antinodes = set()
    rows = len(board)
    cols = len(board[0])

    # Process all pairs of antennas
    for i, (row1, col1, freq1) in enumerate(antennas):
        for j, (row2, col2, freq2) in enumerate(antennas):
            if i <= j or freq1 != freq2:
                continue  # Skip self-pairs and different frequencies

            dist_row = row2 - row1
            dist_col = col2 - col1

            # Include positions of the antennas themselves as antinodes
            antinodes.add((row1, col1))
            antinodes.add((row2, col2))

            # Add middle antinode for (if evenly divisible distances)
            if abs(dist_row) % 2 == 0 and abs(dist_col) % 2 == 0:
                mid_row = row1 + dist_row // 2
                mid_col = col1 + dist_col // 2
                antinodes.add((mid_row, mid_col))

            # Extend antinodes in both directions along the line
            times = 1
            while True:
                new_row = row1 - dist_row * times
                new_col = col1 - dist_col * times
                if 0 <= new_row < rows and 0 <= new_col < cols:
                    antinodes.add((new_row, new_col))
                else:
                    break
                times += 1

            # Forward direction from row2, col2
            times = 1
            while True:
                new_row = row2 + dist_row * times
                new_col = col2 + dist_col * times
                if 0 <= new_row < rows and 0 <= new_col < cols:
                    antinodes.add((new_row, new_col))
                else:
                    break
                times += 1

    return len(antinodes)


if __name__ == "__main__":
    print(find_antinodes_part2())
