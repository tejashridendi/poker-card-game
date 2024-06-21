from enum import Enum


class PokerSuits(Enum):
    HEARTS = 1
    DIAMONDS = 2
    CLUBS = 3
    SPADES = 4


class PokerValues(Enum):
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13


class PokerCard:
    def __init__(self, value, suit):
        if isinstance(value, PokerValues) and isinstance(suit, PokerSuits):
            self.VALUE = value
            self.SUIT = suit
        else:
            raise ValueError("value must be an instance of PokerValues and suit must be an instance of PokerSuits")

    def get_value(self):
        return self.VALUE.value

    def get_suit(self):
        return self.SUIT

    def __str__(self):
        return f"{self.VALUE.name} of {self.SUIT.name}"

    def __repr__(self):
        return self.__str__()


if __name__ == "__main__":
    deck = [
        PokerCard(value, suit)
        for suit in PokerSuits
        for value in PokerValues
    ]
    print(deck)
