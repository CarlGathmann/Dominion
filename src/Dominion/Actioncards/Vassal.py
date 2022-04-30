from src.Dominion.Cardtypes.Actioncard import Actioncard


class Vassal(Actioncard):
    EXPENCES = 3
    CARDS = 0
    ACTIONS = 0
    BUYS = 0
    MONEY = 2

    def specialAction(self, player, game):
        card = player.drawAndReturn()
        if isinstance(card, Actioncard):
            print("playing", card, "with Vassal")
            player.playActioncard(card, game)
