class Card:
    pass

    def __init__(self, expenses):
        self.expenses = expenses

    def __str__(self):
        return str(self.__class__).split(".")[-1].strip("'>")
