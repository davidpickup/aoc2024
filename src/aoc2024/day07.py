def _is_valid(test_value, operands, operators):
    if len(operands) == 1:
        return test_value == operands[0]
    return any(
        _is_valid(
            test_value, [operator(operands[0], operands[1])] + operands[2:], operators
        )
        for operator in operators
    )


def part1(input):
    """Determine which values can be produced with inserted operators, and sum them."""
    tests = {
        int(test_value): list(map(int, operands.split(" ")))
        for test_value, operands in map(lambda x: x.split(": "), input.splitlines())
    }
    return sum(
        test_value
        for test_value, operands in tests.items()
        if _is_valid(test_value, operands, [lambda x, y: x + y, lambda x, y: x * y])
    )


def part2(input):
    """Determine which values can be produced with inserted operators, and sum them."""
    tests = {
        int(test_value): list(map(int, operands.split(" ")))
        for test_value, operands in map(lambda x: x.split(": "), input.splitlines())
    }
    return sum(
        test_value
        for test_value, operands in tests.items()
        if _is_valid(
            test_value,
            operands,
            [lambda x, y: x + y, lambda x, y: x * y, lambda x, y: int(str(x) + str(y))],
        )
    )


if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read()
        print(f"part1: {part1(input)}")
        print(f"part2: {part2(input)}")
