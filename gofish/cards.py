# main deck, player's decks
import random
from gofish import extras

# returns a list of 52 hand
def fill_center_deck():
    deck = []
    for single_type in extras.types:
        for line in range(4):
            deck.append(single_type)

    random.shuffle(deck)
    return deck


class Hand(object):

    # contains self.hand
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.sets = []

    # appends n hand, from center_deck, to self.hand
    def pickup(self, n, center_deck):
        for _ in range(n):
            self.hand.append(center_deck.pop())

    # sorts self.hand
    def sort(self):
        self.hand = sorted(self.hand, key=extras.types.index)

    # look for sets of 4 hand in self.hand
    def search_sets(self):
        for i in extras.types:
            if self.hand.count(i) >= 4:
                for _ in range(4):
                    self.hand.remove(i)

                self.sets.append(i)
