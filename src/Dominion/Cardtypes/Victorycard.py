from abc import ABC, abstractmethod

from src.Dominion.Card import Card


class Victorycard(Card, ABC):

    @classmethod
    @property
    @abstractmethod
    def VICTORYPOINTS(cls):
        raise NotImplementedError
