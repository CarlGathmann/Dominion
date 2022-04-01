import random

from src.Cardtypes.Actioncard import Actioncard


class Laboratory(Actioncard):
    def __init__(self):
        super(Laboratory, self).__init__(0, 0, 0, 0, 5)

    def specialAction(self, player, game):
        cards_in_hand = len(player.hand)
        while cards_in_hand < 7:
            if player.drawAndReturn() is not None:
                card = player.drawAndReturn()
                print('drawing', card, '...')
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
