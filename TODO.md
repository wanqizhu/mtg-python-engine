- TEST CASES!!! (break them down into SMALLER units)

- add ID to each card/gameobject

- distinguish same-named objects in same zone

- make Stack / play.Play object more readable

- helper function for zone changes



- skip unnecessary combat phases

- convoke / other cost modifiers

- Triggered Abilities
	- verify stacking/ordering triggers work and they are being resolved at next priority
	- 'intervening if' only trigger if condition is true
		- need another attribute when creating trigger that performs the 'if' check
			before putting trigger on stack

- Activated Abilities
 - ability have a target
 - IMPLEMENT COSTS OTHER THAN TAP
 	- sacrifice ~
 	- function signatures in general (?)
 		- return True if action successful and did something
 		- raise error if illegal
 		- return False if did nothing
 - make a separate class for abilities/spells that share targeting system, etc.

- Static Abilities

- eot / conditional / aura modifiers on permanents
	- auras
	- MULTIPLE MODIFIERS -- e.g. Zof Shade -- they need to stack correctly while maintaining original

- check target legality upon spell/ability RESOLUTION


rules: http://media.wizards.com/2017/downloads/MagicCompRules_20170707.pdf




KNOWN BUGS
	- non-active player would get priority first if they cast a spell during active player's turn (fixed??)
	- if target selection fails, the card disappears instead of returning to hand





**M15 progress

--- Done (*: need to write test)

Ajani's Pridemate

Congregate

Lightning Strike

Geist of the Moors

Mass Calcify *

Oreskos Swiftclaw

Razorfoot Griffin *

Sungrace Pegasus

Soulmender

Solemn Offering *

Divination

Fugitive Wizard

Jace's Ingenuity

Nimbus of the Isles

Accursed Spirit

Child of Night

Typhoid Rats

Witch's Familiar

Goblin Roughrider

Krenko's Enforcer

Lightning Strike

Thundering Giant

Runeclaw Bear

Bronze Sable

Ornithopter

Serra Angel

Mahamoti Djinn

Walking Corpse

Centaur Courser

Titanic Growth

Ulcerate

Zof Shade

Mind Rot *

Shadowcloak Vampire *

First Response

Raise the Alarm

Resolute Archangel *

Sanctified Charge

Selfless Cathar * - TODO


---


Ajani Steadfast - pwalker



Avacyn, Guardian Angel - activated ability; dmg prevention

Battle Mastery - aura

Boonweaver Giant - aura; search from zones



Constricting Sliver - giving ability to others; etb abilities

Dauntless River Marshal - activated ability

Devouring Light - convoke

Divine Favor - aura

Ephemeral Shields - convoke





Heliod's Pilgrim - etb; search from zones

Hushwing Gryff - disable triggered abilities

Kinsbaile Skirmisher - etb

Marked by Honor - aura



Meditation Puzzle - convoke

Midnight Guard - any creature etb

Oppressive Rays - aura; extra payment costs



Paragon of New Dawns - static ability; activated ability

Pillar of Light - target check on resolution

Preeminent Captain - on attack trigger







Return to the Ranks - convoke; X



Seraph of the Masses - convoke; variable power/toughness



Soul of Theros - ability from graveyard



Spectra Ward - protection; aura

Spirit Bonds - eot



Tireless Missionaries - etb

Triplicate Spirits - convoke; token

Wall of Essence - dealt-combat-dmg trigger

Warden of the Beyond - static ability

Aeronaut Tinkerer - static

Aetherspouts *

Amphin Pathmage - can't be blocked eot

Chasm Skulker - tokens

Chief Engineer - convoke to other spells

Chronostutter - *

Coral Barrier - tokens

Diffusion Sliver - becomes target; counter; optional payment

Dissipate - counter



Encrust - aura; don't untap; can't activate

Ensoul Artifact - becomes creature; aura

Frost Lynx - doesn't untap



Glacial Crasher - conditional attack (static)

Hydrosurge - eot modifiers

Illusory Angel - storm counter

Into the Void - *

Invisibility - aura; block modifier

Jace, the Living Guildpact - p-walker



Jalira, Master Polymorphist - reveal cards

Jorubai Murk Lurker - static; eot modifier

Kapsho Kitefins - other creature etb

Master of Predicaments - *

Mercurial Pretender - copy

Military Intelligence - *

Mind Sculpt - *

Negate - counter



Paragon of Gathering Mists - static apply-to-battlefield

Peel from Reality - *

Polymorphist's Jest - eot; lose abilities; frogify

Quickling - *

Research Assistant - *

Soul of Ravnica - activate ability from grave

Statute of Denial - counter

Stormtide Leviathan - apply-to-battlefield modifier

Turn to Frog - frogify

Void Snare - *

Wall of Frost - doesn't untap

Welkin Tern - conditional blocking



Black Cat - *

Blood Host - *

Carrion Crow - *

Caustic Tar - aura



Covenant of Blood - convoke

Crippling Blight - aura

Cruel Sadist - *

Endless Obedience - convoke

Eternal Thirst - aura

Feast on the Fallen - lost life last turn

Festergloom - eot

Flesh to Dust - can't be regenerated

Gravedigger - *

In Garruk's Wake - *

Indulgent Tormentor - player choice

Leeching Sliver - other creature trigger

Liliana Vess - pwalker



Necrobite - eot modifier; regenerate

Necrogen Scudder - *

Necromancer's Assistant - *

Necromancer's Stockpile - *

Nightfire Giant - static

Ob Nixilis, Unshackled - search library trigger

Paragon of Open Graves - apply-to-battlefield

Rotfeaster Maggot - *



Sign in Blood - *

Soul of Innistrad - ability from graveyard

Stab Wound - aura

Stain the Mind - convoke





Unmake the Graves - convoke

Wall of Limbs - *

Waste Not - *



Xathrid Slyblade - eot



Act on Impulse - eot

Aggressive Mining - *

Altac Bloodseeker - other trigger

Belligerent Sliver - apply-to-battlefield static

Blastfire Bolt - equipments

Borderland Marauder - eot

Brood Keeper - aura

Burning Anger - aura

Chandra, Pyromaster - pwalker

Circle of Flame - other trigger

Clear a Path - *

Cone of Flame - *

Crowd's Favor - convoke; eot

Crucible of Fire - static

Forge Devil - *

Foundry Street Denizen - other trigger

Frenzied Goblin - *

Generator Servant - mana spent on smthing

Goblin Kaboomist - artifact token

Goblin Rabblemaster - other creatuers must attack



Hammerhand - *

Heat Ray - X

Hoarding Dragon - *

Inferno Fist - aura

Kird Chieftain - static



Kurkesh, Onakke Ancient - other trigger

Lava Axe - *



Might Makes Right - *

Miner's Bane - eot

Paragon of Fierce Defiance - apply-to-other static effect

Rummaging Goblin - *

Scrapyard Mongrel - static

Shrapnel Blast - *

Siege Dragon - *

Soul of Shandalar - activate from grave

Stoke the Flames - convoke



Torch Fiend - *

Wall of Fire - eot

Ancient Silverback - regenerate

Back to Nature - *

Carnivorous Moss-Beast - *

Charging Rhino - blocking modifier

Chord of Calling - convoke; X

Elvish Mystic - *

Feral Incarnation - convoke

Gather Courage - convoke; eot

Genesis Hydra - X

Hornet Nest - tokens

Hornet Queen - tokens

Hunt the Weak - *

Hunter's Ambush - prevent combat dmg

Invasive Species - *

Kalonian Twingrove - static

Life's Legacy - additional costs

Living Totem - convoke

Naturalize - *

Netcaster Spider - *

Nissa, Worldwaker - pwalker

Nissa's Expedition - convoke

Overwhelm - convoke

Paragon of Eternal Wilds - apply-to-battlefield static

Phytotitan - delayed effect

Plummet - *

Ranger's Guile - hexproof

Reclamation Sage - *

Restock - *

Roaring Primadox - *



Satyr Wayfinder - *

Shaman of Spring - *

Siege Wurm - convoke

Soul of Zendikar - graveyard ability

Sunblade Elf - static; eot



Undergrowth Scavenger - *

Venom Sliver - apply-to-battlefield static

Verdant Haven - aura

Vineweft - aura

Wall of Mulch - *

Yisan, the Wanderer Bard - *

Garruk, Apex Predator - *

Sliver Hivelord - indestructible; apply-to-battlefield static

Avarice Amulet - equipment

Brawler's Plate - equip



The Chain Veil - pwalkers

Gargoyle Sentinel - eot

Grindclock - *

Haunted Plate Mail - equip

Hot Soup - equip

Juggernaut - must attack

Meteorite - *

Obelisk of Urd - convoke; static



Perilous Vault - *

Phyrexian Revoker - *

Profane Memento - *

Rogue's Gloves - equip

Sacred Armory - *

Scuttling Doom Engine - *

Shield of the Avatar - equip

Soul of New Phyrexia - ability from grave

Staff of the Death Magus - *

Staff of the Flame Magus - *

Staff of the Mind Magus - *

Staff of the Sun Magus - *

Staff of the Wild Magus - *

Tormod's Crypt - *

Tyrant's Machine - *

Will-Forged Golem - convoke

Battlefield Forge - *

Caves of Koilos - *

Darksteel Citadel - indestructible

Evolving Wilds - *

Llanowar Wastes - *

Radiant Fountain - *

Shivan Reef - *

Sliver Hive - conditinal mana spending

Urborg, Tomb of Yawgmoth - static

Yavimaya Coast - *

Plains

Island

Swamp

Mountain

Forest

Aegis Angel - indestructible; static

Divine Verdict - *

Inspired Charge - eot



Cancel - counter



Nightmare - *

Sengir Vampire - other trigger



Furnace Whelp - *

Seismic Strike - *

Shivan Dragon - *



Garruk's Packleader - other trigger

Terra Stomper - can't be countered