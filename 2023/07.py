from typing import List
from collections import Counter
from load_input import load_data
from icecream import ic

data: List[str] = load_data()
hands_rank = [
    "HighC",
    "OneP",
    "TwoP",
    "ThreeOK",
    "FullHouse",
    "FourOK",
    "FiveOK",
]


class PartOne:
    @staticmethod
    def convert_to_alphabet(hand: str) -> str:
        """
        Converts each alphabet with the largest card to A
        This helps with lexical sorting later on

        Args:
            hand (str): 5 letters of A, K, Q, J, T, 9 to 1

        Returns:
            str: Converted hand with A being the largest card value
        """
        card_mapping = {
            "A": "A",
            "K": "B",
            "Q": "C",
            "J": "D",
            "T": "E",
            "9": "F",
            "8": "G",
            "7": "H",
            "6": "I",
            "5": "J",
            "4": "K",
            "3": "L",
            "2": "M",
        }
        new_hand = ""
        for card in hand:
            new_hand += card_mapping[card]
        return new_hand

    @staticmethod
    def determine_hand(cards: str) -> str:
        """
        Generates the hand type based on the input cards
        Hand types are determined by the counts of cards

        Args:
            cards (str): card combination

        Returns:
            str: type of hand
        """
        card_cnt = Counter(cards)

        # Determine the max value
        max_count = max(card_cnt.values())

        if max_count == 5:
            return "FiveOK"
        elif max_count == 4:
            return "FourOK"
        elif max_count == 3:
            # Check if FH or TOK
            if len(card_cnt) == 2:
                return "FullHouse"
            else:
                return "ThreeOK"
        elif max_count == 2:
            # Check if two pari or one pair
            if len(card_cnt) == 3:
                return "TwoP"
            else:
                return "OneP"
        else:
            return "HighC"


class PartTwo:
    @staticmethod
    def convert_to_alphabet(hand: str) -> str:
        """
        Converts each alphabet with the largest card to A
        This helps with lexical sorting later on

        Args:
            hand (str): 5 letters of A, K, Q, J, T, 9 to 1

        Returns:
            str: Converted hand with A being the largest card value
        """
        card_mapping = {
            "A": "A",
            "K": "B",
            "Q": "C",
            "T": "E",
            "9": "F",
            "8": "G",
            "7": "H",
            "6": "I",
            "5": "J",
            "4": "K",
            "3": "L",
            "2": "M",
            "J": "N",
        }
        new_hand = ""
        for card in hand:
            new_hand += card_mapping[card]
        return new_hand

    @staticmethod
    def determine_hand(cards: str) -> str:
        """
        Generates the hand type based on the input cards
        Hand types are determined by the counts of cards

        Args:
            cards (str): card combination

        Returns:
            str: type of hand
        """
        card_cnt = Counter(cards)
        # Determine the max value
        max_count = max(card_cnt.values())

        if max_count == 5:
            return "FiveOK"
        elif max_count == 4:
            # If there is joker in majority or minority, return FiveOK
            if "N" in card_cnt:
                return "FiveOK"
            return "FourOK"
        elif max_count == 3:
            # Check if FH or TOK
            if len(card_cnt) == 2:
                # if J is present, return FiveOK
                if "N" in card_cnt:
                    return "FiveOK"
                return "FullHouse"
            else:
                if "N" in card_cnt:
                    # if J present in majority/minority, return FourOK
                    return "FourOK"
                return "ThreeOK"
        elif max_count == 2:
            # Check if two pair or one pair
            if len(card_cnt) == 3:
                if "N" in card_cnt and card_cnt["N"] == 2:
                    # One pair is "N", highest possibl is "FourOK"
                    return "FourOK"
                if "N" in card_cnt and card_cnt["N"] == 1:
                    # Only has one "N", highest possible is "ThreeOK"
                    return "ThreeOK"
                return "TwoP"
            else:
                if "N" in card_cnt:
                    # Regardless if "N" has a value of 2 or 1, highest
                    # match is ThreeOK
                    return "ThreeOK"
                return "OneP"
        else:
            if "N" in card_cnt:
                return "OneP"
            return "HighC"


def part_one() -> int:
    # Define the dictionary keys in order from lowest to highest rank
    hands = {
        "HighC": [],
        "OneP": [],
        "TwoP": [],
        "ThreeOK": [],
        "FullHouse": [],
        "FourOK": [],
        "FiveOK": [],
    }

    for d in data:
        hand, bid = d.split(" ")[0], int(d.split(" ")[1])
        hand = PartOne.convert_to_alphabet(hand)

        hand_type = PartOne.determine_hand(hand)
        hands[hand_type].append([hand, bid])

    # for each hand type, we want to sort the order, weakest hand at smaller index
    for h_type, cards in hands.items():
        hands[h_type] = sorted(cards, key=lambda x: x[0], reverse=True)

    rank = 1
    res = 0

    for h_rank in hands_rank:
        card_list = hands[h_rank]
        if card_list:
            for _, bid in card_list:
                res += rank * bid
                rank += 1

    return res


def part_two() -> int:
    # Define the dictionary keys in order from lowest to highest rank
    hands = {
        "HighC": [],
        "OneP": [],
        "TwoP": [],
        "ThreeOK": [],
        "FullHouse": [],
        "FourOK": [],
        "FiveOK": [],
    }

    for d in data:
        hand, bid = d.split(" ")[0], int(d.split(" ")[1])
        hand = PartTwo.convert_to_alphabet(hand)

        hand_type = PartTwo.determine_hand(hand)
        hands[hand_type].append([hand, bid])

    # for each hand type, we want to sort the order, weakest hand at smaller index
    for h_type, cards in hands.items():
        hands[h_type] = sorted(cards, key=lambda x: x[0], reverse=True)
    # ic(hands)
    rank = 1
    res = 0
    for h_rank in hands_rank:
        card_list = hands[h_rank]
        ic(h_rank, card_list)
        if card_list:
            for _, bid in card_list:
                res += rank * bid
                rank += 1
    return res


print(part_one())
print(part_two())
