from src.Dominion.Card import Card


class VictoryCard(Card):

    def __init__(self, expenses, victory_points):
        super().__init__(expenses)
        self.victory_points = victory_points
