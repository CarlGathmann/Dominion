import random

from src.Dominion.Cardtypes.ActionCard import ActionCard


class Library(ActionCard):
    EXPENCES = 5
    CARDS = 0
    ACTIONS = 0
    BUYS = 0
    MONEY = 0

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
