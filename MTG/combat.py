# def fight(creature1, creature2):
# 	creature1.deals_damage(creature2, creature1.power)
# 	creature2.deals_damage(creature1, creature2.power)


def check_valid_attack(attacker):
    # TODO: can't attack alone
    return True


def check_valid_block(attacker, defender):
    for creature in defender.battlefield:
        if creature.is_creature and creature.status.is_blocking:
            if not creature.can_block(creature.status.is_blocking):
                return False
    # TODO: can't block alone
    # for creature in attacker.battlefield:
    #     if creature.is_creature:
    #         target = creature.status.is_attacking
            # if target
    return True
