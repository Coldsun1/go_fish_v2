import pytest
import random
import tests.__init__ as ts


def test_fill_center_deck():
    center_deck = ts.cards.fill_center_deck()

    assert len(center_deck) == 52

def test_pickup():
    center_deck = ts.cards.fill_center_deck()

    player1 = ts.cards.Hand('player1')

    player1.pickup(7, center_deck)
    assert len(player1.hand) == 7

def test_sort():
    center_deck = ts.cards.fill_center_deck()

    player2 = ts.cards.Hand('player2')

    for i in ts.extras.types:
        player2.hand.append(i)
    random.shuffle(player2.hand)

    player2.sort()
    assert player2.hand == ts.extras.types

def test_search_sets():
    player3 = ts.cards.Hand('player3')

    for i in range(4):
        player3.hand.append('A')
        player3.hand.append('Q')

    assert len(player3.hand) == 8

    player3.search_sets()

    assert len(player3.hand) == 0
    assert len(player3.sets) == 2
