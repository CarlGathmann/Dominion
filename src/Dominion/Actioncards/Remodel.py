import random

from src.Dominion.Cardtypes.ActionCard import ActionCard


class Remodel(ActionCard):
    def __init__(self):
        super().__init__(0, 0, 0, 0, 4)

    def special_action(self, player, game):
        hand = player.hand
        if len(hand) > 0:
            choice = random.choice(hand)
            possible_cards = []
            for option in player.get_possible_buys(game):
                if choice.expenses + 2 >= option.expenses:
                    possible_cards += game.game_cards[option.__str__()]
            if len(possible_cards) > 0:
                want_to_get = random.choice(possible_cards)
                card_to_draw = game.get_card_from_pile(want_to_get)
                if card_to_draw is not None:
                    print("taking", card_to_draw, "from pile")
                    player.discarding_pile.append(card_to_draw)
                else:
                    print("could not find card to take from pile")
