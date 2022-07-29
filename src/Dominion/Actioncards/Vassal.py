from src.Dominion.Cardtypes.ActionCard import ActionCard


class Vassal(ActionCard):
    def __init__(self):
        super(Vassal, self).__init__(0, 0, 0, 2, 3)

    def special_action(self, player, game):
        card = player.draw_and_return()
        if isinstance(card, ActionCard):
            print("playing", card, "with Vassal")
            player.play_action_card(card, game)
