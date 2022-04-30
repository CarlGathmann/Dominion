import random

from src.Dominion.Cardtypes.Actioncard import Actioncard


class ThroneRoom(Actioncard):
    EXPENCES = 4
    CARDS = 0
    ACTIONS = 0
    BUYS = 0
    MONEY = 0

    def specialAction(self, player, game):
        hand = player.getActionInHand()
        if len(hand) > 0:
            choice = random.choice(hand)
            player.played_cards.append(choice)
            player.hand.remove(choice)
            print("playing ", choice, " twice")
            player.playActioncard(choice, game)
            player.playActioncard(choice, game)
