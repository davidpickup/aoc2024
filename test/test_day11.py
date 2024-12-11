from aoc2024 import day11
import pytest

@pytest.fixture
def sample_input():
    return """125 17"""


def test_day11_part1(sample_input):
    assert day11.part1(sample_input) == 55312

def test_day11_part2(sample_input):
    assert day11.part2(sample_input) == 65601038650482