import random

from src.Dominion.Cardtypes.Actioncard import Actioncard


class Remodel(Actioncard):
    EXPENCES = 4
    CARDS = 0
    ACTIONS = 0
    BUYS = 0
    MONEY = 0

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
                    print("taking", card_to_draw, "from pile")
                    player.discardingPile.append(card_to_draw)
                else:
                    print("could not find card to take from pile")
