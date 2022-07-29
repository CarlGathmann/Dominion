import random

from src.Dominion.Cardtypes.ActionCard import ActionCard


class Militia(ActionCard):
    EXPENCES = 4
    CARDS = 0
    ACTIONS = 0
    BUYS = 0
    MONEY = 2

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
