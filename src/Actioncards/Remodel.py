import random

from src.Cardtypes.Actioncard import Actioncard


class Remodel(Actioncard):
    def __init__(self):
        super().__init__(0, 0, 0, 0, 4)

    def specialAction(self, player, game):
        hand = player.hand
        if len(hand) > 0:
            choice = random.choice(hand)
            possible_cards = []
            for option in player.getPossibleBuys(game):
                if choice.expences + 2 >= option.expences:
                    possible_cards += game.gameCards[option.__str__()]
            if len(possible_cards) > 0:
                want_to_get = random.choice(possible_cards)
                card_to_draw = game.getCardFromPile(want_to_get)
                if card_to_draw is not None:
                    player.discardingPile.append(card_to_draw)
                else:
                    return
