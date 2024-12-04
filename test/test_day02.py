from aoc2024 import day02
import pytest

@pytest.fixture
def sample_input():
    return """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""

def test_day02_part1(sample_input):
    assert day02.part1(sample_input) == 2

def test_day02_part2(sample_input):
    assert day02.part2(sample_input) == 4