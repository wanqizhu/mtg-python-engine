from MTG import gameobject


class Card(gameobject.GameObject):

	def ID(self):
		pass

	def play_func(self):  # defaults to permanent
		permanent.make_permanent(self)
		pass


from MTG import permanent  # need to move this later to avoid circular import stuff

