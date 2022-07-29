import random

from src.Dominion.Cardtypes.ActionCard import ActionCard


class Cellar(ActionCard):
    EXPENCES = 2
    CARDS = 0
    ACTIONS = 1
    BUYS = 0
    MONEY = 0

    def special_action(self, player, game):
        amount_cards = random.randint(0, len(player.hand))
        choices = player.choose_x_cards_from_hand(amount_cards)
        if amount_cards != 0:
            player.discard_list_of_cards(choices)
            player.draw(amount_cards)
        else:
            print("discarding nothing")
