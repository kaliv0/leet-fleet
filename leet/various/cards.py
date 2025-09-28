# Sort (deck of) cards by value && by suit

from dataclasses import dataclass


@dataclass(frozen=True)
class Card:
    value: str
    suit: str


@dataclass(frozen=True)
class MappedCard:
    key: tuple[int, int]
    # key: int
    card: Card


VALUES_MAP = {'J': 11, 'Q': 12, 'K': 13, 'A': 14}
SUIT_MAP = {'C': 1, 'D': 2, 'H': 3, 'S': 4}  # clubs, diamonds, hearts, spades


def sort_cards(cards):
    sorted_cards = [MappedCard(_construct_key(card), card) for card in cards]
    sorted_cards.sort(key=lambda c: c.key)
    return [item.card for item in sorted_cards]


def _construct_key(card):
    return (int(card.value) if card.value.isdigit() else VALUES_MAP[card.value],
            SUIT_MAP[card.suit])
    ## alternatively use single key -> value * 10 + suit -> first 1 or 2 digits represent value code, last digit is the suit code
    # return (int(card.value) if card.value.isdigit() else VALUES_MAP[card.value]) * 10 + SUIT_MAP[card.suit]


if __name__ == "__main__":
    cards = [
        Card("10", "C"),
        Card("8", "H"),
        Card("K", "H"),
        Card("K", "S"),
        Card("J", "D"),
        Card("A", "D"),
        Card("10", "D"),
        Card("K", "D"),
        Card("K", "C"),
        Card("8", "S"),
    ]
    for card in sort_cards(cards):
        print(f"{card.value}{card.suit}")
