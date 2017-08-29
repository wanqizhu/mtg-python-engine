import inspect


class Play(object):
    """
    Represents anything a player can choose to do when they have priority.
    """

    # TODO: implement targets:
    # target selection, validation, conditional targeting, etc.
    def __init__(self, apply_func, apply_condition=lambda: True, card=None, name=None):
        self.is_special_action = False
        self.is_mana_ability = False
        self.apply_func = apply_func
        self.apply_condition = apply_condition
        self.original_card = card
        self.name = name
        self.countered = False
        if not name and card:
            self.name = card.name

    def __repr__(self):
        return str(self.name)
        # + '\n' + inspect.getsource(self.apply)

    def apply(self):
        if self.countered or not self.apply_condition():
            print("All targets invalid. %r fizzles." % self)
            if self.original_card:
                self.original_card.owner.graveyard.add(self.original_card)
        else:
            self.apply_func()

