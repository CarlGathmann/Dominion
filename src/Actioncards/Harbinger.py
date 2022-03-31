import random

from Cardtypes.Actioncard import Actioncard


class Harbinger(Actioncard):
    def __init__(self):
        super().__init__(1, 1, 0, 0, 3)

    def specialAction(self, player):
        if len(player.discardingPile) != 0:
            choice = random.choice(player.discardingPile)
            player.discardingPile.remove(choice)
            player.drawingPile.append(choice)
