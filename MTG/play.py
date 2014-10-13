__author__ = 'Michael'


class Play(object):
    """
    Represents anything a player can choose to do when they have priority.
    """
    def get_action(self):
        raise NotImplementedError()

    def is_special_action(self):
        raise NotImplementedError()

    def is_mana_ability(self):
        raise NotImplementedError()

class LandPlay(Play):
    def get_action(self):
        pass

    def is_special_action(self):
        return True

    def is_mana_ability(self):
        return False