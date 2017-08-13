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


    def test_turn_do_nothing(self):
        with mock.patch('builtins.input', return_value=''):
            self.assertTrue(self.GAME.handle_turn())
        

if __name__ == '__main__':
    unittest.main()