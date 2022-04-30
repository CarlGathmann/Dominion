import random

from src.Dominion.Cardtypes.Actioncard import Actioncard


class Sentury(Actioncard):
    EXPENCES = 5
    CARDS = 1
    ACTIONS = 1
    BUYS = 0
    MONEY = 0

    def specialAction(self, player, game):
        for _ in range(2):
            card = player.drawAndReturn()
            choice = random.randint(0, 2)
            if choice == 0:
                print('discarding', card)
                player.discardingPile.append(card)
            elif choice == 1:
                print('trashing', card)
                game.garbidge.append(card)
            # no choice of order yet
            elif choice == 2:
                print('topdecking', card)
                player.drawingPile.append(card)
