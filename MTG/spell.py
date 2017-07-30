from MTG.game_object import GameObject


class Spell(GameObject):
    def __init__(self, characteristics, controller, status=None):
        GameObject.__init__(self, characteristics)
        self.controller = controller
        
   

def make_spell(card, controller):
    return Spell(card.characteristics, controller)