from src.Dominion.Card import Card


class ActionCard(Card):
    def __init__(self, cards, actions, buys, money, expences):
        super().__init__(expences)
        self.cards = cards
        self.actions = actions
        self.buys = buys
        self.money = money

    def special_action(self, player, game):
        pass
