def _move_box_vertically(
    grid: list[list[str]], position: tuple[int, int], direction: str
) -> tuple[int, int]:
    """Move the box at position in the specified direction."""
    x, y = position
    if direction == "^":
        x -= 1
    elif direction == "v":
        x += 1

    if x < 0 or y < 0 or x >= len(grid) or y+1 >= len(grid[0]):
        return position

    if grid[x][y] == "#" or grid[x][y+1] == "#":
        return position

    if grid[x][y] == "[":
        bx, by = _move_box_vertically(grid, (x, y), direction)
        if bx == x and by == y:
            return position
    elif grid[x][y] == "]":
        bx, by = _move_box_vertically(grid, (x, y-1), direction)
        if bx == x and by == y-1:
            return position

    grid[position[0]][position[1]] = "."
    grid[position[0]][position[1]+1] = "."
    grid[x][y] = "["
    grid[x][y+1] = "]"
    return x, y


def _move(
    grid: list[list[str]], position: tuple[int, int], direction: str
) -> tuple[int, int]:
    """Move the item at position in the specified direction."""

    x, y = position
    if direction == "^":
        x -= 1
    elif direction == ">":
        y += 1
    elif direction == "v":
        x += 1
    elif direction == "<":
        y -= 1

    if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]):
        return position

    if grid[x][y] == "#":
        return position

    if grid[x][y] == "O":
        bx, by = _move(grid, (x, y), direction)
        if bx == x and by == y:
            return position
    elif grid[x][y] == "[":
        bx, by = (
            _move_box_vertically(grid, (x, y), direction)
            if direction in "^v"
            else _move(grid, (x, y), direction)
        )
        if bx == x and by == y:
            return position
    elif grid[x][y] == "]":
        if direction in "^v":
            bx, by = _move_box_vertically(grid, (x, y-1), direction)
            if bx == x and by == y-1:
                return position
        else:
            bx, by = _move(grid, (x, y), direction)
            if bx == x and by == y:
                return position

    if grid[position[0]][position[1]] == "[":
        grid[position[0]][position[1]] = "."
        grid[position[0]][position[1]+1] = "."
        grid[x][y] = "["
        grid[x][y+1] = "]"
    else:
        grid[x][y] = grid[position[0]][position[1]]
        grid[position[0]][position[1]] = "."
    return x, y


def _gps_box_value(grid: list[list[str]], position: tuple[int, int]) -> int:
    """Return the gps box value of the item at position."""
    x, y = position
    if grid[x][y] == "O" or grid[x][y] == "[":
        return 100 * x + y
    return 0


def part1(input):
    """Calculate the sum of box gps positions after a warehouse robot
    has moved around a warehouse according to the input instructions.

    The gps positions are 100 * x + y, where x and y are the coordinates."""
    grid_inputs, instruction_input = input.split("\n\n")
    grid = [list(line) for line in grid_inputs.splitlines()]
    instructions = list("".join(instruction_input.splitlines()))
    position = None
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == "@":
                position = (x, y)
                break
    for instruction in instructions:
        position = _move(grid, position, instruction)
    return sum(
        _gps_box_value(grid, (x, y))
        for x in range(len(grid))
        for y in range(len(grid[0]))
    )


def part2(input):
    """Calculate the same, but this time the items in the warehouse are larger."""
    input = "".join(
        [
            (
                "##"
                if c == "#"
                else "[]" if c == "O" else ".." if c == "." else "@." if c == "@" else c
            )
            for c in input
        ]
    )
    grid_inputs, instruction_input = input.split("\n\n")
    grid = [list(line) for line in grid_inputs.splitlines()]
    instructions = list("".join(instruction_input.splitlines()))
    position = None
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == "@":
                position = (x, y)
                break
    for instruction in instructions:
        position = _move(grid, position, instruction)
    breakpoint()
    return sum(
        _gps_box_value(grid, (x, y))
        for x in range(len(grid))
        for y in range(len(grid[0]))
    )


if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read()
        print(f"part1: {part1(input)}")
        print(f"part2: {part2(input)}")
