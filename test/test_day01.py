from aoc2024 import day01
import pytest

@pytest.fixture
def sample_input():
    return """3   4
4   3
2   5
1   3
3   9
3   3"""

def test_day01_part1(sample_input):
    assert day01.part1(sample_input) == 11

def test_day01_part2(sample_input):
    assert day01.part2(sample_input) == 31