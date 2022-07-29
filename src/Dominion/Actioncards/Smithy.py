from src.Dominion.Cardtypes.ActionCard import ActionCard


class Smithy(ActionCard):
    def __init__(self):
        super().__init__(3, 0, 0, 0, 4)

    def special_action(self, player, game):
        return
