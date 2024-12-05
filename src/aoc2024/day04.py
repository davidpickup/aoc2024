
def part1(input):
    """Count the number of occurrences of the word XMAS in the grid, in any direction."""
    grid = [list(line) for line in input.splitlines()]
    word = "XMAS"
    word_len = len(word)
    count = 0

    def search_word(x, y, dx, dy):
        for i in range(word_len):
            if not (0 <= x < len(grid) and 0 <= y < len(grid[0])) or grid[x][y] != word[i]:
                return 0
            x += dx
            y += dy
        return 1

    directions = [
        (1, 0),  # Horizontal right
        (0, 1),  # Vertical down
        (1, 1),  # Diagonal down-right
        (1, -1), # Diagonal down-left
        (-1, 0), # Horizontal left
        (0, -1), # Vertical up
        (-1, -1),# Diagonal up-left
        (-1, 1)  # Diagonal up-right
    ]

    for x in range(len(grid)):
        for y in range(len(grid[0])):
            for dx, dy in directions:
                count += search_word(x, y, dx, dy)

    return count


def part2(input):
    """Count the number of occurrences of the word MAS in the shape of an X."""
    grid = [list(line) for line in input.splitlines()]
    word = "MAS"
    word_len = len(word)
    count = 0

    def search_word(x, y, dx, dy):
        x -= dx * (word_len // 2)
        y -= dy * (word_len // 2)
        for i in range(word_len):
            if not (0 <= x < len(grid) and 0 <= y < len(grid[0])) or grid[x][y] != word[i]:
                return 0
            x += dx
            y += dy
        return 1

    directions = [
        (1, 1),  # Diagonal down-right
        (1, -1), # Diagonal down-left
        (-1, -1),# Diagonal up-left
        (-1, 1)  # Diagonal up-right
    ]

    for x in range(len(grid)):
        for y in range(len(grid[0])):
            _count = 0
            for dx, dy in directions:
                _count += search_word(x, y, dx, dy)
            if _count == 2:
                count += 1

    return count


if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read()
        print(f"part1: {part1(input)}")
        print(f"part2: {part2(input)}")
