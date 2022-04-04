from src.Dominion.Cardtypes.Actioncard import Actioncard


class Village(Actioncard):
    def __init__(self):
        super().__init__(1, 2, 0, 0, 3)

    def specialAction(self, player, game):
        return
