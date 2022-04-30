import random

from src.Dominion.Cardtypes.Actioncard import Actioncard


class Harbinger(Actioncard):
    EXPENCES = 3
    CARDS = 1
    ACTIONS = 1
    BUYS = 0
    MONEY = 0

    def specialAction(self, player, game):
        if len(player.discardingPile) != 0:
            choice = random.choice(player.discardingPile)
            print("taking", choice, "from discarding pile")
            player.discardingPile.remove(choice)
            player.drawingPile.append(choice)
        else:
            print("no cards to take from discarding pile")
