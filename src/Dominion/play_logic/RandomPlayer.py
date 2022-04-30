from random import random

from src.Dominion import Card
from src.Dominion.Cardtypes import Actioncard
from src.Dominion.PlayerLogic import PlayerLogic


class RandomPlayer(PlayerLogic):
    def chooseActionCard(self, hand_cards, game_table) -> Actioncard:
        if len(self.getActionInHand()) != 0:
            choice = random.choice(self.getActionInHand())
            self.playActioncardInHand(choice, game)
            self.actions -= 1
        else:
            break

    def buyCard(self, hand_cards, game_table) -> Card:

        for card in self.getMoneycardsInHand():
            self.playMoneycard(card)
        while self.buys > 0:
            possible_buys = self.getPossibleBuys(game)
            if len(possible_buys) > 0:
                choice = random.choice(possible_buys)
                if isinstance(choice, Victorycard):
                    self.victorypoints += choice.victorypoints

                print("Buying:", choice)
            else:
                print("can't buy anything")
                self.buys = 0