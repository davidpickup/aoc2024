from aoc2024 import day13
import pytest

@pytest.fixture
def sample_input():
    return """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279"""


def test_day13_part1(sample_input):
    assert day13.part1(sample_input) == 480

def test_day13_part2(sample_input):
    assert day13.part2(sample_input) == 875318608908