def part1(input):
    pairs = [list(map(int, line.split())) for line in input.splitlines()]
    left = sorted([pair[0] for pair in pairs])
    right = sorted([pair[1] for pair in pairs])
    return sum(abs(right[i] - left[i]) for i in range(len(pairs)))


def part2(input):
    pairs = [list(map(int, line.split())) for line in input.splitlines()]
    left = [pair[0] for pair in pairs]
    right = [pair[1] for pair in pairs]

    sums_of_right_occurrences = {
        left_value: right.count(left_value) for left_value in set(left)
    }
    return sum(left_value * sums_of_right_occurrences[left_value] for left_value in left)


if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read()
        print(f"part1: {part1(input)}")
        print(f"part2: {part2(input)}")
