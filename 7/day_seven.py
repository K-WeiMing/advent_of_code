from collections import defaultdict
from typing import List
import os


def part_one(data: List[str]) -> int:
    # Time complexity: O(n)
    # Space complexity: O(n)
    file_sizes = defaultdict(int)
    stack = []

    for cmd in data:
        if cmd.startswith("$ ls") or cmd.startswith("dir"):
            continue
        if cmd.startswith("$ cd"):
            file_dest = cmd.split()[2]
            if file_dest == "..":
                stack.pop()

            else:
                file_path = f"{stack[-1]}_{file_dest}" if stack else file_dest
                stack.append(file_path)
        else:
            file_size, file_name = cmd.split()
            for file_path in stack:
                file_sizes[file_path] += int(file_size)

    req_size = 30000000 - (70000000 - file_sizes["/"])

    for file_size in sorted(file_sizes.values()):
        if file_size > req_size:
            break
    total_sum = sum(n for n in file_sizes.values() if n <= 100000)

    return total_sum, file_size


if __name__ == "__main__":

    # Read in the data
    curr_path = os.path.dirname(os.path.abspath(__file__))
    input_path = "./input.txt"
    with open(os.path.join(curr_path, input_path), "r") as file:
        data = file.readlines()

    p_one, p_two = part_one(data)

    print(f"Answer for part 1: {p_one}")
    print(f"Answer for part 2: {p_two}")
