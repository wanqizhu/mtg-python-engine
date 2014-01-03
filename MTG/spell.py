class Spell(Action):
    def __init__(self, card, controller, actions, targets, divisions, cost, payment):
        self.card = card
        self.controller = controller
        self.effects = effects
        self.targets = targets
        self.divisions = divisions
        self.cost = cost
        self.payment = payment
        
    def resolve(self):
        for effect in effects:
            effect.resolve()
    
    def is_instant_speed(self):
        return self.card.is_instant_speed()