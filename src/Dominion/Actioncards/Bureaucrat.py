from src.Dominion.Cardtypes.Actioncard import Actioncard
from src.Dominion.Cardtypes.Victorycard import Victorycard
from src.Dominion.Moneycards.Silver import Silver


class Bureaucrat(Actioncard):
    def __init__(self):
        super().__init__(0, 0, 0, 0, 4)

    def specialAction(self, player, game):
        try:
            print("taking a Silver")
            player.drawingPile.append(game.getCardFromPile(Silver()))
        except KeyError:
            print("no Silver left")
        for player in game.players:
            if player.canBeAttacked:
                counter = 0
                for card in player.hand:
                    if isinstance(card, Victorycard) and counter == 0:
                        print(player, ' has to topdeck', card)
                        player.drawingPile.append(card)
                        player.hand.remove(card)
                        counter += 1
            else:
                print(player, 'reacts with a Moat')
