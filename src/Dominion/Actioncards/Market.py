from src.Dominion.Cardtypes.Actioncard import Actioncard


class Market(Actioncard):
    EXPENCES = 5
    CARDS = 1
    ACTIONS = 1
    BUYS = 1
    MONEY = 1

    def specialAction(self, player, game):
        return
