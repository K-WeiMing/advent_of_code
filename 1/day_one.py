import os


def part_one(data: list):
    # Time complexity: O(n)
    # Space complexity: O(1) -> for part 1
    # Space complexity: O(n) -> for inclusion of part 2

    # For this section, included an alternative solution for part 2
    # that requires O(n) space complexity

    # Get the elf with the highest number of calories
    max_calories = curr_sum = 0
    calories_list = []

    for index, calories in enumerate(data):
        if calories != "":
            curr_sum += int(calories)

            if index == len(data) - 1:  # Condition once it hits end of the list
                max_calories = max(curr_sum, max_calories)
                calories_list.append(curr_sum)
        else:
            max_calories = max(curr_sum, max_calories)
            calories_list.append(curr_sum)
            curr_sum = 0

    print(f"Elf with the highest calories: {max_calories}")
    calories_list.sort()
    calories_list = calories_list[::-1]
    print(f"Calories of top 3 elves: {calories_list[:3]}")
    print(f"Sum of calories for top 3 elves: {sum(calories_list[:3])}")


def part_two(data: list):
    # Time complexity: O(n)
    # Space complexity: (1)

    def update_calories_list(calories, calories_list):
        if len(calories_list) < 3:
            calories_list.append(calories)
            return calories_list

        if calories > min(calories_list):
            calories_list.remove(min(calories_list))
            calories_list.append(calories)
        return calories_list

    calories_list = []
    curr_sum = 0

    for index, calories in enumerate(data):
        if calories != "":
            curr_sum += int(calories)

            if index == len(data) - 1:
                calories_list = update_calories_list(curr_sum, calories_list)
        else:
            calories_list = update_calories_list(curr_sum, calories_list)
            curr_sum = 0

    print(f"Sum of calories for top 3 elves: {sum(calories_list)}")


if __name__ == "__main__":
    # Read in the data
    curr_path = os.path.dirname(os.path.abspath(__file__))
    input_path = "./input.txt"
    with open(os.path.join(curr_path, input_path), "r") as file:
        data = file.readlines()
    # Replace '\n' in the inputs
    data = [str(i.replace("\n", "")) for i in data]

    part_one(data)
    part_two(data)
