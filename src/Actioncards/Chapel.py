import random

from Cardtype.Actioncard import Actioncard
from Player import Player


class Chapel(Actioncard):
    def __init__(self):
        super().__init__(0, 0, 0, 0, 0)

    def specialAction(self):
        # choose random cards to trash
        cards_to_trash = random.randint(0, 4)
        for card in range(cards_to_trash):
            player.hand.remove(random.choice(player.hand))
