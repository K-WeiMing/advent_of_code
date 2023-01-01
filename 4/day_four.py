import os


def check_overlap(range_one: list, range_two: list) -> int:
    """Checks for overlap for both ranges

    Args:
        range_one (list): [x: int , y: int]
        range_two (list): [x: int , y: int]

    Returns:
        int: 1 or 0
    """
    if (range_one[0] >= range_two[0] and range_one[0] <= range_two[1]) or (
        range_one[1] >= range_two[0] and range_one[1] <= range_two[1]
    ):
        return 1

    if (range_two[0] >= range_one[0] and range_two[0] <= range_one[1]) or (
        range_two[1] >= range_one[0] and range_two[1] <= range_one[1]
    ):
        return 1

    return 0


def check_range_intersection(range_one: list, range_two: list) -> int:
    """Checks whether the ranges each parameter is within each other

    Args:
        range_one (list): [x: int , y: int]
        range_two (list): [x: int, y: int]

    Returns:
        int: 1 or 0
    """
    if range_one[0] >= range_two[0] and range_one[1] <= range_two[1]:
        # Case for when range one is within range two
        return 1

    if range_one[0] <= range_two[0] and range_one[1] >= range_two[1]:
        return 1

    return 0


def part_one(data):

    intersected = 0

    for row in data:
        first_range, second_range = row.split(",")

        first_range = first_range.split("-")
        first_range = [int(i) for i in first_range]

        second_range = second_range.split("-")
        second_range = [int(i) for i in second_range]

        intersected += check_range_intersection(first_range, second_range)

    return intersected


def part_two(data):
    overlap = 0

    for row in data:
        first_range, second_range = row.split(",")

        first_range = first_range.split("-")
        first_range = [int(i) for i in first_range]

        second_range = second_range.split("-")
        second_range = [int(i) for i in second_range]

        overlap += check_overlap(first_range, second_range)

    return overlap


if __name__ == "__main__":

    # Read in the data
    curr_path = os.path.dirname(os.path.abspath(__file__))
    input_path = "./input.txt"
    with open(os.path.join(curr_path, input_path), "r") as file:
        data = file.readlines()
    # Replace '\n' in the inputs
    data = [str(i.replace("\n", "")) for i in data]

    print(f"Answer for part 1: {part_one(data)}")
    print(f"Answer for part 2: {part_two(data)}")
