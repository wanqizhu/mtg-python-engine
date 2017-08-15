import mock
import sys
import os

sys.path.append('/Users/wanqi/Desktop/Python-MTG')
os.chdir('/Users/wanqi/Desktop/Python-MTG')

from MTG.game import *

with mock.patch('builtins.input', side_effect=[
        '__self.discard(7)', '__self.draw_card("Devouring Deep")','',  # p0
        '__self.discard(7)', '__self.draw_card("Devouring Deep")','',  # p1
        '', '',
        '__self.mana.add(mana.Mana.BLUE, 3)',  # player 0
        'p Devouring Deep', '', '', '',
        's precombat_main',  # go to next turn
        's precombat_main',
        '__self.mana.add(mana.Mana.BLUE, 3)',  # player 1's turn
        'p Devouring Deep', '', '', '',
        's precombat_main',  # go to next turn
        's precombat_main',
        '__self.battlefield.elements[0].characteristics.power = 2',
        ]):
    decks = [cards.read_deck('cards/decks/deck1.txt'),
        cards.read_deck('cards/decks/deck1.txt')]
    GAME = Game(decks)
    GAME.run_game()