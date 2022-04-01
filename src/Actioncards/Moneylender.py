import random

from src.Cardtypes.Actioncard import Actioncard
from src.Moneycards.Copper import Copper


class Moneylender(Actioncard):
    def __init__(self):
        super(Moneylender, self).__init__(0, 0, 0, 0, 4)

    def specialAction(self, player, game):
        trashed = False
        if random.randint(0, 1) == 1:
            money_cards = player.getMoneycardsInHand()
            for card in money_cards:
                if not trashed:
                    if card.__class__ == Copper:
                        print("trashing Copper for +3")
                        player.hand.remove(card)
                        player.money += 3
                        trashed = True
        else:
            return
