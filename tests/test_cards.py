import pytest
import random
from gofish import cards, extras


def test_fill_center_deck():
    center_deck = cards.fill_center_deck()

    assert len(center_deck) == 52

def test_pickup():
    center_deck = cards.fill_center_deck()

    player1 = cards.Hand('player1')

    player1.pickup(7, center_deck)
    assert len(player1.hand) == 7

def test_sort():
    center_deck = cards.fill_center_deck()

    player2 = cards.Hand('player2')

    for i in extras.types:
        player2.hand.append(i)

    random.shuffle(player2.hand)

    player2.sort()
    assert player2.hand == extras.types

def test_search_sets():
    player3 = cards.Hand('player3')

    for i in range(4):
        player3.hand.append('A')
        player3.hand.append('Q')

    assert len(player3.hand) == 8

    player3.search_sets()

    assert len(player3.hand) == 0
    assert len(player3.sets) == 2
