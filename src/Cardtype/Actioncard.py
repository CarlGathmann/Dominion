from Card import Card


class Actioncard(Card):
    pass

    def __init__(self, cards, actions, buys, money, expences, victorypoints):
        super().__init__(expences, victorypoints)
        self.cards = cards
        self.actions = actions
        self.buys = buys
        self.money = money
