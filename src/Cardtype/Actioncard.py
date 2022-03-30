from Card import Card


class Actioncard(Card):
    pass

    def __init__(self, cards, actions, buys, money, expences):
        super().__init__(expences)
        self.cards = cards
        self.actions = actions
        self.buys = buys
        self.money = money

    def specialAction(self):
        pass
