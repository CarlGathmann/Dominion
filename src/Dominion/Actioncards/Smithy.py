from src.Dominion.Cardtypes.Actioncard import Actioncard


class Smithy(Actioncard):
    def __init__(self):
        super().__init__(3, 0, 0, 0, 4)

    def specialAction(self, player, game):
        return
