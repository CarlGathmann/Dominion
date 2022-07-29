from src.Dominion.Cardtypes.ActionCard import ActionCard


class Village(ActionCard):
    def __init__(self):
        super().__init__(1, 2, 0, 0, 3)

    def special_action(self, player, game):
        return
