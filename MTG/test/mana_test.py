# mana payment

from MTG.mana import *
from MTG.player import Player
import mock, unittest


class TestManaPayment(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cls.m = ManaPool()
		cls.m.controller = Player([])
		cls.m.pool[Mana.BLUE] = 4
		cls.m.pool[Mana.WHITE] = 3


	def test_basic_mana_payment(self):
		self.assertEqual(self.m.canPay('U')[Mana.BLUE], 1)
		c = self.m.canPay('UUW')
		self.assertEqual(c[Mana.BLUE], 2)
		self.assertEqual(c[Mana.WHITE], 1)

	def test_numbers_in_mana_costs(self):
		with mock.patch('builtins.input', return_value=''):
			self.assertEqual(type(self.m.canPay('4U')), defaultdict)
			self.assertTrue(self.m.canPay('7'))
			self.assertTrue(self.m.canPay('0'))
			self.assertFalse(self.m.canPay('1R'))

		with mock.patch('builtins.input', side_effect=['RUUW']):
			self.assertFalse(self.m.canPay('4U'))


	def test_hybrid_mana_costs(self):
		with mock.patch('builtins.input', side_effect=['0', '0', '0', '']):
			c = self.m.canPay('(2/R)(2/W)(2/U)')
			self.assertEqual(c[Mana.BLUE] + c[Mana.WHITE], 6)

		with mock.patch('builtins.input', side_effect=['1', '0', '1', '']):
			self.assertFalse(self.m.canPay('(U/R)(2/W)(2/U)'))

		with mock.patch('builtins.input', side_effect=['0', '1', '1', 'UU']):
			c = self.m.canPay('U(2/R)(G/W)(W/U)')
			self.assertEqual(c[Mana.BLUE], 4)
			self.assertEqual(c[Mana.WHITE], 1)

if __name__ == '__main__':
    unittest.main()