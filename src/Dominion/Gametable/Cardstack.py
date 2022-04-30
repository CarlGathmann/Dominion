from typing import TypeVar, List

from src.Dominion import Card

T = TypeVar('T', bound=Card)


class Cardstack:

    def __init__(self):
        self.cards: List[T] = None

    def size(self):
        return len(self.cards)
