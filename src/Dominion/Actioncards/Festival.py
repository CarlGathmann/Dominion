from src.Dominion.Cardtypes.ActionCard import ActionCard


class Festival(ActionCard):
    EXPENCES = 5
    CARDS = 0
    ACTIONS = 2
    BUYS = 1
    MONEY = 2

    def special_action(self, player, game):
        return
