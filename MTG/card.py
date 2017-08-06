from MTG.gameObject import *
from MTG.zone import *
from MTG.permanent import *
from enum import Enum


class triggerConditions(Enum):
	# zone changes
	onPlay = 0
	onDraw = 1
	onDiscard = 2
	onEtB = 3
	onPlayfromHand = 4
	onEnterGrave = 5
	onDeath = 6
	onLeaveBattlefield = 7
	# phase (CONTROLLER ONLY or ALL PLAYERS)
	onUpkeep = 10
	onMain1 = 11
	onMain2 = 12
	onEnterCombat = 13
	onDeclareAttackers = 14
	onDeclareBlockers = 15
	onEndofCombat = 16
	onEndstep = 17
	# events
	onUntap = 8
	onTap = 9
	onDealDamage = 18
	onDealDamageToPlayers = 19
	onDealDamageToCreatures = 20
	onTakingDamage = 21
	onAttack = 22
	onBlock = 23
	# global events
	onRevolt = 24 # permanent leaving battlefield
	onControllerLifeLoss = 25
	onLifeLoss = 26
	onControllerLifeGain = 27
	onLifeGain = 28
	onCounterPutOnPermanent = 29



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



