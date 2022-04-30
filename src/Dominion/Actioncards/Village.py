from src.Dominion.Cardtypes.Actioncard import Actioncard


class Village(Actioncard):
    EXPENCES = 3
    CARDS = 1
    ACTIONS = 2
    BUYS = 0
    MONEY = 0

    def specialAction(self, player, game):
        return
