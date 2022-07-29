import random

from src.Dominion.Cardtypes.ActionCard import ActionCard


class Chapel(ActionCard):
    def __init__(self):
        super().__init__(0, 0, 0, 0, 2)

    def special_action(self, player, game):
        # choose random cards to trash
        cards_to_trash = random.randint(0, len(player.hand) or 4)
        if cards_to_trash != 0:
            for _ in range(cards_to_trash):
                if len(player.hand) != 0:
                    choice = random.choice(player.hand)
                    print("trashing %s..." % choice)
                    player.hand.remove(choice)
                    game.garbage.append(choice)
        else:
            print("trashing no cards...")
