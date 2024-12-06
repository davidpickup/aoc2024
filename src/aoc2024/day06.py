from copy import deepcopy
from tqdm import tqdm

def part1(input):
    """Calculate the length of the path a guard takes before exiting a map."""
    grid = list(map(list, input.splitlines()))

    x = grid.index(next(filter(lambda x: "^" in x, grid)))
    y = grid[x].index("^")
    count = 0

    turn = {"^": ">", ">": "v", "v": "<", "<": "^"}
    while True:
        new_x, new_y = {
            "^": (x - 1, y),
            ">": (x, y + 1),
            "v": (x + 1, y),
            "<": (x, y - 1),
        }[grid[x][y]]
        if len(grid) <= new_x or len(grid[0]) <= new_y or new_x < 0 or new_y < 0:
            break
        if grid[new_x][new_y] == "#":
            grid[x][y] = turn[grid[x][y]]
        else:
            if grid[new_x][new_y] == ".":
                count += 1
            grid[new_x][new_y] = grid[x][y]
            x, y = new_x, new_y
    return count + 1


def _causes_loop(grid, x, y, ob_x, ob_y):
    """Check if a given point causes a loop."""
    grid = deepcopy(grid)
    grid[ob_x][ob_y] = "#"
    turn = {"^": ">", ">": "v", "v": "<", "<": "^"}
    visited = set()
    while True:
        if (x, y, grid[x][y]) in visited:
            return True
        visited.add((x, y, grid[x][y]))
        new_x, new_y = {
            "^": (x - 1, y),
            ">": (x, y + 1),
            "v": (x + 1, y),
            "<": (x, y - 1),
        }[grid[x][y]]
        if len(grid) <= new_x or len(grid[0]) <= new_y or new_x < 0 or new_y < 0:
            return False
        if grid[new_x][new_y] == "#":
            grid[x][y] = turn[grid[x][y]]
        else:
            grid[new_x][new_y] = grid[x][y]
            x, y = new_x, new_y


def _get_path(grid, start_x, start_y):
    """Get the path a guard takes before exiting a map."""
    grid = deepcopy(grid)
    path = []
    turn = {"^": ">", ">": "v", "v": "<", "<": "^"}
    x, y = start_x, start_y
    while True:
        new_x, new_y = {
            "^": (x - 1, y),
            ">": (x, y + 1),
            "v": (x + 1, y),
            "<": (x, y - 1),
        }[grid[x][y]]
        if len(grid) <= new_x or len(grid[0]) <= new_y or new_x < 0 or new_y < 0:
            break
        if grid[new_x][new_y] == "#":
            grid[x][y] = turn[grid[x][y]]
        else:
            grid[new_x][new_y] = grid[x][y]
            x, y = new_x, new_y
            if (x, y) != (start_x, start_y):
                path.append((x, y))
    return set(path)


def part2(input):
    """Return the number of places an obstacle could be placed to cause a loop."""
    grid = list(map(list, input.splitlines()))

    x = grid.index(next(filter(lambda x: "^" in x, grid)))
    y = grid[x].index("^")

    possible_positions = _get_path(grid, x, y)
    return sum(1 for ob_x, ob_y in tqdm(possible_positions) if _causes_loop(grid, x, y, ob_x, ob_y))


if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read()
        print(f"part1: {part1(input)}")
        print(f"part2: {part2(input)}")
