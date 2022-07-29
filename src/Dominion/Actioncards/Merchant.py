from src.Dominion.Cardtypes.ActionCard import ActionCard
from src.Dominion.Moneycards.Silver import Silver


class Merchant(ActionCard):
    def __init__(self):
        super().__init__(1, 1, 0, 0, 3)

    def special_action(self, player, game):
        silver = False
        for money_card in player.get_money_cards_in_hand():
            if not silver and money_card.__class__ == Silver:
                print("+1 money from Merchant")
                player.money += 1
                silver = True
