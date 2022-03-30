import random

import AllCards
from Card import Card
from Actioncards.Chapel import Chapel
from Cardtypes.Actioncard import Actioncard
from Cardtypes.Moneycard import Moneycard
from Moneycards.Copper import Copper
from Victorycards.Estate import Estate


class Player:

    def __init__(self):
        self.money = 0
        self.buys = 0
        self.actions = 0
        self.hand = []
        self.drawingPile = []
        self.discardingPile = []
        self.played_and_bought_cards = []
        self.createDeck()
        self.draw(5)

    def createDeck(self):
        for i in range(3):
            self.drawingPile.append(Estate())
        for i in range(7):
            self.drawingPile.append(Copper())
        self.drawingPile.append(Chapel())
        random.shuffle(self.drawingPile)

    def draw(self, cards: int):
        for i in range(cards):
            card = self.drawingPile.pop()
            self.hand.append(card)

    def printDeck(self):
        print("Hand:")
        for card in self.hand:
            print(card)
        print("Drawing Pile:")
        for card in self.drawingPile:
            print(card)

    def takeTurn(self):
        # ACTIONPHASE
        self.playActions()
        # BUYPHASE
        self.buyCards()
        # LAY DOWN CARDS
        self.dicardCards()

    def playActions(self):
        self.actions = 1
        self.buys = 1
        while self.actions > 0:
            actioncards = self.getActionInHand()
            if len(actioncards) > 0:
                choice = random.choice(actioncards)
                self.playCard(choice)
                actioncards.remove(choice)
                self.actions -= 1
            else:
                self.actions = 0

    def buyCards(self):
        possible_buys = self.getPossibleBuys()
        print(possible_buys)
        self.buy(random.choice(possible_buys))

    def getPossibleBuys(self):
        self.getMoneyInHand()
        possible_buys = []
        self.printAttributes()
        for option in AllCards.cardlist.keys():
            if self.money >= option:
                possible_buys += AllCards.cardlist[option]
        return possible_buys

    def playCard(self, card: Actioncard):
        print("playing: ", card.__str__())
        self.hand.remove(card)
        self.actions += card.actions
        self.buys += card.buys
        self.money += card.money
        while card.cards > 0:
            drawncard = self.drawingPile.pop()
            self.hand.append(drawncard)
            card.cards -= 1
        card.specialAction(self.hand)

    def getActionInHand(self):
        actions = []
        for card in self.hand:
            if isinstance(card, Actioncard):
                actions.append(card)
        return actions

    def getMoneyInHand(self):
        for card in self.hand:
            if isinstance(card, Moneycard):
                self.money += card.money

    def printAttributes(self):
        print("Actions: %s, Buys: %s, Money: %s" % (self.actions, self.buys, self.money))

    def buy(self, card: Card):
        self.money -= card.expences
        self.buys -= 1
        print("Buying:", card)

    def dicardCards(self):
        self.discardingPile += self.hand
        self.discardingPile += self.played_and_bought_cards
        self.hand.clear()
