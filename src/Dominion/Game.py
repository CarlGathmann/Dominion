import random
from inflect import engine as eng

from src.Dominion.Actioncards import Library, Workshop, Moneylender, Militia, Merchant, Bureaucrat, Village, Smithy, \
    ThroneRoom, Cellar, Market, Festival, Vassal, Laboratory, Moat, Poacher, Remodel, Bandit, Chapel, Artisan, Mine, \
    Sentury, Harbinger
from src.Dominion.Moneycards import Copper, Silver, Gold
from src.Dominion.Player import Player
from src.Dominion.Victorycards import Estate, Curse, Province, Dutchy

eng = eng()


def get_standard_cards():
    standard_cards = [Curse.Curse(), Copper.Copper(), Silver.Silver(), Gold.Gold(), Estate.Estate(), Dutchy.Dutchy(),
                      Province.Province()]
    return standard_cards


def get_special_cards():
    special_cards = [Cellar.Cellar(), Chapel.Chapel(), Festival.Festival(), Harbinger.Harbinger(), Market.Market(),
                     Merchant.Merchant(), Militia.Militia(), Moneylender.Moneylender(), Smithy.Smithy(),
                     Vassal.Vassal(), Village.Village(), Workshop.Workshop(), Moat.Moat(), Bureaucrat.Bureaucrat(),
                     ThroneRoom.ThroneRoom(), Remodel.Remodel(), Poacher.Poacher(), Bandit.Bandit(),
                     Laboratory.Laboratory(), Library.Library(), Mine.Mine(), Artisan.Artisan(), Sentury.Sentury()]
    return special_cards


def get_all_cards():
    all_cards = get_standard_cards() + get_special_cards()
    return all_cards


def get_card_expenses():
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
        self.game_over = False
        self.garbage = []
        self.game_cards = {}
        self.card_expenses = {}
        self.round = 1
        self.card_expenses = get_card_expenses()
        self.players = [Player(eng.number_to_words(i).upper()) for i in range(1, random.randint(3, 7))]
        self.create_standard_cards()
        self.create_special_cards()
        self.create_decks()

    def next_round(self):
        print("")
        print(("Round: " + str(self.round)).upper())
        for player in self.players:
            print('\n', player.name, 'takes his turn:'.upper())
            player.take_turn(self)
        if len(self.game_cards) <= 14:
            self.game_over = True
            print("\n Game Over".upper())
            print("Tree drawing piles are empty")
        elif len(self.game_cards['Province']) == 0:
            print("\n Game Over".upper())
            print("No Provinces left")
            self.game_over = True
        self.round += 1

    def print_results(self):
        print(('\n results after %s rounds are:' % self.round).upper())
        for player in self.players:
            print(player.name, 'has', player.victory_points, 'Victory points')
        self.players.sort(key=lambda p: p.victory_points, reverse=True)
        print('\n The winner is'.upper(), self.players[0].name)
        print('\n Podium:'.upper())
        for player in self.players:
            print(player.name)

    def create_special_cards(self):
        chosen_cards = random.sample(get_special_cards(), 10)
        # Garden has to be added here because it is not in the getSpecialCards() list
        for card in chosen_cards:
            self.game_cards[str(card.__str__())] = [card for _ in range(10)]

    def get_card_from_pile(self, wanted_card):
        if len(self.game_cards[wanted_card.__str__()]) > 1:
            return self.game_cards[wanted_card.__str__()].pop()
        elif len(self.game_cards[wanted_card.__str__()]) == 1:
            card = self.game_cards[wanted_card.__str__()].pop()
            del self.game_cards[wanted_card.__str__()]
            return card

    def create_decks(self):
        for player in self.players:
            player.create_deck(self)
            player.draw(5)

    def create_standard_cards(self):
        # Money cards (Copper, Silver, Gold)
        self.game_cards["Copper"] = [Copper.Copper() for _ in range(60)]
        self.game_cards["Silver"] = [Silver.Silver() for _ in range(40)]
        self.game_cards["Gold"] = [Gold.Gold() for _ in range(30)]
        # Victory points for Two Players (Estate, Dutchy, Province)
        if len(self.players) == 2:
            self.game_cards["Estate"] = [Estate.Estate() for _ in range(8 + len(self.players) * 3)]
            self.game_cards["Dutchy"] = [Dutchy.Dutchy() for _ in range(8)]
            self.game_cards["Province"] = [Province.Province() for _ in range(8)]
            self.game_cards["Curse"] = [Curse.Curse() for _ in range(10)]

        # Victory points for Three and Four Players (Estate, Dutchy, Province)
        elif len(self.players) == 3 or len(self.players) == 4:
            self.game_cards["Estate"] = [Estate.Estate() for _ in range(12 + len(self.players) * 3)]
            self.game_cards["Dutchy"] = [Dutchy.Dutchy() for _ in range(12)]
            self.game_cards["Province"] = [Province.Province() for _ in range(12)]
            if len(self.players) == 5:
                self.game_cards["Province"] = [Province.Province() for _ in range(12)]
                self.game_cards["Curse"] = [Curse.Curse() for _ in range(20)]
            elif len(self.players) == 6:
                self.game_cards["Province"] = [Province.Province() for _ in range(12)]
                self.game_cards["Curse"] = [Curse.Curse() for _ in range(30)]
        # Victory points for Five and Six Players (Estate, Dutchy, Province, Curse)
        elif len(self.players) == 5 or len(self.players) == 6:
            self.game_cards["Estate"] = [Estate.Estate() for _ in range(12 + len(self.players) * 3)]
            self.game_cards["Dutchy"] = [Dutchy.Dutchy() for _ in range(12)]
            if len(self.players) == 5:
                self.game_cards["Province"] = [Province.Province() for _ in range(15)]
                self.game_cards["Curse"] = [Curse.Curse() for _ in range(40)]
            elif len(self.players) == 6:
                self.game_cards["Province"] = [Province.Province() for _ in range(18)]
                self.game_cards["Curse"] = [Curse.Curse() for _ in range(50)]
