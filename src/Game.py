import random

from src.Actioncards import Cellar, Chapel, Festival, Harbinger, Market, Merchant, Militia, Moneylender, Smithy, \
    Vassal, Village, Workshop, Moat, Bureaucrat, ThroneRoom, Remodel, Poacher, Bandit, Laboratory, Library, Mine, \
    Artisan, Sentury
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
                     Vassal.Vassal(), Village.Village(), Workshop.Workshop(), Moat.Moat(), Bureaucrat.Bureaucrat(),
                     ThroneRoom.ThroneRoom(), Remodel.Remodel(), Poacher.Poacher(), Bandit.Bandit(),
                     Laboratory.Laboratory(), Library.Library(), Mine.Mine(), Artisan.Artisan(), Sentury.Sentury()]
    return special_cards


def getAllCards():
    all_cards = getStandardCards() + getSpecialCards()
    return all_cards


def getCardExpences():
    card_expences = {
        0: [Copper.Copper(), Curse.Curse()],
        2: [Chapel.Chapel(), Cellar.Cellar(), Moat.Moat()],
        3: [Village.Village(), Silver.Silver(), Merchant.Merchant(), Workshop.Workshop(), Vassal.Vassal(),
            Harbinger.Harbinger()],
        4: [Smithy.Smithy(), Moneylender.Moneylender(), Militia.Militia(), Bureaucrat.Bureaucrat(),
            ThroneRoom.ThroneRoom(), Remodel.Remodel(), Poacher.Poacher()],
        5: [Market.Market(), Festival.Festival(), Bandit.Bandit(), Laboratory.Laboratory(), Library.Library(),
            Mine.Mine(), Sentury.Sentury()],
        6: [Gold.Gold(), Artisan.Artisan()]
    }
    return card_expences


class Game:
    pass

    def __init__(self):
        self.gameOver = False
        self.players = [Player(str(i)) for i in range(1, random.randint(3, 7))]
        print(len(self.players))
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
        print(("Round: " + str(self.round)).upper())
        counter = 1
        for player in self.players:
            print(('\n %s_%s takes his turn:' % (player, counter)).upper())
            player.takeTurn(self)
            counter += 1
        if len(self.gameCards) <= 14:
            self.gameOver = True
            print("Tree drawing piles are empty")
        elif len(self.gameCards['Province']) == 0:
            print("No Provinces left")
            self.gameOver = True
        self.round += 1

    def printResults(self):
        print(('\n results after %s rounds are:' % self.round).upper())
        for player in self.players:
            print(player.name, 'has', player.victorypoints, 'Victorypoints')
        self.players.sort(key=lambda p: p.victorypoints, reverse=True)
        print(('\n The winner is %s_%s' % (self.players[0], self.players[0].name)).upper())
        print('\n Podium:'.upper())
        for player in self.players:
            print(player.name)

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

    def getCardFromPile(self, wanted_card):
        if len(self.gameCards[wanted_card.__str__()]) > 1:
            return self.gameCards[wanted_card.__str__()].pop()
        elif len(self.gameCards[wanted_card.__str__()]) == 1:
            card = self.gameCards[wanted_card.__str__()].pop()
            del self.gameCards[wanted_card.__str__()]
            return card

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
            self.gameCards["Curse"] = [Curse.Curse() for _ in range(10)]

        # Victorypoints for Three and Four Players (Estate, Dutchy, Province)
        elif len(self.players) == 3 or len(self.players) == 4:
            self.gameCards["Estate"] = [Estate.Estate() for _ in range(12 + len(self.players) * 3)]
            self.gameCards["Dutchy"] = [Dutchy.Dutchy() for _ in range(12)]
            self.gameCards["Province"] = [Province.Province() for _ in range(12)]
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
