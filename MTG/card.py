from MTG import gameobject
from MTG import permanent


class Card(gameobject.GameObject):

	def ID(self):
		pass

	def play_func(self):  # defaults to permanent
		permanent.make_permanent(self)
		pass



