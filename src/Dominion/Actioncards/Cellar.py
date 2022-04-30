import random

from src.Dominion.Cardtypes.Actioncard import Actioncard


class Cellar(Actioncard):
    EXPENCES = 2
    CARDS = 0
    ACTIONS = 1
    BUYS = 0
    MONEY = 0

    def specialAction(self, player, game):
        amount_cards = random.randint(0, len(player.hand))
        choices = player.chooseXCardsFromHand(amount_cards)
        if amount_cards != 0:
            player.dicardListOfCards(choices)
            player.draw(amount_cards)
        else:
            print("discarding nothing")
