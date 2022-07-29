from src.Dominion.Cardtypes.ActionCard import ActionCard
from src.Dominion.Cardtypes.MoneyCard import MoneyCard


class Bandit(ActionCard):
    def __init__(self):
        super().__init__(0, 0, 0, 0, 5)

    def special_action(self, player, game):
        try:
            player.discarding_pile.append(game.get_card_from_pile('Gold'))
        except KeyError:
            print("no Gold left")
        for player in game.players:
            if player.can_be_attacked:
                for _ in range(2):
                    card = player.draw_and_return()
                    if isinstance(card, MoneyCard):
                        if card.expenses >= 2:
                            print(player, "trashing", card)
                            game.garbage.append(card)
                            return
                        else:
                            print(player, "discarding", card)
                            player.discarding_pile.append(card)
                    else:
                        print("discarding ", card)
                        player.discarding_pile.append(card)
            else:
                print(player, 'reacts with a Moat')