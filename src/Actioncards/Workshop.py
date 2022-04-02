import random

from src.Cardtypes.Actioncard import Actioncard


class Workshop(Actioncard):
    def __init__(self):
        super().__init__(0, 0, 0, 0, 3)

    def specialAction(self, player, game):
        possible_cards = []
        for key in game.gameCards.keys():
            if game.gameCards[key][0].expences <= 4:
                possible_cards.append(game.gameCards[key][0])
        if len(possible_cards) > 0:
            choice = random.choice(possible_cards)
            player.discardingPile.append(game.getCardFromPile(choice))
            print("Taking", choice)
        else:
            print("No cards to take")
