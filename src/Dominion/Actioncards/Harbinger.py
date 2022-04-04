import random

from src.Dominion.Cardtypes.Actioncard import Actioncard


class Harbinger(Actioncard):
    def __init__(self):
        super().__init__(1, 1, 0, 0, 3)

    def specialAction(self, player, game):
        if len(player.discardingPile) != 0:
            choice = random.choice(player.discardingPile)
            print("taking", choice, "from discarding pile")
            player.discardingPile.remove(choice)
            player.drawingPile.append(choice)
        else:
            print("no cards to take from discarding pile")
