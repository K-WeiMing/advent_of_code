import os


def part_one(data):
    # Time complexity: O(n)
    # Space complexity: O(1)

    priorities = 0

    for items in data:
        l = len(items)
        first, second = items[: int(l / 2)], items[int(l / 2) :]

        common_items = set(first).intersection(set(second))

        for item in common_items:

            if item.islower():
                priorities += ord(item) - ord("a") + 1
            else:
                # Include 27 to push the first alphabet ('A') to 27
                priorities += ord(item) - ord("A") + 27

    return priorities


def part_two(data):
    # Time complexity: O(n)
    # Space complexity: O(1)

    tmp = []
    priorities = 0

    counter = -1
    for items in data:
        tmp.append(items)
        counter += 1

        if counter == 2:
            # Process the result
            common_items = set(tmp[0]) & set(tmp[1]) & set(tmp[2])
            priorities += get_common(common_items)

            # Reset values
            tmp = []
            counter = -1

    return priorities


def get_common(com_item: set) -> int:
    """Goes through the list and returns the cumulative priorities

    Args:
        com_item (List[str]): List of items in elves bag

    Returns:
        int: cumulative priorities of all common items
    """
    res = 0
    for common in com_item:
        if common.islower():
            res += ord(common) - ord("a") + 1
        else:
            # Include 27 to push the first alphabet ('A') to 27
            res += ord(common) - ord("A") + 27
    return res


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
