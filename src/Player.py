import random
import Card

from Moneycards.Copper import Copper
from Victorycards.Estate import Estate
from Cardtype.Actioncard import Actioncard

class Player:

    def __init__(self):
        self.money = 0
        self.buys = 0
        self.actions = 0
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

    def takeTurn(self):
        self.actions = 1
        self.buys = 1
        # ACTIONPHASE
        while self.actions > 0:
            actioncards = self.getActionInHand()
            if len(actioncards) > 0:
                choice = random.choice(actioncards)
                self.playCard(choice)
                actioncards.remove(choice)
                self.actions -= 1
            else:
                self.actions = 0
        # BUYPHASE
            
    def playCard(self, card: Card):
        self.hand.remove(card)
        self.actions += card.actions
        self.buys += card.buys
        self.money += card.money
        while card.cards > 0:
            drawncard = self.drawingPile.pop()
            self.hand.append(drawncard)
            card.cards -= 1

    def getActionInHand(self):
        actions = []
        for card in self.hand:
            if isinstance(card, Actioncard):
                actions.append(card)
        return actions

    def printAttributes(self):
        print("Actions: %s, Buys: %s, Money: %s" % (self.actions, self.buys, self.money))
