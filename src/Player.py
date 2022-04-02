import random

from src.Actioncards.Moat import Moat
from src.Cardtypes.Actioncard import Actioncard
from src.Cardtypes.Moneycard import Moneycard
from src.Cardtypes.Victorycard import Victorycard
from src.Moneycards.Copper import Copper
from src.Victorycards.Estate import Estate


class Player:

    def __init__(self, name):
        self.name = 'Player_' + name
        self.money = 0
        self.buys = 0
        self.actions = 0
        self.victorypoints = 0
        self.canBeAttacked = True
        self.hand = []
        self.drawingPile = []
        self.discardingPile = []
        self.played_cards = []

    def takeTurn(self, game):
        # PREP
        self.actions = 1
        self.buys = 1
        self.money = 0
        self.canBeAttacked = True
        # ACTIONPHASE
        print("# ACTIONPHASE")
        self.playActions(game)
        # BUYPHASE
        print("# BUYPHASE")
        self.printAttributes()
        self.buyCards(game)

        # DISCARD CARDS
        self.dicardAllCards()

        self.draw(5)

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
            if len(possible_buys) > 0:
                choice = random.choice(possible_buys)
                if isinstance(choice, Victorycard):
                    self.victorypoints += choice.victorypoints
                self.discardingPile.append(game.getCardFromPile(choice))
                self.money -= choice.expences
                self.buys -= 1
                print("Buying:", choice)
            else:
                print("can't buy anything")
                self.buys = 0

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
        for key in game.gameCards.keys():
            if game.gameCards[key][0].expences <= self.money:
                possible_buys.append(game.gameCards[key][0])
        return possible_buys

    def draw(self, amount: int):
        if amount != 0:
            print("Drawing", amount, "cards...")

        for i in range(amount):
            if len(self.drawingPile) != 0:
                card = self.drawingPile.pop()
                if card.__class__ == Moat:
                    self.canBeAttacked = False
                self.hand.append(card)
            elif len(self.discardingPile) != 0:
                self.shuffle()
                card = self.drawingPile.pop()
                if card.__class__ == Moat:
                    self.canBeAttacked = False
                self.hand.append(card)
            else:
                print("No cards to draw")
                break

    def shuffle(self):
        self.drawingPile += self.discardingPile
        self.discardingPile.clear()
        random.shuffle(self.drawingPile)

    def createDeck(self, game):
        print("\n Creating Deck for player %s..." % self.name)
        for _ in range(7):
            self.drawingPile.append(game.gameCards.get(str(Copper())).pop())
        for _ in range(3):
            self.drawingPile.append(game.gameCards.get(str(Estate())).pop())
        self.shuffle()

    def discardFromHand(self, card):
        self.hand.remove(card)
        self.discardingPile.append(card)

    def drawAndReturn(self):
        if len(self.drawingPile) != 0:
            return self.drawingPile.pop()
        elif len(self.discardingPile) != 0:
            self.shuffle()
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

    def __str__(self):
        return str(self.__class__).split(".")[-1].strip("'>")
