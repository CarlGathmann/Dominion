import random

from src.Dominion.Actioncards.Moat import Moat
from src.Dominion.Cardtypes.ActionCard import ActionCard
from src.Dominion.Cardtypes.Moneycard import Moneycard
from src.Dominion.Cardtypes.Victorycard import Victorycard
from src.Dominion.Moneycards.Copper import Copper
from src.Dominion.Victorycards.Estate import Estate


class Player:

    def __init__(self, name):
        self.name = 'Player' + name
        self.money = 0
        self.buys = 0
        self.actions = 0
        self.victory_points = 0
        self.can_be_attacked = True
        self.hand = []
        self.drawing_pile = []
        self.discarding_pile = []
        self.played_cards = []

    def take_turn(self, game):
        # PREP
        self.actions = 1
        self.buys = 1
        self.money = 0
        self.can_be_attacked = True
        # ACTION PHASE
        print("# ACTION PHASE")
        self.print_hand()
        self.play_actions(game)
        # BUY-PHASE
        print("# BUY-PHASE")
        self.buy_cards(game)

        # DISCARD CARDS
        self.dicard_all_cards()

        self.draw(5)

    def play_actions(self, game):
        while self.actions > 0:
            if len(self.get_action_in_hand()) != 0:
                choice = random.choice(self.get_action_in_hand())
                self.play_action_card_in_hand(choice, game)
                self.actions -= 1
            else:
                break

    def buy_cards(self, game):
        for card in self.get_money_cards_in_hand():
            self.play_money_card(card)
        while self.buys > 0:
            possible_buys = self.get_possible_buys(game)
            if len(possible_buys) > 0:
                choice = random.choice(possible_buys)
                if isinstance(choice, Victorycard):
                    self.victory_points += choice.victory_points
                self.discarding_pile.append(game.get_card_from_pile(choice))
                self.money -= choice.expenses
                self.buys -= 1
                print("Buying:", choice)
            else:
                print("can't buy anything")
                self.buys = 0

    def play_money_card(self, card: Moneycard):
        print("playing: ", card.__str__())
        self.hand.remove(card)
        self.played_cards.append(card)
        self.money += card.money

    def play_action_card_in_hand(self, card: ActionCard, game):
        print("playing: ", card.__str__())
        self.hand.remove(card)
        self.played_cards.append(card)
        self.actions += card.actions
        self.buys += card.buys
        self.money += card.money
        self.draw(card.cards)
        card.special_action(self, game)

    def play_action_card(self, card: ActionCard, game):
        print("playing: ", card.__str__())
        self.actions += card.actions
        self.buys += card.buys
        self.money += card.money
        self.draw(card.cards)
        card.special_action(self, game)

    def get_action_in_hand(self):
        actions = []
        for card in self.hand:
            if isinstance(card, ActionCard):
                actions.append(card)
        return actions

    def get_money_cards_in_hand(self):
        money_cards = []
        for card in self.hand:
            if isinstance(card, Moneycard):
                money_cards.append(card)
        return money_cards

    def get_possible_buys(self, game):
        possible_buys = []
        for key in game.game_cards.keys():
            if game.game_cards[key][0].expenses <= self.money:
                possible_buys.append(game.game_cards[key][0])
        return possible_buys

    def draw(self, amount: int):
        if amount != 0:
            print("Drawing", amount, "cards...")

        for _ in range(amount):
            if len(self.drawing_pile) != 0:
                card = self.drawing_pile.pop()
                if card.__class__ == Moat:
                    self.can_be_attacked = False
                self.hand.append(card)
            elif len(self.discarding_pile) != 0:
                self.shuffle()
                card = self.drawing_pile.pop()
                if card.__class__ == Moat:
                    self.can_be_attacked = False
                self.hand.append(card)
            else:
                print("No cards to draw")
                break

    def shuffle(self):
        self.drawing_pile += self.discarding_pile
        self.discarding_pile.clear()
        random.shuffle(self.drawing_pile)

    def create_deck(self, game):
        print("\n Creating Deck for player %s..." % self.name)
        for _ in range(7):
            self.drawing_pile.append(game.game_cards.get(str(Copper())).pop())
        for _ in range(3):
            self.drawing_pile.append(game.game_cards.get(str(Estate())).pop())
        self.shuffle()

    def discard_from_hand(self, card):
        self.hand.remove(card)
        self.discarding_pile.append(card)

    def draw_and_return(self):
        if len(self.drawing_pile) != 0:
            return self.drawing_pile.pop()
        elif len(self.discarding_pile) != 0:
            self.shuffle()
            return self.drawing_pile.pop()
        else:
            print("no cards to draw")
            return None

    def dicard_all_cards(self):
        self.discarding_pile += self.hand
        self.discarding_pile += self.played_cards
        self.played_cards.clear()
        self.hand.clear()

    def discard_list_of_cards(self, cards):
        print("discarding", len(cards), "cards...")
        for card in cards:
            self.discarding_pile.append(card)
            self.hand.remove(card)

    def choose_x_cards_from_hand(self, x):
        choices = random.sample(self.hand, x)
        return choices

    def print_attributes(self):
        print(
            "Actions: %s, Buys: %s, Money: %s, Handcards: %s, All Cards: %s"
            % (self.actions, self.buys, self.money, len(self.hand),
               len(self.hand + self.drawing_pile + self.discarding_pile + self.played_cards))
        )

    def print_hand(self):
        print("Hand:")
        print(*self.hand)

    def print_deck(self):
        print("Hand:")
        print(*self.hand)
        print("Drawing Pile:")
        print(*self.drawing_pile)

    def __str__(self):
        return str(self.__class__).split(".")[-1].strip("'>")
