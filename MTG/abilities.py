from enum import Enum
from MTG import mana
from MTG import play
from MTG import gameobject


# TODO: integrate with Spell.py?
# TODO: unify __init__ from diff kinds of ability & class hierarchies
class Ability(gameobject.GameObject):
    def __init__(self, card, effect, target_criterias=None,
                 prompts=None):
        super(Ability, self).__init__()
        self.card = card
        self.controller = card.controller
        self.game = self.controller.game
        self.effect = effect

        self.target_criterias = target_criterias
        if target_criterias and not prompts:
            prompts = ["Choose a target\n"] * len(target_criterias)
        self.target_prompts = prompts



    def __str__(self):
        return str(self.effect) + " from " + str(self.card)
    
    def __repr__(self):
        return str(self)

    def resolve(self):
        return eval(self.effect)
        



class ActivatedAbility(Ability):
    def __init__(self, card, cost, effect, target_criterias=None, prompts=None, is_mana_ability=False):
        """ card: permanent that the ability is attached to """
        super(ActivatedAbility, self).__init__(card, effect, target_criterias, prompts)
        self.cost = cost
        self.is_mana_ability = is_mana_ability


    def can_activate(self):
        """ choose targets, pays ability's costs, attempt to activate """
        cost = self.cost
        _card = self.card

        targets_chosen = self.choose_targets()

        return targets_chosen and (lambda self: eval(cost))(_card)


class TriggeredAbility(Ability):
    def __init__(self, card, effect, requirements, target_criterias=None,
                 prompts=None, intervening_if=None):
        super(TriggeredAbility, self).__init__(card, effect, target_criterias, prompts)
        
        self.requirements = requirements
        
        if not intervening_if:
            self.intervening_if = lambda self: True
        else:
            self.intervening_if = intervening_if

        self.trigger_amount = 1
        self.trigger_source = None

    def condition_satisfied(self):
        return self.requirements(self) and self.intervening_if(self)

    def put_on_stack(self):
        if self.choose_targets():
            return play.Play(lambda: self.resolve(),
                               apply_condition=lambda: self.intervening_if(self),
                               name=str(self),
                               source=self)
        return None

