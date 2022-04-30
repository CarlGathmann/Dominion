from src.Dominion.Cardtypes.Actioncard import Actioncard
from src.Dominion.Moneycards.Silver import Silver


class Merchant(Actioncard):
    EXPENCES = 3
    CARDS = 1
    ACTIONS = 1
    BUYS = 0
    MONEY = 0

    def specialAction(self, player, game):
        silver = False
        for moneycard in player.getMoneycardsInHand():
            if not silver:
                if moneycard.__class__ == Silver:
                    print("+1 money from Merchant")
                    player.money += 1
                    silver = True
