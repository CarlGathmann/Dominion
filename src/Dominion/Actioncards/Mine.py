import random

from src.Dominion.Cardtypes.Actioncard import Actioncard
from src.Dominion.Moneycards.Copper import Copper
from src.Dominion.Moneycards.Silver import Silver


class Mine(Actioncard):
    def __init__(self):
        super().__init__(0, 0, 0, 0, 5)

    def specialAction(self, player, game):
        money_cards = player.getMoneycardsInHand()
        if len(money_cards) > 0:
            choice = random.choice(money_cards)
            if choice.__class__ == Copper:
                try:
                    player.hand.remove(choice)
                    game.garbidge.append(choice)
                    player.hand.append(game.getCardFromPile("Silver"))
                    print("trashing a Copper for a Silver")
                except KeyError:
                    print('no Silver left')

            elif choice.__class__ == Silver:
                try:
                    player.hand.remove(choice)
                    game.garbidge.append(choice)
                    player.hand.append(game.getCardFromPile("Gold"))
                    print("trashing a Silver for a Gold")
                except KeyError:
                    print('no Gold left')
            else:
                pass
