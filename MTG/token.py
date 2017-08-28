import re
from collections import defaultdict

from MTG import permanent
from MTG import gameobject
from MTG import cardtype
from MTG import abilities


class Token(permanent.Permanent):
    # todo: add abilities
    def __init__(self, characteristics, controller):
        super(Token, self).__init__(characteristics, controller)
        self.is_token = True


creature_token_pattern = re.compile('\d/\d '
                                    '((colorless)|(white)|(blue)|(black)|(red)|(green)) '
                                    '[A-Za-z ]+')


token_ability_dict = defaultdict(lambda: [])
token_ability_dict['Spirit'] = [abilities.StaticAbilities.Flying]
token_ability_dict['Thopter'] = [abilities.StaticAbilities.Flying]



def create_token(attributes, controller, num=1):
    if type(attributes) is str:
        if creature_token_pattern.match(attributes):
            pt, color, *c_type = attributes.split(' ')
            p, t = map(int, pt.split('/'))
            color = {'colorless': 'C',
                     'white': 'W',
                     'blue': 'U',
                     'black': 'B',
                     'red': 'R',
                     'green': 'G'}[color]

            name = ' '.join(c_type)
            print("making token... %d %d %s %s" % (p, t, color, name))
            

            for i in range(num):
                characteristics = gameobject.Characteristics(name='Token: %s' % name,
                                                             types=[
                                                                 cardtype.CardType.CREATURE],
                                                             power=p,
                                                             toughness=t,
                                                             subtype=c_type,
                                                             color=[color],
                                                             abilities=token_ability_dict[name])

                Token(characteristics, controller)
