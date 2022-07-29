import random

from src.Dominion.Cardtypes.ActionCard import ActionCard
from src.Dominion.Moneycards.Copper import Copper
from src.Dominion.Moneycards.Silver import Silver


class Mine(ActionCard):
    def __init__(self):
        super().__init__(0, 0, 0, 0, 5)

    def special_action(self, player, game):
        money_cards = player.get_money_cards_in_hand()
        if len(money_cards) > 0:
            choice = random.choice(money_cards)
            if choice.__class__ == Copper:
                try:
                    player.hand.remove(choice)
                    game.garbage.append(choice)
                    player.hand.append(game.get_card_from_pile("Silver"))
                    print("trashing a Copper for a Silver")
                except KeyError:
                    print('no Silver left')

            elif choice.__class__ == Silver:
                try:
                    player.hand.remove(choice)
                    game.garbage.append(choice)
                    player.hand.append(game.get_card_from_pile("Gold"))
                    print("trashing a Silver for a Gold")
                except KeyError:
                    print('no Gold left')
