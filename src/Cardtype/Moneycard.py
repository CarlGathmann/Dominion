from Card import Card


class Moneycard(Card):
    pass

    def __init__(self, expences, money):
        super().__init__(expences)
        self.money = money
