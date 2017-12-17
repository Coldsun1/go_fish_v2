# contains everything extra

types = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']







# Checks to see it someone in the game won
def test_win(player_dict):

    empty = 0

    for k, v in player_dict.items():
        if len(v.cards) == 0:
            empty += 1

    if len(Player.cards) == 0 and empty == len(player_dict):
        print("End game!")

        temp_dict = {}

        for k, v in player_dict.items():
            v.look_for_sets()
            temp_dict[v.name] = len(v.card_sets)

        winner = max(temp_dict, key=temp_dict.get)
        print(f'{winner} won!')
        exit(0)

# old
def check_inquire_input(player, choice_player, choice_card):
    types = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    choice_player = choice_player.strip().lower()
    choice_card = choice_card.strip().upper()

    if choice_player not in player.player_dict:
        print("Invalid Player.")
        print('Re-enter your player choice.')
        choice_player = input('Enter the player name -> ')
        check_inquire_input(player, choice_player, choice_card)

    elif choice_card not in types:
        print("Invalid Card Type.")
        print('Re-enter your card choice.')
        choice_card = input('Enter the card type -> ')
        check_inquire_input(player, choice_player, choice_card)

    return choice_player, choice_card

# old
def inquire(player):
    current_cards = len(player.cards)
    response = ['Inquire']
    while True:
        screen(response, player)

        choice_player = input('Enter the player name -> ')
        choice_card = input('Enter the card type -> ')

        choice_player, choice_card = check_inquire_input(player, choice_player, choice_card)

        taken = 0
        if choice_card in player.player_dict[choice_player].cards:
            for i in player.player_dict[choice_player].cards:
                if choice_card == i:
                    player.cards.append(choice_card)
                    taken += 1

            for _ in range(taken):
                player.player_dict[choice_player].cards.remove(choice_card)

            response = [f"You took {taken} '{choice_card}' card from {choice_player}.",
                         "You can ask another time."]

        elif choice_card not in player.player_dict[choice_player].cards and current_cards == len(player.cards):
            response = [f"{choice_player} didn't have any '{choice_card}' cards.",
                         "Pick up a card instead."]
            return response

        elif choice_card not in player.player_dict[choice_player].cards and current_cards < len(player.cards):
            response = [f"{choice_player} didn't have any '{choice_card}' cards."]
            return response

        else:
            response = ['LOCATION inquire(): INPUT INVALID']
            screen(response, player)
