import random
from inflect import engine as eng


from src.Dominion.Actioncards import Library, Workshop, Moneylender, Militia, Merchant, Bureaucrat, Village, Smithy, \
    ThroneRoom, Cellar, Market, Festival, Vassal, Laboratory, Moat, Poacher, Remodel, Bandit, Chapel, Artisan, Mine, \
    Sentury, Harbinger
from src.Dominion.Moneycards import Copper, Silver, Gold
from src.Dominion.Player import Player
from src.Dominion.Victorycards import Estate, Curse, Province, Dutchy

eng = eng()

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

    def __init__(self):
        self.gameOver = False
        self.garbidge = []
        self.gameCards = {}
        self.card_expences = {}
        self.round = 1
        self.card_expences = getCardExpences()
        self.players = [Player(eng.number_to_words(i).upper()) for i in range(1, random.randint(3, 7))]
        self.createStandardCards()
        self.createSpecialCards()
        self.createDecks()

    def nextRound(self):
        print("")
        print(("Round: " + str(self.round)).upper())
        for player in self.players:
            print('\n', player.name, 'takes his turn:'.upper())
            player.takeTurn(self)
        if len(self.gameCards) <= 14:
            self.gameOver = True
            print("\n Game Over".upper())
            print("Tree drawing piles are empty")
        elif len(self.gameCards['Province']) == 0:
            print("\n Game Over".upper())
            print("No Provinces left")
            self.gameOver = True
        self.round += 1

    def printResults(self):
        print(('\n results after %s rounds are:' % self.round).upper())
        for player in self.players:
            print(player.name, 'has', player.victorypoints, 'Victorypoints')
        self.players.sort(key=lambda p: p.victorypoints, reverse=True)
        print('\n The winner is'.upper(), self.players[0].name)
        print('\n Podium:'.upper())
        for player in self.players:
            print(player.name)

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

    def createDecks(self):
        for player in self.players:
            player.createDeck(self)
            player.draw(5)

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
