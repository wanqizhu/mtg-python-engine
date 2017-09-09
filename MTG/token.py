import re
from collections import defaultdict

from MTG import permanent
from MTG import gameobject
from MTG import cardtype
from MTG import abilities
from MTG import helper_funcs


class Token(permanent.Permanent):
    # todo: add abilities
    def __init__(self, characteristics, controller, activated_abilities=[]):
        super(Token, self).__init__(characteristics, controller)
        self.is_token = True

        self.activated_abilities = [abilities.ActivatedAbility(self, *params) for params in activated_abilities]


creature_token_pattern = re.compile('\d/\d '
                                    '((colorless)|(white)|(blue)|(black)|(red)|(green)) '
                                    '[A-Za-z ]+')


# token_ability_dict = defaultdict(lambda: [])
# token_ability_dict['Spirit'] = [abilities.StaticAbilities.Flying]
# token_ability_dict['Thopter'] = [abilities.StaticAbilities.Flying]



def create_token(attributes, controller, num=1, keyword_abilities=[], activated_abilities=[]):
    if isinstance(attributes, str):
        if creature_token_pattern.match(attributes):
            pt, color, *c_type = attributes.split(' ')
            p, t = map(int, pt.split('/'))
            types = [cardtype.CardType.CREATURE]
            if 'artifact' in c_type:
                types.append(cardtype.CardType.ARTIFACT)
                c_type.remove('artifact')
        else:
            p, t = None, None
            color, *c_type = attributes.split(' ')
            types = [cardtype.CardType[c_type.pop().upper()]]

        color = {'colorless': 'C',
                 'white': 'W',
                 'blue': 'U',
                 'black': 'B',
                 'red': 'R',
                 'green': 'G'}[color]

        name = ' '.join(c_type)
        
        print("making token... %s" % attributes)

        if isinstance(keyword_abilities, str):
            keyword_abilities = [keyword_abilities]
            print("with %s" % ' '.join(keyword_abilities))

        for ablty in activated_abilities:
            ablty[0] = helper_funcs.parse_ability_costs(ablty[0])


        for i in range(num):
            characteristics = gameobject.Characteristics(name='Token: %s' % name,
                                                         types=types,
                                                         power=p,
                                                         toughness=t,
                                                         subtype=c_type,
                                                         color=[color],
                                                         abilities=[abilities.StaticAbilities[a] for a in keyword_abilities])

            Token(characteristics, controller, activated_abilities)
