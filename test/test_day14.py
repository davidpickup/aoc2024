from aoc2024 import day14
import pytest

@pytest.fixture
def sample_input():
    return """p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3"""


def test_day14_part1(sample_input):
    assert day14.part1(sample_input, width=11, height=7) == 12

def test_day14_part2(sample_input):
    assert day14.part2(sample_input) is None