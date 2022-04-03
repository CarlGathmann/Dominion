import random

from src.Dominion.Cardtypes.Actioncard import Actioncard


class Militia(Actioncard):
    def __init__(self):
        super().__init__(0, 0, 0, 2, 4)

    # Every other Player discards down to 3 cards in hand
    def specialAction(self, player, game):
        if player.canBeAttacked:
            for p in game.players:
                if p != player:
                    while len(p.hand) > 3:
                        choice = random.choice(p.hand)
                        p.discardFromHand(choice)
                        print(p.name, 'discarding', choice)
        else:
            print(player, 'reacts with a Moat')
