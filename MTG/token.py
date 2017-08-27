import re

from MTG import permanent
from MTG import gameobject
from MTG import cardtype


class Token(permanent.Permanent):
    # todo: add abilities
    def __init__(self, characteristics, controller):
        super(Token, self).__init__(characteristics, controller)
        self.is_token = True


creature_token_pattern = re.compile('\d/\d '
                                    '((colorless)|(white)|(blue)|(black)|(red)|(green)) '
                                    '[A-Za-z ]+')


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

            print("making token... %d %d %s %s" % (p, t, color, c_type))

            for i in range(num):
                characteristics = gameobject.Characteristics(name='Token: ' + ' '.join(c_type),
                                                             types=[
                                                                 cardtype.CardType.CREATURE],
                                                             power=p,
                                                             toughness=t,
                                                             subtype=c_type,
                                                             color=[color])

                Token(characteristics, controller)
