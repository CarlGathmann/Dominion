from src.Cardtypes.Actioncard import Actioncard
from src.Cardtypes.Victorycard import Victorycard


class Bureaucrat(Actioncard):
    def __init__(self):
        super().__init__(0, 0, 0, 0, 4)

    def specialAction(self, player, game):
        player.drawingPile.append(game.gameCards.get('Silver').pop())
        for player in game.players:
            if player.canBeAttacked:
                counter = 0
                for card in player.hand:
                    if isinstance(card, Victorycard) and counter == 0:
                        print(player, ' has to discard a card')
                        print(card)
                        player.drawingPile.append(card)
                        player.hand.remove(card)
                        counter += 1
