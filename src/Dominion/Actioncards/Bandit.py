from src.Dominion.Cardtypes.Actioncard import Actioncard
from src.Dominion.Cardtypes.Moneycard import Moneycard


class Bandit(Actioncard):
    EXPENCES = 5
    CARDS = 0
    ACTIONS = 0
    BUYS = 0
    MONEY = 0

    def specialAction(self, player, game):
        try:
            player.discardingPile.append(game.getCardFromPile('Gold'))
        except KeyError:
            print("no Gold left")
        for player in game.players:
            if player.canBeAttacked:
                for _ in range(2):
                    card = player.drawAndReturn()
                    if isinstance(card, Moneycard):
                        if card.expences >= 2:
                            print(player, "trashing", card)
                            game.garbidge.append(card)
                            return
                        else:
                            print(player, "discarding", card)
                            player.discardingPile.append(card)
                    else:
                        print("discarding ", card)
                        player.discardingPile.append(card)
            else:
                print(player, 'reacts with a Moat')