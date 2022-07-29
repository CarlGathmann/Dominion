import random

from src.Dominion.Cardtypes.ActionCard import ActionCard


class Cellar(ActionCard):
    def __init__(self):
        super().__init__(0, 1, 0, 0, 2)

    def special_action(self, player, game):
        amount_cards = random.randint(0, len(player.hand))
        choices = player.choose_x_cards_from_hand(amount_cards)
        if amount_cards != 0:
            player.discard_list_of_cards(choices)
            player.draw(amount_cards)
        else:
            print("discarding nothing")
