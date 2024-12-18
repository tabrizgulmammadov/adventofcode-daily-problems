
SEARCHED_WORD = "XMAS"
def find_word_occurrences_part1():
    with open("part1-input.txt", "r") as input_file:
        lines = input_file.read().splitlines()
        board = [list(line) for line in lines]
        rows = len(board)
        cols = len(board[0])

        found_patterns = set()  # Use a set to prevent duplicates

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "X":
                    find_occurrences(board, row, col, found_patterns)
        return len(found_patterns)


def find_occurrences(board, row, col, found_patterns):
    rows = len(board)
    cols = len(board[0])
    directions = [
        (0, 1),   # Left to right
        (0, -1),  # Right to left
        (1, 0),   # Top to bottom
        (-1, 0),  # Bottom to top
        (1, 1),   # Top-left to bottom-right
        (-1, -1), # Bottom-right to top-left
        (1, -1),  # Top-right to bottom-left
        (-1, 1)   # Bottom-left to top-right
    ]

    for dr, dc in directions:
        pattern = []
        for index in range(len(SEARCHED_WORD)):
            new_row = row + dr * index
            new_col = col + dc * index
            if not (0 <= new_row < rows and 0 <= new_col < cols):
                break
            if board[new_row][new_col] != SEARCHED_WORD[index]:
                break
            pattern.append((new_row, new_col))
        if len(pattern) == len(SEARCHED_WORD):
            found_patterns.add(tuple(sorted(pattern)))  # Use a tuple to ensure immutability and prevent duplicates


SEARCHED_WORDS = ["MAS", "SAM"]
def find_word_occurrences_part2():
    with open("part1-input.txt", "r") as input_file:
        lines = input_file.read().splitlines()
        board = [list(line) for line in lines]
        rows = len(board)
        cols = len(board[0])
        count = 0

        # Iterate through each cell, treating 'A' as the center of the X
        for row in range(1, rows - 1):  # Exclude first and last rows
            for col in range(1, cols - 1):  # Exclude first and last columns
                if board[row][col] == "A":  # Check if the center is 'A'
                    if is_valid_xmas(board, row, col):
                        count += 1
        return count

def is_valid_xmas(board: list[list[str]], row: int, col: int) -> bool:
    # Top-left to bottom-right diagonal
    tl_to_br = board[row - 1][col - 1] + board[row][col] + board[row + 1][col + 1]

    # Bottom-left to top-right diagonal
    bl_to_tr = board[row + 1][col - 1] + board[row][col] + board[row - 1][col + 1]

    # Check if both diagonals are valid "MAS" or "SAM"
    return tl_to_br in SEARCHED_WORDS and bl_to_tr in SEARCHED_WORDS


if __name__ == "__main__":
    print(find_word_occurrences_part2())
