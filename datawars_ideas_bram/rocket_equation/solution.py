def fuel_required_for_module(module_mass: int) -> int:
    return int(module_mass / 3) - 2


def total_fuel_required_for_module(module_mass: int) -> int:
    fuel = fuel_required_for_module(module_mass)
    total_fuel = fuel

    while fuel_required_for_module(fuel) > 0:
        fuel = fuel_required_for_module(fuel)
        total_fuel += fuel
    return total_fuel


def part_one() -> int:
    with open('input.txt', 'r') as f:
        return sum([fuel_required_for_module(int(module_mass)) for module_mass in f.readlines()])


def part_two() -> int:
    with open('input.txt', 'r') as f:
        return sum([total_fuel_required_for_module(int(module_mass)) for module_mass in f.readlines()])


if __name__ == '__main__':
    print(f"Answer for part one: {part_one()}")
    print(f"Answer for part two: {part_two()}")
