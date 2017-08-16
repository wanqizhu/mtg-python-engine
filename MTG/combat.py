def fight(creature1, creature2):
	creature1.deals_damage(creature2, creature1.characteristics.power)
	creature2.deals_damage(creature1, creature2.characteristics.power)

def check_valid_attack(attacker, defender):
	return True

def check_valid_block(attacker, defender):
	return True