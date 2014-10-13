from collections import defaultdict

__author__ = 'Michael'

class Mana(object):
    def __init__(self, color, source):
        self.color = color
        self.source = source

    def __hash__(self):
        return hash((hash(self.source), hash(self.color)))

class ManaPool(object):
    pool = defaultdict(lambda: 0)

    def add(self, mana, amount):
        self.pool[mana] += amount

    def clear(self):
        self.pool.clear()