import random

from src.Cardtypes.Actioncard import Actioncard


class Poacher(Actioncard):
    def __init__(self):
        super().__init__(1, 1, 0, 1, 4)

    def specialAction(self, player, game):
        for i in range(17 - len(game.gameCards.keys())):
            if len(player.hand) != 0:
                choice = random.choice(player.hand)
                print('discarding', choice)
                player.hand.remove(choice)
                player.discardingPile.append(choice)
