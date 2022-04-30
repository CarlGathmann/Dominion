import random

from src.Dominion.Cardtypes.Actioncard import Actioncard


class Chapel(Actioncard):
    EXPENCES = 2
    CARDS = 0
    ACTIONS = 0
    BUYS = 0
    MONEY = 0

    def specialAction(self, player, game):
        # choose random cards to trash
        cards_to_trash = random.randint(0, len(player.hand) or 4)
        if cards_to_trash != 0:
            for card in range(cards_to_trash):
                if len(player.hand) != 0:
                    choise = random.choice(player.hand)
                    print("trashing %s..." % choise)
                    player.hand.remove(choise)
                    game.garbidge.append(choise)
        else:
            print("trashing no cards...")
