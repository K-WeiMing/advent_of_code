import os


# ===== CONSTANTS HERE USED FOR PART 1 =====

# Rock (1 points) [A, X]
# Paper (2 points) [B, Y]
# Scissors (3 points) [C, Z]

# Outcomes:
# Loss -> 0 points
# Draw -> 3 points
# Win -> 6 points

HAND_MAP = {"X": 1, "Y": 2, "Z": 3}
MAP_TO_SYMBOL = {
    "A": "Rock",
    "X": "Rock",
    "B": "Paper",
    "Y": "Paper",
    "C": "Scissors",
    "Z": "Scissors",
}

# ===== CONSTANTS HERE USED FOR PART 2 =====

# Scores of the results for part 2
OUTCOME_MAP = {"X": 0, "Y": 3, "Z": 6}
MAP_TO_OUTCOME = {"X": "Lose", "Y": "Draw", "Z": "Win"}
SYMBOL_SCORE = {"Rock": 1, "Paper": 2, "Scissors": 3}


def get_game_score(opponent: str, yourself: str) -> int:
    """Computes the outcome to Win / Loss / Draw and returns the result

    Args:
        opponent (str): 'Rock' / 'Paper' / 'Scissors
        yourself (str): 'Rock' / 'Paper' / 'Scissors

    Returns:
        int: Win-> 6, Draw-> 3, Lose-> 0
    """

    MAP_SCORE = {"Rock": 0, "Paper": 1, "Scissors": 2}

    opponent_value = MAP_SCORE[opponent]
    your_value = MAP_SCORE[yourself]

    # Only possible outcomes:
    # Rock - Scissors -> -2 (Win)
    # Scissors - Rock -> 2 (Lose)

    # Paper - Rock -> 1 (Win)
    # Rock - Paper -> -1 (Lose)

    # Scissors - Paper -> 1 (Win)
    # Paper - Scissors -> -1 (Lose)

    # Win Conditions: -2, 1
    # Lose Conditions: 2, -1

    if your_value == opponent_value:
        # Draw condition
        return 3
    if your_value - opponent_value == -2 or your_value - opponent_value == 1:
        # Rock > Scissors = -2, Scissors > Paper = 1, Paper > Rock = 1
        return 6
    return 0


def determine_symbol(opponent: str, outcome: str) -> str:
    """Determines the hand you need to show to have the outcome required of
    -> Win / Lose / Draw

    Args:
        opponent (str): Rock / Paper / Scissors
        outcome (str): Win / Lose / Draw

    Returns:
        str: Rock / Paper / Scissors
    """

    if outcome == "Draw":
        return opponent

    # Determine win {opponent_hand: player_hand_to_win}
    PLAYER_WIN = {"Rock": "Paper", "Paper": "Scissors", "Scissors": "Rock"}
    if outcome == "Win":
        return PLAYER_WIN[opponent]
    # Determine lose {opponent_hand: player_hand_to_win}
    OPPONENT_WIN = {"Rock": "Scissors", "Scissors": "Paper", "Paper": "Rock"}
    return OPPONENT_WIN[opponent]


def part_one(data: list):
    # Time complexity: O(n)
    # Space complexity: O(1)

    curr_score = 0
    for game in data:
        opponent, player = game.split()
        curr_score += HAND_MAP[player]

        # Determine if win/loss/draw
        curr_score += get_game_score(MAP_TO_SYMBOL[opponent], MAP_TO_SYMBOL[player])

    return curr_score


def part_two(data: list):
    # Time complexity: O(n)
    # Space complexity: O(1)

    curr_score = 0

    for game in data:
        opponent, player = game.split()
        curr_score += OUTCOME_MAP[player]  # Add final game result to the score first

        # Determine the symbol required to win/lose/draw
        player_hand = determine_symbol(MAP_TO_SYMBOL[opponent], MAP_TO_OUTCOME[player])
        curr_score += SYMBOL_SCORE[player_hand]

    return curr_score


if __name__ == "__main__":
    # Read in the data
    curr_path = os.path.dirname(os.path.abspath(__file__))
    input_path = "./input.txt"
    with open(os.path.join(curr_path, input_path), "r") as file:
        data = file.readlines()
    # Replace '\n' in the inputs
    data = [str(i.replace("\n", "")) for i in data]

    print(f"Answer for part 1: {part_one(data)}")
    print(f"Answer for part 2: {part_two(data)}")
