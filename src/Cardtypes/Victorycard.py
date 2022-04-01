from src.Card import Card


class Victorycard(Card):
    pass

    def __init__(self, expences, victorypoints):
        super().__init__(expences)
        self.victorypoints = victorypoints
