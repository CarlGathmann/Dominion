from src.Cardtype.Actioncard import Actioncard


class Market(Actioncard):
    def __init__(self):
        self.expences = 5
        super().__init__(1, 1, 1, 1)
