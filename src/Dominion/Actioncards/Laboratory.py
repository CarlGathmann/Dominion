from src.Dominion.Cardtypes.ActionCard import ActionCard


class Laboratory(ActionCard):
    def __init__(self):
        super(Laboratory, self).__init__(2, 1, 0, 0, 5)

    def special_action(self, player, game):
        pass
