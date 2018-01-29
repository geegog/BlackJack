from __future__ import print_function
from random import *


class Utility(object):

    def __init__(self, cards=None):
        if cards is None:
            self.cards = []
        else:
            self.cards = cards

    def dispense(self):
        x = sample(self.cards, 1)
        k = None
        for k in x[0].keys():
            k = k

        if k == 'FV':
            r = sample(x[0].get(k), 1)
            return r[0]
        elif k == 'A':
            return x[0].get(k)
        else:
            return x[0].get(k)


class Deck(object):

    cards = [{"FV": range(2, 11)}, {"K": 10}, {"Q": 10}, {"A": (1, 11)}, {"J": 10}] * 5
    picks = {}

    def __init__(self):
        print('Empty Constructor')


class Player(object):

    cash = 50
    hand = []

    def __init__(self, cash):
        self.cash = cash

    def bet(self, amount):
        self.cash -= amount


class Dealer(object):

    hand = []

    def __init__(self, hand):
        self.hand = hand


y = Utility(Deck().cards)
print(y.dispense())
