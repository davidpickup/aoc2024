from functools import reduce
from tqdm import tqdm

def _draw_robots(positions: list[tuple[int, int]], width: int, height: int) -> str:
    """Draw the robots on a grid."""
    grid = [['.' for _ in range(width)] for _ in range(height)]
    for x, y in positions:
        grid[y][x] = '#'
    return '\n'.join(''.join(row) for row in grid)

def part1(input, width: int=101, height: int=103):
    """Calculate the product of the number of robots in each quadrant.
    
    Robots have a starting position and velocity. They move in a straight line,
    and wrap around the grid. Robots in the exact middle, do not count as being
    in any quadrant.
    """
    steps = 100
    robots = [
        (int(p[2:].split(',')[0]), int(p[2:].split(',')[1]), int(v[2:].split(',')[0]), int(v[2:].split(',')[1]))
        for line in input.strip().split('\n')
        for p, v in [line.split(' ')]
    ]
    end_positions = [((robot[0] + steps*robot[2]) % width, (robot[1] + steps*robot[3]) % height) for robot in robots]
    quadrants = [0, 0, 0, 0]
    for x, y in end_positions:
        if x < width//2:
            if y < height//2:
                quadrants[0] += 1
            elif y > height//2:
                quadrants[2] += 1
        elif x > width//2:
            if y < height//2:
                quadrants[1] += 1
            elif y > height//2:
                quadrants[3] += 1
    return reduce(lambda x, y: x * y, quadrants)


def part2(input, width: int=101, height: int=103):
    """Calculate the frame where the robots form an image of a Christmas tree."""
    robots = [
        (int(p[2:].split(',')[0]), int(p[2:].split(',')[1]), int(v[2:].split(',')[0]), int(v[2:].split(',')[1]))
        for line in input.strip().split('\n')
        for p, v in [line.split(' ')]
    ]

    xmas_tree_centre = set()
    for x in range(width // 2 - 5, width // 2 + 5):
        for y in range(height // 2 - height // 5, height // 2 + height // 5):
            xmas_tree_centre.add((x, y))

    with open("output.txt", "w") as f:
        for steps in tqdm(range(10000000)):
            end_positions = [((robot[0] + steps*robot[2]) % width, (robot[1] + steps*robot[3]) % height) for robot in robots]
            if xmas_tree_centre.issubset(end_positions):
                drawing = _draw_robots(end_positions, width, height)
                f.write(drawing)
                f.write(f"\n{steps}\n\n")
                tqdm.write(f"Found at step {steps}")
                tqdm.write(drawing)
    return None


if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read()
        print(f"part1: {part1(input)}")
        print(f"part2: {part2(input)}")
