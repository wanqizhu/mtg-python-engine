from MTG import gameobject


class Attributes():
	def __init__(self):
		# attributes goes here
		self.num_creatures_can_block = 1


class Card(gameobject.GameObject):

	def __init__(self, characteristics=gameobject.Characteristics(),
             controller=None, owner=None, zone=None, previousState=None):

		super(Card, self).__init__(characteristics, controller, owner, zone, previousState)
		
		self.attributes = Attributes()



	def ID(self):
		pass

	def play_func(self):  # defaults to permanent
		permanent.make_permanent(self)
		pass


from MTG import permanent  # need to move this later to avoid circular import stuff

