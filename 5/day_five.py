import os
from typing import List


def load_data(stack_info: str) -> dict:
    """Generates stack information from the input data

    Args:
        stack_info (str): string data containing stack information

    Returns:
        dict: key, value pair of stack number: crates
    """
    stacks = {int(stack): [] for stack in stack_info[-1].replace(" ", "")}

    # Load the index values of the last row
    indexes = [index for index, char in enumerate(stack_info[-1]) if char != " "]

    # Go through the stack_info and load in the crate information

    for line in stack_info[:-1]:
        # Reset the stack number for each row
        stack_num = 1

        for index in indexes:
            if line[index] != " ":
                stacks[stack_num].insert(0, line[index])
            stack_num += 1

    return stacks


def format_instructions(input_instruction: List[str]) -> List[int]:
    """Format the instructions to return a 3 value array

    Args:
        instructions (List[str]): Instructions in string format

    Returns:
        List[str]: Instructions in array format e.g. [1, 10, 5]
    """
    for index, instruction in enumerate(input_instruction):

        instruction = (
            instruction.replace("move ", "")
            .replace("from ", "")
            .replace("to ", "")
            .split()
        )
        input_instruction[index] = [int(i) for i in instruction]

    return input_instruction


def part_one(stack_info, input_instructions):

    stacks = load_data(stack_info)

    for instruction in input_instructions:
        move_crates = instruction[0]
        move_from = instruction[1]
        move_to = instruction[2]

        for _ in range(move_crates):
            tmp_crate = stacks[move_from].pop()
            stacks[move_to].append(tmp_crate)

    answer = ""
    for stack in stacks:
        answer += stacks[stack][-1]
    return answer


def part_two(stack_info, input_instructions):
    stacks = load_data(stack_info)

    for instruction in input_instructions:
        move_crates = instruction[0]
        move_from = instruction[1]
        move_to = instruction[2]

        remove_crates = stacks[move_from][-move_crates:]
        stacks[move_from] = stacks[move_from][:-move_crates]

        for crate in remove_crates:
            stacks[move_to].append(crate)

    answer = ""
    for stack in stacks:
        answer += stacks[stack][-1]
    return answer


if __name__ == "__main__":

    # Read in the data
    curr_path = os.path.dirname(os.path.abspath(__file__))
    input_path = "./input.txt"

    with open(os.path.join(curr_path, input_path), "r") as file:
        stack_list, instructions = (
            i.splitlines() for i in file.read().strip("\n").split("\n\n")
        )

    instructions = format_instructions(instructions)

    print(f"Answer for part 1: {part_one(stack_list, instructions)}")
    print(f"Answer for part 2: {part_two(stack_list, instructions)}")
