from bs4 import BeautifulSoup
# from lexer import lexer
from MTG.card import Card
from MTG.cardType import *
# import pickle
import re

cards = []





def run():
    with open('parser/cards_sm.xml') as f:
        soup = BeautifulSoup(f, 'xml')

    card_list = soup.cockatrice_carddatabase.cards.find_all('card')
    cnt = 0
    fout = open("MTG/parsed_cards.py", "w")
    fout.write("from MTG.card import *\nfrom MTG.gameObject import *\n\n")

    id_to_name = {}
    name_to_id = {}

    for card in card_list[:100]:
        supertype = []
        types = []
        try:
            ID = 'c' + re.search('(?<=multiverseid=)[0-9]+', card.set['picURL']).group(0)
            name = card.find('name').text
            characteristics = {'name': name}
            characteristics['text'] = card.find('text').text
            characteristics['color'] = [c.text for c in card.find_all('color')]
            characteristics['mana_cost'] = card.find('manacost').text
            _type = card.find('type').text.split(' - ')
            if len(_type) > 1:
                characteristics['subtype'] = _type[1].split(' ')
            _type = _type[0].split(' ')

            if len(_type) > 1 and _type[0].upper() in SuperType._member_names_:
                supertype = '[SuperType.'+_type[0].upper() + ']'
                _type.pop(0)

            types = '[' + ', '.join(['CardType.'+i.upper() for i in _type]) + ']'
        except:
            pass

        fout.write(
"""
class {}(Card):
    "{}"
    def __init__(self):
        super({}, self).__init__(Characteristics(**{}, supertype={}, types={}))

""".format(ID, name, ID, characteristics, supertype, types))

        id_to_name[ID] = name
        name_to_id[name] = ID
        
        # cards.append(Card(characteristics))


    fout.write(
"""
id_to_name_dict = {}

name_to_id_dict = {}

def id_to_name(ID):
    return id_to_name_dict.get(ID, None)

def name_to_id(name):
    return name_to_id_dict.get(name, None)

def card_from_name(name):
    if name_to_id(name) is not None:
        return eval(name_to_id(name)+'()')
    else:
        return None
""".format(id_to_name, name_to_id))

    fout.close()

    # return cards


        # try:
        #     card.find('text').text.replace(card.find('name').text, '<self>'))
        #     print("Card: {}".format(card.find('name').text))
        #     for tok in lexer:
        #         print(tok)
        #         pass
        #     print()
        # except ValueError as e:
        #     print(e)
        #     continue

if __name__ == '__main__':
    run()