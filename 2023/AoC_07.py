from __future__ import annotations

import re
from collections import Counter
from dataclasses import dataclass
from typing import Callable, DefaultDict, Dict, List, NamedTuple, Set, Tuple, Union

from aocd.models import Puzzle

# get puzzle
puzzle = Puzzle(year=2023, day=7)

TEST_INPUT = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""

CARD_ORDER = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
CARD_ORDER_NEW_RULES = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']
HAND_ORDER = ['High card', 'One pair', 'Two pair', 'Three of a kind', 'Full house', 'Four of a kind', 'Five of a kind']


@dataclass(eq=True, frozen=True)
class Card:
    card: str
    new_rules: bool = False

    def __lt__(self, other):
        if self.new_rules:
            return CARD_ORDER_NEW_RULES.index(self.card) < CARD_ORDER_NEW_RULES.index(other.card)
        return CARD_ORDER.index(self.card) < CARD_ORDER.index(other.card)

    def __repr__(self) -> str:
        return self.card


@dataclass(eq=True, frozen=True)
class HandType:
    hand_type: str

    def __lt__(self, other):
        return HAND_ORDER.index(self.hand_type) < HAND_ORDER.index(other.hand_type)

    def __repr__(self) -> str:
        return self.hand_type


@dataclass
class Hand:
    cards: List[Card]
    bid: int
    new_rules: bool = False

    @staticmethod
    def parse_hand_str(input_str, new_rules=False) -> Hand:
        hand, bid = input_str.split()
        return Hand([Card(c, new_rules) for c in hand], int(bid), new_rules)

    def evaluate_hand(self) -> HandType:
        if self.new_rules:
            non_jokers = [card for card in self.cards if card.card != 'J']
            number_of_jokers = 5 - len(non_jokers)
            if number_of_jokers == 5:
                counter_values = [5]
            else:
                counter_values = sorted(Counter(non_jokers).values(), reverse=True)
                counter_values[0] += number_of_jokers
        else:
            counter_values = sorted(Counter(self.cards).values(), reverse=True)

        return self._evaluate_card_counter(counter_values)

    @staticmethod
    def _evaluate_card_counter(counter_values):
        if counter_values[0] == 5:
            return HandType('Five of a kind')
        if counter_values[0] == 4:
            return HandType('Four of a kind')
        if counter_values[0] == 3 and counter_values[1] == 2:
            return HandType('Full house')
        if counter_values[0] == 3:
            return HandType('Three of a kind')
        if counter_values[0] == 2 and counter_values[1] == 2:
            return HandType('Two pair')
        if counter_values[0] == 2:
            return HandType('One pair')
        return HandType('High card')

    def __lt__(self, other):
        if self.evaluate_hand() < other.evaluate_hand():
            return True
        if self.evaluate_hand() > other.evaluate_hand():
            return False
        # compare cards
        for card_self, card_other in zip(self.cards, other.cards):
            if card_self < card_other:
                return True
            if card_self > card_other:
                return False
        return False


@dataclass
class PokerHands:
    hands: List[Hand]
    new_rules: bool = False

    @staticmethod
    def parse_input(input_str, new_rules=False) -> PokerHands:
        return PokerHands([Hand.parse_hand_str(line, new_rules) for line in input_str.split('\n')])

    def total_winnings(self) -> int:
        return sum([rank * hand.bid for rank, hand in enumerate(sorted(self.hands), start=1)])


def part_one(input_str) -> int:
    return PokerHands.parse_input(input_str).total_winnings()


def part_two(input_str) -> int:
    return PokerHands.parse_input(input_str, new_rules=True).total_winnings()


if __name__ == "__main__":
    # test pt 1
    print(part_one(TEST_INPUT))

    # pt 1
    print(part_one(puzzle.input_data))

    # test pt 2
    print(part_two(TEST_INPUT))

    # pt 2
    print(part_two(puzzle.input_data))
