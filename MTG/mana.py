from .color import Color

class HybridManaCostElement(object):
    """Represents a converted mana cost symbol in a mana cost"""
    def __init__(self, colors, colorless=0, amount=1):
        if not ((len(colors) == 2 and colorless == 0) or (len(colors) == 1 and colorless > 0)):
            raise ValueError("Not enough options for a hybrid")
        self.colorless = colorless
        self._colors = set(colors)
        self.amount = amount
        
    @property
    def cmc(self):
        """Returns the converted mana cost of this hybrid cost"""
        return max(self.colorless, 1) * self.amount

    @property
    def colors(self):
        """Returns the set of all colors represented by this mana symbol"""
        return self._colors

class PhyrexianManaCostElement(object):
    """Represents a phyrexian mana symbol in a mana cost"""
    def __init__(self, color, amount=1):
        self.color = color
        self.amount = amount
        HybridManaCostElement([Color.RED, Color.GREEN])

    @property
    def colors(self):
        return {self.color}
    
    @property
    def cmc(self):
        """Returns the converted mana cost of this phyrexian cost"""
        return self.amount

class ManaCost(object):
    """Represents the mana cost of anything"""
    # TODO: Add in snow mana support
    # TODO: Add in support for that one multi-hybrid card
    def __init__(self, colorless=0, colors=None, phyrexian=None, hybrid=None, variables=None):
        if colors is None:
            colors = {}
        if variables is None:
            variables = []
        if phyrexian is not None and phyrexian.amount == 0:
            phyrexian = None
        if hybrid is not None and hybrid.amount == 0:
            hybrid = None
        if phyrexian is not None and hybrid is not None:
            raise ValueError("Hybrid and phyrexian mana together is unsupported")
        self.colorless = colorless
        self.color_amounts = {color:count for (color, count) in colors.items() if count>0}
        self.phyrexian = phyrexian
        self.hybrid = hybrid
        self.variables = variables

    @property
    def cmc(self):
        """Returns the converted mana cost"""
        return (self.colorless +
                sum(self.colors.values()) +
                self.phyrexian.cmc +
                self.hybrid.cmc)

    @property
    def colors(self):
        """Returns the set of colors represented by this mana cost"""
        # TODO: Fix this, it's a mess right now
        return (set(self.color_amounts.keys()) |
                (self.phyrexian.colors if self.phyrexian is not None else set()) |
                (self.hybrid.colors() if self.hybrid is not None else set()))

    def mana_used(self, mana, life=0, variable_values=None):
        """Returns whether a given mana payment and an optional payment of life
        is sufficient to pay for this mana cost with the given variable
        assignments"""
        if variable_values is None:
            variable_values = {x:0 for x in self.variables}
        total_colorless = self.colorless + sum([variable_values[x] for x in self.variables])
        for color in self.colors:
            mana[color] -= self.colors[color]
            if mana[color] < 0:
                return False
        if self.hybrid is not None:
            hybrid_amount = self.hybrid.amount #remaining hybrid mana to match
            for color in self.hybrid.colors:
                matched = min(hybrid_amount, mana[color])
                hybrid_amount -= matched
                mana[color] -= matched
            if self.hybrid.colorless > 0:
                total_colorless += self.hybrid.colorless * hybrid_amount
        if self.phyrexian is not None:
            mana[self.phyrexian.color] -= (self.phyrexian.amount - life//2)
        return total_colorless <= sum(mana.values())
