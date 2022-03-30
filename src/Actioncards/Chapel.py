import random

from Cardtypes.Actioncard import Actioncard


class Chapel(Actioncard):
    def __init__(self):
        super().__init__(0, 0, 0, 0, 2)

    def specialAction(self, hand):
        # choose random cards to trash
        cards_to_trash = random.randint(0, 4)
        print("Trashing", cards_to_trash, "cards...")
        for card in range(cards_to_trash):
            hand.remove(random.choice(hand))
