def _is_safe(report):
    """Check elements are sorted, either increasing or decreasing,
        with a difference of 1, 2, or 3 between each element.
    """
    if report[0] < report[-1]:
        report = report[::-1]
    return all(
        report[i] - report[i + 1] in {1, 2, 3}
        for i in range(len(report) - 1)
    )


def _is_safe_2(report):
    """Check if a report is safe, or can be made safe by removing one element."""
    if _is_safe(report):
        return True
    for i in range(len(report)):
        if _is_safe(report[:i] + report[i + 1 :]):
            return True
    return False


def part1(input):
    reports = [list(map(int, line.split())) for line in input.splitlines()]
    return sum(1 for report in reports if _is_safe(report))


def part2(input):
    reports = [list(map(int, line.split())) for line in input.splitlines()]
    return sum(1 for report in reports if _is_safe_2(report))


if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read()
        print(f"part1: {part1(input)}")
        print(f"part2: {part2(input)}")
