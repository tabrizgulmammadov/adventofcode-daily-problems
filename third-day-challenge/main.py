MAX_OPERANDS_LENGTH = 7
MUL_STARTING_LENGTH = 4


def find_valid_mul_part1() -> int:
    with open("part1-input.txt", "r") as input_file:
        expression = input_file.read()
        total = 0
        index = 0
        while index < len(expression):
            product, _, parenthesize_end_in = find_valid_mul_operands(expression, index)
            total += product
            index = parenthesize_end_in + 1
        return total


def find_valid_mul_part2() -> int:
    with open("part2-input.txt", "r") as input_file:
        expression = input_file.read()

        enable_cond_indexes = find_indexes_by_condition(expression, "do()")
        disable_cond_indexes = find_indexes_by_condition(expression, "don't()")

        enable_cond_indexes.sort()
        disable_cond_indexes.sort()

        total = 0
        index = 0
        while index < len(expression):
            product, parenthesize_start_in, parenthesize_end_in = find_valid_mul_operands(expression, index)
            # if product is after disable condition
            if product and len(disable_cond_indexes) > 0 and parenthesize_start_in > disable_cond_indexes[0]:
                # if enable condition exist and is after disable condition
                # we remove disable condition index and consider product in total sum
                if len(enable_cond_indexes) > 0 and parenthesize_start_in >= enable_cond_indexes[0] > \
                        disable_cond_indexes[0]:
                    disable_cond_indexes.pop(0)
                    total += product
                # we remove enable condition index if its index is after disable condition index
                if len(enable_cond_indexes) > 0 and len(disable_cond_indexes) > 0 and parenthesize_start_in >= \
                        disable_cond_indexes[0] > enable_cond_indexes[0]:
                    enable_cond_indexes.pop(0)
            else:
                total += product
            index = parenthesize_end_in + 1
        return total


def find_valid_mul_operands(expression: str, start: int) -> (int, int, int):
    try:
        # find start and indexes for operands
        mul_start_index = expression.index("mul(", start) + MUL_STARTING_LENGTH
        mul_end_index = expression.index(")", mul_start_index)

        # if the length of the expression of operands expression
        # then there are some invalid characters
        if mul_end_index - mul_start_index > MAX_OPERANDS_LENGTH:
            return 0, mul_start_index, mul_start_index

        operands = expression[mul_start_index:mul_end_index]
        first, second = operands.split(",")
        if first.isdigit() and second.isdigit():
            return int(first) * int(second), mul_start_index, mul_end_index
        # if operands are not valid, then we will look at the remaining part of the expression
        return 0, mul_start_index, mul_end_index
    except ValueError:
        # this means that there is not any valid substring
        return 0, start, start + MAX_OPERANDS_LENGTH


def find_indexes_by_condition(expression: str, condition: str) -> list[int]:
    indexes = []
    try:
        start = 0
        while start < len(expression):
            index = expression.index(condition, start)
            indexes.append(index)
            start = index + len(condition)
    except ValueError:
        return indexes


if __name__ == "__main__":
    print(find_valid_mul_part2())
