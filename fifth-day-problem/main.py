def find_total_middle_page_numbers_part1():
    with open("part1-input.txt", "r") as input_file:
        content = input_file.read().split("\n\n")

        # define precedence of rules as dictionary
        rules = [list(map(int, rule.split("|"))) for rule in content[0].splitlines()]
        precedence_dict = {}
        for first, second in rules:
            precedence_dict.setdefault(first, []).append(second)

        # define orders
        orders = [list(map(int, order.split(","))) for order in content[1].splitlines()]

        # define correct orders and calculate total of middle page numbers for valid orders
        total = 0
        for order in orders:
            precedence_checks = [second in precedence_dict.get(first, []) for first, second in zip(order, order[1:])]
            if all(precedence_checks):
                total += order[len(order) // 2]
        return total


def find_total_middle_page_numbers_part2():
    with open("part2-input.txt", "r") as input_file:
        content = input_file.read().split("\n\n")

        # define precedence of rules as dictionary
        rules = [list(map(int, rule.split("|"))) for rule in content[0].splitlines()]
        precedence_dict = {}
        for first, second in rules:
            precedence_dict.setdefault(first, []).append(second)

        # define orders
        orders = [list(map(int, order.split(","))) for order in content[1].splitlines()]

        # define correct orders and calculate total of middle page numbers for invalid orders
        total = 0
        for order in orders:
            # Check if the current order is invalid
            is_invalid = False
            for i in range(len(order)):
                for j in range(i + 1, len(order)):
                    if order[i] in precedence_dict.get(order[j], []):
                        is_invalid = True
                        break
                if is_invalid:
                    break

            # If the order is invalid, try to correct it
            if is_invalid:
                # Ensure each element is moved to satisfy precedence rules
                for i in range(len(order)):
                    for j in range(i + 1, len(order)):
                        if order[i] in precedence_dict.get(order[j], []):
                            # Swap to correct the order
                            order[i], order[j] = order[j], order[i]

                # Calculate and add middle page
                total += order[len(order) // 2]

        return total


if __name__ == "__main__":
    print(find_total_middle_page_numbers_part2())
