def trailhead_score(grid, i, j, visited=None, ignore_visited=False):
    if visited is None:
        visited = set()
    visited.add((i, j))
    current_value = grid[i][j]
    if current_value == 9:
        return 1
    new_positions = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
    return sum(
        trailhead_score(grid, x, y, visited, ignore_visited)
        for x, y in new_positions
        if 0 <= x < len(grid)
        and 0 <= y < len(grid[0])
        and grid[x][y] == current_value + 1
        and (ignore_visited or (x, y) not in visited)
    )


def part1(input):
    """Return the sum of the score of each trailhead in a topological map.

    A trail is a path that starts at zero, and increases incrementally to 9.
    A trailhead is any position that begins a trail, and its score is the number
    of peaks reachable from that position.
    """
    grid = [[int(x) for x in line] for line in input.splitlines()]
    score = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                score += trailhead_score(grid, i, j)
    return score


def part2(input):
    """Return the sum of the score of each trailhead in a topological map.

    A trail is a path that starts at zero, and increases incrementally to 9.
    A trailhead is any position that begins a trail, and its score is the number
    of trails that start at that position.
    """
    grid = [[int(x) for x in line] for line in input.splitlines()]
    score = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                score += trailhead_score(grid, i, j, ignore_visited=True)
    return score


if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read()
        print(f"part1: {part1(input)}")
        print(f"part2: {part2(input)}")
