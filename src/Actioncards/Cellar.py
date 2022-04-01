import random

from src.Cardtypes.Actioncard import Actioncard


class Cellar(Actioncard):
    def __init__(self):
        super().__init__(0, 1, 0, 0, 2)

    def specialAction(self, player, game):
        amount_cards = random.randint(0, len(player.hand))
        choices = player.chooseXCardsFromHand(amount_cards)
        player.dicardListOfCards(choices)
        player.draw(amount_cards)
