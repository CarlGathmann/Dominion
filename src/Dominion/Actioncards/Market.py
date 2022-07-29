from src.Dominion.Cardtypes.ActionCard import ActionCard


class Market(ActionCard):
    EXPENCES = 5
    CARDS = 1
    ACTIONS = 1
    BUYS = 1
    MONEY = 1

    def special_action(self, player, game):
        return
