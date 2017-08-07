from MTG.gameObject import *
from MTG.zone import *
from MTG.permanent import *




class Card(GameObject):


	def name(self):
		return self.characteristics.name
		
	def manacost(self):
		return self.characteristics.mana_cost
		
	def ID(self):
		pass

	def play_func(self):  # defaults to permanent
		make_permanent(self)
		pass



