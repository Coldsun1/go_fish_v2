import pytest
from gofish import ask, cards, extras


def test_is_player():
    player1 = cards.Hand('player1')
    player2 = cards.Hand('player2')
    player3 = None

    players = [player1, player2]

    assert ask.is_player(player1, players)
    assert not ask.is_player(player3, players)

def test_is_card():
    assert ask.is_card('A', extras.types)

def test_clean_word():

    assert ask.clean_word('WORD') == 'word'
    assert ask.clean_word('WORD ONLY !!! DERP _+@!*(%)') == 'wordonlyderp'

def test_clean_sentence():
    assert ask.clean_sentence('THIS IS A SENTENCE!') == ['this', 'is', 'a', 'sentence']
    assert ask.clean_sentence('123 $$$$$ play```er1') == ['123', 'player1']
