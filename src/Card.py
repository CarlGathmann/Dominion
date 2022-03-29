class Card:
    pass

    def __init__(self, expences, victorypoints):
        self.expences = expences
        self.victorypoints = victorypoints

    def __str__(self):
        return str(self.__class__).split(".")[-1].strip("'>")
