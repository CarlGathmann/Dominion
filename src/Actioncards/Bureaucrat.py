from src.Cardtypes.Actioncard import Actioncard


class Bureaucrat(Actioncard):
    def __init__(self):
        super().__init__(0, 0, 0, 0, 4)

    def specialAction(self, player, game):
        player.drawingPile.append(game.gameCards.get('Silver').pop())
        for player in game.players:
            if player.canBeAttacked:
                counter = 0
                for card in player.hand:
                    if isinstance(card, Actioncard) and counter == 0:
                        player.drawingPile.append(card)
                        player.hand.remove(card)
