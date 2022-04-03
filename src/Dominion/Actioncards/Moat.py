from src.Dominion.Cardtypes.Actioncard import Actioncard


class Moat(Actioncard):
    def __init__(self):
        super().__init__(2, 0, 0, 0, 2)

    # Moat is realised in attack cards
    def specialAction(self, player, game):
        pass
