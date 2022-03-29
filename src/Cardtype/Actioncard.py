from src.Card import Card


class Actioncard(Card):
    pass

    def __init__(self, cards, actions, buys, money):
        self.victorypoints = 0
        self.cards = cards
        self.actions = actions
        self.buys = buys
        self.money = money


