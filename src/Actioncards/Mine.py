from src.Cardtypes.Actioncard import Actioncard
from src.Moneycards.Copper import Copper
from src.Moneycards.Silver import Silver


class Mine(Actioncard):
    def __init__(self):
        super().__init__(0, 0, 0, 0, 5)

    def specialAction(self, player, game):
        for moneycard in player.getMoneycardsInHand():
            if moneycard.__class__ == Copper:
                try:
                    player.hand.remove(moneycard)
                    game.garbidge.append(moneycard)
                    player.hand.append(game.getCardFromPile("Silver"))
                except KeyError:
                    print('No silver left')

            if moneycard.__class__ == Silver:
                try:
                    player.hand.remove(moneycard)
                    game.garbidge.append(moneycard)
                    player.hand.append(game.getCardFromPile("Gold"))
                except KeyError:
                    print('No gold left')
            else:
                pass
