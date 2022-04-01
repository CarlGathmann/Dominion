import random

from src.Actioncards import Cellar, Chapel, Festival, Harbinger, Market, Merchant, Militia, Moneylender, Smithy, Vassal, \
    Village, Workshop
from src.Moneycards import Copper, Silver, Gold
from src.Player import Player
from src.Victorycards import Estate, Dutchy, Province, Curse


class Game:
    pass

    def __init__(self):
        self.gameOver = False
        self.players = [Player() for _ in range(random.randint(2, 6))]
        self.garbidge = []
        self.allCards = {}
        self.card_expences = {}
        self.round = 1
        self.createPlayingCards()
        self.createCardExpences()

    def nextRound(self):
        print("Round: " + str(self.round))
        for player in self.players:
            player.takeTurn(self)
            print(len(self.allCards["Copper"]))
        self.round += 1

    def createPlayingCards(self):
        # Money cards (Copper, Silver, Gold)
        self.allCards["Copper"] = [Copper.Copper() for _ in range(60)]
        self.allCards["Silver"] = [Silver.Silver() for _ in range(40)]
        self.allCards["Gold"] = [Gold.Gold() for _ in range(30)]
        # Victorypoints for Two Players (Estate, Dutchy, Province)
        if len(self.players) == 2:
            self.allCards["Estate"] = [Estate.Estate() for _ in range(8)]
            self.allCards["Dutchy"] = [Dutchy.Dutchy() for _ in range(8)]
            self.allCards["Province"] = [Province.Province() for _ in range(8)]

        # Victorypoints for Three and Four Players (Estate, Dutchy, Province)
        elif len(self.players) == 3 or len(self.players) == 4:
            self.allCards["Estate"] = [Estate.Estate() for _ in range(12)]
            self.allCards["Dutchy"] = [Dutchy.Dutchy() for _ in range(12)]
            self.allCards["Province"] = [Province.Province() for _ in range(12)]
            self.allCards["Curse"] = [Curse.Curse() for _ in range(10)]
            if len(self.players) == 5:
                self.allCards["Province"] = [Province.Province() for _ in range(12)]
                self.allCards["Curse"] = [Curse.Curse() for _ in range(20)]
            elif len(self.players) == 6:
                self.allCards["Province"] = [Province.Province() for _ in range(12)]
                self.allCards["Curse"] = [Curse.Curse() for _ in range(30)]
        # Victorypoints for Five and Six Players (Estate, Dutchy, Province, Curse)
        elif len(self.players) == 5 or len(self.players) == 6:
            self.allCards["Estate"] = [Estate.Estate() for _ in range(12)]
            self.allCards["Dutchy"] = [Dutchy.Dutchy() for _ in range(12)]
            if len(self.players) == 5:
                self.allCards["Province"] = [Province.Province() for _ in range(15)]
                self.allCards["Curse"] = [Curse.Curse() for _ in range(40)]
            elif len(self.players) == 6:
                self.allCards["Province"] = [Province.Province() for _ in range(18)]
                self.allCards["Curse"] = [Curse.Curse() for _ in range(50)]

    def createCardExpences(self):

        self.card_expences = {
            0: [Copper.Copper(), Chapel.Chapel()],
            2: [Chapel.Chapel(), Cellar.Cellar()],
            3: [Village.Village(), Silver.Silver(), Merchant.Merchant(), Workshop.Workshop(), Vassal.Vassal(),
                Harbinger.Harbinger()],
            4: [Smithy.Smithy(), Moneylender.Moneylender(), Militia.Militia()],
            5: [Market.Market(), Festival.Festival()],
            6: [Gold.Gold()]
        }
