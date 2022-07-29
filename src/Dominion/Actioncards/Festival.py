from src.Dominion.Cardtypes.ActionCard import ActionCard


class Festival(ActionCard):
    def __init__(self):
        super().__init__(0, 2, 1, 2, 5)

    def special_action(self, player, game):
        return
