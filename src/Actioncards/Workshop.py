import random

from src.Cardtypes.Actioncard import Actioncard


class Workshop(Actioncard):
    def __init__(self):
        super().__init__(0, 0, 0, 0, 3)

    def specialAction(self, player, game):
        possible_cards = []
        for option in game.card_expences.keys():
            if option <= 4:
                possible_cards += game.card_expences[option]
        choice = random.choice(possible_cards)
        player.discardingPile.append(choice)
        print("Taking", choice)
