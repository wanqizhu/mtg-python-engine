class Spell(object):
    def __init__(self, card, controller, actions, targets, divisions, cost, payment):
        self.card = card
        self.controller = controller
        self.actions = actions
        self.targets = targets
        self.divisions = divisions
        self.cost = cost
        self.payment = payment