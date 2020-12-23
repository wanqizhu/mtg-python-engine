Python-MTG
==========

**Start the Game with `python -m MTG.game`**
*Run tests with `./test.sh`*

This is intended to be an implementation of the algorithm described in the [Magic: the Gathering Comprehensive Rules](http://media.wizards.com/images/magic/tcg/resources/rules/MagicCompRules_20130201.pdf)

Magic: the Gathering is owned by Wizards of the Coast.


Note: In the following documentation, `filename.funcOrClassName()` refers to the function/class defined in MTG/filename.py. If we refer to a specific card, look for how that card is parsed in `data/[SETNAME]_cards.txt`.


To see the engine in action, run `pip install -r requirements.txt` then `python -m MTG.game`.
You cannot run the script directly due to [shadowed imports.](http://python-notes.curiousefficiency.org/en/latest/python_concepts/import_traps.html#the-double-import-trap)


Cards
==========

Raw card data are obtained from mtgjson (json) or cockatrice (xml, obsolele; should use json from now on). They are then fed through their respective [parsers](parser/), where each card turns into its own class inheriting from card.Card(). [An example of a parsed file](data/M15_cards.py) contains all the printed information on the card (power, toughness, text, manacost, etc). It has an associated *id_to_name_dict* and *name_to_id_dict* so that we can easily refence a card's class based on its display string name.

Keyword abilities are automatically parsed. Other abilities are implemented manually in [data/M15_cards.txt](data/M15_cards.txt), following a set format outlined at the top of the file.

These abilities are parsed by [MTG/cards.py's setup_cards() function](MTG/cards.py), and various othr functions in cards.py detail how each ability is processed from the text file to the game engine.

The actual code that's executed from `setup_cards` is logged in [setup_cards.log](setup_cards.log).


Abilities
==========

Abilities in general are stored in the individual card class (e.g. `class c383180(card.Card)` in data/M15_cards.py), but they aren't in effect until the card become a permanent.

### Activated Ability

```python
def add_activated_ability(cardname, cost, effect, 
                          target_criterias=None, prompts=None)
```

An example of an activated ability, which we specify in `setup_cards.log`:

```python
add_activated_ability("Soulmender", 'T', 'self.controller.gain_life(1)', [])
```

The last param is empty because this ability has no targets.

When a permanent is initiated (`p = permanent.make_permanent(card)`), it turns all activated abilities of the original card into `abilities.ActivatedAbility()` instances. They can be accessed as `p.activated_abilities`, and when activated the individual abilities, as its standalone object, is passed onto the stack. Abilities refer back to the original card via `self.card` (see Ajani's Pridemate).

Abilities are activated via console interface when a player inputs `a N_M`, where M defaults to 0 if ommitted. *a* stands for *activate*, *N* refers to the N-th object on that player's battlefield and *M* is the M-th activated ability of that object. See `player.get_action() ...elif answer[:2] == 'a '`.

If an activation is illegal (cannot pay costs, no legal targets, etc.), the game rewinds (by setting itself equal to a previous Deepcopy). Whether a cost can be paid is determined by checking each part of the cost function, when paid, returns True. For example, `permanent.Permanent.tap()` returns True iff the permanent can be tapped. See `abilities.ActivatedAbilities.can_activate()`.


### Triggered Ability

Triggered ability have the following forms:

- Trigger condition: e.g. onEtB, onAttack -- see `triggers.triggerConditions`.
- Trigger effect: what happens when the trigger resolves
- (Optional) trigger targets: any targets the player need to choose, and criterias on those targets (e.g. player, creature, etc.)
- (Optional) intervening-if's: conditions that must be satisfied BOTH during the trigger condition AND before the trigger resolves

The details are implemented in `cards.add_trigger_ability()` and `abilities.TriggeredAbility()`.


### Static Ability

Evergreen Abilities: (`static_abilities.StaticAbilities`)

Other static effects: See Permanents --> Effects below.


Spells
==========

Everything on the stack, spell or ability, is a `play.Play()` object. When it resolves, if it's not countered & its targets are still legal, it calls `play.Play.apply()`.


### Without Targets

Spell without targets have their apply function having the signature

```lambda self: do_something```

where self refers to the spell. This functionality is implemented via `cards.add_play_func_no_targets()`.

All permanent spells (except auras) have no targets. Their apply_func defaults to `permanent.make_permanent(card)`, which is the default `card.Card.play_func`.


### With targets

Spell with targets have their apply function having the signature

```lambda self, targets, is_legal_target: do_something_to_targets_based_on_is_legal_target```

`is_legal_target` is a boolean list of the spell's chosen targets' legality.

If there's only one target, then is_legal_target must be `[True]` (since otherwise none of the spells' targets would be legal and it would fizzle).

The reason why this is needed is because some spells' resolution have separate abilities for each target, and some spells (e.g. two creatures fighting each other) require multiple targets to be legal to resolve its effect. So this enables spells to customize which effects to resolve should some (but not all) of its targets become illegal.



Targeting
==========

A spell/ability on the stack (`play.Play()`) tracks its own targets_chosen and target_criterias. Before resolution, if the targets are illegal, the spell fizzles.

When a spell/ability requires its user to choose a target, `utils.choose_targets()` is called. See `utils.get_target_from_user_input()` for details (e.g. 'b 2' gets the 2nd (0-indexed) permanent on your side of the battlefield).


Permanents
==========

`permanent.Permanent()`, inheriting from `gameobject.GameObject`

### Effects

`permanent.Permanent.effects()` -- temporary/static effects affecting the permanent

e.g. power modifying effects until eot; (conditional) static effects like "all creatures get +1/+1" (this applies to all permanenets but only active for creatures)

When a card or ability adds an effect, it will call `permanent.Permanent.add_effect(effect_name, effect_details, effect_source, effect_expiration, _optional_toggle_function)`. For example, *Titanic Growth*, which gives a creature +4/+4 until eot, has the following play function:

```targets[0].add_effect('modifyPT', (4, 4), self, self.game.eot_time)```

Board-affecting static effects that are conditional on a card's state, such as *Paragon of the New Dawn*'s ability "other white creatures you control get +1/+1", are applied to
every permanent you control but are toggled off for nonwhite creatures. This is done via

```add_static_effect("Paragon of New Dawns", 'controller -self', 'modifyPT', (1, 1), lambda eff: eff.apply_target.is_creature and eff.apply_target.has_color("W"))```

Note that `cards.add_static_effect()` will call `p.add_effect()` for each relevant permanent (in this case, everything under Paragon's controller's control except the Paragon itself). The last param, `lambda eff: ...`, is the toggle function, which determines which permanents the effect will be toggled on. (See `permanent.Permanent.add_effect` and `permanent.Permanent.check_effect_expiration`)



### Characteristics

These are the printed characteristics of the card. (`gameobject.Characteristics()`)



Combat
==========

`game.handle_combat_phase()`

Note that during blocking, the game will display all untapped creatures, even if none of them are relevant in this combat (say if all attackers can't be blocked). You assign blocks, then the game checks its legality and rewinds if it's not legal.


Other Game Rules
==========

SBAs: `game.check_state_based_actions()`

Tokens: `token.create_token(); player.create_token()` A Permanent p is a token iff `p.is_token == True`.


Parser
==========
The `parser` folder contains raw card information in text format, e.g. json/xml, and parsing code that translation raw text into individual card classes that extend `card.Card`.

Example from `data/M15_cards.py`:
```python
class c383181(card.Card):
    "Ajani's Pridemate"
    def __init__(self):
        super(c383181, self).__init__(gameobject.Characteristics(**{'mana_cost': '1W', 'text': "Whenever you gain life, you may put a +1/+1 counter on Ajani's Pridemate.", 'subtype': ['Cat', 'Soldier'], 'power': 2, 'color': ['W'], 'name': "Ajani's Pridemate", 'toughness': 2}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

```

To generate this, run `python -m parser.parse_mtgjson`.

Notice this only has static information. To give the card its actual ability, we need to encode it manually in [data/M15_cards.txt](data/M15_cards.txt), which then gets processed by `cards.setup_cards()`.

```python
add_trigger("Ajani's Pridemate", triggers.triggerConditions['onControllerLifeGain'], '[self.card.add_counter("+1/+1") if self.controller.make_choice( "Would you like to put a +1/+1 counter on %r?" % self.card) else None]', None, [], intervening_if=None)
```



Progress
==========

...

M15 cards: 56/256

Cube cards: .../450




Comp Rules Implementation Process
==========
[Comprehensive Rules 2017](http://media.wizards.com/2017/downloads/MagicCompRules_20170707.pdf)

*Rule#.subrules-implemented - subrules-or-generic-exceptions-not-implemented*

100/101/other generic rules - Only for 2-player, casual format

102

103/104 - Except for alternate win conditions (empty lib, poison); game draws

105.1-2 - .3-4

...
