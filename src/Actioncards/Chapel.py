import random

from Cardtypes.Actioncard import Actioncard


class Chapel(Actioncard):
    def __init__(self):
        super().__init__(0, 0, 0, 0, 2)

    def specialAction(self, player):
        # choose random cards to trash
        cards_to_trash = random.randint(0, len(player.hand) or 4)
        for card in range(cards_to_trash):
            choise = random.choice(player.hand)
            print("Trashing %s..." % choise)
            player.hand.remove(choise)
