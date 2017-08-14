import mock, unittest

from MTG import mana
from MTG import game
from MTG import cards


class TestPlayer(unittest.TestCase):
    def setUp(self):
        decks = [cards.read_deck('cards/decks/deck1.txt'), cards.read_deck('cards/decks/deck1.txt')]
        self.GAME = game.Game(decks)
        self.GAME.current_player = next(self.GAME.players)
        self.GAME.set_up_game()
        self.player = self.GAME.players_list[0]
        self.opponent = self.GAME.players_list[1]


    def test_turn_do_nothing(self):
        with mock.patch('builtins.input', return_value=''):
            self.assertTrue(self.GAME.handle_turn())

    def test_play_land(self):
    	"""

    	Fetches an island from deck, plays it, adds blue mana.
    	Validates that mana is correctly added & landPlayed count went up
    	"""

        with mock.patch('builtins.input', side_effect=['__self.draw_card("Island")',
        	'', '', '', '',
        	'p Island',
        	'a0',
        	'__self.name = self.mana.pool[mana.Mana.BLUE] == 1',  # use name as a placeholder
        	'sdraw',
        	'sdraw'
        	]):

            self.assertTrue(self.GAME.handle_turn())
            self.assertTrue(self.player.name)
            self.assertEqual(self.player.landPlayed, 1)
        

if __name__ == '__main__':
    unittest.main()