from aoc2024 import day12
import pytest

@pytest.fixture
def sample_input():
    return """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE"""


def test_day12_part1(sample_input):
    assert day12.part1(sample_input) == 1930

def test_day12_part2(sample_input):
    assert day12.part2(sample_input) == 1206