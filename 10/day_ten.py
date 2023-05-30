import os

CYCLE_COUNT_CHECK = [20, 60, 100, 140, 180, 220]


def part_one(data: list):
    # Time complexity: O(n)
    # Space complexity: O(1)

    total = 0
    signal_strength = 1

    cycle_count = 1
    flag = True
    counter = 0
    add_cycle = 0
    add_value = 0
    while counter < len(data):
        if add_cycle == cycle_count:
            signal_strength += add_value
            counter += 1
            flag = True

        if counter < len(data) and data[counter] == "noop":
            counter += 1

        elif counter < len(data) and "addx" in data[counter] and flag:
            add_cycle = cycle_count + 2
            add_value = int(data[counter].split()[1])
            flag = False

        if cycle_count in CYCLE_COUNT_CHECK:
            print(f"cycle count: {cycle_count}, signal_strength: {signal_strength}")
            total += cycle_count * signal_strength
        cycle_count += 1

    return total


def part_two(data: list):
    ...


if __name__ == "__main__":
    # Read in the data
    curr_path = os.path.dirname(os.path.abspath(__file__))
    input_path = "./input.txt"
    with open(os.path.join(curr_path, input_path), "r") as file:
        data = file.read().splitlines()

    print(f"Answer for part 1: {part_one(data)}")
    # print(f"Answer for part 2: {part_two(data)}")
