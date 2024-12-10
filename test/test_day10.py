from aoc2024 import day10
import pytest

@pytest.fixture
def sample_input():
    return """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""


def test_day10_part1(sample_input):
    assert day10.part1(sample_input) == 36

def test_day10_part2(sample_input):
    assert day10.part2(sample_input) == 81