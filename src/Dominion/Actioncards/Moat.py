from src.Dominion.Cardtypes.Actioncard import Actioncard


class Moat(Actioncard):
    EXPENCES = 2
    CARDS = 2
    ACTIONS = 0
    BUYS = 0
    MONEY = 0

    # Moat is realised in attack cards
    def specialAction(self, player, game):
        pass
