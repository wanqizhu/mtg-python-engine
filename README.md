Python-MTG
==========

This is intended to be an implementation of the algorithm described in the [Magic: the Gathering Comprehensive Rules](http://media.wizards.com/images/magic/tcg/resources/rules/MagicCompRules_20130201.pdf)

Magic: the Gathering is owned by Wizards of the Coast.


Note: In the following documentation, `filename.funcOrClassName()` refers to the function/class defined in MTG/filename.py. If we refer to a specific card, look for how that card is parsed in data/cards.txt or set_up_cards.log.


Cards
==========

Raw card data are obtained from mtgjson (json) or cockatrice (xml, obsolele; should use json from now on). They are then fed through their respective [parsers](parser/), where each card turns into its own class inheriting from card.Card(). [An example of a parsed file](data/M15_cards.py) contains all the printed information on the card (power, toughness, text, manacost, etc). It has an associated *id_to_name_dict* and *name_to_id_dict* so that we can easily refence a card's class based on its display string name.

Keyword abilities are automatically parsed. Other abilities are implemented manually in [data/cards.txt](data/cards.txt), following a set format outlined at the top of the file.

These abilities are parsed by [MTG/cards.py's set_up_cards() function](MTG/cards.py), and various othr functions in cards.py detail how each ability is processed from the text file to the game engine.

The actual code that's executed from `set_up_cards` is logged in [set_up_cards.log](set_up_cards.log).


Abilities
==========

Abilities in general are stored in the individual card class (`class c383180(card.Card)` in data/M15_cards.py, for example), but they aren't in effect until the card become a permanent.

## Activated Ability

An example of an activated ability:

```add_activated_ability("Soulmender", 'T', 'self.controller.gain_life(1)', [])```

processed by `cards.add_activated_ability()`. The last param is empty because this ability has no targets.

When a permanent is initiated (`p = permanent.make_permanent(card)`), it turns all activated abilities of the original card into `abilities.ActivatedAbility()` instances. They can be accessed as `p.activated_abilities`, and when activated the individual abilities, NOT the permanent, is passed onto the stack. Abilities refer back to the original card via `self.card` (see Ajani's Pridemate).

Abilities are activated when a player inputs `a N_M`, where M defaults to 0 if _M is ommitted. *a* stands for *activate*, *N* refers to the N-th object on that player's battlefield and *M* is the M-th activated ability of that object. See `player.get_action() ...elif answer[:2] == 'a '`.

If an activation is illegal (cannot pay costs, no legal targets, etc.), the game rewinds (by setting itself equal to a previous Deepcopy). Whether a cost can be paid is determined by checking each part of the cost function, when paid, returns True. For example, `permanent.Permanent.tap()` returns True iff the permanent can be tapped. See `abilities.ActivatedAbilities.can_activate()`.


## Triggered Ability


## Static Ability


Spells
==========



Targeting
==========

A spell/ability on the stack (`play.Play()`) tracks its own targets_chosen and target_criterias. Before resolution, if the targets are illegal, the spell fizzles.



Permanents
==========

`permanent.Permanent()`, inheriting from `gameobject.GameObject`

## Characteristics

`gameobject.Characteristics()`



Combat
==========

`game.handle_combat_phase()`



Other Game Rules
==========

SBAs: `game.check_state_based_actions()`