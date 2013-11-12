class Action(object):
    """Represents an action in the game. Specifically, something that
    goes on the stack"""

    def is_instant_speed(self):
        """Checks whether this action is instant speed, i.e. whether it can
        be played on top of other spells on the stack"""
        raise NotImplementedError()

    def resolve(self):
        """Does whatever is supposed to happen when the action resolves"""
        raise NotImplementedError()
