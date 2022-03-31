from Cardtypes.Actioncard import Actioncard
from Game import Game


class Militia(Actioncard):
    def __init__(self):
        super().__init__(0, 0, 0, 2, 4)

    # muss noch gemacht werden... ist stressig wegen Decks von anderen Spielern
    def specialAction(self, player):
        pass
