from src.Dominion.Cardtypes.Actioncard import Actioncard


class Vassal(Actioncard):
    def __init__(self):
        super(Vassal, self).__init__(0, 0, 0, 2, 3)

    def specialAction(self, player, game):
        card = player.drawAndReturn()
        if isinstance(card, Actioncard):
            print("playing", card, "with Vassal")
            player.playActioncard(card, game)
