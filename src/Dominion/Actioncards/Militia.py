import random

from src.Dominion.Cardtypes.ActionCard import ActionCard


class Militia(ActionCard):
    def __init__(self):
        super().__init__(0, 0, 0, 2, 4)

    # Every other Player discards down to 3 cards in hand
    def special_action(self, player, game):
        if player.can_be_attacked:
            for p in game.players:
                if p != player:
                    while len(p.hand) > 3:
                        choice = random.choice(p.hand)
                        p.discard_from_hand(choice)
                        print(p.name, 'discarding', choice)
        else:
            print(player, 'reacts with a Moat')
