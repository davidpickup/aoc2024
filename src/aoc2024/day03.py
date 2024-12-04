import re




def part1(input):
    """Find all instances of mul(X,Y), where X and Y are 1-3 digit integers. No other characters are allowed.
    Return the sum of the products of X and Y.
    """
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    matches = re.findall(pattern, input)
    total_sum = sum(int(x) * int(y) for x, y in matches)
    return total_sum


def part2(input):
    """Doesn't sum mul instructions if they follow a 'don't() command, unless there is a more recent do() command."""
    do_pattern = r"do\(\)"
    dont_pattern = r"don't\(\)"
    
    total_sum = 0
    dos = re.split(do_pattern, input)
    for do in dos:
        donts = re.split(dont_pattern, do)
        total_sum += part1(donts[0])

    
    return total_sum


if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read()
        print(f"part1: {part1(input)}")
        print(f"part2: {part2(input)}")
