from __future__ import print_function
from random import *


class Utility(object):

    def __init__(self):
        print('Utility Constructor')

    @staticmethod
    def picks_count(value):
        return Deck.picks.count(value)

    @staticmethod
    def dispense(cards=None):
        if cards is None:
            cards = []
        i = randint(0, 24)
        shuffle(cards)
        v = cards[i]

        k = None
        for k in v.keys():
            k = k

        if k == 'FV':
            r = sample(v.get(k), 1)
            return k+str(r[0]), r[0]
        else:
            return k, v.get(k)

    @staticmethod
    def compute(hand=None):
        if hand is None:
            hand = []

        aces = hand.count('A')
        low = 1
        high = 11

        if (aces == 1) and (Utility.count_hand_without_aces(hand) + high > 21):
            return Utility.count_hand_without_aces(hand) + low
        elif (aces == 1) and (Utility.count_hand_without_aces(hand) + high == 21):
            return Utility.count_hand_without_aces(hand) + high
        elif (aces == 2) and (Utility.count_hand_without_aces(hand) + high + low == 21):
            return Utility.count_hand_without_aces(hand) + high + low
        elif (aces == 2) and (Utility.count_hand_without_aces(hand) + high + low > 21):
            return Utility.count_hand_without_aces(hand) + low + low
        else:
            return Utility.count_hand_without_aces(hand)

    @staticmethod
    def count_hand_without_aces(hand=None):
        total = 0
        for i in hand:
            try:
                total += i
            except TypeError:
                pass
        return total


class Hand(object):

    def __int__(self, c=None):
        self.c = c

    def get_hand(self):
        return self.c

    def add_hand(self, value):
        return self.c.append(value)


class Deck(object):

    cards = [{"FV": range(2, 11)}, {"K": 10}, {"Q": 10}, {"A": (1, 11)}, {"J": 10}] * 5
    picks = []

    def __init__(self):
        print('Deck Constructor')

    def bet(self):
        value, result = Utility.dispense(self.cards)

        if Utility.picks_count(value) > 5:
            Deck.bet(self)

            Deck.picks = value
        if value == 'A':
            return value
        return result

    def init_hand(self):

        i_h = []
        i = 0
        while True:
            value, result = Utility.dispense(self.cards)
            Deck.picks = value

            if value == 'A':
                i_h.append(value)
            else:
                i_h.append(result)

            i += 1
            if i == 2:
                break

        return i_h


class Player(object):

    def __init__(self, cash, bet_amount=50, hand=None, deck = Deck()):
        if hand is None:
            hand = []
        self.cash = cash
        self.bet_amount = bet_amount
        self.hand = hand
        self.deck = deck

    def set_hand(self):
        self.hand = self.deck.init_hand()

    def add_to_hand(self):
        self.hand.append(self.deck.bet())

    def deal(self, amount):
        self.bet_amount = amount
        self.cash -= amount

    def push(self):
        self.cash += self.bet_amount

    def win(self):
        self.cash += (self.bet_amount * 3)

    def loss(self):
        return self.cash

    def hit(self, dk=Deck().bet()):
        self.hand.append(dk)
        return self.hand


class Dealer(object):

    def __init__(self, hand=None, deck = Deck()):
        if hand is None:
            hand = []
        self.hand = hand
        self.deck = deck

    def set_hand(self):
        self.hand = self.deck.init_hand()

    def add_to_hand(self):
        self.hand.append(self.deck.bet())


def play():
    deck = Deck()
    player = Player(500, deck)
    dealer = Dealer(deck)

    amount = int(raw_input('Enter Betting Amount'))

    player.deal(amount)
    player.set_hand()
    dealer.set_hand()

    print('Player Hand', player.hand)
    print('Dealer Hand', dealer.hand)

    player_action = int(raw_input('Enter 1 for a HIT and 2 for a STAND'))

    while player_action == 1:
        player.add_to_hand()
        player_action = int(raw_input('Enter 1 for a HIT and 2 for a STAND'))

    if player_action == 2:
        if Utility.compute(dealer.hand) <= 17:
            dealer.add_to_hand()

        if Utility.compute(player.hand) == 21 and Utility.compute(dealer.hand) != 21:
            player.win()
            print('BlackJack', player.hand, player.cash)
        elif Utility.compute(player.hand) == 21 and Utility.compute(dealer.hand) == 21:
            player.push()
            print('Push', player.hand, player.cash)
        elif Utility.compute(player.hand) == Utility.compute(dealer.hand):
            player.push()
            print('Push', player.hand, player.cash)
        elif Utility.compute(player.hand) > Utility.compute(dealer.hand):
            player.win()
            print('Win', player.hand, player.cash)
        elif Utility.compute(player.hand) < Utility.compute(dealer.hand):
            player.loss()
            print('Loss', player.hand, player.cash)


play()
