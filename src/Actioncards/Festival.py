from Cardtypes.Actioncard import Actioncard


class Festival(Actioncard):
    def __init__(self):
        super().__init__(0, 2, 1, 2, 5)

    def specialAction(self, hand):
        return
