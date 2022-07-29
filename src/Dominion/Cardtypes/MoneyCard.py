from src.Dominion.Card import Card


class MoneyCard(Card):
    pass

    def __init__(self, expenses, money):
        super().__init__(expenses)
        self.money = money
