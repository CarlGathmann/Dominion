import random

from src.Dominion.play_logic import PlayerLogic
from src.Dominion.Actioncards.Moat import Moat
from src.Dominion.Cardtypes.Actioncard import Actioncard
from src.Dominion.Cardtypes.Moneycard import Moneycard
from src.Dominion.Moneycards.Copper import Copper
from src.Dominion.Victorycards.Estate import Estate


class Player:

    def __init__(self, name):
        self.name = 'Player' + name
        self.money = 0
        self.buys = 0
        self.actions = 0
        self.victorypoints = 0
        self.canBeAttacked = True
        self.hand = []
        self.drawingPile = []
        self.discardingPile = []
        self.played_cards = []
        self.play_logic : PlayerLogic = None

    def takeTurn(self, game):
        # PREP
        self.actions = 1
        self.buys = 1
        self.money = 0
        self.canBeAttacked = True
        # ACTIONPHASE
        print("# ACTIONPHASE")
        self.printHand()
        self.playActions(game)
        # BUYPHASE
        print("# BUYPHASE")
        self.buyCards(game)

        # DISCARD CARDS
        self.dicardAllCards()

        self.draw(5)

    def playActions(self, game):
        while self.actions > 0:
            chosen_card = self.play_logic.chooseActionCard(self.hand, game.gameCards)
            # check if card is valid
            if chosen_card in self.hand:
                self.playActioncardInHand(chosen_card, game)
                self.actions -= 1

    def buyCards(self, game):
        while self.buys > 0:
            chosen_card = self.play_logic.buyCard(self.hand, game.gameCards)
            # check if card is buyable
            # TODO!
            if yes:
                self.discardingPile.append(game.getCardFromPile(choice))
                self.money -= choice.expences
                self.buys -= 1



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

        for _ in range(amount):
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
            print("no cards to draw")
            return None

    def dicardAllCards(self):
        self.discardingPile += self.hand
        self.discardingPile += self.played_cards
        self.played_cards.clear()
        self.hand.clear()

    def dicardListOfCards(self, cards):
        print("discarding", len(cards), "cards...")
        for card in cards:
            self.discardingPile.append(card)
            self.hand.remove(card)

    def chooseXCardsFromHand(self, x):
        choices = random.sample(self.hand, x)
        return choices

    def printAttributes(self):
        print(
            "Actions: %s, Buys: %s, Money: %s, Handcards: %s, All Cards: %s"
            % (self.actions, self.buys, self.money, len(self.hand),
               len(self.hand + self.drawingPile + self.discardingPile + self.played_cards))
        )

    def printHand(self):
        print("Hand:")
        print(*self.hand)

    def printDeck(self):
        print("Hand:")
        print(*self.hand)
        print("Drawing Pile:")
        print(*self.drawingPile)

    def __str__(self):
        return str(self.__class__).split(".")[-1].strip("'>")
