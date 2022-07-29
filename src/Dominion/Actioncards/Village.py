from src.Dominion.Cardtypes.ActionCard import ActionCard


class Village(ActionCard):
    EXPENCES = 3
    CARDS = 1
    ACTIONS = 2
    BUYS = 0
    MONEY = 0

    def special_action(self, player, game):
        return
