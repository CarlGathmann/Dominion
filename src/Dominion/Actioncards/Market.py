from src.Dominion.Cardtypes.ActionCard import ActionCard


class Market(ActionCard):
    def __init__(self):
        super().__init__(1, 1, 1, 1, 5)

    def special_action(self, player, game):
        return
