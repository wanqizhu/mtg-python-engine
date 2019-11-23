import mock
import sys
import os

from MTG.game import *
from MTG import cards

cards.setup_cards()

with mock.patch('builtins.input', side_effect=[
        's main',
        's main',
        '__self.discard(7)', '',
        '__self.discard(7)', '',
        '__self.add_card_to_hand("Path to Exile")',
        '__self.battlefield.add("Sungrace Pegasus")',
        '', '',
        's upkeep', 's upkeep',
        's upkeep', 's upkeep',
        '',
        ''
        ]):
    decks = [cards.read_deck('data/decks/deck1.txt'),
        cards.read_deck('data/decks/deck1.txt')]
    GAME = Game(decks)
    GAME.setup_game()
    for p in GAME.players_list:
        p.autoOrderTriggers = False
    GAME.handle_turn()
    GAME.handle_turn()


GAME.handle_turn()