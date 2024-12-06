from functools import cmp_to_key


def _process_input(input) -> tuple[dict, dict]:
    lines = input.splitlines()
    dependencies = {}
    updates = []

    for line in lines:
        if "|" in line:
            x, y = map(int, line.split("|"))
            if y not in dependencies:
                dependencies[y] = []
            if x not in dependencies:
                dependencies[x] = []
            dependencies[x].append(y)
        elif "," in line:
            updates.append(list(map(int, line.split(","))))

    return dependencies, updates


def part1(input):
    """Output the middle element of the list of updates that are sorted."""
    dependencies, updates = _process_input(input)

    def _is_sorted(update):
        return all(j in dependencies[i] for i, j in zip(update, update[1:]))

    return sum(update[len(update) // 2] for update in updates if _is_sorted(update))


def part2(input):
    """Output the middle element of the sorted list of updates that are not sorted."""
    dependencies, updates = _process_input(input)

    def _is_sorted(update):
        return all(j in dependencies[i] for i, j in zip(update, update[1:]))

    return sum(
        sorted(
            update,
            key=cmp_to_key(
                lambda x, y: (
                    -1 if y in dependencies[x] else 1 if x in dependencies[y] else 0
                )
            ),
        )[len(update) // 2]
        for update in updates
        if not _is_sorted(update)
    )


if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read()
        print(f"part1: {part1(input)}")
        print(f"part2: {part2(input)}")
