from src.Dominion.Cardtypes.ActionCard import ActionCard


class Laboratory(ActionCard):
    EXPENCES = 5
    CARDS = 2
    ACTIONS = 1
    BUYS = 0
    MONEY = 0

    def special_action(self, player, game):
        return
