import random

import AllCards
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
        self.played_cards = []
        self.createDeck()

    def takeTurn(self):
        # PREP
        self.actions = 1
        self.buys = 1
        self.money = 0
        self.draw(5)
        # ACTIONPHASE
        self.printDeck()
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
            if len(actioncards) != 0:
                for card in actioncards:
                    choice = random.choice(actioncards)
                    self.playActioncard(choice)
                    actioncards.remove(choice)
                    self.actions -= 1
            else:
                break

    def buyCards(self):
        for card in self.getMoneycardsInHand():
            self.playMoneycard(card)
        self.printAttributes()
        while self.buys > 0:
            possible_buys = self.getPossibleBuys()
            choice = random.choice(possible_buys)
            self.played_cards.append(choice)
            self.money -= choice.expences
            self.buys -= 1
            print("Buying:", choice)

    def playMoneycard(self, card: Moneycard):
        print("playing: ", card.__str__())
        self.hand.remove(card)
        self.played_cards.append(card)
        self.money += card.money

    def playActioncard(self, card: Actioncard):
        print("playing: ", card.__str__())
        self.hand.remove(card)
        self.played_cards.append(card)
        self.actions += card.actions
        self.buys += card.buys
        self.money += card.money
        self.draw(card.cards)
        card.specialAction(self)

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
            if len(self.drawingPile) != 0:
                card = self.drawingPile.pop()
                self.hand.append(card)
            else:
                self.drawingPile += self.discardingPile
                self.discardingPile.clear()
                random.shuffle(self.drawingPile)

                card = self.drawingPile.pop()
                self.hand.append(card)

    def dicardAllCards(self):
        self.discardingPile += self.hand
        self.discardingPile += self.played_cards
        self.hand.clear()

    def dicardAmountOfCards(self, cards):
        for card in cards:
            self.discardingPile.append(card)
            self.hand.remove(card)

    def chooseXCardsFromHand(self, x):
        choices = []
        for card in range(x):
            choice = random.choice(self.hand)
            while choice in choices:
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
