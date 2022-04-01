import random

from src.Cardtypes.Actioncard import Actioncard


class Chapel(Actioncard):
    def __init__(self):
        super().__init__(0, 0, 0, 0, 2)

    def specialAction(self, player, game):
        # choose random cards to trash
        cards_to_trash = random.randint(0, len(player.hand) or 4)
        if cards_to_trash != 0:
            for card in range(cards_to_trash):
                if len(player.hand) != 0:
                    choise = random.choice(player.hand)
                    print("Trashing %s..." % choise)
                    player.hand.remove(choise)
                    game.garbidge.append(choise)
        else:
            print("Trashing no cards...")
