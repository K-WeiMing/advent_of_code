from typing import List
import re
import math
from load_input import load_data


data: List[str] = load_data()


def iterate_inst(inst: List[int], node_map: dict) -> int:
    """
    Iterates through the instruction set and node map till destination

    Args:
        inst (List[int]): instructions
        node_map (dict): node map

    Returns:
        int: counts of steps taken
    """
    dest = "ZZZ"
    counter = 0

    curr_node = "AAA"
    while curr_node != dest:
        # Iterate through the instruction set
        dir = inst[counter % len(inst)]
        curr_node = node_map[curr_node][dir]
        counter += 1

    return counter


def iterate_isnt_parallel(inst: List[int], node_map: dict) -> int:
    """
    Iterates through the instruction set and node map till destination
    Note that all nodes must end with Z simultaneously

    Args:
        inst (List[int]): instructions
        node_map (dict): node map

    Returns:
        int: counts of steps taken
    """

    # Count the number of nodes that end with "A"
    # This will be the number of nodes that will end with "Z"
    counter = 0
    node_list = [key for key in node_map if key.endswith("A")]
    cycles = []

    for node in node_list:
        # Iterate through each node and find the cycles where it ends with "Z"
        step_count = 0
        cycle = []
        curr_node = node
        first_z = None
        while True:
            while curr_node[-1] != "Z":
                dir = inst[step_count % len(inst)]
                curr_node = node_map[curr_node][dir]
                step_count += 1

            cycle.append(step_count)
            if first_z is None:
                first_z = curr_node

            elif curr_node == first_z:
                break
        cycles.append(cycle)

    cycle_count = [cycle[0] for cycle in cycles]
    # To get the common cycle where they all have a value ending with Z
    # get the LCM pair wise
    lcm = cycle_count.pop()
    for cycle in cycle_count:
        lcm = lcm * cycle // (math.gcd(lcm, cycle))
    return lcm


def gen_node_map(mapping_info: List[str]) -> dict:
    """
    Generates the node mapping based on the raw input format:
    "AAA" = ("BBB", "BBB") to
    {
        "AAA": ["BBB", "BBB"]
    }

    Args:
        mapping_info (List[str]): input data

    Returns:
        dict: mapping of the node and its subsequent nodes
    """
    node_map = {}
    for m in mapping_info:
        src = m.split("=")[0].strip()
        dirs = m.split("=")[1].strip()
        dirs = re.sub(r"[()]", "", dirs).split(",")
        dirs = [d.strip() for d in dirs]

        node_map[src] = dirs
    return node_map


def part_one() -> int:
    instructions = data[0]
    # Convert instructions to 0 and 1, corresponding to the mapping
    instructions = [0 if i == "L" else 1 for i in instructions]

    mapping = data[2:]
    # Perform mapping of the data into an adjacency list
    mapping = gen_node_map(mapping)
    return iterate_inst(instructions, mapping)


def part_two() -> int:
    instructions = data[0]
    # Convert instructions to 0 and 1, corresponding to the mapping
    instructions = [0 if i == "L" else 1 for i in instructions]

    mapping = data[2:]
    # Perform mapping of the data into an adjacency list
    mapping = gen_node_map(mapping)

    return iterate_isnt_parallel(instructions, mapping)


print(part_one())
print(part_two())
