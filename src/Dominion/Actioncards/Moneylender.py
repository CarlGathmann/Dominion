import random

from src.Dominion.Cardtypes.Actioncard import Actioncard
from src.Dominion.Moneycards.Copper import Copper


class Moneylender(Actioncard):
    EXPENCES = 4
    CARDS = 0
    ACTIONS = 0
    BUYS = 0
    MONEY = 0

    def specialAction(self, player, game):
        trashed = False
        money_cards = player.getMoneycardsInHand()
        if len(money_cards) > 0:
            if random.randint(0, 1) == 1:
                for card in money_cards:
                    if not trashed and card.__class__ == Copper:
                        print("trashing Copper for +3")
                        player.hand.remove(card)
                        player.money += 3
                        trashed = True
            else:
                print("not trashing copper")
        else:
            print("no copper in hand")
