from src.Cardtypes.Actioncard import Actioncard
from src.Victorycards.Curse import Curse


class Witch(Actioncard):
    def __init__(self):
        super(Witch, self).__init__(2, 0, 0, 0, 5)

    def specialAction(self, player, game):
        for p in game.players:
            if p.canBeAttacked:
                p.discardingPile.append(game.getCardFromPile(Curse()))
            else:
                print(p, 'reacts with a Moat')
