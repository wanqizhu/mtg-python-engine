import traceback

from MTG import gameobject



class Attributes():
    def __init__(self):
        # attributes goes here
        self.num_creatures_can_block = 1


class Card(gameobject.GameObject):
    target_criterias = None
    target_prompts = None

    trigger_listeners = {}

    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []

    def __init__(self, characteristics=gameobject.Characteristics(),
                 controller=None, owner=None, zone=None, previousState=None):

        super(Card, self).__init__(characteristics,
                                   controller, owner, zone, previousState)

        self.attributes = Attributes()

    def targets(self):
        if not self.target_criterias:
            return True

        print("choosing targets...\n")
        targets_chosen = []
        for criteria, prompt in zip(self.target_criterias, self.target_prompts):

            answer = self.controller.make_choice(prompt)
            card = get_card_from_user_input(self.controller, answer)
            print(card)

            try:
                if not criteria(card):
                    return False
            except:
                traceback.print_exc()
                return False

            targets_chosen.append(card)

        self.targets_chosen = targets_chosen
        return targets_chosen

    def ID(self):
        pass

    def play_func(self):  # defaults to permanent
        permanent.make_permanent(self)


def get_card_from_user_input(player, string):
    """Convert a user input (naming a card in a zone) to an actual game object

    b 2 --> 2nd(3rd) card on battlefield
    b Grizzly Bear --> Grizzly Bear on battlefield

    s 0 --> 1st card on stack (from top)

    h -1 --> last card in hand

    og 3 --> 3rd(4th) card on opponent's graveyard
    """

    if string[0] == 'o':  # opponent
        string = string[1:]
        player = player.game.opponent(player)

    if string[0] == 'p':
        return player

    if string[0] == 'b':
        zone = player.battlefield
    elif string[0] == 's':
        zone = player.game.stack
    elif string[0] == 'h':
        zone = player.hand
    elif string[0] == 'g':
        zone = player.graveyard

    try:
        i = int(string[2:])
        if i < len(zone):
            return zone[i]
        else:
            return None
    except:
        return zone.get_card_by_name(string[2:])

# need it here to avoid circular imports
from MTG import permanent
