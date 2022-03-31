import random

import AllCards
from Cardtypes.Actioncard import Actioncard


class Workshop(Actioncard):
    def __init__(self):
        super().__init__(0, 0, 0, 0, 3)

    def specialAction(self, player):
        possible_cards = []
        for option in AllCards.cardlist.keys():
            if option <= 4:
                possible_cards += AllCards.cardlist[option]
        choice = random.choice(possible_cards)
        player.discardingPile.append(choice)
        print("Taking", choice)
