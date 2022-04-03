from src.Dominion.Cardtypes.Actioncard import Actioncard


class Laboratory(Actioncard):
    def __init__(self):
        super(Laboratory, self).__init__(2, 1, 0, 0, 5)

    def specialAction(self, player, game):
        pass
