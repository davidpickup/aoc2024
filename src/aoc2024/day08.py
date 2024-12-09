from collections import defaultdict
from itertools import combinations

def _parse_input(input):
    antennas = defaultdict(list)
    for y, line in enumerate(input.splitlines()):
        for x, char in enumerate(line):
            if char.isdigit() or char.isalpha():
                antennas[char].append((x, y))
    width, height = len(line), len(input.splitlines())
    return dict(antennas), width, height


def part1(input):
    """Return the number of antinodes in the grid.
    
    An antinode aligns with two antennas of the same frequency,
    where one antenna is twice as far from the antinode as the other.
    """
    antennas, width, height = _parse_input(input)

    antinodes = set()
    for positions in antennas.values():
        for pairs in combinations(positions, 2):
            vector = (pairs[1][0] - pairs[0][0], pairs[1][1] - pairs[0][1])
            antinode_positions = [(pairs[1][0] + vector[0], pairs[1][1] + vector[1]), (pairs[0][0] - vector[0], pairs[0][1] - vector[1])]
            antinodes.update(antinode_positions)

    antinodes = {pos for pos in antinodes if 0 <= pos[0] < width and 0 <= pos[1] < height}
    return len(antinodes)


def part2(input):
    """Return the number of antinodes in the grid.
    
    An antinode aligns with two antennas of the same frequency.
    """
    antennas, width, height = _parse_input(input)

    antinodes = set()
    for positions in antennas.values():
        for pairs in combinations(positions, 2):
            vector = (pairs[1][0] - pairs[0][0], pairs[1][1] - pairs[0][1])
            for i in range(width + height):
                antinode_positions = [(pairs[1][0] + vector[0] * i, pairs[1][1] + vector[1] * i), (pairs[0][0] - vector[0] * i, pairs[0][1] - vector[1] * i)]
                antinodes.update(antinode_positions)

    antinodes = {pos for pos in antinodes if 0 <= pos[0] < width and 0 <= pos[1] < height}
    return len(antinodes)


if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read()
        print(f"part1: {part1(input)}")
        print(f"part2: {part2(input)}")
