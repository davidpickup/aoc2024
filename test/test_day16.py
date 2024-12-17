from aoc2024 import day16
import pytest

@pytest.fixture
def sample_input():
    return """###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############"""


def test_day16_part1(sample_input):
    assert day16.part1(sample_input) == 7036

def test_day16_part2(sample_input):
    assert day16.part2(sample_input) == 45