from src.Dominion.Card import Card


class Moneycard(Card):
    pass

    def __init__(self, expenses, money):
        super().__init__(expenses)
        self.money = money
