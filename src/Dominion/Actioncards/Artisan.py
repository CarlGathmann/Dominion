import random

from src.Dominion.Cardtypes.ActionCard import ActionCard


class Artisan(ActionCard):
    def __init__(self):
        super().__init__(0, 0, 0, 0, 6)

    def special_action(self, player, game):
        possible_cards = []
        for key in game.game_cards.keys():
            if game.game_cards[key][0].expenses <= 5:
                possible_cards.append(game.game_cards[key][0])
        if len(possible_cards) > 0:
            choice = random.choice(possible_cards)
            player.hand.append(game.get_card_from_pile(choice))
            second_choice = random.choice(player.hand)
            player.hand.remove(second_choice)
            player.drawing_pile.append(second_choice)
            print("taking", choice, "and top decking", second_choice)

        else:
            print("no cards to take")
