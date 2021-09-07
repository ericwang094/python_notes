import collections
Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchCard:

    suits = ['hearts', 'diamonds', 'clubs', 'spades']
    ranks = [x for x in range(2, 11)] + list("JQKA")

    def __init__(self):
        self._cards = [Card(rank, suit) for rank in self.ranks for suit in self.suits]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


deck = FrenchCard()

from random import choice
print(choice(deck))
print(choice(deck))
print(choice(deck))
print(choice(deck))

print(deck[-1])


Point = collections.namedtuple('Point', ['x', 'y', 'z', 'x'], rename=True, defaults=[1, 2])

test1 = Point(3,4)

print(test1)