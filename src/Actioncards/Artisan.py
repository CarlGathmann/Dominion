import random

from src.Cardtypes.Actioncard import Actioncard


class Artisan(Actioncard):
    def __init__(self):
        super().__init__(0, 0, 0, 0, 6)

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
            print("Taking", choice, "and topdecking", second_choice)

        else:
            print("No cards to take")
