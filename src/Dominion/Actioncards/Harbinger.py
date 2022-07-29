import random

from src.Dominion.Cardtypes.ActionCard import ActionCard


class Harbinger(ActionCard):
    EXPENCES = 3
    CARDS = 1
    ACTIONS = 1
    BUYS = 0
    MONEY = 0

    def special_action(self, player, game):
        if len(player.discarding_pile) != 0:
            choice = random.choice(player.discarding_pile)
            print("taking", choice, "from discarding pile")
            player.discarding_pile.remove(choice)
            player.drawing_pile.append(choice)
        else:
            print("no cards to take from discarding pile")
