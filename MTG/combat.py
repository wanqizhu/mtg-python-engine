def fight(creature1, creature2):
	creature1.take_damage(creature2.characteristics.power)
	creature2.take_damage(creature1.characteristics.power)