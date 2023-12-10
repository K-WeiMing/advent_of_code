import os


def part_one(data: list):
    # Time complexity: O(n)
    # Space complexity: O(1)

    # Use a sliding window technique to find the answer
    for i in range(len(data) - 3):
        if len(set(data[i : i + 4])) == 4:
            return i + 4


def part_two(data: list):
    # Time complexity: O(n)
    # Space complexity: O(1)

    # Use a sliding window technique to find the answer
    for i in range(len(data) - 13):
        if len(set(data[i : i + 14])) == 14:
            return i + 14


if __name__ == "__main__":
    # Read in the data
    curr_path = os.path.dirname(os.path.abspath(__file__))
    input_path = "./input.txt"
    with open(os.path.join(curr_path, input_path), "r") as file:
        data = file.readlines()

    data = data[0]

    print(f"Answer for part 1: {part_one(data)}")
    print(f"Answer for part 2: {part_two(data)}")
