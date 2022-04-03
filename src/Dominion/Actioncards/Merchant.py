from src.Dominion.Cardtypes.Actioncard import Actioncard
from src.Dominion.Moneycards.Silver import Silver


class Merchant(Actioncard):
    def __init__(self):
        super().__init__(1, 1, 0, 0, 3)

    def specialAction(self, player, game):
        silver = False
        for moneycard in player.getMoneycardsInHand():
            if not silver:
                if moneycard.__class__ == Silver:
                    print("+1 money from Merchant")
                    player.money += 1
                    silver = True
