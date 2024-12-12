def _is_edge(grid, i, j, x, y):
    return (
        0 <= i < len(grid)
        and 0 <= j < len(grid)
        and (
            x < 0
            or x >= len(grid)
            or y < 0
            or y >= len(grid[0])
            or grid[x][y] != grid[i][j]
        )
    )


def _fence_cost(grid, i, j):
    return sum(
        [
            1
            for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
            if _is_edge(grid, i, j, x, y)
        ]
    )


def _corner_cost(grid, i, j):
    return sum(
        [
            _is_edge(grid, i, j, i - 1, j) and _is_edge(grid, i, j, i, j - 1),
            _is_edge(grid, i, j, i + 1, j) and _is_edge(grid, i, j, i, j - 1),
            _is_edge(grid, i, j, i - 1, j) and _is_edge(grid, i, j, i, j + 1),
            _is_edge(grid, i, j, i + 1, j) and _is_edge(grid, i, j, i, j + 1),
            not (_is_edge(grid, i, j, i - 1, j) or _is_edge(grid, i, j, i, j - 1))
            and (i > 0 and j > 0 and grid[i - 1][j - 1] != grid[i][j]),
            not (_is_edge(grid, i, j, i + 1, j) or _is_edge(grid, i, j, i, j - 1))
            and (i < len(grid) - 1 and j > 0 and grid[i + 1][j - 1] != grid[i][j]),
            not (_is_edge(grid, i, j, i - 1, j) or _is_edge(grid, i, j, i, j + 1))
            and (i > 0 and j < len(grid[0]) - 1 and grid[i - 1][j + 1] != grid[i][j]),
            not (_is_edge(grid, i, j, i + 1, j) or _is_edge(grid, i, j, i, j + 1))
            and (
                i < len(grid) - 1
                and j < len(grid[0]) - 1
                and grid[i + 1][j + 1] != grid[i][j]
            ),
        ]
    )


def _region_cost(grid, i, j, visited, fence_cost_func):
    """Calculate the price of the region containing the cell at (i, j)."""
    visited.add((i, j))
    fence_cost = fence_cost_func(grid, i, j)
    area_cost = 1
    for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
        if (
            0 <= x < len(grid)
            and 0 <= y < len(grid[0])
            and grid[x][y] == grid[i][j]
            and (x, y) not in visited
        ):
            f, a = _region_cost(grid, x, y, visited, fence_cost_func)
            fence_cost += f
            area_cost += a
    return fence_cost, area_cost


def part1(input):
    """Calculate the price of each region containing the same letter, as the product of its area and perimeter."""
    grid = [list(line) for line in input.splitlines()]
    total_cost = 0
    visited = set()
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (i, j) not in visited:
                fence_cost, area_cost = _region_cost(grid, i, j, visited, _fence_cost)
                total_cost += fence_cost * area_cost
    return total_cost


def part2(input):
    """Calculate the price of each region containing the same letter, as the product of its area and edge count."""
    grid = [list(line) for line in input.splitlines()]
    total_cost = 0
    visited = set()
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (i, j) not in visited:
                fence_cost, area_cost = _region_cost(grid, i, j, visited, _corner_cost)
                total_cost += fence_cost * area_cost
    return total_cost


if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read()
        print(f"part1: {part1(input)}")
        print(f"part2: {part2(input)}")
