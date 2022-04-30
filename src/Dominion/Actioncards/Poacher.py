import random

from src.Dominion.Cardtypes.Actioncard import Actioncard


class Poacher(Actioncard):
    EXPENCES = 4
    CARDS = 1
    ACTIONS = 1
    BUYS = 0
    MONEY = 1

    def specialAction(self, player, game):
        for i in range(17 - len(game.gameCards)):
            if len(player.hand) != 0:
                choice = random.choice(player.hand)
                print('discarding', choice)
                player.hand.remove(choice)
                player.discardingPile.append(choice)
