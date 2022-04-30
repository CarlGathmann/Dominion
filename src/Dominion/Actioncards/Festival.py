from src.Dominion.Cardtypes.Actioncard import Actioncard


class Festival(Actioncard):
    EXPENCES = 5
    CARDS = 0
    ACTIONS = 2
    BUYS = 1
    MONEY = 2

    def specialAction(self, player, game):
        return
