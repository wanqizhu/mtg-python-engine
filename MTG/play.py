import inspect


class Play(object):
    """
    Represents anything a player can choose to do when they have priority.
    """

    # TODO: implement targets:
    # target selection, validation, conditional targeting, etc.
    def __init__(self, apply_func, apply_condition=lambda: True, card=None, source=None,
                name=None, targets_chosen=None, target_criterias=None, is_mana_ability=False):
        self.is_special_action = False
        self.is_mana_ability = is_mana_ability
        self.apply_func = apply_func
        self.apply_condition = apply_condition
        self.original_card = card
        self.source = source
        self.targets_chosen = targets_chosen
        self.target_criterias = target_criterias
        self.name = name
        self.countered = False
        if not name and card:
            self.name = card.name
        if not name and not card and source:
            self.name = source.name

        if card:
            self.controller = card.controller
        elif source:
            self.controller = source.controller
        else:
            self.controller = None

        if not targets_chosen and card:
            self.targets_chosen = card.targets_chosen
            self.target_criterias = card.target_criterias
        elif not targets_chosen and source:
            self.targets_chosen = source.targets_chosen
            self.target_criterias = source.target_criterias


    def __repr__(self):
        return str(self.name)
        # + '\n' + inspect.getsource(self.apply)

    def apply(self):
        fizzles = False

        if self.targets_chosen and not any([c(self, t) for c, t in zip(self.target_criterias,
                                           self.targets_chosen)]):
            print("All targets invalid. %r fizzles." % self)
            fizzles = True

        if self.countered:
            print("%r was countered" % self)
            fizzles = True

        if not self.apply_condition():
            print("Intervening-if for %r not satisfied" % self)
            fizzles = True


        if fizzles:
            if self.original_card:
                self.original_card.owner.graveyard.add(self.original_card)
            return

        self.apply_func()

