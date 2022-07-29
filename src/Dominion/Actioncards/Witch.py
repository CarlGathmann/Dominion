from src.Dominion.Cardtypes.ActionCard import ActionCard
from src.Dominion.Victorycards.Curse import Curse


class Witch(ActionCard):
    EXPENCES = 5
    CARDS = 2
    ACTIONS = 0
    BUYS = 0
    MONEY = 0

    def special_action(self, player, game):
        for p in game.players:
            if p.can_be_attacked:
                p.discarding_pile.append(game.get_card_from_pile(Curse()))
                print(p.name + "takes a curse")
            else:
                print(p, 'reacts with a Moat')
