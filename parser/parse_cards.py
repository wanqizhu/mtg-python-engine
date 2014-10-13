__author__ = 'Michael'

from bs4 import BeautifulSoup
from lexer import lexer


def run():
    with open('cards.xml') as f:
        soup = BeautifulSoup(f, 'xml');
    card_list = soup.cockatrice_carddatabase.cards.find_all('card')
    for card in card_list:
        try:
            lexer.input(card.find('text').text.replace(card.find('name').text, '<self>'))
            print("Card: {}".format(card.find('name').text))
            for tok in lexer:
                pass
            print()
        except ValueError:
            raise

if __name__ == '__main__':
    run()