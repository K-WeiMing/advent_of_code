import os


def part_one(data: list):
    # Time complexity: O(m*n)
    # Space complexity: O(1)
    ROWS, COLS = len(data), len(data[0])

    # Get all the trees along the edges
    edges = ROWS * 2 + (COLS - 2) * 2
    total = edges

    for row in range(1, ROWS - 1):
        for col in range(1, COLS - 1):
            # Iterate through all the trees
            tree = data[row][col]

            # Get all the trees to the left, right, above and bottom
            left = [data[row][col - i] for i in range(1, col + 1)]
            right = [data[row][col + i] for i in range(1, COLS - col)]
            top = [data[row - i][col] for i in range(1, row + 1)]
            bottom = [data[row + i][col] for i in range(1, ROWS - row)]

            # Checking the tallest tree on every side
            if (
                max(left) < tree
                or max(right) < tree
                or max(top) < tree
                or max(bottom) < tree
            ):
                total += 1

    return total


def part_two(data: list):
    # Time complexity: O(m*n)
    # Space complexity: O(1)
    ROWS, COLS = len(data), len(data[0])
    scores = []
    for row in range(1, ROWS - 1):
        for col in range(1, COLS - 1):
            # Iterate through all the trees
            tree = data[row][col]

            # Get all the trees to the left, right, above and bottom
            left = [data[row][col - i] for i in range(1, col + 1)]
            right = [data[row][col + i] for i in range(1, COLS - col)]
            top = [data[row - i][col] for i in range(1, row + 1)]
            bottom = [data[row + i][col] for i in range(1, ROWS - row)]

            score = 1
            for lst in (left, right, top, bottom):
                tracker = 0
                for i in range(len(lst)):
                    if lst[i] < tree:
                        tracker += 1
                    elif lst[i] == tree:
                        tracker += 1
                        break
                    else:
                        break
                score *= tracker
            scores.append(score)

    return max(scores)


if __name__ == "__main__":
    # Read in the data
    curr_path = os.path.dirname(os.path.abspath(__file__))
    input_path = "./input.txt"
    with open(os.path.join(curr_path, input_path), "r") as file:
        data = file.read().splitlines()

    print(f"Answer for part 1: {part_one(data)}")
    print(f"Answer for part 2: {part_two(data)}")
