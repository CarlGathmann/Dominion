from src.Dominion.Cardtypes.ActionCard import ActionCard
from src.Dominion.Cardtypes.VictoryCard import VictoryCard
from src.Dominion.Moneycards.Silver import Silver


class Bureaucrat(ActionCard):
    def __init__(self):
        super().__init__(0, 0, 0, 0, 4)

    def special_action(self, player, game):
        try:
            print("taking a Silver")
            player.drawing_pile.append(game.get_card_from_pile(Silver()))
        except KeyError:
            print("no Silver left")
        for player in game.players:
            if player.can_be_attacked:
                counter = 0
                for card in player.hand:
                    if isinstance(card, VictoryCard) and counter == 0:
                        print(player, ' has to top-deck', card)
                        player.drawing_pile.append(card)
                        player.hand.remove(card)
                        counter += 1
            else:
                print(player, 'reacts with a Moat')
