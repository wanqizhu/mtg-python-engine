(Flameborn Viron - vanilla 6/4 for 4RR)


- test game w/ vanilla creatures & lands

- make option to always make default choice with mana payment
	- smart mana payments when there's only 1 way

- discard prompts user
	- make sure test cases still work (since new input)


- TARGETS -- implement Lightning Bolt


rules: http://media.wizards.com/2017/downloads/MagicCompRules_20170707.pdf


- unit tests
	- mocking: see https://www.toptal.com/python/an-introduction-to-mocking-in-python


KNOWN BUGS
	- after multiple creatures receiving lethal dmg in combat, SOME creatures seem to survive the first state-based-action check and doesn't call dies() until the next state-based-action check
		- FIXED (?) by iterating over a copy of battlefield (since items were getting removed during iteration)