from __future__ import print_function
from random import *


class Utility(object):

    def __init__(self):
        print('Utility Constructor')

    @staticmethod
    def picks_count(value):
        return Deck.picks.count(value)

    @staticmethod
    def dispense(cards=[]):
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
    def compute(hand=[]):
        total = 0
        for i in hand:
            try:
                total += i
            except TypeError:
                key, value = i
                low, high = value
                if (total + low) < 21:
                    total += high
                elif (total + high) > 21:
                    total += low
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
            return value, result
        return result

    def init_hand(self):

        i_h = []
        i = 0
        while True:
            value, result = Utility.dispense(self.cards)
            Deck.picks = value

            if value == 'A':
                i_h.append((value, result))
            else:
                i_h.append(result)

            i += 1
            if i == 2:
                break

        return i_h


class Player(object):

    def __init__(self, cash, bet_amount=50, hand=None):
        if hand is None:
            hand = []
        self.cash = cash
        self.bet_amount = bet_amount
        self.hand = hand

    def bet(self, amount):
        self.bet_amount = amount
        self.cash -= amount

    def win(self):
        self.cash = self.bet_amount * 2

    def loss(self):
        self.cash = self.cash

    def hit(self, dk=Deck().bet()):
        self.hand.append(dk)
        return self.hand


class Dealer(object):

    def __init__(self, hand=None):
        if hand is None:
            hand = []
        self.hand = hand


deck = Deck()
player = Player(500, 250, deck.init_hand())
dealer = Dealer(deck.init_hand())

player.hit(deck.bet())

print(Utility.compute(player.hand))

print(player.hand)
print(player.cash)
print(player.bet_amount)
