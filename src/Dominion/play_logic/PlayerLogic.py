from abc import ABC
from abc import abstractmethod

from src.Dominion import Card
from src.Dominion.Cardtypes import Actioncard


class PlayerLogic(ABC):

    @abstractmethod
    def chooseActionCard(self, hand_cards, game_table) -> Actioncard:
        return None

    @abstractmethod
    def buyCard(self, hand_cards, game_table) -> Card:
        return None
