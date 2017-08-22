- TEST CASES!!! (break them down into SMALLER units)

- add ID to each card/gameobject

- distinguish same-named objects in same zone

- make Stack / play.Play object more readable

- helper function for zone changes

- skip unnecessary combat phases

- Triggered Abilities
	- verify stacking/ordering triggers work and they are being resolved at next priority

- Activated Abilities
 - ability have a target
 - make a separate class for abilities/spells that share targeting system, etc.

- Static Abilities


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

Razorfoot Griffin

Sungrace Pegasus





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

First Response - log events (e.g. life loss) last turn



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

Raise the Alarm - tokens



Resolute Archangel - etb

Return to the Ranks - convoke; X

Sanctified Charge - "until eot" effects

Selfless Cathar - "until eot" effects

Seraph of the Masses - convoke; variable power/toughness

Solemn Offering *

Soul of Theros - ability from graveyard

Soulmender *

Spectra Ward - protection; aura

Spirit Bonds - eot



Tireless Missionaries - etb

Triplicate Spirits - convoke; token

Wall of Essence - dealt-combat-dmg trigger

Warden of the Beyond - static ability

Aeronaut Tinkerer - static

Aetherspouts *

Amphin Pathmage

Chasm Skulker

Chief Engineer

Chronostutter

Coral Barrier

Diffusion Sliver

Dissipate

Divination

Encrust

Ensoul Artifact

Frost Lynx

Fugitive Wizard

Glacial Crasher

Hydrosurge

Illusory Angel

Into the Void

Invisibility

Jace, the Living Guildpact

Jace's Ingenuity

Jalira, Master Polymorphist

Jorubai Murk Lurker

Kapsho Kitefins

Master of Predicaments

Mercurial Pretender

Military Intelligence

Mind Sculpt

Negate

Nimbus of the Isles

Paragon of Gathering Mists

Peel from Reality

Polymorphist's Jest

Quickling

Research Assistant

Soul of Ravnica

Statute of Denial

Stormtide Leviathan

Turn to Frog

Void Snare

Wall of Frost

Welkin Tern

Accursed Spirit

Black Cat

Blood Host

Carrion Crow

Caustic Tar

Child of Night

Covenant of Blood

Crippling Blight

Cruel Sadist

Endless Obedience

Eternal Thirst

Feast on the Fallen

Festergloom

Flesh to Dust

Gravedigger

In Garruk's Wake

Indulgent Tormentor

Leeching Sliver

Liliana Vess

Mind Rot

Necrobite

Necrogen Scudder

Necromancer's Assistant

Necromancer's Stockpile

Nightfire Giant

Ob Nixilis, Unshackled

Paragon of Open Graves

Rotfeaster Maggot

Shadowcloak Vampire

Sign in Blood

Soul of Innistrad

Stab Wound

Stain the Mind

Typhoid Rats

Ulcerate

Unmake the Graves

Wall of Limbs

Waste Not

Witch's Familiar

Xathrid Slyblade

Zof Shade

Act on Impulse

Aggressive Mining

Altac Bloodseeker

Belligerent Sliver

Blastfire Bolt

Borderland Marauder

Brood Keeper

Burning Anger

Chandra, Pyromaster

Circle of Flame

Clear a Path

Cone of Flame

Crowd's Favor

Crucible of Fire

Forge Devil

Foundry Street Denizen

Frenzied Goblin

Generator Servant

Goblin Kaboomist

Goblin Rabblemaster

Goblin Roughrider

Hammerhand

Heat Ray

Hoarding Dragon

Inferno Fist

Kird Chieftain

Krenko's Enforcer

Kurkesh, Onakke Ancient

Lava Axe

Lightning Strike

Might Makes Right

Miner's Bane

Paragon of Fierce Defiance

Rummaging Goblin

Scrapyard Mongrel

Shrapnel Blast

Siege Dragon

Soul of Shandalar

Stoke the Flames

Thundering Giant

Torch Fiend

Wall of Fire

Ancient Silverback

Back to Nature

Carnivorous Moss-Beast

Charging Rhino

Chord of Calling

Elvish Mystic

Feral Incarnation

Gather Courage

Genesis Hydra

Hornet Nest

Hornet Queen

Hunt the Weak

Hunter's Ambush

Invasive Species

Kalonian Twingrove

Life's Legacy

Living Totem

Naturalize

Netcaster Spider

Nissa, Worldwaker

Nissa's Expedition

Overwhelm

Paragon of Eternal Wilds

Phytotitan

Plummet

Ranger's Guile

Reclamation Sage

Restock

Roaring Primadox

Runeclaw Bear

Satyr Wayfinder

Shaman of Spring

Siege Wurm

Soul of Zendikar

Sunblade Elf

Titanic Growth

Undergrowth Scavenger

Venom Sliver

Verdant Haven

Vineweft

Wall of Mulch

Yisan, the Wanderer Bard

Garruk, Apex Predator

Sliver Hivelord

Avarice Amulet

Brawler's Plate

Bronze Sable

The Chain Veil

Gargoyle Sentinel

Grindclock

Haunted Plate Mail

Hot Soup

Juggernaut

Meteorite

Obelisk of Urd

Ornithopter

Perilous Vault

Phyrexian Revoker

Profane Memento

Rogue's Gloves

Sacred Armory

Scuttling Doom Engine

Shield of the Avatar

Soul of New Phyrexia

Staff of the Death Magus

Staff of the Flame Magus

Staff of the Mind Magus

Staff of the Sun Magus

Staff of the Wild Magus

Tormod's Crypt

Tyrant's Machine

Will-Forged Golem

Battlefield Forge

Caves of Koilos

Darksteel Citadel

Evolving Wilds

Llanowar Wastes

Radiant Fountain

Shivan Reef

Sliver Hive

Urborg, Tomb of Yawgmoth

Yavimaya Coast

Plains

Plains

Plains

Plains

Island

Island

Island

Island

Swamp

Swamp

Swamp

Swamp

Mountain

Mountain

Mountain

Mountain

Forest

Forest

Forest

Forest

Aegis Angel

Divine Verdict

Inspired Charge

Serra Angel

Cancel

Mahamoti Djinn

Nightmare

Sengir Vampire

Walking Corpse

Furnace Whelp

Seismic Strike

Shivan Dragon

Centaur Courser

Garruk's Packleader

Terra Stomper"