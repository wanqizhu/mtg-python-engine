import mock, unittest
from copy import deepcopy

from MTG import mana
from MTG import game
from MTG import cards
from MTG import player
from MTG import permanent
from MTG import gameobject
from MTG.exceptions import *



class TestPlayer(unittest.TestCase):
    def setUp(self):
        decks = [cards.read_deck('cards/decks/deck1.txt'), cards.read_deck('cards/decks/deck1.txt')]
        self.GAME = game.Game(decks, test=True)
        self.GAME.set_up_game()
        self.player = self.GAME.players_list[0]
        self.player.tmp = False
        self.opponent = self.GAME.players_list[1]
        self.opponent.tmp = False


    def test_turn_do_nothing(self):
        with mock.patch('builtins.input', return_value=''):
            self.assertTrue(self.GAME.handle_turn())

    def test_game_over(self):
        """ Make sure that going to 0 life terminates the game"""
        with mock.patch('builtins.input', side_effect=['__self.life = 0', '']):
            with self.assertRaises(GameOverException):
                self.GAME.handle_turn()
                self.assertEqual(self.player.life, 0)
                self.assertTrue(self.player.lost)
                self.assertTrue(self.player not in self.GAME.players_list)


    def test_rewind_to_previous_state(self):
        """Make sure deepcopy resets everything"""
        previous_state = deepcopy(self.GAME)

        self.player.take_damage(None, 13)
        self.player.discard(3)
        self.player.mana.add(mana.Mana.RED, 13)
        self.player.battlefield.add("Island")
        self.GAME.stack.add("Sewn-Eye Drake")
        self.assertEqual(self.player.life, 7)
        self.assertEqual(self.player.hand.size(), 4)
        self.assertFalse(self.player.mana.is_empty())
        self.assertTrue(self.GAME.stack)
        self.assertTrue(self.player.battlefield)

        self.GAME = previous_state
        self.player = self.GAME.players_list[0]
        
        self.assertEqual(self.player.life, 20)
        self.assertEqual(self.player.hand.size(), 7)
        self.assertTrue(self.player.mana.is_empty())
        self.assertFalse(self.GAME.stack)
        self.assertFalse(self.player.battlefield)




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


    @mock.patch.object(permanent.Permanent, 'take_damage')
    def test_blocking(self, mock_take_damage):
        """ single creature blocking single attacker; each do nonlethal damage"""
  
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
                '', '', '', '',  # skipping to declare_attackers
                '0', '', '',  # attacking w/ Devouring Deep
                '0', '', '',  # blocking
                's precombat_main',
                's precombat_main',
                '']):

            self.GAME.handle_turn()
            self.GAME.handle_turn()
            self.GAME.handle_turn()
            self.assertEqual(mock_take_damage.call_count, 2)
            c1 = self.player.battlefield.elements[0]
            c2 = self.opponent.battlefield.elements[0]

            # unfortunately each instance of the patched method share the same call history
            # so we can't assert that, for example, c1.take_damage was called with source=c2 and vice versa
            mock_take_damage.assert_has_calls([mock.call(c1, 2), mock.call(c2, 1)])



    @mock.patch.object(permanent.Permanent, 'dies')
    def test_lethal_damage_in_combat(self, mock_dies):
        """ single creature blocking single attacker; both die"""
        with mock.patch('builtins.input', side_effect=[
                '__self.battlefield.add("Sewn-Eye Drake")','',  # p0
                '__self.battlefield.add("Sewn-Eye Drake")','',  # p1
                '', '',
                '', '', '', '',  # skipping to declare_attackers
                '0', '', '',  # attacking w/ Drake
                '0',  # blocking
                's precombat_main',
                's precombat_main',
                '']):

            self.GAME.handle_turn()
            mock_dies.assert_any_call()
            self.assertEqual(self.player.life, 20)
            self.assertEqual(self.opponent.life, 20)


    def test_multiple_attacker(self):
        """ multiple attacker, one blocker. Damage goes to both player and creature."""
        with mock.patch('builtins.input', side_effect=[
                '__self.battlefield.add("Sewn-Eye Drake")',
                '__self.battlefield.add("Sewn-Eye Drake")',
                '__self.battlefield.add("Sewn-Eye Drake")', '',  # p0

                '__self.battlefield.add("Sewn-Eye Drake")', '',  # p1
                '', '',
                '', '', '', '',  # skipping to declare_attackers
                '0 1 2', '', '',  # attacking w/ everything
                '', '0', '',  # blocking the second drake
                's precombat_main',
                's precombat_main',
                '']):

            self.GAME.handle_turn()
            self.assertEqual(self.opponent.life, 14)
            self.assertEqual(self.player.graveyard.size(), 1)
            self.assertEqual(self.opponent.graveyard.size(), 1)


    def test_multiple_attacker_multiple_blocker(self):
        with mock.patch('builtins.input', side_effect=[
                '__self.discard(7)', '__self.draw_card("Devouring Deep")',  # p0
                '__self.draw_card("Devouring Deep")',
                '__self.draw_card("Sewn-Eye Drake")',
                '', '', '', '',
                '__self.mana.add(mana.Mana.BLUE, 9)',  # player 0, main step
                '__self.mana.add(mana.Mana.BLACK, 1)',
                'p Devouring Deep', '', '', '',  # pay mana, letting it resolve
                'p Devouring Deep', '', '', '',
                'p Sewn-Eye Drake', '', '', '', '',  # pay mana (choose hybrid & unrestricted), letting it resolve
                's precombat_main',
                's precombat_main',
                '0',  # attacking for 3 w/ haste
            
                '__self.discard(7)', '__self.draw_card("Devouring Deep")',
                '__self.draw_card("Devouring Deep")',  # player 1's turn, main step
                '__self.draw_card("Sewn-Eye Drake")',
                '__self.mana.add(mana.Mana.BLUE, 9)',  
                '__self.mana.add(mana.Mana.BLACK, 1)',
                'p Devouring Deep', '', '', '',  # pay mana, letting it resolve
                'p Devouring Deep', '', '', '',
                'p Sewn-Eye Drake', '', '', '', '',
                's precombat_main',
                's precombat_main',
                '0', '0', '', # attacking w/ flyer, tries to block with Devouring Deep (but should fail due to flying), no blocks

                's precombat_main',  # go to next turn
                's precombat_main',
                '',  # no attacks
                
                's end_of_combat',  # go to next turn: player 1's attack
                's end_of_combat',
                '0 1 2',  # player 1 attacking with everything

                '0 1',  # Devouring Deep #1 gets blocked by both Devouring Deeps
                '',  # Devouring Deep #2 goes through
                '2',  # Drakes block each other

                # both drakes kill each other
                # double-block kills one of Player 1's Devouring Deep
                # player 0 takes 1 damage

                # player 1
                '__self.tmp = self.battlefield.elements[0]'
                        '.status.damage_taken == 0'
                        ' and self.graveyard.get_card_by_name("Sewn-Eye Drake")'
                        ' and self.graveyard.get_card_by_name("Devouring Deep")',
                's draw',
                # player 0
                 '__self.tmp = self.game.players_list[0].battlefield.elements[0]'
                        '.status.damage_taken == 1'
                        ' and self.game.players_list[0].battlefield.elements[1]'
                        '.status.damage_taken == 0'
                        ' and self.graveyard.get_card_by_name("Sewn-Eye Drake")',
                's draw']):

            self.GAME.handle_turn()
            self.GAME.handle_turn()
            self.GAME.handle_turn()
            self.GAME.handle_turn()
            self.assertEqual(self.player.battlefield.size(), 2)
            self.assertEqual(self.opponent.battlefield.size(), 1)
            self.assertEqual(self.player.life, 16)
            self.assertEqual(self.opponent.life, 17)
            self.assertTrue(self.player.tmp)
            self.assertTrue(self.opponent.tmp)




if __name__ == '__main__':
    unittest.main()