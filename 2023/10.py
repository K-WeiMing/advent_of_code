from typing import List
from collections import deque
from load_input import load_data

data: List[str] = load_data()


def part_one() -> int:
    # Find the starting position (row, col)
    ROWS, COLS = len(data), len(data[0])

    for i in range(ROWS):
        for j in range(COLS):
            if data[i][j] == "S":
                r_start, c_start = i, j
                break

    # BFS to find the maximum distance
    # Note that the distance is always an even number
    # The length of the visited set will be halved to get the answer
    visited = set()
    q = deque([(r_start, c_start)])

    while q:
        r, c = q.popleft()
        curr = data[r][c]

        visited.add((r, c))

        # Up
        if (
            r > 0
            and curr in "S|JL"
            and data[r - 1][c] in "|F7"
            and (r - 1, c) not in visited
        ):
            q.append((r - 1, c))

        # Down
        if (
            r < ROWS - 1
            and curr in "S|F7"
            and data[r + 1][c] in "|JL"
            and (r + 1, c) not in visited
        ):
            q.append((r + 1, c))

        # Left
        if (
            c > 0
            and curr in "S-7J"
            and data[r][c - 1] in "-LF"
            and (r, c - 1) not in visited
        ):
            q.append((r, c - 1))

        # Right
        if (
            c < COLS
            and curr in "S-FL"
            and data[r][c + 1] in "-7J"
            and (r, c + 1) not in visited
        ):
            q.append((r, c + 1))

    return len(visited) // 2


def part_two() -> int:
    ...


print(part_one())
