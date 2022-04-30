from src.Dominion.Cardtypes.Actioncard import Actioncard
from src.Dominion.Victorycards.Curse import Curse


class Witch(Actioncard):
    EXPENCES = 5
    CARDS = 2
    ACTIONS = 0
    BUYS = 0
    MONEY = 0

    def specialAction(self, player, game):
        for p in game.players:
            if p.canBeAttacked:
                p.discardingPile.append(game.getCardFromPile(Curse()))
                print(p.name + "takes a curse")
            else:
                print(p, 'reacts with a Moat')
