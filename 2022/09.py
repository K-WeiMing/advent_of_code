import os
import numpy as np

# Create a dictionary to map tail movement based on head & tail difference
TAIL_UPDATE = {
    # head -> 2 up, 1 right, tail 1 up, 1 right (diagonal)
    (2, 1): (1, 1),
    # head -> 1 up, 2 right
    (1, 2): (1, 1),
    # head -> 2 up
    (2, 0): (1, 0),
    # head -> 2 up, 1 left
    (2, -1): (1, -1),
    # head -> 1 up, 2 left
    (1, -2): (1, -1),
    # head -> 2 left
    (0, -2): (0, -1),
    # head -> 1 down, 2 left
    (-1, -2): (-1, -1),
    # head -> 2 down, 1 left
    (-2, -1): (-1, -1),
    # head -> 2 left
    (-2, 0): (-1, 0),
    # head -> 2 down, 1 right
    (-2, 1): (-1, 1),
    # head -> 1 down, 2 right
    (-1, 2): (-1, 1),
    # head -> 2 right
    (0, 2): (0, 1),
    # Include additional cases for p2:
    # positions can now move diagonally for tails after the head
    (2, 2): (1, 1),
    (-2, -2): (-1, -1),
    (-2, 2): (-1, 1),
    (2, -2): (1, -1),
}


def part_one(data: list):
    # Time complexity: O(n)
    # Space complexity: O(n)

    # Use a array to keep track of the positions for H and T
    # Note that the starting position fo H and T are the same
    # Initialize both to 0, 0
    head, tail = np.array([0, 0]), np.array([0, 0])

    # Keep track of all tail positons
    tail_positions = set([tuple(tail)])

    for movement in data:
        direction, distance = movement.split()
        distance = int(distance)
        while distance > 0:
            head = head_update(head, direction)
            distance -= 1
            tail = tail_update(head, tail)
            tail_positions.add(tuple(tail))
    return len(tail_positions)


def part_two(data: list):
    # Time complexity: O(n)
    # Space complexity: O(n)

    rope = [np.array([0, 0]) for _ in range(10)]
    # Get the initialized tail position
    tail_positions = set([tuple(rope[9])])

    # Update each rope segment for each movement
    for movement in data:
        direction, distance = movement.split()
        distance = int(distance)
        while distance > 0:
            rope[0] = head_update(rope[0], direction)
            distance -= 1
            # Update each subsequent knot's position
            for i in range(1, len(rope)):
                rope[i] = tail_update(rope[i - 1], rope[i])
            tail_positions.add(tuple(rope[9]))
    return len(tail_positions)


def tail_update(head: np.array, tail: np.array) -> np.array:
    # Function to track the tail movements w.r.t. head position
    diff = head - tail

    # Since dictionaries don't take arrays, we need to store the results in a tuple
    tail_pos = tail + np.array(TAIL_UPDATE.get(tuple(diff), (0, 0)))
    return tail_pos


def head_update(head: np.array, direction: str) -> np.array:
    if direction == "R":
        head[1] += 1
    elif direction == "L":
        head[1] -= 1
    elif direction == "U":
        head[0] += 1
    elif direction == "D":
        head[0] -= 1
    return head


if __name__ == "__main__":
    # Read in the data
    curr_path = os.path.dirname(os.path.abspath(__file__))
    input_path = "./input.txt"
    with open(os.path.join(curr_path, input_path), "r") as file:
        data = file.read().splitlines()

    print(f"Answer for part 1: {part_one(data)}")
    print(f"Answer for part 2: {part_two(data)}")
