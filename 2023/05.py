from load_input import load_data
from typing import List, Tuple
from icecream import ic

data: List[str] = load_data()
ROWS = len(data)


def convert_mapping(line: str) -> List[int]:
    """
    Converts the mapping information from a strings to integer

    Args:
        line (str):
            destination range start, source range start, range length

    Returns:
        List[int]: inputs in List[int] format
    """
    return [int(d) for d in line.split(" ")]


def update_seeds(r_start: int, r_end: int, seed_vals: List[int]) -> List[int]:
    """
    Updates the mapping based on the input information

    Args:
        r_start (int): row start
        r_end (int): row end
        seed_vals (List[int]): seed values

    Returns:
        List[int]: List of updated seed map
    """
    for i in range(len(seed_vals)):
        for j in range(r_start, r_end):
            dest, src, rng = convert_mapping(data[j])

            if seed_vals[i] >= src and seed_vals[i] < src + rng:
                # Perform mapping if its within the range
                delta = seed_vals[i] - src
                seed_vals[i] = dest + delta
                break

    return seed_vals


def update_row_num(r: int, section_name: str) -> Tuple[int, int]:
    """
    Get the row start and row end, note that row end is n + 1, (data[row_num] == "")

    Args:
        r (int): row start
        section_name (str): section to check

    Returns:
        Tuple[int, int]: r_start, r_end
    """
    while r < ROWS:
        if section_name in data[r]:
            r_start = r + 1
        if data[r] == "" or r == ROWS - 1:
            r_end = r
            break
        r += 1
    return r_start, r_end


def iterate_map(row_num: int, seeds: List[int]) -> int:
    """
    Iterate through the entire mapping

    Args:
        row_num (int): initialized row number
        seeds (List[int]): initialized seed values

    Returns:
        int: minimum value of the final seed mapping
    """
    r_start, r_end = update_row_num(row_num, "seed-to-soil map")

    # Once we know the start and end, we iterate through seeds and get the updated mapping
    seeds = update_seeds(r_start, r_end, seeds)

    r_num = r_end + 1
    r_start, r_end = update_row_num(r_num, "soil-to-fertilizer map")
    seeds = update_seeds(r_start, r_end, seeds)

    r_num = r_end + 1
    r_start, r_end = update_row_num(r_num, "fertilizer-to-water map")
    seeds = update_seeds(r_start, r_end, seeds)

    r_num = r_end + 1
    r_start, r_end = update_row_num(r_num, "water-to-light map")
    seeds = update_seeds(r_start, r_end, seeds)

    r_num = r_end + 1
    r_start, r_end = update_row_num(r_num, "light-to-temperature map")
    seeds = update_seeds(r_start, r_end, seeds)

    r_num = r_end + 1
    r_start, r_end = update_row_num(r_num, "temperature-to-humidity map")
    seeds = update_seeds(r_start, r_end, seeds)

    r_num = r_end + 1
    r_start, r_end = update_row_num(r_num, "humidity-to-location map")
    seeds = update_seeds(r_start, r_end, seeds)

    return min(seeds)


def part_one() -> int:
    seeds = convert_mapping(data[0].split("seeds:")[1].lstrip())

    r_num = 2
    return iterate_map(r_num, seeds)


def part_two() -> int:
    seeds = convert_mapping(data[0].split("seeds:")[1].lstrip())
    seeds_list = []
    # Expand the seed ranges into a list of each seed number
    # init dummy values
    rng_start = 0
    rng_end = 0
    for i in range(len(seeds)):
        if (i + 1) % 2 != 0:
            rng_start = seeds[i]
        else:
            # With the even number the range of numbers can be obtained
            rng_end = seeds[i]
            seeds_list += [s for s in range(rng_start, rng_start + rng_end + 1)]
            ic(seeds_list)

    r_num = 2
    return iterate_map(r_num, seeds)


print(part_one())
print(part_two())
