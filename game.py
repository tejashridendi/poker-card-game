from card import PokerCard, PokerSuits, PokerValues
import random


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw_cards(self, deck, num=5):
        self.hand = deck[:num]

    def show_hand(self):
        print(f"{self.name}'s hand:")
        for i, card in enumerate(self.hand, 1):
            print(f"{i}. {card}")
        print()

    def discard_and_draw(self, deck, indices):
        for index in sorted(indices, reverse=True):
            self.hand.pop(index)
        self.hand += deck[:len(indices)]


def create_deck():
    return [
        PokerCard(value, suit)
        for suit in PokerSuits
        for value in PokerValues
    ]


def evaluate_hand(hand):
    values = [card.get_value() for card in hand]
    suits = [card.get_suit() for card in hand]

    is_flush = len(set(suits)) == 1
    sorted_values = sorted(values)
    is_straight = (max(sorted_values) - min(sorted_values) == 4) and len(set(sorted_values)) == 5

    if is_straight and is_flush:
        return (8, sorted_values)  # Straight flush
    if len(set(values)) == 2:
        return (7, sorted_values)  # Four of a kind
    if len(set(values)) == 3 and sorted_values.count(sorted_values[0]) in (2, 3):
        return (6, sorted_values)  # Full house
    if is_flush:
        return (5, sorted_values)  # Flush
    if is_straight:
        return (4, sorted_values)  # Straight
    if len(set(values)) == 3:
        return (3, sorted_values)  # Three of a kind
    if len(set(values)) == 4:
        return (2, sorted_values)  # Two pairs
    if len(set(values)) == 5:
        return (1, sorted_values)  # One pair
    return (0, sorted_values)  # High card


def compare_hands(hand1, hand2):
    rank1, key_cards1 = evaluate_hand(hand1)
    rank2, key_cards2 = evaluate_hand(hand2)

    if rank1 > rank2:
        return 1
    elif rank1 < rank2:
        return -1
    else:
        if key_cards1 > key_cards2:
            return 1
        elif key_cards1 < key_cards2:
            return -1
        else:
            return 0


def main():
    deck = create_deck()
    random.shuffle(deck)

    player1_name = input("Enter the name of Player 1: ")
    player2_name = input("Enter the name of Player 2: ")

    player1 = Player(player1_name)
    player2 = Player(player2_name)

    player1.draw_cards(deck, 5)
    player2.draw_cards(deck[5:], 5)

    player1.show_hand()
    player2.show_hand()

    while True:
        discard_indices = input(
            f"{player1.name}, enter the indices of cards to discard (comma separated), or 'none' to keep all: ")
        if discard_indices.lower() != 'none':
            indices = [int(x) - 1 for x in discard_indices.split(',')]
            player1.discard_and_draw(deck[10:], indices)
            player1.show_hand()

        discard_indices = input(
            f"{player2.name}, enter the indices of cards to discard (comma separated), or 'none' to keep all: ")
        if discard_indices.lower() != 'none':
            indices = [int(x) - 1 for x in discard_indices.split(',')]
            player2.discard_and_draw(deck[10 + len(indices):], indices)
            player2.show_hand()

        result = compare_hands(player1.hand, player2.hand)
        if result == 1:
            print(f"{player1.name} wins!")
        elif result == -1:
            print(f"{player2.name} wins!")
        else:
            print("It's a tie!")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break
        deck = create_deck()
        random.shuffle(deck)
        player1.draw_cards(deck, 5)
        player2.draw_cards(deck[5:], 5)
        player1.show_hand()
        player2.show_hand()


if __name__ == "__main__":
    main()
