from core.rungame import main

# -*- coding: utf-8 -*-
from random import shuffle
from collections import deque

SUITES = tuple('♣♠♦♥')
HEADS = tuple(tuple(h for h in map(str, range(2, 11))) + tuple('JQKA'))
DECK = frozenset(h + s for h in HEADS for s in SUITES)

def new_deck():
    deck = list(DECK)
    shuffle(deck)
    return deque(deck)

class Core(object):

    # TODO probably we should change players on the class like config, or use current configuration
    def start(self, players, debug):
        print('Started game for {} and debug option set on: {}'.format(players, debug))
        main()