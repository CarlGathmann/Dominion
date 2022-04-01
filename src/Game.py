import random

from src.Actioncards import Cellar, Chapel, Festival, Harbinger, Market, Merchant, Militia, Moneylender, Smithy, Vassal, \
    Village, Workshop, Moat, Bureaucrat
from src.Moneycards import Copper, Silver, Gold
from src.Player import Player
from src.Victorycards import Estate, Dutchy, Province, Curse


def getStandardCards():
    standard_cards = [Curse.Curse(), Copper.Copper(), Silver.Silver(), Gold.Gold(), Estate.Estate(), Dutchy.Dutchy(),
                      Province.Province()]
    return standard_cards


def getSpecialCards():
    special_cards = [Cellar.Cellar(), Chapel.Chapel(), Festival.Festival(), Harbinger.Harbinger(), Market.Market(),
                     Merchant.Merchant(), Militia.Militia(), Moneylender.Moneylender(), Smithy.Smithy(),
                     Vassal.Vassal(), Village.Village(), Workshop.Workshop(), Moat.Moat(), Bureaucrat.Bureaucrat()]
    return special_cards


def getAllCards():
    all_cards = getStandardCards() + getSpecialCards()
    return all_cards


def getCardExpences():
    card_expences = {
        0: [Copper.Copper(), Chapel.Chapel()],
        2: [Chapel.Chapel(), Cellar.Cellar()],
        3: [Village.Village(), Silver.Silver(), Merchant.Merchant(), Workshop.Workshop(), Vassal.Vassal(),
            Harbinger.Harbinger()],
        4: [Smithy.Smithy(), Moneylender.Moneylender(), Militia.Militia()],
        5: [Market.Market(), Festival.Festival()],
        6: [Gold.Gold()]
    }
    return card_expences


class Game:
    pass

    def __init__(self):
        self.gameOver = False
        self.players = [Player() for _ in range(random.randint(2, 6))]
        self.garbidge = []
        self.gameCards = {}
        self.card_expences = {}
        self.round = 1
        self.card_expences = getCardExpences()
        self.createStandardCards()
        self.createSpecialCards()
        self.createDecks()

    def nextRound(self):
        print("")
        print("Round: " + str(self.round))
        for player in self.players:
            player.takeTurn(self)
        self.round += 1

    def createDecks(self):
        print("Creating Decks... \n")
        for player in self.players:
            for _ in range(7):
                player.drawingPile.append(self.gameCards.get(str(Copper.Copper())).pop())
            for _ in range(3):
                player.drawingPile.append(self.gameCards.get(str(Estate.Estate())).pop())

    def createSpecialCards(self):
        chosen_cards = random.sample(getSpecialCards(), 10)
        # Garden has to be added here because it is not in the getSpecialCards() list
        for card in chosen_cards:
            self.gameCards[str(card.__str__())] = [card for _ in range(10)]

    def createStandardCards(self):
        # Money cards (Copper, Silver, Gold)
        self.gameCards["Copper"] = [Copper.Copper() for _ in range(60)]
        self.gameCards["Silver"] = [Silver.Silver() for _ in range(40)]
        self.gameCards["Gold"] = [Gold.Gold() for _ in range(30)]
        # Victorypoints for Two Players (Estate, Dutchy, Province)
        if len(self.players) == 2:
            self.gameCards["Estate"] = [Estate.Estate() for _ in range(8 + len(self.players) * 3)]
            self.gameCards["Dutchy"] = [Dutchy.Dutchy() for _ in range(8)]
            self.gameCards["Province"] = [Province.Province() for _ in range(8)]

        # Victorypoints for Three and Four Players (Estate, Dutchy, Province)
        elif len(self.players) == 3 or len(self.players) == 4:
            self.gameCards["Estate"] = [Estate.Estate() for _ in range(12 + len(self.players) * 3)]
            self.gameCards["Dutchy"] = [Dutchy.Dutchy() for _ in range(12)]
            self.gameCards["Province"] = [Province.Province() for _ in range(12)]
            self.gameCards["Curse"] = [Curse.Curse() for _ in range(10)]
            if len(self.players) == 5:
                self.gameCards["Province"] = [Province.Province() for _ in range(12)]
                self.gameCards["Curse"] = [Curse.Curse() for _ in range(20)]
            elif len(self.players) == 6:
                self.gameCards["Province"] = [Province.Province() for _ in range(12)]
                self.gameCards["Curse"] = [Curse.Curse() for _ in range(30)]
        # Victorypoints for Five and Six Players (Estate, Dutchy, Province, Curse)
        elif len(self.players) == 5 or len(self.players) == 6:
            self.gameCards["Estate"] = [Estate.Estate() for _ in range(12 + len(self.players) * 3)]
            self.gameCards["Dutchy"] = [Dutchy.Dutchy() for _ in range(12)]
            if len(self.players) == 5:
                self.gameCards["Province"] = [Province.Province() for _ in range(15)]
                self.gameCards["Curse"] = [Curse.Curse() for _ in range(40)]
            elif len(self.players) == 6:
                self.gameCards["Province"] = [Province.Province() for _ in range(18)]
                self.gameCards["Curse"] = [Curse.Curse() for _ in range(50)]
