def calculate_diffs_part1() -> int:
    with open("part1-input.txt", "r") as input_file:
        nums_as_str = input_file.read().split()
        nums = [int(num) for num in nums_as_str]

        left = nums[0::2]
        right = nums[1::2]

        left.sort()
        right.sort()

        total = 0
        for l, r in zip(left, right):
            total += abs(r - l)
        return total

def calculate_diffs_part2() -> int:
    with open("part2-input.txt", "r") as input_file:
        nums_as_str = input_file.read().split()
        nums = [int(num) for num in nums_as_str]

        left = nums[0::2]
        right = nums[1::2]

        total = 0
        for num in left:
            total += right.count(num) * num
        return total

if __name__ == "__main__":
    print(calculate_diffs_part2())