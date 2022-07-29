from src.Dominion.Cardtypes.ActionCard import ActionCard


class Moat(ActionCard):
    EXPENCES = 2
    CARDS = 2
    ACTIONS = 0
    BUYS = 0
    MONEY = 0

    # Moat is realised in attack cards
    def special_action(self, player, game):
        return
