import mock, unittest

from MTG import mana
from MTG import game
from MTG import cards
from MTG import player


class TestPlayer(unittest.TestCase):
    def setUp(self):
        decks = [cards.read_deck('cards/decks/deck1.txt'), cards.read_deck('cards/decks/deck1.txt')]
        self.GAME = game.Game(decks, test=True)
        self.GAME.current_player = next(self.GAME.players)
        self.GAME.set_up_game()
        self.player = self.GAME.players_list[0]
        self.player.tmp = False
        self.opponent = self.GAME.players_list[1]


    def test_turn_do_nothing(self):
        with mock.patch('builtins.input', return_value=''):
            self.assertTrue(self.GAME.handle_turn())

    def test_skip_priority(self):
        with mock.patch('builtins.input', return_value='s upkeep'):
            self.assertTrue(self.GAME.handle_turn())


    def test_mana_emptying(self):
        """Verify that both players' mana pool empties at end of phase"""
        with mock.patch('builtins.input', side_effect=['__self.mana.add(mana.Mana.WHITE, 2)',
                '__self.mana.add(mana.Mana.RED, 3)', '',  # player 0
                '__self.mana.add(mana.Mana.BLUE, 2)', '',  # player 1
                '__self.tmp = self.mana.pool[mana.Mana.WHITE] '
                            '+ self.mana.pool[mana.Mana.RED] == 0', '', # p 0
                '__self.tmp = self.mana.pool[mana.Mana.BLUE] == 0', '', # p 1 
                's draw',
                's draw']):

            self.assertTrue(self.GAME.handle_turn())
            self.assertTrue(self.player.tmp)
            self.assertTrue(self.opponent.tmp)


    def test_drawing_cards(self):
        with mock.patch('builtins.input', side_effect=['', '', '', '',
                '__self.tmp = self.hand.size() == 7',
                '__self.draw_card("Swamp")',
                '__self.draw(5)',
                '__self.tmp = self.tmp and self.hand.size() == 13',
                's draw',
                's draw',
                '']):

            self.assertTrue(self.GAME.handle_turn())
            self.assertTrue(self.player.tmp)
            self.assertEqual(self.player.hand.size(), 7)  # discard down to 7 eot


    def test_discard(self):
        with mock.patch('builtins.input', side_effect=['', '', '', '',
                '__self.draw(4)',
                '__self.discard(5)', '',
                's draw',
                's draw',
                '']):

            self.assertTrue(self.GAME.handle_turn())
            
            self.assertEqual(self.player.hand.size(), 6)  # discard down to 7 eot
            self.assertEqual(self.player.graveyard.size(), 5)



    def test_play_land(self):
        """Fetch an island from deck, play it, add blue mana.

        Validate that mana is correctly added & landPlayed count went up
        """

        with mock.patch('builtins.input', side_effect=['__self.draw_card("Island")',
                '', '', '', '',
                'p Island',
                'a 0',
                '__self.tmp = self.mana.pool[mana.Mana.BLUE] == 1',  # use player.tmp as a placeholder
                's draw',
                's draw',
                '']):

            self.assertTrue(self.GAME.handle_turn())
            self.assertTrue(self.player.tmp)
            self.assertEqual(self.player.landPlayed, 1)



    def test_play_creature_basic(self):
        """Play a creature while having sufficient mana (automatic payment)

        Devouring Deep costs 2U
        """
        with mock.patch('builtins.input', side_effect=['__self.draw_card("Devouring Deep")',
                '', '', '', '',
                '__self.mana.add(mana.Mana.BLUE, 3)',
                'p Devouring Deep', '',  # extra '' is used for automatic mana payment
                's draw',
                's draw',
                '']):

            self.assertTrue(self.GAME.handle_turn())
            self.assertTrue(self.player.battlefield.get_card_by_name("Devouring Deep"))


    def test_play_creature_custom_mana_payment(self):
        """Play a creature while having sufficient mana (custom payment)"""
        with mock.patch('builtins.input', side_effect=['__self.draw_card("Devouring Deep")',
                '', '', '', '',
                '__self.mana.add(mana.Mana.BLUE, 1)',
                '__self.mana.add(mana.Mana.RED, 1)',
                '__self.mana.add(mana.Mana.GREEN, 1)',
                'p Devouring Deep', 'RG',
                's draw',
                's draw',
                '']):

            self.assertTrue(self.GAME.handle_turn())
            self.assertTrue(self.player.battlefield.get_card_by_name("Devouring Deep"))




    def test_play_creature_over_three_turns(self):
        """ Fetch 3 lands, play them over 3 turns, tap for mana, play Devouring Deep

        Validate that creature uses the stack & is added to battlefield correctly
        Validate multiple turns pose no problem
        """

        with mock.patch('builtins.input', side_effect=['__self.discard(7)',
                '__self.draw_card("Island")',
                '__self.draw_card("Island")',
                '__self.draw_card("Plains")',
                '__self.draw_card("Devouring Deep")',
                '', '', '', '',
                'p Island',
                's precombat_main',
                's precombat_main',
                'p Plains',
                's precombat_main',
                's precombat_main',
                'p Island',
                'a 0', 'a 1', 'a 2',
                'p Devouring Deep', '',
                '__self.tmp = self.game.stack.size() == 1',
                '', '',
                's precombat_main',
                's precombat_main']):

            self.GAME.handle_turn()
            self.GAME.current_player = self.player
            self.GAME.handle_turn()
            self.GAME.current_player = self.player
            self.GAME.handle_turn()

            self.assertTrue(self.player.tmp)
            self.assertEqual(self.player.battlefield.size(), 4)
            self.assertTrue(self.player.battlefield.get_card_by_name("Devouring Deep"))
        


    def test_summoning_sickness(self):
        with mock.patch('builtins.input', side_effect=['__self.draw_card("Devouring Deep")',
                '', '', '', '',
                '__self.mana.add(mana.Mana.BLUE, 3)',
                'p Devouring Deep', '',  # auto payment
                '', '',  # letting it resolve
                '__self.tmp = not self.battlefield.get_card_by_name("Devouring Deep").can_attack()',
                's draw',
                's draw',
                '']):

            self.GAME.handle_turn()
            
            self.assertTrue(self.player.tmp)


    def test_attacking(self):
        with mock.patch('builtins.input', side_effect=['__self.discard(7)',
                '__self.draw_card("Devouring Deep")',
                '', '', '', '',
                '__self.mana.add(mana.Mana.BLUE, 3)',
                'p Devouring Deep', '',
                's draw',  # go to next turn
                's draw',
                '', '', '', '', '', '',  # skipping to declare_attackers
                '0',  # attacking w/ Devouring Deep
                      # check that it's tapped and attacking
                '__self.tmp = (self.battlefield.get_card_by_name("Devouring Deep")'
                            '.status.is_attacking == self.game.players_list[1]'
                            ' and self.battlefield.get_card_by_name("Devouring Deep")'
                            '.status.tapped)',
                's precombat_main',
                's precombat_main',
                '']):

            self.GAME.handle_turn()
            self.GAME.current_player = self.player
            self.GAME.handle_turn()
            

            self.assertTrue(self.player.tmp)
            self.assertTrue(self.player.battlefield.get_card_by_name("Devouring Deep").status.tapped)
            self.assertFalse(self.player.battlefield.get_card_by_name("Devouring Deep").in_combat())
            self.assertEqual(self.opponent.life, 19, "incorrect combat damage")


if __name__ == '__main__':
    unittest.main()