import pytest
import tests.__init__ as ts


def test_is_player():
    player1 = ts.cards.Hand('player1')
    player2 = ts.cards.Hand('player2')
    player3 = None

    players = [player1, player2]

    assert ts.ask.is_player(player1, players)
    assert not ts.ask.is_player(player3, players)

def test_is_card():
    assert ts.ask.is_card('A', ts.extras.types)

def test_clean_word():

    assert ts.ask.clean_word('WORD') == 'word'
    assert ts.ask.clean_word('WORD ONLY !!! DERP _+@!*(%)') == 'wordonlyderp'

def test_clean_sentence():
    assert ts.ask.clean_sentence('THIS IS A SENTENCE!') == ['this', 'is', 'a', 'sentence']
    assert ts.ask.clean_sentence('123 $$$$$ play```er1') == ['123', 'player1']
