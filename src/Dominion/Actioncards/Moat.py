from src.Dominion.Cardtypes.ActionCard import ActionCard


class Moat(ActionCard):
    def __init__(self):
        super().__init__(2, 0, 0, 0, 2)

    # Moat is realised in attack cards
    def special_action(self, player, game):
        pass
