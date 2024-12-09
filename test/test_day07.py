from aoc2024 import day07
import pytest

@pytest.fixture
def sample_input():
    return """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""


def test_day07_part1(sample_input):
    assert day07.part1(sample_input) == 3749

def test_day07_part2(sample_input):
    assert day07.part2(sample_input) == 11387