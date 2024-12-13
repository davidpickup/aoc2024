from dataclasses import dataclass


@dataclass
class Prize:
    x: int
    y: int

    def __repr__(self):
        return f"Prize({self.x}, {self.y})"


@dataclass
class Button:
    cost: int
    x: int
    y: int

    def __repr__(self):
        return f"Button({self.cost}, {self.x}, {self.y})"


@dataclass
class Machine:
    button_a: Button
    button_b: Button
    prize: Prize

    def __repr__(self):
        return f"Machine({self.button_a}, {self.button_b}, {self.prize})"


def _cost_to_reach_position(machine: Machine) -> int:
    numerator = (
        machine.button_a.y * machine.prize.x - machine.button_a.x * machine.prize.y
    )
    denominator = (
        machine.button_a.y * machine.button_b.x
        - machine.button_a.x * machine.button_b.y
    )
    if denominator != 0:
        y = numerator / denominator
        x = (machine.prize.x - machine.button_b.x * y) / machine.button_a.x
        if x >= 0 and y >= 0 and x.is_integer() and y.is_integer():
            return int(x) * machine.button_a.cost + int(y) * machine.button_b.cost
    return float("inf")


def part1(input):
    """Calculate the cost to reach the prize from each machine by pressing buttons.

    Button A costs 3 tokens.
    Button B costs 1 token.
    """
    machines = []
    for block in input.strip().split("\n\n"):
        lines = block.split("\n")
        button_a = Button(
            cost=3, x=int(lines[0].split()[2][2:-1]), y=int(lines[0].split()[3][2:])
        )
        button_b = Button(
            cost=1, x=int(lines[1].split()[2][2:-1]), y=int(lines[1].split()[3][2:])
        )
        prize = Prize(x=int(lines[2].split()[1][2:-1]), y=int(lines[2].split()[2][2:]))
        machines.append(Machine(button_a=button_a, button_b=button_b, prize=prize))

    costs = [_cost_to_reach_position(machine) for machine in machines]
    return sum(cost for cost in costs if cost < float("inf"))


def part2(input):
    """Calculate the cost to reach the prize from each machine by pressing buttons.

    Button A costs 3 tokens.
    Button B costs 1 token.

    The prize is 10000000000000 higher in both x and y than reported.
    """
    machines = []
    for block in input.strip().split("\n\n"):
        lines = block.split("\n")
        button_a = Button(
            cost=3, x=int(lines[0].split()[2][2:-1]), y=int(lines[0].split()[3][2:])
        )
        button_b = Button(
            cost=1, x=int(lines[1].split()[2][2:-1]), y=int(lines[1].split()[3][2:])
        )
        prize = Prize(
            x=int(lines[2].split()[1][2:-1]) + 10000000000000,
            y=int(lines[2].split()[2][2:]) + 10000000000000,
        )
        machines.append(Machine(button_a=button_a, button_b=button_b, prize=prize))

    costs = [_cost_to_reach_position(machine) for machine in machines]
    return sum(cost for cost in costs if cost < float("inf"))


if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read()
        print(f"part1: {part1(input)}")
        print(f"part2: {part2(input)}")
