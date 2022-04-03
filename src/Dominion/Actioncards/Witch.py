from src.Dominion.Cardtypes.Actioncard import Actioncard
from src.Dominion.Victorycards.Curse import Curse


class Witch(Actioncard):
    def __init__(self):
        super(Witch, self).__init__(2, 0, 0, 0, 5)

    def specialAction(self, player, game):
        for p in game.players:
            if p.canBeAttacked:
                p.discardingPile.append(game.getCardFromPile(Curse()))
                print(p.name + "takes a curse")
            else:
                print(p, 'reacts with a Moat')
