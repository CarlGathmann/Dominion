from Cardtype.Actioncard import Actioncard
from Player import Player


class Market(Actioncard):
    def __init__(self):
        super().__init__(1, 1, 1, 1, 5)

    def specialAction(self):
        return
