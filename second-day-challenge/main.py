MIN_DIFF = 1
MAX_DIFF = 3


def calculate_diffs_part1() -> int:
    with open("part1-input.txt", "r") as input_file:
        levels = input_file.read().strip().split("\n")
        safe_levels = 0

        for level in levels:
            reports = [int(report) for report in level.split()]
            if is_safe(reports):
                safe_levels += 1

        return safe_levels


def calculate_diffs_part2() -> int:
    with open("part2-input.txt", "r") as input_file:
        levels = input_file.read().strip().split("\n")
        safe_levels = 0

        for level in levels:
            reports = [int(report) for report in level.split()]

            # case 1: current level is safe
            if is_safe(reports):
                safe_levels += 1
                continue

            # case 2: after removing a report from the list,
            # the list of remaining reports is safe
            for index in range(len(reports)):
                if is_safe(reports[:index] + reports[index + 1:]):
                    safe_levels += 1
                    break

        return safe_levels

def is_safe(reports: list[int]) -> bool:
    index = 1
    # we define order of reports
    asc = reports[index] > reports[index - 1]

    while index < len(reports):
        diff = abs(reports[index] - reports[index - 1])
        # if order of reports is not valid or difference exceed limits
        # then reports are not safe
        if (asc and reports[index] < reports[index - 1]) or \
                (not asc and reports[index] > reports[index - 1]) or \
                diff < MIN_DIFF or diff > MAX_DIFF:
            return False
        index += 1

    return True


if __name__ == "__main__":
    print(calculate_diffs_part2())
