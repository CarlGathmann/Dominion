from src.Cardtype.Actioncard import Actioncard


class Village(Actioncard):
    def __init__(self):
        self.expences = 3
        super().__init__(1, 2, 0, 0)