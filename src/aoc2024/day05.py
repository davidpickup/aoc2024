from collections import defaultdict

def part1(input):
    lines = input.splitlines()
    dependencies = defaultdict(list)
    updates = []

    for line in lines:
        if "|" in line:
            x, y = map(int, line.split("|"))
            dependencies[y].append(x)
        elif "," in line:
            updates.append(list(map(int, line.split(","))))

    def is_valid_update(update):
        position = {page: idx for idx, page in enumerate(update)}
        for y, deps in dependencies.items():
            if y in position:
                for x in deps:
                    if x in position and position[x] > position[y]:
                        return False
        return True

    result = 0
    for update in updates:
        if is_valid_update(update):
            result += update[len(update) // 2]

    return result

def part2(input):
    return 0

if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read()
        print(f"part1: {part1(input)}")
        print(f"part2: {part2(input)}")