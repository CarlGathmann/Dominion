import random

from Moneycards.Copper import Copper
from Victorycards.Estate import Estate
from random import shuffle


class Player:

    def __init__(self):
        self.hand = []
        self.drawingPile = []
        self.discardingPile = []
        self.createDeck()
        self.draw(5)

    def createDeck(self):
        for i in range(3):
            self.drawingPile.append(Estate())
        for i in range(7):
            self.drawingPile.append(Copper())
        random.shuffle(self.drawingPile)

    def draw(self, cards: int):
        for i in range(cards):
            card = self.drawingPile.pop(i)
            self.hand.append(card)

    def printDeck(self):
        print("Hand:")
        for card in self.hand:
            print(card)
        print("Drawing Pile:")
        for card in self.drawingPile:
            print(card)
