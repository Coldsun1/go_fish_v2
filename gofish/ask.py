# this will contain operations on cards

# checks to see if player is in game
def is_player(player, players):
    if player in players:
        return True

    elif player not in players:
        return False

# checks if card in cards
def is_card(card, cards):
    if card in cards:
        return True

    elif card not in cards:
        return False

# strip all none alphanumeric charaters
# return cleaned_string
def input_clean(input_string):
    cleaned_string = ''
    allow_char = 'abcdefghijklmnopqrstuvwxyz1234567890'

    for char in input_string:
        if char in allow_char:
            cleaned_string += char

    return cleaned_string
