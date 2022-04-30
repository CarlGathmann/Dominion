from abc import ABC, abstractmethod

class Card(ABC):

    @classmethod
    @property
    @abstractmethod
    def EXPENCES(cls):
        raise NotImplementedError

    def __str__(self):
        return str(self.__class__).split(".")[-1].strip("'>")
