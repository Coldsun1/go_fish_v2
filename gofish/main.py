# Run this to run everythin else
import cards


main_deck = cards.fill_center_deck()

player1 = cards.Hand('player1')
player2 = cards.Hand('player2')

players = [player1, player2]

print(f'Main Deck: {main_deck}\n')

for player in players:
    player.pickup(7, main_deck)
    player.sort()

while True:
