import re, sys, traceback

from bs4 import BeautifulSoup
# from lexer import lexer
import pickle

from MTG import cardtype
from MTG import abilities





def run():
    # switch to sm_cards and replace-all 'all_set', 'sm_set' to just parse a sample of cards
    with open('parser/data/cards.xml') as f:
        soup = BeautifulSoup(f, 'xml')

    card_list = soup.cockatrice_carddatabase.cards.find_all('card')
    cnt = 0
    fout = open("data/all_set_cards.py", "w")
    fout.write("from MTG import card\n"
        "from MTG import gameobject\n"
        "from MTG import cardtype\n"
        "from MTG import abilities\n"
        "from MTG import mana\n\n")

    id_to_name = {}
    name_to_id = {}

    for card in card_list:
        supertype = []
        types = []
        try:
            ID = 'c' + re.search('(?<=multiverseid=)[0-9]+', card.set['picURL']).group(0)
            name = card.find('name').text
            characteristics = {'name': name}
            characteristics['text'] = card.find('text').text
            characteristics['color'] = [c.text for c in card.find_all('color')]
            characteristics['mana_cost'] = card.find('manacost').text

            # types
            _type = card.find('type').text.split(' - ')
            if len(_type) > 1:
                characteristics['subtype'] = _type[1].split(' ')
            _type = _type[0].split(' ')

            if len(_type) > 1 and _type[0].upper() in cardtype.SuperType._member_names_:
                supertype = '[cardtype.SuperType[%r]]' % _type[0].upper()
                _type.pop(0)

            types = '[' + ', '.join(['cardtype.CardType[%r]' % i.upper() for i in _type]) + ']'

            if 'Creature' in _type:
                try:
                    characteristics['power'], characteristics['toughness'] = map(int, card.find('pt').text.split('/'))
                except ValueError:
                    pass
            # static abilities
            _abilities = []

            texts = characteristics['text'].replace(' ', '_')
            for ability in abilities.StaticAbilities._member_names_:
                if ability in texts or ',_' + ability.lower() in texts.lower():
                    _abilities.append(ability)

            if len(_abilities):
                _abilities = '[abilities.StaticAbilities.' + ', abilities.StaticAbilities.'.join(_abilities) + ']'

        except:

            traceback.print_exc()
            pass



        fout.write(
"""class {}(card.Card):
    "{}"
    def __init__(self):
        super({}, self).__init__(gameobject.Characteristics(**{}, supertype={}, types={}, abilities={}))

""".format(ID, name, ID, characteristics, supertype, types, _abilities))

        id_to_name[ID] = name
        name_to_id[name] = ID
        


#     fout.write(
# """id_to_name_dict = {}

# name_to_id_dict = {}


# """.format(id_to_name, name_to_id))


    with open("data/all_set_id_to_name_dict.pkl", "wb") as f:
        pickle.dump(id_to_name, f)

    with open("data/all_set_name_to_id_dict.pkl", "wb") as f:
        pickle.dump(name_to_id, f)

    fout.close()


        # try:
        #     card.find('text').text.replace(card.find('name').text, '<self>'))


if __name__ == '__main__':
    run()