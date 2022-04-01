from src.Cardtypes.Actioncard import Actioncard


class Market(Actioncard):
    def __init__(self):
        super().__init__(1, 1, 1, 1, 5)

    def specialAction(self, player, game):
        return
