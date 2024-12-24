import time

MAX_BLINKS_PART1 = 25
MAX_BLINKS_PART2 = 75

def count_stones_after_blinks(initial_stones, max_blinks):
    # instead of storing all stones, we just store frequencies of stones
    stone_counts = {stone: 1 for stone in initial_stones}

    for _ in range(max_blinks):
        next_counts = {}

        for stone, count in stone_counts.items():
            if stone == "0":
                next_counts["1"] = next_counts.get("1", 0) + count
            elif len(stone) % 2 == 0:
                half_len = len(stone) // 2
                first_half = stone[:half_len]
                second_half = stone[half_len:].lstrip("0") or "0"
                next_counts[first_half] = next_counts.get(first_half, 0) + count
                next_counts[second_half] = next_counts.get(second_half, 0) + count
            else:
                multiplied = str(int(stone) * 2024)
                next_counts[multiplied] = next_counts.get(multiplied, 0) + count

        stone_counts = next_counts

    # Sum up all stone counts
    total_stones = sum(stone_counts.values())
    return total_stones

if __name__ == "__main__":
    with open("input.txt", "r") as input_file:
        initial_stones = input_file.read().split()

    start_time = time.time()
    result = count_stones_after_blinks(initial_stones, MAX_BLINKS_PART1)
    end_time = time.time()

    execution_time = end_time - start_time
    print(f"Execution time: {execution_time:.5f} seconds, result: {result}")
