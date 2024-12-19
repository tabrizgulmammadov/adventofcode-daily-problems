def find_valid_operations(input_file: str, is_part2: bool = False):
    with open(input_file, "r") as input_file:
        lines = [[int(line.split(": ")[0]), line.split(": ")[1]] for line in input_file.read().splitlines()]

    operations = []
    for result, operands_as_str in lines:
        operations.append((result, list(map(int, operands_as_str.split()))))

    valid_operations_sum = 0
    for operation in operations:
        if is_valid_operation(operation, is_part2):
            valid_operations_sum += operation[0]
    return valid_operations_sum


def is_valid_operation(operation: tuple[int, list[int]], is_part2: bool) -> bool:
    target, operands = operation
    # Use a set to avoid duplicate results
    current_results = set([operands[0]])

    for operand in operands[1:]:
        next_results = set()
        for res in current_results:
            # Add both possible operations (+ and *) if they don't exceed the target
            if res + operand <= target:
                next_results.add(res + operand)
            if res * operand <= target:
                next_results.add(res * operand)
            if is_part2 and int(f'{res}{operand}') <= target:
                next_results.add(int(f'{res}{operand}'))
        # If no new results are generated, the operation cannot reach the target
        if not next_results:
            return False
        current_results = next_results

    return target in current_results


if __name__ == '__main__':
    print(find_valid_operations("part2-input.txt", True))
