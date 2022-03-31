import random

from Cardtypes.Actioncard import Actioncard


class Cellar(Actioncard):
    def __init__(self):
        super().__init__(0, 1, 0, 0, 2)

    def specialAction(self, player):
        amount_cards = random.randint(0, len(player.hand))
        print("Discarding", amount_cards, "cards...")
        choice = player.chooseXCardsFromHand(amount_cards)
        player.dicardAmountOfCards(choice)
        player.draw(amount_cards)
