from typing import List
from load_input import load_data

data: List[str] = load_data()

mapping = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def part_one() -> int:
    calibration_values = 0

    for d in data:
        nums = []
        l, r = 0, len(d) - 1
        while l < len(d):
            if d[l].isnumeric():
                nums.append(d[l])
                break
            l += 1

        while r >= 0:
            if d[r].isnumeric():
                nums.append(d[r])
                break
            r -= 1
        calibration_values += int("".join(nums))

    return calibration_values


def part_two() -> int:
    calibration_values = 0

    for d in data:
        nums = []
        for index, char in enumerate(d):
            if char.isdigit():
                nums.append(char)
                continue

            for key, value in mapping.items():
                if d[index:].startswith(key):
                    nums.append(str(value))
                    break
        calibration_values += int(nums[0] + nums[-1])
    return calibration_values


print(part_one())
print(part_two())
