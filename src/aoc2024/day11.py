from functools import lru_cache

@lru_cache(maxsize=None)
def _stone_blinks(stone, time):
    if time == 0:
        return 1
    if stone == 0:
        return _stone_blinks(1, time - 1)
    stone_str = str(stone)
    if len(stone_str) % 2 == 0:
        half = len(stone_str) // 2
        return _stone_blinks(int(stone_str[:half]), time - 1) + _stone_blinks(int(stone_str[half:]), time - 1)
    return _stone_blinks(stone * 2024, time - 1)


def _blinks(stones, number_of_blinks):
    return sum(_stone_blinks(stone, number_of_blinks) for stone in stones)

def part1(input):
    """Receive a list of stones and return the number of stones after blinking 25 times.

    Each blink causes the following changes:
    * If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
    * If the stone is engraved with a number that has an even number of digits, it is replaced by two stones.
        The left half of the digits are engraved on the new left stone, and the right half of the digits are
        engraved on the new right stone. (The new numbers don't keep extra leading zeroes: 1000 would become
        stones 10 and 0.)
    * If none of the other rules apply, the stone is replaced by a new stone; the old stone's number
        multiplied by 2024 is engraved on the new stone."""

    stones = list(map(int, input.split()))
    number_of_blinks = 25
    return _blinks(stones, number_of_blinks)


def part2(input):
    """Receive a list of stones and return the number of stones after blinking 75 times."""

    stones = list(map(int, input.split()))
    number_of_blinks = 75
    return _blinks(stones, number_of_blinks)


if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read()
        print(f"part1: {part1(input)}")
        print(f"part2: {part2(input)}")
