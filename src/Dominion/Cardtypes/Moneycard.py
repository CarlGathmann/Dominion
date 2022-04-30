from abc import ABC, abstractmethod

from src.Dominion.Card import Card


class Moneycard(Card, ABC):

    @classmethod
    @property
    @abstractmethod
    def MONEY(cls):
        raise NotImplementedError
