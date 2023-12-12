from typing import List, Tuple
from load_input import load_data
import re

data: List[str] = load_data()


def d_travelled(i: int, total_t: int) -> int:
    """
    Computes the distance based on the formula of
    n * (time - n)

    Args:
        i (int): time spent pressing the button
        total_t (int): total time in the competition

    Returns:
        int: distance travelled
    """
    return i * (total_t - i)


def process_input() -> Tuple[List[int], List[int]]:
    """
    Preprocess the inputs to get the corresponding time and distance

    Returns:
        Tuple[List[int], List[int]]: [[time], [dist]]
    """
    # time
    c_time = data[0]
    c_time = c_time.split("Time:")[1].strip("")
    c_time = re.sub(" +", " ", c_time).strip().split()
    c_time = [int(c) for c in c_time]

    # distance
    dist = data[1]
    dist = dist.split("Distance:")[1].strip("")
    dist = re.sub(" +", " ", dist).strip().split()
    dist = [int(d) for d in dist]

    return c_time, dist


def part_one() -> int:
    t, d = process_input()

    res = 1

    N = len(t)

    for i in range(N):
        t_to_beat = d[i]

        total_c_time = t[i]
        ways_to_beat = 0
        for j in range(1, total_c_time):
            if d_travelled(j, total_c_time) > t_to_beat:
                ways_to_beat += 1

        if ways_to_beat:
            res *= ways_to_beat

    return res


def part_two() -> int:
    t, d = process_input()

    t = [int("".join([str(i) for i in t]))]
    d = [int("".join([str(i) for i in d]))]

    res = 1

    N = len(t)

    for i in range(N):
        t_to_beat = d[i]

        total_c_time = t[i]
        ways_to_beat = 0
        for j in range(1, total_c_time):
            if d_travelled(j, total_c_time) > t_to_beat:
                ways_to_beat += 1

        if ways_to_beat:
            res *= ways_to_beat

    return res


print(part_one())
print(part_two())
