from collections import defaultdict
from enum import Enum
import re


manachr = ['W', 'U', 'B', 'R', 'G', 'C', '1']

class Mana(Enum):
    WHITE = 0
    BLUE = 1
    BLACK = 2
    RED = 3
    GREEN = 4
    COLORLESS = 5
    GENERIC = 6


# any length > 0 of the following: { X, numbers, hybrid e.g. (U/R), WUBRGC }
mana_pattern = re.compile(
    '(X|' '\d|' '(\([WUBRGC2]/[WUBRGC]\))|' '[WUBRGC])+')


def str_to_mana_dict(manacost):
    cost = defaultdict(lambda: 0)
    for c in manacost:
        if c in manachr:
            cost[chr_to_mana(c)] += 1
    num = re.match('\d+', manacost)  # find leading number
    if num:
        cost[Mana.GENERIC] = int(num.group(0))
    return cost


def chr_to_mana(c):
    assert c in manachr
    if c == 'W':
        return Mana.WHITE
    if c == 'U':
        return Mana.BLUE
    if c == 'B':
        return Mana.BLACK
    if c == 'R':
        return Mana.RED
    if c == 'G':
        return Mana.GREEN
    if c == 'C':
        return Mana.COLORLESS
    if c == '1':
        return Mana.GENERIC



class ManaPool():

    def __init__(self, controller=None):
        self.pool = defaultdict(lambda: 0)
        self.controller = controller

    def add(self, mana, amount=1):
        if isinstance(mana, str):
            self.add_str(mana)
            return

        self.pool[mana] += amount

    def add_str(self, mana_str):
        for c in mana_str:
            self.add(chr_to_mana(c))



    def pay(self, manacost):
        if manacost is None:
            return

        for manatype in manacost:
            assert self.pool[manatype] >= manacost[manatype]
        for manatype in manacost:
            self.pool[manatype] -= manacost[manatype]

    def is_empty(self):
        for c in manachr:
            if self.pool[chr_to_mana(c)] != 0:
                return False
        return True


    def determine_costs(self, manacost):
        """ Converts string mana costs to mana dict, resolving hybrid / additional costs"""
        cost = str_to_mana_dict(manacost)

        # hybrid mana costs
        # note the mana symbols will have already been scanned above, so we need to subtract the cost we're not paying
        hybrid = re.findall('\([WUBRGC2]/[WUBRGC]\)', manacost)
        for h in hybrid:
            if self.controller.autoPayMana:
                choice = '0'
            else:
                choice = self.controller.make_choice(
                    'How would you like to pay? 0 (default): {}\t 1: {}\n'.format(h[1], h[3]))

            if choice == '1':
                if h[1] != '2':
                    cost[chr_to_mana(h[1])] -= 1  # already scanned above
            else:  # default 0
                cost[chr_to_mana(h[3])] -= 1
                if h[1] == '2':
                    cost[Mana.GENERIC] += 2


        # TODO: define value of X
        return cost


    def canPay(self, manacost, convoke=False):
        """manacost here is a string, e.g. 2U, or a dict of Manas (e.g. {Mana.BLUE, 3})

        This returns False if not possible, or a cost dict of Mana(Enum)s
         that can be passed to self.pay for actual payment

        This determines generic mana and converts it to actual colored mana

        Note this DOES NOT pay any mana
        """
        if manacost is None:
            return True

        if isinstance(manacost, str):
            manacost = self.determine_costs(manacost)

        genericMana = manacost[Mana.GENERIC]

        if genericMana > 0:
            if self.controller.autoPayMana:
                choice = ''
            else:
                choice = self.controller.make_choice(
                    'How would you like to pay {}? Enter blank for automatic payment, or enter a string of colored mana\n'.format(genericMana))

            if re.match('[WUBRGC]+', choice) and len(choice) == genericMana:
                for c in choice:
                    manacost[chr_to_mana(c)] += 1
                genericMana = 0
            else:  # default
                # print("automatic payment...\n")
                for mana in Mana:
                    if genericMana == 0:
                        break
                    if self.pool[mana] > manacost[mana]:
                        amount = min(self.pool[mana] - manacost[mana], genericMana)
                        manacost[mana] += amount
                        genericMana -= amount

        manacost[Mana.GENERIC] = genericMana
        if genericMana > 0:
            return False

        for mana in Mana:
            if self.pool[mana] < manacost[mana]:
                return False

        return manacost

    def clear(self):
        self.pool.clear()

    def __repr__(self):
        return '  '.join([str(manatype) + ': ' + str(self.pool[manatype]) for manatype in Mana])
