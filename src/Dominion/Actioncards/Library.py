import random

from src.Dominion.Cardtypes.Actioncard import Actioncard


class Library(Actioncard):
    def __init__(self):
        super(Library, self).__init__(0, 0, 0, 0, 5)

    def specialAction(self, player, game):
        cards_in_hand = len(player.hand)
        while cards_in_hand < 7:
            card = player.drawAndReturn()
            if card is not None:
                print('drawing %s...' % card)
                if isinstance(card, Actioncard):
                    if random.randint(0, 1) == 1:
                        print('discarding', card, '...')
                        player.discardingPile.append(card)

                    else:
                        print('adding', card, 'to hand')
                        player.hand.append(card)
                        cards_in_hand += 1
                else:
                    cards_in_hand += 1
            else:
                break
