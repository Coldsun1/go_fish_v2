import pytest
from gofish.cards import fill_center_deck, Hand

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
    player2.pickup(7, center_deck)
    player2.sort()
