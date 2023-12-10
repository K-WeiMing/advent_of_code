from load_input import load_data
from typing import List

data: List[str] = load_data()


CUBE_LIMITS = {"red": 12, "green": 13, "blue": 14}


def part_one():
    res = 0

    for d in data:
        game_str, cubes = d.split(":")[0], d.split(":")[1].lstrip()
        game_id = int(game_str.split(" ")[1])

        # Iterate through cubes to check if the game is possible
        games = cubes.split(";")
        is_possible = True
        for game in games:
            if is_possible:
                for g in game.split(","):
                    cube_cnt, colour = (
                        int(g.lstrip().split(" ")[0]),
                        g.lstrip().split(" ")[1],
                    )
                    if cube_cnt > CUBE_LIMITS[colour]:
                        is_possible = False
                        break

        if is_possible:
            res += game_id
    return res


def part_two():
    res = 0

    for d in data:
        game_str, cubes = d.split(":")[0], d.split(":")[1].lstrip()

        # Iterate through cubes to check if the game is possible
        games = cubes.split(";")
        colour_cnt = {"red": 0, "blue": 0, "green": 0}
        for game in games:
            for g in game.split(","):
                cube_cnt, colour = (
                    int(g.lstrip().split(" ")[0]),
                    g.lstrip().split(" ")[1],
                )
                # Update colour_cnt to have the maximum value
                colour_cnt[colour] = max(colour_cnt.get(colour), cube_cnt)

        # Get the power sum
        power_sum = 1
        for colour, counts in colour_cnt.items():
            power_sum *= counts
        res += power_sum

    return res


print(part_one())
print(part_two())
