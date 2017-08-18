class Play(object):
    """
    Represents anything a player can choose to do when they have priority.
    """
    

    ## TODO: implement targets: target selection, validation, conditional targeting, etc.
    def __init__(self, apply_func, card=None):
        self.is_special_action = False
        self.is_mana_ability = False
        self.apply = apply_func
        self.original_card = card
        return 

