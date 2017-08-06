# mana payment

from MTG.mana import *
m = ManaPool(); m.pool[Mana.BLUE] = 4; m.pool[Mana.WHITE] = 3

assert m.canPay('U')
assert m.canPay('UUW')
assert m.canPay('1R') is False

m.canPay('4U')
m.canPay('(2/R)(2/W)(2/U)')