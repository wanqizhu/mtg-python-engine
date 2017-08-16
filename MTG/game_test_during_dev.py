import mock
import sys
import os

sys.path.append('/Users/wanqi/Desktop/Python-MTG')
os.chdir('/Users/wanqi/Desktop/Python-MTG')

from MTG.game import *

with mock.patch('builtins.input', side_effect=[
        '__self.discard(7)', '__self.draw_card("Devouring Deep")',  # p0
        '__self.draw_card("Sewn-Eye Drake")', '',
        '__self.discard(7)', '__self.draw_card("Devouring Deep")',  # p1
        '__self.draw_card("Sewn-Eye Drake")','',
        '', '',
        '__self.mana.add(mana.Mana.BLUE, 6)',  # player 0, main step
        '__self.mana.add(mana.Mana.BLACK, 1)',
        'p Devouring Deep', '', '', '',  # pay mana, letting it resolve
        'p Sewn-Eye Drake', '', '', '', '',  # pay mana (choose hybrid & unrestricted), letting it resolve
        's precombat_main',  # go to next turn
        's precombat_main',
        '0',  # attacking
    
        '__self.mana.add(mana.Mana.BLUE, 6)',  # player 1's turn, main step
        '__self.mana.add(mana.Mana.BLACK, 1)',
        'p Devouring Deep', '', '', '',
        'p Sewn-Eye Drake', '', '', '', '',
        's precombat_main',
        's precombat_main',
        '0', '0', '', # attacking, tries to block (but should fail due to flying), no blocks

        's precombat_main',  # go to next turn
        's precombat_main',
        '',  # no attacks
        
        's precombat_main',  # go to next turn
        's precombat_main',
        '',  # no attacks
        ]):
    decks = [cards.read_deck('cards/decks/deck1.txt'),
        cards.read_deck('cards/decks/deck1.txt')]
    GAME = Game(decks)
    GAME.set_up_game()
    GAME.handle_turn()
    GAME.handle_turn()
    GAME.handle_turn()
    GAME.handle_turn()


GAME.handle_turn()