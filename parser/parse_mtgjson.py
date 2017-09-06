import sys
import json
import pickle

from MTG import abilities


# SET = 'M15'
SET = 'AllSets'
NAME = 'cube'

# only_parse_list = None
only_parse_list = set(open('parser/cube_card_list.txt').read().strip().split('\n'))


def star_or_int(c):
    if c == '*':
        return c
    else:
        return int(c)


def run():
    with open('parser/data/%s.json' % SET) as f:
        cards = json.load(f)
        card_list = []
        for _set in cards.values():
            card_list.extend(_set['cards'])


    fout = open("data/%s_cards.py" % NAME, "w")
    fout.write("from MTG import card\n"
               "from MTG import gameobject\n"
               "from MTG import cardtype\n"
               "from MTG import abilities\n"
               "from MTG import mana\n\n")


    name_to_id = {}

    for card in card_list:
        if only_parse_list and card["name"] not in only_parse_list:
            continue

        if card["name"] in name_to_id:  # already parsed card (ignore reprints)
            continue

        try:
            supertype = []
            subtype = []
            _abilities = []

            if "multiverseid" in card:
                ID = 'c' + str(card["multiverseid"])
            else:
                continue
                # ID = 'c' + str(card["id"])
            name = card["name"]
            characteristics = {'name': name}
            characteristics['text'] = card["text"] if "text" in card else ''
            characteristics['color'] = card["colorIdentity"] if "colorIdentity" in card else ''
            characteristics['mana_cost'] = (card["manaCost"].replace('{', '').replace('}', '')
                                            if "manaCost" in card else '')
            # types
            if "supertypes" in card:
                supertype = ('['
                             + ', '.join(['cardtype.SuperType.' + i.upper()
                                          for i in card["supertypes"]])
                             + ']')

            types = '[' + ', '.join(['cardtype.CardType.' + i.upper()
                                     for i in card["types"]]) + ']'

            if 'Creature' in card["types"]:
                characteristics['power'], characteristics['toughness'] = star_or_int(
                    card["power"]), star_or_int(card["toughness"])

            if "subtypes" in card:
                characteristics["subtype"] = card["subtypes"]

            # static abilities

            texts = characteristics['text'].replace(' ', '_')
            for ability in abilities.StaticAbilities._member_names_:
                if ability in texts or ',_' + ability.lower() in texts.lower():
                    _abilities.append(ability)

            if len(_abilities):
                _abilities = '[abilities.StaticAbilities.' + \
                    ', abilities.StaticAbilities.'.join(_abilities) + ']'

        except:
            print("\n\n")
            print(card)
            print(sys.exc_info())
            pass

        fout.write(
            """class {}(card.Card):
    "{}"
    def __init__(self):
        super({}, self).__init__(gameobject.Characteristics(**{}, supertype={}, types={}, abilities={}))

""".format(ID, name, ID, characteristics, supertype, types, _abilities))

        name_to_id[name] = ID


#     fout.write(
# """id_to_name_dict = {}

# name_to_id_dict = {}


# """.format(id_to_name, name_to_id))



    with open("data/%s_name_to_id_dict.pkl" % NAME, "wb") as f:
        pickle.dump(name_to_id, f)

    fout.close()

    # try:
    #     card.find('text').text.replace(card.find('name').text, '<self>'))


if __name__ == '__main__':
    run()
