from collections import defaultdict
from enum import Enum
import re

class Mana(Enum):
    WHITE = 0
    BLUE = 1
    BLACK = 2
    RED = 3
    GREEN = 4
    COLORLESS = 5

class ManaPool():
    manachr = ['W', 'U', 'B', 'R', 'G', 'C']

    def __init__(self, controller=None):
        self.pool = defaultdict(lambda: 0)
        self.controller = controller
        
    def add(self, mana, amount):
        self.pool[mana] += amount

    
    def pay(self, manacost):
        for manatype in manacost:
            assert self.pool[manatype] >= manacost[manatype]
        for manatype in manacost:
            self.pool[manatype] -= manacost[manatype]


    def chr_to_mana(self, c):
        assert c in self.manachr
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


    def canPay(self, manacost):
        "manacost here is a string, e.g. 2U"
        cost = defaultdict(lambda: 0)
        for c in manacost:
            if c in self.manachr:
                cost[self.chr_to_mana(c)] += 1

        # unrestricted costs (numbers in mana costs)
        anyTypeMana = 0

        numbers = re.match('\d+', manacost)  # find leading number
        if numbers:
            anyTypeMana += int(numbers.group(0))


        # hybrid mana costs
        # note the mana symbols will have already been scanned above, so we need to subtract the cost we're not paying
        hybrid = re.findall('\([WUBRGC2]/[WUBRGC]\)', manacost)
        for h in hybrid:
            choice = input('How would you like to pay? 0 (default): {}\t 1: {}\n'.format(h[1], h[3]))
       
            if choice == '1':
                if h[1] != '2':
                    cost[self.chr_to_mana(h[1])] -= 1  # already scanned above
            else:  # default 0
                cost[self.chr_to_mana(h[3])] -= 1
                if h[1] == '2':
                    anyTypeMana += 2

        

        if anyTypeMana > 0:
            choice = input('How would you like to pay {}? Enter blank for automatic payment, or enter a string of colored mana\n'.format(anyTypeMana))
            
            if re.match('[WUBRGC]+', choice) and len(choice) == anyTypeMana:
                for c in choice:
                    cost[self.chr_to_mana(c)] += 1
                anyTypeMana = 0
            else:  # default
                print("automatic payment...\n")
                for mana in Mana:
                    if anyTypeMana == 0:
                        break
                    if self.pool[mana] > cost[mana]:
                        amount = min(self.pool[mana] - cost[mana], anyTypeMana)
                        cost[mana] += amount
                        anyTypeMana -= amount

        if anyTypeMana > 0:
            return False

        for mana in Mana:
            if self.pool[mana] < cost[mana]:
                return False

        return cost




    def clear(self):
        self.pool.clear()

    def __repr__(self):
        return '  '.join([str(manatype) + ': ' + str(self.pool[manatype]) for manatype in Mana])