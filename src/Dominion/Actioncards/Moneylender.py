import random

from src.Dominion.Cardtypes.ActionCard import ActionCard
from src.Dominion.Moneycards.Copper import Copper


class Moneylender(ActionCard):
    def __init__(self):
        super(Moneylender, self).__init__(0, 0, 0, 0, 4)

    def special_action(self, player, game):
        trashed = False
        money_cards = player.get_money_cards_in_hand()
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
