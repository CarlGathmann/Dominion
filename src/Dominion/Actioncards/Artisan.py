import random

from src.Dominion.Cardtypes.Actioncard import Actioncard


class Artisan(Actioncard):
    EXPENCES = 6
    CARDS = 0
    ACTIONS = 0
    BUYS = 0
    MONEY = 0

    def specialAction(self, player, game):
        possible_cards = []
        for key in game.gameCards.keys():
            if game.gameCards[key][0].expences <= 5:
                possible_cards.append(game.gameCards[key][0])
        if len(possible_cards) > 0:
            choice = random.choice(possible_cards)
            player.hand.append(game.getCardFromPile(choice))
            second_choice = random.choice(player.hand)
            player.hand.remove(second_choice)
            player.drawingPile.append(second_choice)
            print("taking", choice, "and topdecking", second_choice)

        else:
            print("no cards to take")
