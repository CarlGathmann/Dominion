from abc import ABC, abstractmethod

from src.Dominion.Card import Card


class Actioncard(Card, ABC):
    @classmethod
    @property
    @abstractmethod
    def CARDS(cls):
        raise NotImplementedError

    @classmethod
    @property
    @abstractmethod
    def ACTIONS(cls):
        raise NotImplementedError

    @classmethod
    @property
    @abstractmethod
    def BUYS(cls):
        raise NotImplementedError

    @classmethod
    @property
    @abstractmethod
    def MONEY(cls):
        raise NotImplementedError

    @abstractmethod
    def specialAction(self, player, game):
        pass
