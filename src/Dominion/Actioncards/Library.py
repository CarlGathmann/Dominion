import random

from src.Dominion.Cardtypes.ActionCard import ActionCard


class Library(ActionCard):
    def __init__(self):
        super(Library, self).__init__(0, 0, 0, 0, 5)

    def special_action(self, player, game):
        cards_in_hand = len(player.hand)
        while cards_in_hand < 7:
            card = player.draw_and_return()
            if card is not None:
                print('drawing %s...' % card)
                if isinstance(card, ActionCard):
                    if random.randint(0, 1) == 1:
                        print('discarding', card, '...')
                        player.discarding_pile.append(card)

                    else:
                        print('adding', card, 'to hand')
                        player.hand.append(card)
                        cards_in_hand += 1
                else:
                    cards_in_hand += 1
            else:
                break
