from src.Dominion.Cardtypes.ActionCard import ActionCard


class Vassal(ActionCard):
    EXPENCES = 3
    CARDS = 0
    ACTIONS = 0
    BUYS = 0
    MONEY = 2

    def special_action(self, player, game):
        card = player.draw_and_return()
        if isinstance(card, ActionCard):
            print("playing", card, "with Vassal")
            player.play_action_card(card, game)
