import random

from src.Dominion.Cardtypes.ActionCard import ActionCard


class Workshop(ActionCard):
    def __init__(self):
        super().__init__(0, 0, 0, 0, 3)

    def special_action(self, player, game):
        possible_cards = []
        for key in game.game_cards.keys():
            if game.game_cards[key][0].expenses <= 4:
                possible_cards.append(game.game_cards[key][0])
        if len(possible_cards) > 0:
            choice = random.choice(possible_cards)
            player.discarding_pile.append(game.get_card_from_pile(choice))
            print("taking", choice)
        else:
            print("no cards to take")
