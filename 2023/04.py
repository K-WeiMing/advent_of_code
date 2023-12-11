from load_input import load_data
from typing import List, Set

data: List[str] = load_data()


def compute_points(matches: int) -> int:
    if matches == 0:
        return 0
    if matches == 1:
        return 1
    return pow(2, matches - 1)


def get_winning_nums(line: str) -> Set[int]:
    """
    Generalized function to use in part one and part two

    Args:
        line (str): input line from raw data

    Returns:
        List[int]: list of winning numbers in scratchcard
    """
    # For single digit integers, there may be empty strings '' after the split
    win_nums = line.split("|")[0].split(":")[1].strip("").split(" ")
    win_nums = set([int(n) for n in win_nums if n != ""])

    return win_nums


def get_curr_nums(line: str) -> Set[int]:
    """
    Generalized function to use in part one and part two

    Args:
        line (str): input line from raw data

    Returns:
        List[int]: list of current numbers in scratchcard
    """
    curr_nums = line.split("|")[1].strip().split(" ")
    curr_nums = set([int(n) for n in curr_nums if n != ""])

    return curr_nums


def part_one() -> int:
    points = 0
    for d in data:
        # Get the winning numbers and numbers you have
        winning_nums = get_winning_nums(d)
        current_nums = get_curr_nums(d)
        # Get the intersection to find the winning numbers
        matching_nums = winning_nums.intersection(current_nums)
        points += compute_points(len(matching_nums))

    return points


def part_two() -> int:
    card_cnt = {i + 1: 1 for i in range(len(data))}

    for card_num, d in enumerate(data):
        winning_nums = get_winning_nums(d)
        current_nums = get_curr_nums(d)
        matching_nums = winning_nums.intersection(current_nums)

        # Increment the card numbers gained
        curr_card_num = card_num + 1
        for i in range(curr_card_num + 1, curr_card_num + len(matching_nums) + 1):
            card_cnt[i] += card_cnt[curr_card_num]

    return sum(card_cnt.values())


print(part_one())
print(part_two())
