from Cardtypes.Actioncard import Actioncard
from Moneycards.Silver import Silver


class Merchant(Actioncard):
    def __init__(self):
        super().__init__(1, 1, 0, 0, 3)

    def specialAction(self, player):
        counter = 0
        for moneycard in player.getMoneycardsInHand():
            if counter == 0:
                if moneycard.__class__ == Silver:
                    player.money += 1
                    counter += 1
