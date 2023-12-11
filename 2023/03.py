from load_input import load_data
from typing import List

data: List[str] = load_data()

# Note that the column inputs are of the same size throughout
ROWS, COLS = len(data), len(data[0])
DIRECTIONS = [[1, 0], [-1, 0], [0, 1], [0, -1], [-1, -1], [-1, 1], [1, -1], [1, 1]]


def two_ptr(row_index, col_index):
    # Use two pointers to get the entire number
    l, r = col_index, col_index

    while l >= 0 and data[row_index][l].isnumeric():
        visited.add((row_index, l))
        l -= 1
    l += 1

    while r < COLS and data[row_index][r].isnumeric():
        visited.add((row_index, r))
        r += 1

    return l, r


def part_one():
    res = 0
    for i in range(ROWS):
        for j in range(COLS):
            if not data[i][j].isnumeric() and data[i][j] != ".":
                # Check surrounding for numbers
                for di, dj in DIRECTIONS:
                    i_new, j_new = i + di, j + dj

                    if data[i_new][j_new].isnumeric() and (i_new, j_new) not in visited:
                        l_num, r_num = two_ptr(i_new, j_new)
                        part_num = int(data[i_new][l_num:r_num])
                        res += part_num
    return res


def part_two():
    res = 0
    for i in range(ROWS):
        for j in range(COLS):
            if not data[i][j].isnumeric() and data[i][j] == "*":
                # Check surrounding for numbers
                num_count = 0
                tmp_prod = 1

                for di, dj in DIRECTIONS:
                    i_new, j_new = i + di, j + dj

                    if data[i_new][j_new].isnumeric() and (i_new, j_new) not in visited:
                        l_num, r_num = two_ptr(i_new, j_new)
                        part_num = int(data[i_new][l_num:r_num])
                        tmp_prod *= part_num
                        num_count += 1
                if num_count == 2:
                    res += tmp_prod
    return res


visited = set()
print(part_one())
visited = set()
print(part_two())
