import mock
import sys
import os

sys.path.append('/Users/wanqi/Desktop/Python-MTG')
os.chdir('/Users/wanqi/Desktop/Python-MTG')

from MTG.game import *
from MTG import cards

cards.set_up_cards()

with mock.patch('builtins.input', side_effect=[
        's main',
        's main',
        '__self.discard(7)', '',
        '__self.discard(7)', '',
        '__self.draw_card("Path to Exile")',
        '__self.battlefield.add("Sungrace Pegasus")',
        '', '',
        's upkeep', 's upkeep',
        's upkeep', 's upkeep'
        ]):
    decks = [cards.read_deck('data/decks/deck1.txt'),
        cards.read_deck('data/decks/deck1.txt')]
    GAME = Game(decks)
    GAME.set_up_game()
    GAME.handle_turn()
    GAME.handle_turn()


GAME.handle_turn()