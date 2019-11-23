import mock
import unittest

from MTG.test.test_game import TestGameBase
from MTG.exceptions import *

class TestPlayer(TestGameBase):
    def test_optional_trigger_on_lifegain(self):
        """ Ajani's Pridemate: on life gain, put +1/+1 counter. """
        with mock.patch('builtins.input', side_effect=[
                '__self.battlefield.add("Ajani\'s Pridemate")',
                '__self.gain_life(3)',
                '', '', 'yes',  # resolving trigger
                '__self.tmp = self.battlefield[0].power == 3',
                '__self.gain_life(2)',
                '', '', '',  # resolving trigger, saying 'no'
                '__self.tmp = self.tmp and self.battlefield[0].power == 3',
                '__self.gain_life(1)',
                '', '', 'yes',  # resolving trigger
                '__self.tmp = self.tmp and self.battlefield[0].toughness == 4',
                '', '',
                '', '__self.gain_life(1)', '',  # opponent gains life
                '__self.tmp = self.tmp and not self.stack',  # no trigger
                's upkeep',
                's upkeep']):  # no attack

            self.GAME.handle_turn()
            self.assertTrue(self.player.tmp)

    def test_pt_modifiers(self):
        """Testing casting +4/+4 and -3/-3 until eot effects (plus +1/+1 counters)"""
        with mock.patch('builtins.input', side_effect=[
                '__self.battlefield.add("Ajani\'s Pridemate")',
                '__self.gain_life(1)',
                '', '', 'yes',  # resolving trigger
                '__self.tmp = self.battlefield[0].power == 3',
                '__self.gain_life(1)',
                '', '', 'yes',
                '__self.tmp = self.tmp and self.battlefield[0].power == 4',
                '__self.add_card_to_hand("Ulcerate")',
                '__self.add_card_to_hand("Titanic Growth")',
                '__self.mana.add("BGG")',
                'p Ulcerate', 'b 0',  # target
                '', '',
                '__self.tmp = self.tmp and self.battlefield[0].toughness == 1',
                'p Titanic Growth', 'b 0', '', # target
                '', '',
                '__self.tmp = self.tmp and self.battlefield[0].toughness == 5',
                's upkeep',
                's upkeep']):

            self.GAME.handle_turn()
            self.assertTrue(self.player.tmp)
            # both ulcerate and titanic growth should have fallen off
            self.assertEqual(self.player.battlefield[0].power, 4)

    def test_activated_ability_no_target(self):
        """Zof shade: self buff until eot """
        with mock.patch('builtins.input', side_effect=[
                '__self.battlefield.add("Zof Shade")',
                '__self.mana.add(mana.Mana.BLACK, 9)',
                'a 0', '', '',
                '__self.tmp = self.battlefield[0].power == 4',
                'a 0', 'a 0', '', '',
                '__self.tmp = self.tmp and self.battlefield[0].power == 6',
                '', '',
                '__self.tmp = self.tmp and self.battlefield[0].power == 8',
                's end', 's end',
                # should still keep the power at beginning of end step
                '__self.tmp = self.tmp and self.battlefield[0].power == 8',
                's upkeep',
                's upkeep']):

            self.GAME.handle_turn()
            self.assertTrue(self.player.tmp)
            # buffs should off
            self.assertEqual(self.player.battlefield[0].power, 2)

    def test_phase_based_conditional_trigger(self):
        """Testing trigger on each upkeep -- if lost life last turn, create token"""
        with mock.patch('builtins.input', side_effect=[
                '__self.battlefield.add("First Response")',
                '__self.lose_life(3)',
                's upkeep', 's upkeep', '', '',
                's upkeep',  # player 1's turn
                # player 0 verifying token
                '__self.tmp = self.battlefield[1].power == 1'
            ' and self.battlefield[1].is_color(["W"])', 's upkeep',
                '', '', 's upkeep', 's upkeep',  # player 0's turn again
                '0'  # attacking with token
        ]):

            self.player.autoDiscard = True
            self.opponent.autoDiscard = True
            self.GAME.handle_turn()
            self.GAME.handle_turn()
            self.GAME.handle_turn()
            self.assertTrue(self.player.tmp)
            # buffs should off
            self.assertEqual(self.player.opponent.life, 19)


    def test_activated_ability_targeting(self):
        """Testing Grindclock: mill based on # counters"""
        with mock.patch('builtins.input', side_effect=[
                '', '',
                '__self.battlefield.add("Grindclock")',
                'a 0_1', 'p',  # mill myself; the amount should be checked on RESOLUTION
                '__self.battlefield[0].untap()',
                'a 0_0',
                '__self.battlefield[0].untap()',
                'a 0_0',  # put 2 charge counters; activated in respond, so they should resolve first
                's upkeep', 's upkeep'
        ]):
            self.GAME.handle_turn()
            self.assertEqual(len(self.player.graveyard), 2)  # mill 2 cards


    def test_triggered_ability_targeting(self):
        """Testing Kinsbaile Skirmisher"""
        with mock.patch('builtins.input', side_effect=[
                's main', 's main',
                '__self.battlefield.add("Soulmender")',
                '__self.add_card_to_hand("Kinsbaile Skirmisher")',
                '__self.add_card_to_hand("Kinsbaile Skirmisher")',
                '__self.mana.add(mana.Mana.WHITE, 4)',
                'p Kinsbaile Skirmisher',
                '', '',
                'b 0',
                '', '',
                '__self.tmp = [self.battlefield[0].power == 2]',  # buffed soulmender
                'p Kinsbaile Skirmisher',
                '', '',
                'b 2',  # buff itself
                '', '',
                '__self.tmp.append(self.battlefield[2].toughness == 3)',
                's upkeep', 's upkeep'
        ]):
            self.GAME.handle_turn()
            self.assertTrue(all(self.player.tmp))


    def test_board_affecting_static_abilities(self):
        """Testing Kinsbaile Skirmisher"""
        with mock.patch('builtins.input', side_effect=[
                '__self.battlefield.add("Soulmender")',
                '__self.battlefield.add("Paragon of New Dawns")',
                '__self.battlefield.add("Child of Night")',
                '__self.tmp = [[p.power for p in self.battlefield] == [2, 2, 2]]',
                '__self.battlefield.add("Paragon of New Dawns")',
                '__self.tmp.append([p.power for p in self.battlefield] == [3, 3, 2, 3])',
                'addmana',
                '__self.add_card_to_hand("Lightning Bolt")',
                'p Lightning Bolt', 'b 1', '', '',
                '__self.tmp.append([p.power for p in self.battlefield] == [2, 2, 2])',
                '__self.battlefield.add("Paragon of New Dawns")',
                '__self.battlefield.add("Paragon of New Dawns")',
                '__self.battlefield.add("Soulmender")',
                's end', 's end',
                '__self.tmp.append([p.power for p in self.battlefield] == [4, 2, 4, 4, 4, 4])',
                's upkeep', 's upkeep'
        ]):
            self.GAME.handle_turn()
            # assert effect still holds
            self.player.tmp.append([p.power for p in self.player.battlefield] == [4, 2, 4, 4, 4, 4])
            self.assertTrue(all(self.player.tmp), msg=self.player.tmp)


    def test_conditional_self_affecting_static_abilities(self):
        """Testing Dauntless River Marshall & Warden of the Beyond

        Conditional +1/+1 (or +2/+2) -- examples of self-affecting static abilities
        """
        with mock.patch('builtins.input', side_effect=[
                '__self.battlefield.add("Dauntless River Marshal")',
                '__self.battlefield.add("Warden of the Beyond")',
                '__self.tmp = [[p.power for p in self.battlefield] == [2, 2]]',
                's main', 's main',
                '__self.add_card_to_hand("Island")',
                'p Island',
                '__self.tmp.append([p.power for p in self.battlefield if p.is_creature] == [3, 2])',
                '',
                '__self.battlefield.add("Plains")',  # player 1 exiles a card
                '__self.battlefield[0].exile()',
                '',
                '__self.tmp.append([p.power for p in self.battlefield if p.is_creature] == [3, 4])',
                'addmana',
                '__self.add_card_to_hand("Lightning Bolt")',
                'p Lightning Bolt', 'b 1', '', '',  # deal 3 dmg to warden, which is currently a 4/4
                '__self.tmp.append(len(self.battlefield) == 3)',  # warden should still be alive
                '__self.opponent.exile.pop()',  # clear opponent exile
                '', '',  # apply SBAs,
                '__self.tmp.append(len(self.battlefield) == 2)',  # warden should die
                '__self.battlefield.add("Dauntless River Marshal")',  # new River Marshal should immediately get buff
                '__self.tmp.append([p.power for p in self.battlefield if p.is_creature] == [3, 3])',
                's upkeep', 's upkeep'
        ]):
            self.GAME.handle_turn()
            self.assertTrue(all(self.player.tmp), msg=self.player.tmp)


    def test_multiple_triggers_ordering_active_player(self):
        """ Test trigger ordering"""
        with mock.patch('builtins.input', side_effect=[
                '__self.life=1',
                '__[self.battlefield.add("Tireless Missionaries"),'
                    'self.battlefield.add("Forge Devil")]',
                '1 0', # ordering trigger, forge devil first (i.e. bottom in stack)
                'b 1', # choose target, forge devil target self
                '', '',  # resolving first trigger
                '', '',  # resolving second trigger
                         # forge devil should be dead here
                '__self.tmp = self.life == 3',
                '__self.life=1',
                '__[self.battlefield.add("Tireless Missionaries"),'
                    'self.battlefield.add("Forge Devil")]',
                '0 1',  # order trigger; this will make forge devil kill us first
                'b 1',  # target
                '', ''  # should be dead, but only after self.tmp = True
                ]):

            self.player.autoOrderTriggers = False
            with self.assertRaises(GameOverException):
                self.GAME.handle_turn()
                self.assertTrue(self.player.tmp)
                self.assertTrue(self.player.lost)
                self.assertTrue(self.opponent.won)


    def test_multiple_triggers_ordering_inactive_player(self):
        """ same triggers as above, but on opponent's control """
        with mock.patch('builtins.input', side_effect=[
                '__[self.opponent.battlefield.add("Tireless Missionaries"),'
                    'self.opponent.battlefield.add("Forge Devil")]',
                '1 0',  # order trigger; this will make them gain life first
                'b 1',  # target smth on battlefield
                '', '', '', '',  # stack should be clear, back to player 1
                '__self.tmp = self.name == "player0" and self.game.stack.isEmpty',
                '__self.opponent.life=1',
                '__[self.opponent.battlefield.add("Tireless Missionaries"),'
                    'self.opponent.battlefield.add("Forge Devil")]',
                '0 1',  # order trigger; this will make forge devil kill them first
                'b 1',  # target
                '', ''  # should be dead
                ]):

            self.opponent.autoOrderTriggers = False
            with self.assertRaises(GameOverException):
                self.GAME.handle_turn()
                self.assertTrue(self.player.won)
                self.assertTrue(self.opponent.lost)
                self.assertTrue(self.player.tmp)


    def test_multiple_triggers_ordering_both_players(self):
        """ Both players have triggers waiting to be put onto the stack, 
        should be ordered by APNAP order.

        This happens w/ e.g. Destroy all Creatures.
        """
        
        with mock.patch('builtins.input', side_effect=[
                's main', 's main',
                '__self.add_card_to_hand("Mass Calcify")',  # destroy all nonwhite creatures
                '__[self.battlefield.add("Chasm Skulker"),'  # on-draw trigger
                    'self.battlefield.add("Chasm Skulker"),'
                    'self.opponent.battlefield.add("Chasm Skulker")]',
                '__[self.draw(), self.opponent.draw()]',  # should cause three triggers
                '0 1',  # player orders his two triggers
                '', '',  # first trigger resolves, inactive player
                '__self.tmp = [self.opponent.battlefield[0].power == 2]',
                '', '', '', '',  # second + third trigger
                '__self.tmp.append(self.opponent.battlefield[0].power == 2)',
                'addmana',
                'p Mass Calcify',
                '', '', # let it resolve
                '0 1',  # order trigger
                's upkeep', 's upkeep',  # let all 3 triggers resolve
                ]):

            self.player.autoOrderTriggers = False
            self.opponent.autoOrderTriggers = False
           
            self.GAME.handle_turn()
            self.assertTrue(all(self.player.tmp), self.player.tmp)


if __name__ == '__main__':
    unittest.main()
