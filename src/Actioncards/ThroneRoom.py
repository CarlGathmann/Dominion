import random

from src.Cardtypes.Actioncard import Actioncard


class ThroneRoom(Actioncard):
    def __init__(self):
        super(ThroneRoom, self).__init__(0, 0, 0, 0, 4)

    def specialAction(self, player, game):
        hand = player.getActionInHand()
        if len(hand) != 0:
            choice = random.choice(hand)
            player.played_cards.append(choice)
            player.hand.remove(choice)
            print("Playing ", choice, " twice")
            player.playActioncard(choice, game)
            player.playActioncard(choice, game)
