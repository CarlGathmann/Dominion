from src.Dominion.Card import Card


class MoneyCard(Card):
    def __init__(self, expenses, money):
        super().__init__(expenses)
        self.money = money
