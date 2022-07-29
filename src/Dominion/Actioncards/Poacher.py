import random

from src.Dominion.Cardtypes.ActionCard import ActionCard


class Poacher(ActionCard):
    def __init__(self):
        super().__init__(1, 1, 0, 1, 4)

    def special_action(self, player, game):
        for _ in range(17 - len(game.game_cards)):
            if len(player.hand) != 0:
                choice = random.choice(player.hand)
                print('discarding', choice)
                player.hand.remove(choice)
                player.discarding_pile.append(choice)
