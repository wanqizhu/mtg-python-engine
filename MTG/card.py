from MTG.gameObject import *
from MTG.zone import *
from MTG.permanent import *




class Card(GameObject):


	def ID(self):
		pass

	def play_func(self):  # defaults to permanent
		make_permanent(self)
		pass



