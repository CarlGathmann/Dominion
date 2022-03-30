class Card:
    pass

    def __init__(self, expences):
        self.expences = expences

    def __str__(self):
        return str(self.__class__).split(".")[-1].strip("'>")
