class Play(object):
    """
    Represents anything a player can choose to do when they have priority.
    """
    is_special_action = False
    is_mana_ability = False

    ## TODO: implement targets: target selection, validation, conditional targeting, etc.
    def __init__(self, apply_func):
        self.apply = apply_func
        return 

