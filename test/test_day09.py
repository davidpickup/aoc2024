from aoc2024 import day09
import pytest

@pytest.fixture
def sample_input():
    return """2333133121414131402"""


def test_day09_part1(sample_input):
    assert day09.part1(sample_input) == 1928

def test_day09_part2(sample_input):
    assert day09.part2(sample_input) == 2858