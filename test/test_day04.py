from aoc2024 import day04
import pytest

@pytest.fixture
def sample_input():
    return """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""


def test_day04_part1(sample_input):
    assert day04.part1(sample_input) == 18

def test_day04_part2(sample_input):
    assert day04.part2(sample_input) == 9