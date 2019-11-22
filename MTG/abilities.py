from enum import Enum
from MTG import mana
from MTG import helper_funcs
from MTG import play

class StaticAbilities(Enum):
    Deathtouch = 0
    Defender = 1
    Double_Strike = 2
    First_Strike = 3
    Flash = 4
    Flying = 5
    Haste = 6
    Hexproof = 7
    Indestructible = 8
    Intimidate = 9
    Menace = 10

    Lifelink = 12
    Reach = 13
    Shroud = 14
    Trample = 15
    Vigilance = 16
    Plainswalk = 17
    Islandwalk = 18
    Swampwalk = 19
    Mountainwalk = 20
    Forestwalk = 21

    # protection


    Convoke = 30


class Ability():
    pass


class ActivatedAbility(Ability):
    def __init__(self, card, cost, effect, target_criterias=None, prompts=None, is_mana_ability=False):
        """ card: permanent that the ability is attached to """
        self.card = card
        self.controller = card.controller
        self.game = self.controller.game
        self.cost = cost
        self.effect = effect
        self.target_criterias = target_criterias
        if target_criterias and not prompts:
            prompts = ["Choose a target\n"] * len(target_criterias)
        self.target_prompts = prompts
        self.targets_chosen = []
        self.is_mana_ability = is_mana_ability


    def resolve(self):
        return eval(self.effect)

    def can_activate(self):
        """ choose targets, pays ability's costs, attemp to activate """
        cost = self.cost
        _card = self.card

        targets_chosen = helper_funcs.choose_targets(self)
        if isinstance(targets_chosen, list):
            self.targets_chosen = targets_chosen

        return targets_chosen and (lambda self: eval(cost))(_card)


class TriggeredAbility(Ability):
    def __init__(self, card, effect, requirements, target_criterias=None,
                 prompts=None, intervening_if=None):
        self.card = card
        self.controller = card.controller
        self.game = self.controller.game
        self.effect = effect
        self.requirements = requirements
        
        if not intervening_if:
            self.intervening_if = lambda self: True
        else:
            self.intervening_if = intervening_if

        self.target_criterias = target_criterias
        if target_criterias and not prompts:
            prompts = ["Choose a target\n"] * len(target_criterias)
        self.target_prompts = prompts
        self.targets_chosen = []
        self.trigger_amount = 1
        self.trigger_source = None

    def __str__(self):
        return str(self.effect) + " from " + str(self.card)

    def resolve(self):
        return eval(self.effect)

    def condition_satisfied(self):
        return self.requirements(self) and self.intervening_if(self)

    def choose_targets(self):
        targets_chosen = helper_funcs.choose_targets(self)
        if isinstance(targets_chosen, list):
            self.targets_chosen = targets_chosen

        return targets_chosen


    def put_on_stack(self):
        if self.choose_targets():
            return play.Play(lambda: self.resolve(),
                               apply_condition=lambda: self.intervening_if(self),
                               name=self.card.name + ' triggered ability ' + str(self),
                               source=self)
        return None

