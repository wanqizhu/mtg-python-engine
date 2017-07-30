__author__ = 'Michael'

from bs4 import BeautifulSoup
# from lexer import lexer
from MTG.card import Card
from MTG.cardType import *
import pickle

cards = []





def run():
    with open('parser/cards.xml') as f:
        soup = BeautifulSoup(f, 'xml')

    card_list = soup.cockatrice_carddatabase.cards.find_all('card')
    cnt = 0
    fout = open("card_list.txt", "w")

    for card in card_list[:100]:
        try:
            characteristics = {'name': card.find('name').text}
            characteristics['text'] = card.find('text').text
            characteristics['color'] = [c.text for c in card.find_all('color')]
            characteristics['mana_cost'] = card.find('manacost').text
            _type = card.find('type').text.split(' - ')
            if len(_type) > 1:
                characteristics['subtype'] = _type[1].split(' ')
            _type = _type[0].split(' ')
            if len(_type) > 1:
                characteristics['supertype'] = SuperType[_type[0].upper()]
            characteristics['card_type'] = CardType[_type[-1].upper()]
        except:
            pass

        fout.write("id: {}\n".format(cnt))
        for i, j in characteristics.items():
            fout.write("{}: {},\n".format(i, j))
        fout.write("\n\n")
        cnt += 1
        # cards.append(Card(characteristics))

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