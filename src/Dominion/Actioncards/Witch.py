from src.Dominion.Cardtypes.ActionCard import ActionCard
from src.Dominion.Victorycards.Curse import Curse


class Witch(ActionCard):
    def __init__(self):
        super(Witch, self).__init__(2, 0, 0, 0, 5)

    def special_action(self, player, game):
        for p in game.players:
            if p.can_be_attacked:
                p.discarding_pile.append(game.get_card_from_pile(Curse()))
                print(p.name + "takes a curse")
            else:
                print(p, 'reacts with a Moat')
