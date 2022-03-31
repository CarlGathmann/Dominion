import random

from Cardtypes.Actioncard import Actioncard


class Chapel(Actioncard):
    def __init__(self):
        super().__init__(0, 0, 0, 0, 2)

    def specialAction(self, player):
        # choose random cards to trash
        cards_to_trash = random.randrange(0, len(player.hand) or 4, 1)
        print("Trashing", cards_to_trash, "cards...")
        for card in range(cards_to_trash):
            player.hand.remove(random.choice(player.hand))
