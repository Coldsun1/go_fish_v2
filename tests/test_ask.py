import pytest
import tests.__init__ as ts


def test_is_player():
    player1 = ts.cards.Hand('player1')
    player2 = ts.cards.Hand('player2')

    players = [player1, player2]

    assert ts.ask.is_player(player1, players)
