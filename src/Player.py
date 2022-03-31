import random

import AllCards
from Actioncards.Cellar import Cellar
from Card import Card
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
        self.hand.append(Cellar())

    def takeTurn(self):
        # PREP
        self.actions = 1
        self.buys = 1
        self.money = 0
        self.draw(5)
        # ACTIONPHASE
        self.printDeck()
        self.printAttributes()
        self.playActions()
        self.printAttributes()
        # BUYPHASE
        self.buyCards()
        self.printAttributes()
        # DISCARD CARDS
        self.dicardAllCards()

    def playActions(self):
        while self.actions > 0:
            actioncards = self.getActionInHand()
            for card in actioncards:
                choice = random.choice(actioncards)
                self.playCard(choice)
                actioncards.remove(choice)
                self.actions -= 1
        self.countMoney()

    def playCard(self, card: Actioncard):
        print("playing: ", card.__str__())
        self.hand.remove(card)
        self.played_and_bought_cards.append(card)
        self.actions += card.actions
        self.buys += card.buys
        self.money += card.money
        self.draw(card.cards)
        card.specialAction(self)

    def buyCards(self):
        while self.buys > 0:
            possible_buys = self.getPossibleBuys()
            choice = random.choice(possible_buys)
            self.played_and_bought_cards.append(choice)
            self.buy(choice)

    def buy(self, card: Card):
        self.money -= card.expences
        self.buys -= 1
        print("Buying:", card)

    def getActionInHand(self):
        actions = []
        for card in self.hand:
            if isinstance(card, Actioncard):
                actions.append(card)
        return actions

    def getMoneycardsInHand(self):
        moneycards = []
        for card in self.hand:
            if isinstance(card, Moneycard):
                moneycards.append(card)
        return moneycards

    def countMoney(self):
        for card in self.hand:
            if isinstance(card, Moneycard):
                self.money += card.money

    def getPossibleBuys(self):
        possible_buys = []
        for option in AllCards.cardlist.keys():
            if self.money >= option:
                possible_buys += AllCards.cardlist[option]
        return possible_buys

    def createDeck(self):
        for i in range(3):
            self.drawingPile.append(Estate())
        for i in range(7):
            self.drawingPile.append(Copper())
        random.shuffle(self.drawingPile)

    def draw(self, cards: int):
        if cards != 0:
            print("Drawing", cards, "cards...")
        for i in range(cards):
            try:
                card = self.drawingPile.pop()
                self.hand.append(card)
            except IndexError:
                self.drawingPile += self.discardingPile
                self.discardingPile.clear()
                random.shuffle(self.drawingPile)

                card = self.drawingPile.pop()
                self.hand.append(card)

    def dicardAllCards(self):
        self.discardingPile += self.hand
        self.discardingPile += self.played_and_bought_cards
        self.hand.clear()

    def dicardAmountOfCards(self, cards):
        for card in cards:
            self.discardingPile.append(card)
            self.hand.remove(card)

    def chooseXCardsFromHand(self, x):
        choices = []
        for card in range(x):
            choice = random.choice(self.hand)
            choices.append(choice)
        return choices

    def printAttributes(self):
        print("Actions: %s, Buys: %s, Money: %s" % (self.actions, self.buys, self.money))

    def printDeck(self):
        print("Hand:")
        for card in self.hand:
            print(card)
        print("Drawing Pile:")
        for card in self.drawingPile:
            print(card)
