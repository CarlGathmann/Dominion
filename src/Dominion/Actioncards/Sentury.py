import random

from src.Dominion.Cardtypes.ActionCard import ActionCard


class Sentury(ActionCard):
    def __init__(self):
        super(Sentury, self).__init__(1, 1, 0, 0, 5)

    def special_action(self, player, game):
        for _ in range(2):
            card = player.draw_and_return()
            choice = random.randint(0, 2)
            if choice == 0:
                print('discarding', card)
                player.discarding_pile.append(card)
            elif choice == 1:
                print('trashing', card)
                game.garbage.append(card)
            # no choice of order yet
            elif choice == 2:
                print('top decking', card)
                player.drawing_pile.append(card)
