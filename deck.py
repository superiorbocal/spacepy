from typing import List, Iterable

import card


class Deck(List[card.Card]):

    def __init__(self, title: str, cards: Iterable[card.Card] = None):
        super().__init__()
        self.title = title
        if cards:
            self.extend(cards)

    def reviewable_cards(self):
        return sorted(filter(lambda x: x.is_reviewable(), self),
                      key=lambda x: x.unix_time_to_review)


def create_test_deck():
    descriptions = ['the powerhouse of the cell',
                    'a delicious fruit',
                    'a disgusting pizza topping',
                    'Why']
    responses = ['mitochondria',
                 'banana',
                 'pineapple',
                 '為什麼']
    cards = [card.Card(d, r) for d, r in zip(descriptions, responses)]
    return Deck('TestDeck', cards)
