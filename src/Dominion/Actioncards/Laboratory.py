from src.Dominion.Cardtypes.Actioncard import Actioncard


class Laboratory(Actioncard):
    EXPENCES = 5
    CARDS = 2
    ACTIONS = 1
    BUYS = 0
    MONEY = 0

    def specialAction(self, player, game):
        pass
