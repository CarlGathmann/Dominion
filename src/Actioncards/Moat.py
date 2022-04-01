from src.Cardtypes.Actioncard import Actioncard


class Moat(Actioncard):
    def __init__(self):
        super().__init__(2, 0, 0, 0, 2)

    # if Moat is in Hand player cant be attacked
    def specialAction(self, player, game):
        player.CanBeAttacked = False
