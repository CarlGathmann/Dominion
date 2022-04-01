import random

from src.Cardtypes.Actioncard import Actioncard
from src.Cardtypes.Moneycard import Moneycard
from src.Moneycards.Copper import Copper
from src.Victorycards.Estate import Estate


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

    def takeTurn(self, game):
        # PREP
        self.actions = 1
        self.buys = 1
        self.money = 0
        self.draw(5)
        # ACTIONPHASE
        print("# ACTIONPHASE")
        self.playActions(game)
        # BUYPHASE
        print("# BUYPHASE")
        self.buyCards(game)
        # DISCARD CARDS
        self.dicardAllCards()

    def playActions(self, game):
        while self.actions > 0:
            if len(self.getActionInHand()) != 0:
                choice = random.choice(self.getActionInHand())
                self.playActioncardInHand(choice, game)
                self.actions -= 1
            else:
                break

    def buyCards(self, game):
        for card in self.getMoneycardsInHand():
            self.playMoneycard(card)
        while self.buys > 0:
            possible_buys = self.getPossibleBuys(game)
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

    def playActioncardInHand(self, card: Actioncard, game):
        print("playing: ", card.__str__())
        self.hand.remove(card)
        self.played_cards.append(card)
        self.actions += card.actions
        self.buys += card.buys
        self.money += card.money
        self.draw(card.cards)
        card.specialAction(self, game)

    def playActioncard(self, card: Actioncard, game):
        print("playing: ", card.__str__())
        self.actions += card.actions
        self.buys += card.buys
        self.money += card.money
        self.draw(card.cards)
        card.specialAction(self, game)

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

    def getPossibleBuys(self, game):
        possible_buys = []
        for option in game.card_expences.keys():
            print((option, game.card_expences[option]))
            if self.money >= option:
                possible_buys += game.card_expences[option]
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
            elif len(self.discardingPile) != 0:
                self.drawingPile += self.discardingPile
                self.discardingPile.clear()
                random.shuffle(self.drawingPile)
                card = self.drawingPile.pop()
                self.hand.append(card)
            else:
                print("No cards to draw")
                break

    def drawAndReturn(self):
        if len(self.drawingPile) != 0:
            return self.drawingPile.pop()
        elif len(self.discardingPile) != 0:
            self.drawingPile += self.discardingPile
            self.discardingPile.clear()
            random.shuffle(self.drawingPile)
            return self.drawingPile.pop()
        else:
            print("No cards to draw")
            return None

    def dicardAllCards(self):
        self.discardingPile += self.hand
        self.discardingPile += self.played_cards
        self.played_cards.clear()
        self.hand.clear()

    def dicardListOfCards(self, cards):
        print("Discarding", len(cards), "cards...")
        for card in cards:
            self.discardingPile.append(card)
            self.hand.remove(card)

    def chooseXCardsFromHand(self, x):
        choices = random.sample(self.hand, x)
        return choices

    def printAttributes(self):
        print(
            "Actions: %s, Buys: %s, Money: %s, Handkarten: %s, Alle Karten: %s"
            % (self.actions, self.buys, self.money, len(self.hand),
               len(self.hand + self.drawingPile + self.discardingPile + self.played_cards))
        )

    def printDeck(self):
        print("Hand:")
        for card in self.hand:
            print(card)
        print("Drawing Pile:")
        for card in self.drawingPile:
            print(card)
