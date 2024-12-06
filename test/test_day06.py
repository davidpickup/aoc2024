from aoc2024 import day06
import pytest

@pytest.fixture
def sample_input():
    return """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""


def test_day06_part1(sample_input):
    assert day06.part1(sample_input) == 41

def test_day05_part2(sample_input):
    assert day06.part2(sample_input) == 6