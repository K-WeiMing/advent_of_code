from typing import List
from load_input import load_data


data: List[str] = load_data()


def gen_hist(line: str) -> int:
    """
    Takes the input of each sequence and generates the history
    Return the last sequence of the history

    Args:
        line (str): input row

    Returns:
        int: last history of the first row
    """

    curr_row = line
    hist = [curr_row]

    # Iterate through to get the last line of zeros
    while any(n != 0 for n in curr_row):
        next_row = []

        for i in range(len(curr_row) - 1):
            diff = curr_row[i + 1] - curr_row[i]
            next_row.append(diff)

        hist.append(next_row.copy())
        curr_row = next_row

    hist[-1].append(0)
    # To get the history value, we take the last value of the last row
    # and add the last value of the row above it

    for i in range(len(hist) - 1, 0, -1):
        curr_num = hist[i][-1]
        next_num = hist[i - 1][-1]
        hist[i - 1].append(curr_num + next_num)

    return hist[0][-1]


def gen_hist_front(line: str) -> int:
    """
    Takes the input of each sequence and generates the history
    Return the last sequence of the history

    Args:
        line (str): input row

    Returns:
        int: last history of the first row
    """

    curr_row = line
    hist = [curr_row]

    # Iterate through to get the last line of zeros
    while any(n != 0 for n in curr_row):
        next_row = []

        for i in range(len(curr_row) - 1):
            diff = curr_row[i + 1] - curr_row[i]
            next_row.append(diff)

        hist.append(next_row.copy())
        curr_row = next_row

    hist[-1].append(0)

    # Reverse the lists in each row
    for h_index, h in enumerate(hist):
        hist[h_index] = h[::-1]

    # To get the history value, we take the last value of the last row
    # and add the last value of the row above it
    # Note that the difference from part one is that it is
    # next_num - curr_num as we are extrapolating the number before

    for i in range(len(hist) - 1, 0, -1):
        curr_num = hist[i][-1]
        next_num = hist[i - 1][-1]
        hist[i - 1].append(next_num - curr_num)

    return hist[0][-1]


def part_one() -> int:
    res = 0
    for d in data:
        d_int = [int(num) for num in d.split(" ")]
        res += gen_hist(d_int)

    return res


def part_two() -> int:
    res = 0
    for d in data:
        d_int = [int(num) for num in d.split(" ")]
        res += gen_hist_front(d_int)

    return res


print(part_one())
print(part_two())
