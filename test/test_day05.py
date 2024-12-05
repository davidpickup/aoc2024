from aoc2024 import day05
import pytest

@pytest.fixture
def sample_input():
    return """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""


def test_day05_part1(sample_input):
    assert day05.part1(sample_input) == 143

def test_day05_part2(sample_input):
    assert day05.part2(sample_input) == 0