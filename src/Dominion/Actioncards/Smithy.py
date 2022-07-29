from src.Dominion.Cardtypes.ActionCard import ActionCard


class Smithy(ActionCard):
    EXPENCES = 4
    CARDS = 3
    ACTIONS = 0
    BUYS = 0
    MONEY = 0

    def special_action(self, player, game):
        return
