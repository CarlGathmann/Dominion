import random

from src.Dominion.Cardtypes.ActionCard import ActionCard


class ThroneRoom(ActionCard):
    def __init__(self):
        super(ThroneRoom, self).__init__(0, 0, 0, 0, 4)

    def special_action(self, player, game):
        hand = player.get_action_in_hand()
        if len(hand) > 0:
            choice = random.choice(hand)
            player.played_cards.append(choice)
            player.hand.remove(choice)
            print("playing ", choice, " twice")
            player.play_action_card(choice, game)
            player.play_action_card(choice, game)
