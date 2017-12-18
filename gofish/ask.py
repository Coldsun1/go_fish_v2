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
def clean_word(word):
    cleaned_word = ''
    allow_char = 'abcdefghijklmnopqrstuvwxyz1234567890'

    for char in word.lower():
        if char in allow_char:
            cleaned_word += char

    return cleaned_word

# takes a sentence and returns a list with the words
def clean_sentence(sentence):
    cleaned_sentence = []

    words = sentence.split()

    for word in words:
        cleaned_sentence.append(clean_word(word))

    cleaned_sentence = list(filter(None, cleaned_sentence))

    return cleaned_sentence
