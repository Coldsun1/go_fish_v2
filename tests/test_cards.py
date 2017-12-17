import pytest
from gofish.cards import fill_center_deck, Hand
import gofish.extras as extras
import random

def test_fill_center_deck():
    center_deck = fill_center_deck()

    assert len(center_deck) == 52

def test_pickup():
    center_deck = fill_center_deck()

    player1 = Hand()

    player1.pickup(7, center_deck)
    assert len(player1.hand) == 7

def test_sort():
    center_deck = fill_center_deck()

    player2 = Hand()

    for i in extras.types:
        player2.hand.append(i)
    random.shuffle(player2.hand)
    
    player2.sort()
    assert player2.hand == extras.types
