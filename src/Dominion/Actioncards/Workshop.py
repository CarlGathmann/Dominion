import random

from src.Dominion.Cardtypes.Actioncard import Actioncard


class Workshop(Actioncard):
    EXPENCES = 3
    CARDS = 0
    ACTIONS = 0
    BUYS = 0
    MONEY = 0

    def specialAction(self, player, game):
        possible_cards = []
        for key in game.gameCards.keys():
            if game.gameCards[key][0].expences <= 4:
                possible_cards.append(game.gameCards[key][0])
        if len(possible_cards) > 0:
            choice = random.choice(possible_cards)
            player.discardingPile.append(game.getCardFromPile(choice))
            print("taking", choice)
        else:
            print("no cards to take")
