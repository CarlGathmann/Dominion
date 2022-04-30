from src.Dominion.Cardtypes.Actioncard import Actioncard


class Smithy(Actioncard):
    EXPENCES = 4
    CARDS = 3
    ACTIONS = 0
    BUYS = 0
    MONEY = 0

    def specialAction(self, player, game):
        return
