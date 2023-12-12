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


def update_seed_ranges(r_start: int, r_end: int, seed_ranges: List[int]) -> List[int]:
    """
    Updates the mapping based on the input information on seed ranges

    Args:
        r_start (int): row start
        r_end (int): row end
        seed_ranges (List[int]): Seed ranges map

    Returns:
        List[int]: List of updated seed ranges map
    """
    seed_rng_updated = []
    for i in range(len(seed_ranges)):
        for j in range(r_start, r_end):
            # Update the ranges based on the mapping provided
            # Note that the incoming array may be split into a maximum of 3 separate ranges
            dest, src, rng = convert_mapping(data[j])

            # Check start of the range
            # 1. if its less than src
            # 2. if its >= src and < src + rng
            # 3. if its >= src + rng: Maintain the range
            seed_rng_start = seed_ranges[i][0]
            seed_rng_end = seed_ranges[i][1]
            if seed_rng_start >= src + rng:
                seed_rng_updated.append(seed_ranges[i])
            elif seed_rng_start < src:
                # Check if the ending range is within or exceeding src + rng
                if seed_rng_end >= src + rng:
                    # First half of the range
                    seed_rng_updated.append([seed_rng_start, src - 1])
                    # Second half of the range (Re-mapped)
                    seed_rng_updated.append([dest, dest + rng - 1])
                    # Third part of the range, note that this may be in another mapping

                elif seed_rng_end >= src:
                    ...
                else:
                    # Update end range and append
                    delta = seed_rng_end - src
                    seed_rng_end = delta + dest
                    seed_rng_updated.append([seed_rng_start, seed_rng_end])

            elif src <= seed_rng_start < src + rng:
                # Check if the ending range is within or exceeding src + rng
                # Update start boundary
                ...
                delta = seed_ranges[i][0] - src
                new_start = dest + delta


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


def get_seed_ranges(seed_vals: List[int]) -> List[list]:
    """
    Generates a list of seed ranges instead of using actual seed values

    Args:
        seed_vals (List[int]): Initial seed values

    Returns:
        List[List[int, int]]: Updated to seed ranges
    """
    rng = []
    tmp = []
    for i in range(len(seed_vals)):
        if (i + 1) % 2 != 0:
            tmp.append(seed_vals[i])
        else:
            # With the even number, end of range can be obtained
            tmp.append(tmp[0] + seed_vals[i] - 1)
            rng.append(tmp.copy())
            tmp = []
    return rng


def part_one() -> int:
    seeds = convert_mapping(data[0].split("seeds:")[1].lstrip())

    r_num = 2
    return iterate_map(r_num, seeds)


def part_two() -> int:
    seeds = convert_mapping(data[0].split("seeds:")[1].lstrip())

    # Store the seeds in format of [[seed_start, seed_end], ...]
    seed_ranges = get_seed_ranges(seeds)
    ic(seed_ranges)
    r_num = 2
    return iterate_map(r_num, seeds)


print(part_one())
print(part_two())
