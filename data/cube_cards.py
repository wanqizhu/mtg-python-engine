from MTG import card
from MTG import gameobject
from MTG import cardtype
from MTG import abilities
from MTG import mana

class c189902(card.Card):
    "Elite Vanguard"
    def __init__(self):
        super(c189902, self).__init__(gameobject.Characteristics(**{'color': ['W'], 'text': '', 'power': 2, 'mana_cost': 'W', 'name': 'Elite Vanguard', 'subtype': ['Human', 'Soldier'], 'toughness': 1}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c191240(card.Card):
    "Jace Beleren"
    def __init__(self):
        super(c191240, self).__init__(gameobject.Characteristics(**{'color': ['U'], 'name': 'Jace Beleren', 'subtype': ['Jace'], 'text': '+2: Each player draws a card.\n−1: Target player draws a card.\n−10: Target player puts the top twenty cards of his or her library into his or her graveyard.', 'mana_cost': '1UU'}, supertype=[], types=[cardtype.CardType.PLANESWALKER], abilities=[]))

class c190159(card.Card):
    "Ponder"
    def __init__(self):
        super(c190159, self).__init__(gameobject.Characteristics(**{'color': ['U'], 'name': 'Ponder', 'text': 'Look at the top three cards of your library, then put them back in any order. You may shuffle your library.\nDraw a card.', 'mana_cost': 'U'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c190193(card.Card):
    "Cemetery Reaper"
    def __init__(self):
        super(c190193, self).__init__(gameobject.Characteristics(**{'color': ['B'], 'text': 'Other Zombie creatures you control get +1/+1.\n{2}{B}, {T}: Exile target creature card from a graveyard. Create a 2/2 black Zombie creature token.', 'power': 2, 'mana_cost': '1BB', 'name': 'Cemetery Reaper', 'subtype': ['Zombie'], 'toughness': 2}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c190535(card.Card):
    "Doom Blade"
    def __init__(self):
        super(c190535, self).__init__(gameobject.Characteristics(**{'color': ['B'], 'name': 'Doom Blade', 'text': 'Destroy target nonblack creature.', 'mana_cost': '1B'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c191089(card.Card):
    "Lightning Bolt"
    def __init__(self):
        super(c191089, self).__init__(gameobject.Characteristics(**{'color': ['R'], 'name': 'Lightning Bolt', 'text': 'Lightning Bolt deals 3 damage to target creature or player.', 'mana_cost': 'R'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c193751(card.Card):
    "Siege-Gang Commander"
    def __init__(self):
        super(c193751, self).__init__(gameobject.Characteristics(**{'color': ['R'], 'text': 'When Siege-Gang Commander enters the battlefield, create three 1/1 red Goblin creature tokens.\n{1}{R}, Sacrifice a Goblin: Siege-Gang Commander deals 2 damage to target creature or player.', 'power': 2, 'mana_cost': '3RR', 'name': 'Siege-Gang Commander', 'subtype': ['Goblin'], 'toughness': 2}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c189880(card.Card):
    "Acidic Slime"
    def __init__(self):
        super(c189880, self).__init__(gameobject.Characteristics(**{'color': ['G'], 'text': 'Deathtouch (Any amount of damage this deals to a creature is enough to destroy it.)\nWhen Acidic Slime enters the battlefield, destroy target artifact, enchantment, or land.', 'power': 2, 'mana_cost': '3GG', 'name': 'Acidic Slime', 'subtype': ['Ooze'], 'toughness': 2}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Deathtouch]))

class c191080(card.Card):
    "Birds of Paradise"
    def __init__(self):
        super(c191080, self).__init__(gameobject.Characteristics(**{'color': ['G'], 'text': 'Flying\n{T}: Add one mana of any color to your mana pool.', 'power': 0, 'mana_cost': 'G', 'name': 'Birds of Paradise', 'subtype': ['Bird'], 'toughness': 1}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Flying]))

class c189878(card.Card):
    "Llanowar Elves"
    def __init__(self):
        super(c189878, self).__init__(gameobject.Characteristics(**{'color': ['G'], 'text': '{T}: Add {G} to your mana pool.', 'power': 1, 'mana_cost': 'G', 'name': 'Llanowar Elves', 'subtype': ['Elf', 'Druid'], 'toughness': 1}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c189887(card.Card):
    "Rampant Growth"
    def __init__(self):
        super(c189887, self).__init__(gameobject.Characteristics(**{'color': ['G'], 'name': 'Rampant Growth', 'text': 'Search your library for a basic land card and put that card onto the battlefield tapped. Then shuffle your library.', 'mana_cost': '1G'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c191315(card.Card):
    "Howling Mine"
    def __init__(self):
        super(c191315, self).__init__(gameobject.Characteristics(**{'color': '', 'name': 'Howling Mine', 'text': "At the beginning of each player's draw step, if Howling Mine is untapped, that player draws an additional card.", 'mana_cost': '2'}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c191091(card.Card):
    "Dragonskull Summit"
    def __init__(self):
        super(c191091, self).__init__(gameobject.Characteristics(**{'color': ['B', 'R'], 'name': 'Dragonskull Summit', 'text': 'Dragonskull Summit enters the battlefield tapped unless you control a Swamp or a Mountain.\n{T}: Add {B} or {R} to your mana pool.', 'mana_cost': ''}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c191067(card.Card):
    "Drowned Catacomb"
    def __init__(self):
        super(c191067, self).__init__(gameobject.Characteristics(**{'color': ['U', 'B'], 'name': 'Drowned Catacomb', 'text': 'Drowned Catacomb enters the battlefield tapped unless you control an Island or a Swamp.\n{T}: Add {U} or {B} to your mana pool.', 'mana_cost': ''}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c190562(card.Card):
    "Glacial Fortress"
    def __init__(self):
        super(c190562, self).__init__(gameobject.Characteristics(**{'color': ['W', 'U'], 'name': 'Glacial Fortress', 'text': 'Glacial Fortress enters the battlefield tapped unless you control a Plains or an Island.\n{T}: Add {W} or {U} to your mana pool.', 'mana_cost': ''}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c191100(card.Card):
    "Sunpetal Grove"
    def __init__(self):
        super(c191100, self).__init__(gameobject.Characteristics(**{'color': ['G', 'W'], 'name': 'Sunpetal Grove', 'text': 'Sunpetal Grove enters the battlefield tapped unless you control a Forest or a Plains.\n{T}: Add {G} or {W} to your mana pool.', 'mana_cost': ''}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c190560(card.Card):
    "Terramorphic Expanse"
    def __init__(self):
        super(c190560, self).__init__(gameobject.Characteristics(**{'color': '', 'name': 'Terramorphic Expanse', 'text': '{T}, Sacrifice Terramorphic Expanse: Search your library for a basic land card and put it onto the battlefield tapped. Then shuffle your library.', 'mana_cost': ''}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c266299(card.Card):
    "Ajani Vengeant"
    def __init__(self):
        super(c266299, self).__init__(gameobject.Characteristics(**{'color': ['W', 'R'], 'name': 'Ajani Vengeant', 'subtype': ['Ajani'], 'text': "+1: Target permanent doesn't untap during its controller's next untap step.\n−2: Ajani Vengeant deals 3 damage to target creature or player and you gain 3 life.\n−7: Destroy all lands target player controls.", 'mana_cost': '2RW'}, supertype=[], types=[cardtype.CardType.PLANESWALKER], abilities=[]))

class c249405(card.Card):
    "Qasali Pridemage"
    def __init__(self):
        super(c249405, self).__init__(gameobject.Characteristics(**{'color': ['W', 'G'], 'text': 'Exalted (Whenever a creature you control attacks alone, that creature gets +1/+1 until end of turn.)\n{1}, Sacrifice Qasali Pridemage: Destroy target artifact or enchantment.', 'power': 2, 'mana_cost': 'GW', 'name': 'Qasali Pridemage', 'subtype': ['Cat', 'Wizard'], 'toughness': 2}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c249383(card.Card):
    "Briarhorn"
    def __init__(self):
        super(c249383, self).__init__(gameobject.Characteristics(**{'color': ['G'], 'text': "Flash\nWhen Briarhorn enters the battlefield, target creature gets +3/+3 until end of turn.\nEvoke {1}{G} (You may cast this spell for its evoke cost. If you do, it's sacrificed when it enters the battlefield.)", 'power': 3, 'mana_cost': '3G', 'name': 'Briarhorn', 'subtype': ['Elemental'], 'toughness': 3}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Flash]))

class c249386(card.Card):
    "Lightning Helix"
    def __init__(self):
        super(c249386, self).__init__(gameobject.Characteristics(**{'color': ['W', 'R'], 'name': 'Lightning Helix', 'text': 'Lightning Helix deals 3 damage to target creature or player and you gain 3 life.', 'mana_cost': 'RW'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c249395(card.Card):
    "Evolving Wilds"
    def __init__(self):
        super(c249395, self).__init__(gameobject.Characteristics(**{'color': '', 'name': 'Evolving Wilds', 'text': '{T}, Sacrifice Evolving Wilds: Search your library for a basic land card and put it onto the battlefield tapped. Then shuffle your library.', 'mana_cost': ''}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c259274(card.Card):
    "Blazing Specter"
    def __init__(self):
        super(c259274, self).__init__(gameobject.Characteristics(**{'color': ['B', 'R'], 'text': 'Flying, haste\nWhenever Blazing Specter deals combat damage to a player, that player discards a card.', 'power': 2, 'mana_cost': '2BR', 'name': 'Blazing Specter', 'subtype': ['Specter'], 'toughness': 2}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Flying, abilities.StaticAbilities.Haste]))

class c249384(card.Card):
    "Icy Manipulator"
    def __init__(self):
        super(c249384, self).__init__(gameobject.Characteristics(**{'color': '', 'name': 'Icy Manipulator', 'text': '{1}, {T}: Tap target artifact, creature, or land.', 'mana_cost': '4'}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c249365(card.Card):
    "Deep Analysis"
    def __init__(self):
        super(c249365, self).__init__(gameobject.Characteristics(**{'color': ['U'], 'name': 'Deep Analysis', 'text': 'Target player draws two cards.\nFlashback—{1}{U}, Pay 3 life. (You may cast this card from your graveyard for its flashback cost. Then exile it.)', 'mana_cost': '3U'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[abilities.StaticAbilities.Flash]))

class c259262(card.Card):
    "Cruel Ultimatum"
    def __init__(self):
        super(c259262, self).__init__(gameobject.Characteristics(**{'color': ['U', 'B', 'R'], 'name': 'Cruel Ultimatum', 'text': 'Target opponent sacrifices a creature, discards three cards, then loses 5 life. You return a creature card from your graveyard to your hand, draw three cards, then gain 5 life.', 'mana_cost': 'UUBBBRR'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c393915(card.Card):
    "Rancor"
    def __init__(self):
        super(c393915, self).__init__(gameobject.Characteristics(**{'color': ['G'], 'name': 'Rancor', 'subtype': ['Aura'], 'text': "Enchant creature\nEnchanted creature gets +2/+0 and has trample.\nWhen Rancor is put into a graveyard from the battlefield, return Rancor to its owner's hand.", 'mana_cost': 'G'}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c393931(card.Card):
    "Treetop Village"
    def __init__(self):
        super(c393931, self).__init__(gameobject.Characteristics(**{'color': ['G'], 'name': 'Treetop Village', 'text': "Treetop Village enters the battlefield tapped.\n{T}: Add {G} to your mana pool.\n{1}{G}: Treetop Village becomes a 3/3 green Ape creature with trample until end of turn. It's still a land. (If it would assign enough damage to its blockers to destroy them, you may have it assign the rest of its damage to defending player or planeswalker.)", 'mana_cost': ''}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c136209(card.Card):
    "Venser, Shaper Savant"
    def __init__(self):
        super(c136209, self).__init__(gameobject.Characteristics(**{'color': ['U'], 'text': "Flash\nWhen Venser, Shaper Savant enters the battlefield, return target spell or permanent to its owner's hand.", 'power': 2, 'mana_cost': '2UU', 'name': 'Venser, Shaper Savant', 'subtype': ['Human', 'Wizard'], 'toughness': 2}, supertype=[cardtype.SuperType.LEGENDARY], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Flash]))

class c126215(card.Card):
    "Sword of the Meek"
    def __init__(self):
        super(c126215, self).__init__(gameobject.Characteristics(**{'color': '', 'name': 'Sword of the Meek', 'subtype': ['Equipment'], 'text': 'Equipped creature gets +1/+2.\nEquip {2}\nWhenever a 1/1 creature enters the battlefield under your control, you may return Sword of the Meek from your graveyard to the battlefield, then attach it to that creature.', 'mana_cost': '2'}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c247525(card.Card):
    "Mother of Runes"
    def __init__(self):
        super(c247525, self).__init__(gameobject.Characteristics(**{'color': ['W'], 'text': '{T}: Target creature you control gains protection from the color of your choice until end of turn.', 'power': 1, 'mana_cost': 'W', 'name': 'Mother of Runes', 'subtype': ['Human', 'Cleric'], 'toughness': 1}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c247156(card.Card):
    "Oblivion Ring"
    def __init__(self):
        super(c247156, self).__init__(gameobject.Characteristics(**{'color': ['W'], 'name': 'Oblivion Ring', 'text': "When Oblivion Ring enters the battlefield, exile another target nonland permanent.\nWhen Oblivion Ring leaves the battlefield, return the exiled card to the battlefield under its owner's control.", 'mana_cost': '2W'}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c247180(card.Card):
    "Path to Exile"
    def __init__(self):
        super(c247180, self).__init__(gameobject.Characteristics(**{'color': ['W'], 'name': 'Path to Exile', 'text': 'Exile target creature. Its controller may search his or her library for a basic land card, put that card onto the battlefield tapped, then shuffle his or her library.', 'mana_cost': 'W'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c247400(card.Card):
    "Wall of Omens"
    def __init__(self):
        super(c247400, self).__init__(gameobject.Characteristics(**{'color': ['W'], 'text': 'Defender\nWhen Wall of Omens enters the battlefield, draw a card.', 'power': 0, 'mana_cost': '1W', 'name': 'Wall of Omens', 'subtype': ['Wall'], 'toughness': 4}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Defender]))

class c247331(card.Card):
    "Brainstorm"
    def __init__(self):
        super(c247331, self).__init__(gameobject.Characteristics(**{'color': ['U'], 'name': 'Brainstorm', 'text': 'Draw three cards, then put two cards from your hand on top of your library in any order.', 'mana_cost': 'U'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c247186(card.Card):
    "Fact or Fiction"
    def __init__(self):
        super(c247186, self).__init__(gameobject.Characteristics(**{'color': ['U'], 'name': 'Fact or Fiction', 'text': 'Reveal the top five cards of your library. An opponent separates those cards into two piles. Put one pile into your hand and the other into your graveyard.', 'mana_cost': '3U'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c247302(card.Card):
    "Mulldrifter"
    def __init__(self):
        super(c247302, self).__init__(gameobject.Characteristics(**{'color': ['U'], 'text': "Flying\nWhen Mulldrifter enters the battlefield, draw two cards.\nEvoke {2}{U} (You may cast this spell for its evoke cost. If you do, it's sacrificed when it enters the battlefield.)", 'power': 2, 'mana_cost': '4U', 'name': 'Mulldrifter', 'subtype': ['Elemental'], 'toughness': 2}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Flying]))

class c247552(card.Card):
    "Vampire Nighthawk"
    def __init__(self):
        super(c247552, self).__init__(gameobject.Characteristics(**{'color': ['B'], 'text': 'Flying, deathtouch, lifelink', 'power': 2, 'mana_cost': '1BB', 'name': 'Vampire Nighthawk', 'subtype': ['Vampire', 'Shaman'], 'toughness': 3}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Deathtouch, abilities.StaticAbilities.Flying, abilities.StaticAbilities.Lifelink]))

class c247539(card.Card):
    "Comet Storm"
    def __init__(self):
        super(c247539, self).__init__(gameobject.Characteristics(**{'color': ['R'], 'name': 'Comet Storm', 'text': 'Multikicker {1} (You may pay an additional {1} any number of times as you cast this spell.)\nChoose target creature or player, then choose another target creature or player for each time Comet Storm was kicked. Comet Storm deals X damage to each of them.', 'mana_cost': 'XRR'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c247368(card.Card):
    "Flametongue Kavu"
    def __init__(self):
        super(c247368, self).__init__(gameobject.Characteristics(**{'color': ['R'], 'text': 'When Flametongue Kavu enters the battlefield, it deals 4 damage to target creature.', 'power': 4, 'mana_cost': '3R', 'name': 'Flametongue Kavu', 'subtype': ['Kavu'], 'toughness': 2}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c247148(card.Card):
    "Eternal Witness"
    def __init__(self):
        super(c247148, self).__init__(gameobject.Characteristics(**{'color': ['G'], 'text': 'When Eternal Witness enters the battlefield, you may return target card from your graveyard to your hand.', 'power': 2, 'mana_cost': '1GG', 'name': 'Eternal Witness', 'subtype': ['Human', 'Shaman'], 'toughness': 1}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c238141(card.Card):
    "Hornet Queen"
    def __init__(self):
        super(c238141, self).__init__(gameobject.Characteristics(**{'color': ['G'], 'text': 'Flying\nDeathtouch (Any amount of damage this deals to a creature is enough to destroy it.)\nWhen Hornet Queen enters the battlefield, create four 1/1 green Insect creature tokens with flying and deathtouch.', 'power': 2, 'mana_cost': '4GGG', 'name': 'Hornet Queen', 'subtype': ['Insect'], 'toughness': 2}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Deathtouch, abilities.StaticAbilities.Flying]))

class c247176(card.Card):
    "Sakura-Tribe Elder"
    def __init__(self):
        super(c247176, self).__init__(gameobject.Characteristics(**{'color': ['G'], 'text': 'Sacrifice Sakura-Tribe Elder: Search your library for a basic land card, put that card onto the battlefield tapped, then shuffle your library.', 'power': 1, 'mana_cost': '1G', 'name': 'Sakura-Tribe Elder', 'subtype': ['Snake', 'Shaman'], 'toughness': 1}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c233181(card.Card):
    "Scavenging Ooze"
    def __init__(self):
        super(c233181, self).__init__(gameobject.Characteristics(**{'color': ['G'], 'text': '{G}: Exile target card from a graveyard. If it was a creature card, put a +1/+1 counter on Scavenging Ooze and you gain 1 life.', 'power': 2, 'mana_cost': '1G', 'name': 'Scavenging Ooze', 'subtype': ['Ooze'], 'toughness': 2}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c247145(card.Card):
    "Troll Ascetic"
    def __init__(self):
        super(c247145, self).__init__(gameobject.Characteristics(**{'color': ['G'], 'text': "Hexproof (This creature can't be the target of spells or abilities your opponents control.)\n{1}{G}: Regenerate Troll Ascetic.", 'power': 3, 'mana_cost': '1GG', 'name': 'Troll Ascetic', 'subtype': ['Troll', 'Shaman'], 'toughness': 2}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Hexproof]))

class c247276(card.Card):
    "Electrolyze"
    def __init__(self):
        super(c247276, self).__init__(gameobject.Characteristics(**{'color': ['U', 'R'], 'name': 'Electrolyze', 'text': 'Electrolyze deals 2 damage divided as you choose among one or two target creatures and/or players.\nDraw a card.', 'mana_cost': '1UR'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c247373(card.Card):
    "Boros Signet"
    def __init__(self):
        super(c247373, self).__init__(gameobject.Characteristics(**{'color': ['R', 'W'], 'name': 'Boros Signet', 'text': '{1}, {T}: Add {R}{W} to your mana pool.', 'mana_cost': '2'}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c247377(card.Card):
    "Dimir Signet"
    def __init__(self):
        super(c247377, self).__init__(gameobject.Characteristics(**{'color': ['U', 'B'], 'name': 'Dimir Signet', 'text': '{1}, {T}: Add {U}{B} to your mana pool.', 'mana_cost': '2'}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c247381(card.Card):
    "Golgari Signet"
    def __init__(self):
        super(c247381, self).__init__(gameobject.Characteristics(**{'color': ['B', 'G'], 'name': 'Golgari Signet', 'text': '{1}, {T}: Add {B}{G} to your mana pool.', 'mana_cost': '2'}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c247277(card.Card):
    "Gruul Signet"
    def __init__(self):
        super(c247277, self).__init__(gameobject.Characteristics(**{'color': ['R', 'G'], 'name': 'Gruul Signet', 'text': '{1}, {T}: Add {R}{G} to your mana pool.', 'mana_cost': '2'}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c247281(card.Card):
    "Izzet Signet"
    def __init__(self):
        super(c247281, self).__init__(gameobject.Characteristics(**{'color': ['U', 'R'], 'name': 'Izzet Signet', 'text': '{1}, {T}: Add {U}{R} to your mana pool.', 'mana_cost': '2'}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c247285(card.Card):
    "Orzhov Signet"
    def __init__(self):
        super(c247285, self).__init__(gameobject.Characteristics(**{'color': ['W', 'B'], 'name': 'Orzhov Signet', 'text': '{1}, {T}: Add {W}{B} to your mana pool.', 'mana_cost': '2'}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c247193(card.Card):
    "Rakdos Signet"
    def __init__(self):
        super(c247193, self).__init__(gameobject.Characteristics(**{'color': ['B', 'R'], 'name': 'Rakdos Signet', 'text': '{1}, {T}: Add {B}{R} to your mana pool.', 'mana_cost': '2'}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c247388(card.Card):
    "Selesnya Signet"
    def __init__(self):
        super(c247388, self).__init__(gameobject.Characteristics(**{'color': ['G', 'W'], 'name': 'Selesnya Signet', 'text': '{1}, {T}: Add {G}{W} to your mana pool.', 'mana_cost': '2'}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c247195(card.Card):
    "Simic Signet"
    def __init__(self):
        super(c247195, self).__init__(gameobject.Characteristics(**{'color': ['G', 'U'], 'name': 'Simic Signet', 'text': '{1}, {T}: Add {G}{U} to your mana pool.', 'mana_cost': '2'}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c247201(card.Card):
    "Skullclamp"
    def __init__(self):
        super(c247201, self).__init__(gameobject.Characteristics(**{'color': '', 'name': 'Skullclamp', 'subtype': ['Equipment'], 'text': 'Equipped creature gets +1/-1.\nWhenever equipped creature dies, draw two cards.\nEquip {1}', 'mana_cost': '1'}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c247340(card.Card):
    "Solemn Simulacrum"
    def __init__(self):
        super(c247340, self).__init__(gameobject.Characteristics(**{'color': '', 'text': 'When Solemn Simulacrum enters the battlefield, you may search your library for a basic land card, put that card onto the battlefield tapped, then shuffle your library.\nWhen Solemn Simulacrum dies, you may draw a card.', 'power': 2, 'mana_cost': '4', 'name': 'Solemn Simulacrum', 'subtype': ['Golem'], 'toughness': 2}, supertype=[], types=[cardtype.CardType.ARTIFACT, cardtype.CardType.CREATURE], abilities=[]))

class c234706(card.Card):
    "Grim Lavamancer"
    def __init__(self):
        super(c234706, self).__init__(gameobject.Characteristics(**{'color': ['R'], 'text': '{R}, {T}, Exile two cards from your graveyard: Grim Lavamancer deals 2 damage to target creature or player.', 'power': 1, 'mana_cost': 'R', 'name': 'Grim Lavamancer', 'subtype': ['Human', 'Wizard'], 'toughness': 1}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c236456(card.Card):
    "Figure of Destiny"
    def __init__(self):
        super(c236456, self).__init__(gameobject.Characteristics(**{'color': ['W', 'R'], 'text': '{R/W}: Figure of Destiny becomes a Kithkin Spirit with base power and toughness 2/2.\n{R/W}{R/W}{R/W}: If Figure of Destiny is a Spirit, it becomes a Kithkin Spirit Warrior with base power and toughness 4/4.\n{R/W}{R/W}{R/W}{R/W}{R/W}{R/W}: If Figure of Destiny is a Warrior, it becomes a Kithkin Spirit Warrior Avatar with base power and toughness 8/8, flying, and first strike.', 'power': 1, 'mana_cost': 'R/W', 'name': 'Figure of Destiny', 'subtype': ['Kithkin'], 'toughness': 1}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Flying]))

class c234709(card.Card):
    "Keldon Marauders"
    def __init__(self):
        super(c234709, self).__init__(gameobject.Characteristics(**{'color': ['R'], 'text': 'Vanishing 2 (This creature enters the battlefield with two time counters on it. At the beginning of your upkeep, remove a time counter from it. When the last is removed, sacrifice it.)\nWhen Keldon Marauders enters the battlefield or leaves the battlefield, it deals 1 damage to target player.', 'power': 3, 'mana_cost': '1R', 'name': 'Keldon Marauders', 'subtype': ['Human', 'Warrior'], 'toughness': 3}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c217977(card.Card):
    "Chain Lightning"
    def __init__(self):
        super(c217977, self).__init__(gameobject.Characteristics(**{'color': ['R'], 'name': 'Chain Lightning', 'text': "Chain Lightning deals 3 damage to target creature or player. Then that player or that creature's controller may pay {R}{R}. If the player does, he or she may copy this spell and may choose a new target for that copy.", 'mana_cost': 'R'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c234736(card.Card):
    "Fireblast"
    def __init__(self):
        super(c234736, self).__init__(gameobject.Characteristics(**{'color': ['R'], 'name': 'Fireblast', 'text': "You may sacrifice two Mountains rather than pay Fireblast's mana cost.\nFireblast deals 4 damage to target creature or player.", 'mana_cost': '4RR'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c382187(card.Card):
    "Inquisition of Kozilek"
    def __init__(self):
        super(c382187, self).__init__(gameobject.Characteristics(**{'color': ['B'], 'name': 'Inquisition of Kozilek', 'text': 'Target player reveals his or her hand. You choose a nonland card from it with converted mana cost 3 or less. That player discards that card.', 'mana_cost': 'B'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c382196(card.Card):
    "Shrine of Loyal Legions"
    def __init__(self):
        super(c382196, self).__init__(gameobject.Characteristics(**{'color': '', 'name': 'Shrine of Loyal Legions', 'text': 'At the beginning of your upkeep or whenever you cast a white spell, put a charge counter on Shrine of Loyal Legions.\n{3}, {T}, Sacrifice Shrine of Loyal Legions: Create a 1/1 colorless Myr artifact creature token for each charge counter on Shrine of Loyal Legions.', 'mana_cost': '2'}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c382204(card.Card):
    "Zealous Persecution"
    def __init__(self):
        super(c382204, self).__init__(gameobject.Characteristics(**{'color': ['W', 'B'], 'name': 'Zealous Persecution', 'text': 'Until end of turn, creatures you control get +1/+1 and creatures your opponents control get -1/-1.', 'mana_cost': 'WB'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c382191(card.Card):
    "Lingering Souls"
    def __init__(self):
        super(c382191, self).__init__(gameobject.Characteristics(**{'color': ['W', 'B'], 'name': 'Lingering Souls', 'text': 'Create two 1/1 white Spirit creature tokens with flying.\nFlashback {1}{B} (You may cast this card from your graveyard for its flashback cost. Then exile it.)', 'mana_cost': '2W'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[abilities.StaticAbilities.Flash]))

class c382198(card.Card):
    "Spectral Procession"
    def __init__(self):
        super(c382198, self).__init__(gameobject.Characteristics(**{'color': ['W'], 'name': 'Spectral Procession', 'text': 'Create three 1/1 white Spirit creature tokens with flying.', 'mana_cost': '2/W2/W2/W'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c382189(card.Card):
    "Isolated Chapel"
    def __init__(self):
        super(c382189, self).__init__(gameobject.Characteristics(**{'color': ['W', 'B'], 'name': 'Isolated Chapel', 'text': 'Isolated Chapel enters the battlefield tapped unless you control a Plains or a Swamp.\n{T}: Add {W} or {B} to your mana pool.', 'mana_cost': ''}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c382202(card.Card):
    "Vault of the Archangel"
    def __init__(self):
        super(c382202, self).__init__(gameobject.Characteristics(**{'color': ['W', 'B'], 'name': 'Vault of the Archangel', 'text': '{T}: Add {C} to your mana pool.\n{2}{W}{B}, {T}: Creatures you control gain deathtouch and lifelink until end of turn.', 'mana_cost': ''}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c382182(card.Card):
    "Dismember"
    def __init__(self):
        super(c382182, self).__init__(gameobject.Characteristics(**{'color': ['B'], 'name': 'Dismember', 'text': '({B/P} can be paid with either {B} or 2 life.)\nTarget creature gets -5/-5 until end of turn.', 'mana_cost': '1B/PB/P'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c389515(card.Card):
    "Feldon of the Third Path"
    def __init__(self):
        super(c389515, self).__init__(gameobject.Characteristics(**{'color': ['R'], 'text': "{2}{R}, {T}: Create a token that's a copy of target creature card in your graveyard, except it's an artifact in addition to its other types. It gains haste. Sacrifice it at the beginning of the next end step.", 'power': 2, 'mana_cost': '1RR', 'name': 'Feldon of the Third Path', 'subtype': ['Human', 'Artificer'], 'toughness': 3}, supertype=[cardtype.SuperType.LEGENDARY], types=[cardtype.CardType.CREATURE], abilities=[]))

class c389521(card.Card):
    "Flickerwisp"
    def __init__(self):
        super(c389521, self).__init__(gameobject.Characteristics(**{'color': ['W'], 'text': "Flying\nWhen Flickerwisp enters the battlefield, exile another target permanent. Return that card to the battlefield under its owner's control at the beginning of the next end step.", 'power': 3, 'mana_cost': '1WW', 'name': 'Flickerwisp', 'subtype': ['Elemental'], 'toughness': 1}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Flying]))

class c389594(card.Card):
    "Mentor of the Meek"
    def __init__(self):
        super(c389594, self).__init__(gameobject.Characteristics(**{'color': ['W'], 'text': 'Whenever another creature with power 2 or less enters the battlefield under your control, you may pay {1}. If you do, draw a card.', 'power': 2, 'mana_cost': '2W', 'name': 'Mentor of the Meek', 'subtype': ['Human', 'Soldier'], 'toughness': 2}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c389699(card.Card):
    "Sun Titan"
    def __init__(self):
        super(c389699, self).__init__(gameobject.Characteristics(**{'color': ['W'], 'text': 'Vigilance\nWhenever Sun Titan enters the battlefield or attacks, you may return target permanent card with converted mana cost 3 or less from your graveyard to the battlefield.', 'power': 6, 'mana_cost': '4WW', 'name': 'Sun Titan', 'subtype': ['Giant'], 'toughness': 6}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Vigilance]))

class c389560(card.Card):
    "Into the Roil"
    def __init__(self):
        super(c389560, self).__init__(gameobject.Characteristics(**{'color': ['U'], 'name': 'Into the Roil', 'text': "Kicker {1}{U} (You may pay an additional {1}{U} as you cast this spell.)\nReturn target nonland permanent to its owner's hand. If Into the Roil was kicked, draw a card.", 'mana_cost': '1U'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c389422(card.Card):
    "Abyssal Persecutor"
    def __init__(self):
        super(c389422, self).__init__(gameobject.Characteristics(**{'color': ['B'], 'text': "Flying, trample\nYou can't win the game and your opponents can't lose the game.", 'power': 6, 'mana_cost': '2BB', 'name': 'Abyssal Persecutor', 'subtype': ['Demon'], 'toughness': 6}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Flying, abilities.StaticAbilities.Trample]))

class c389474(card.Card):
    "Crypt Ghast"
    def __init__(self):
        super(c389474, self).__init__(gameobject.Characteristics(**{'color': ['B'], 'text': 'Extort (Whenever you cast a spell, you may pay {W/B}. If you do, each opponent loses 1 life and you gain that much life.)\nWhenever you tap a Swamp for mana, add {B} to your mana pool (in addition to the mana the land produces).', 'power': 2, 'mana_cost': '3B', 'name': 'Crypt Ghast', 'subtype': ['Spirit'], 'toughness': 2}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c389540(card.Card):
    "Grave Titan"
    def __init__(self):
        super(c389540, self).__init__(gameobject.Characteristics(**{'color': ['B'], 'text': 'Deathtouch\nWhenever Grave Titan enters the battlefield or attacks, create two 2/2 black Zombie creature tokens.', 'power': 6, 'mana_cost': '4BB', 'name': 'Grave Titan', 'subtype': ['Giant'], 'toughness': 6}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Deathtouch]))

class c389541(card.Card):
    "Gray Merchant of Asphodel"
    def __init__(self):
        super(c389541, self).__init__(gameobject.Characteristics(**{'color': ['B'], 'text': 'When Gray Merchant of Asphodel enters the battlefield, each opponent loses X life, where X is your devotion to black. You gain life equal to the life lost this way. (Each {B} in the mana costs of permanents you control counts toward your devotion to black.)', 'power': 2, 'mana_cost': '3BB', 'name': 'Gray Merchant of Asphodel', 'subtype': ['Zombie'], 'toughness': 4}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c389615(card.Card):
    "Nekrataal"
    def __init__(self):
        super(c389615, self).__init__(gameobject.Characteristics(**{'color': ['B'], 'text': "First strike\nWhen Nekrataal enters the battlefield, destroy target nonartifact, nonblack creature. That creature can't be regenerated.", 'power': 2, 'mana_cost': '2BB', 'name': 'Nekrataal', 'subtype': ['Human', 'Assassin'], 'toughness': 1}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c389675(card.Card):
    "Skirsdag High Priest"
    def __init__(self):
        super(c389675, self).__init__(gameobject.Characteristics(**{'color': ['B'], 'text': 'Morbid — {T}, Tap two untapped creatures you control: Create a 5/5 black Demon creature token with flying. Activate this ability only if a creature died this turn.', 'power': 1, 'mana_cost': '1B', 'name': 'Skirsdag High Priest', 'subtype': ['Human', 'Cleric'], 'toughness': 2}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c389735(card.Card):
    "Vampire Hexmage"
    def __init__(self):
        super(c389735, self).__init__(gameobject.Characteristics(**{'color': ['B'], 'text': 'First strike\nSacrifice Vampire Hexmage: Remove all counters from target permanent.', 'power': 2, 'mana_cost': 'BB', 'name': 'Vampire Hexmage', 'subtype': ['Vampire', 'Shaman'], 'toughness': 1}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c389512(card.Card):
    "Faithless Looting"
    def __init__(self):
        super(c389512, self).__init__(gameobject.Characteristics(**{'color': ['R'], 'name': 'Faithless Looting', 'text': 'Draw two cards, then discard two cards.\nFlashback {2}{R} (You may cast this card from your graveyard for its flashback cost. Then exile it.)', 'mana_cost': 'R'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[abilities.StaticAbilities.Flash]))

class c389537(card.Card):
    "Goblin Welder"
    def __init__(self):
        super(c389537, self).__init__(gameobject.Characteristics(**{'color': ['R'], 'text': "{T}: Choose target artifact a player controls and target artifact card in that player's graveyard. If both targets are still legal as this ability resolves, that player simultaneously sacrifices the artifact and returns the artifact card to the battlefield.", 'power': 1, 'mana_cost': 'R', 'name': 'Goblin Welder', 'subtype': ['Goblin', 'Artificer'], 'toughness': 1}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c389499(card.Card):
    "Elvish Mystic"
    def __init__(self):
        super(c389499, self).__init__(gameobject.Characteristics(**{'color': ['G'], 'text': '{T}: Add {G} to your mana pool.', 'power': 1, 'mana_cost': 'G', 'name': 'Elvish Mystic', 'subtype': ['Elf', 'Druid'], 'toughness': 1}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c389545(card.Card):
    "Harrow"
    def __init__(self):
        super(c389545, self).__init__(gameobject.Characteristics(**{'color': ['G'], 'name': 'Harrow', 'text': 'As an additional cost to cast Harrow, sacrifice a land.\nSearch your library for up to two basic land cards and put them onto the battlefield. Then shuffle your library.', 'mana_cost': '2G'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c389623(card.Card):
    "Overwhelming Stampede"
    def __init__(self):
        super(c389623, self).__init__(gameobject.Characteristics(**{'color': ['G'], 'name': 'Overwhelming Stampede', 'text': 'Until end of turn, creatures you control gain trample and get +X/+X, where X is the greatest power among creatures you control.', 'mana_cost': '3GG'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c389647(card.Card):
    "Rampaging Baloths"
    def __init__(self):
        super(c389647, self).__init__(gameobject.Characteristics(**{'color': ['G'], 'text': 'Trample\nLandfall — Whenever a land enters the battlefield under your control, you may create a 4/4 green Beast creature token.', 'power': 6, 'mana_cost': '4GG', 'name': 'Rampaging Baloths', 'subtype': ['Beast'], 'toughness': 6}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Trample]))

class c389651(card.Card):
    "Reclamation Sage"
    def __init__(self):
        super(c389651, self).__init__(gameobject.Characteristics(**{'color': ['G'], 'text': 'When Reclamation Sage enters the battlefield, you may destroy target artifact or enchantment.', 'power': 2, 'mana_cost': '2G', 'name': 'Reclamation Sage', 'subtype': ['Elf', 'Shaman'], 'toughness': 1}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c389506(card.Card):
    "Everflowing Chalice"
    def __init__(self):
        super(c389506, self).__init__(gameobject.Characteristics(**{'color': '', 'name': 'Everflowing Chalice', 'text': 'Multikicker {2} (You may pay an additional {2} any number of times as you cast this spell.)\nEverflowing Chalice enters the battlefield with a charge counter on it for each time it was kicked.\n{T}: Add {C} to your mana pool for each charge counter on Everflowing Chalice.', 'mana_cost': '0'}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c389575(card.Card):
    "Lashwrithe"
    def __init__(self):
        super(c389575, self).__init__(gameobject.Characteristics(**{'color': ['B'], 'name': 'Lashwrithe', 'subtype': ['Equipment'], 'text': 'Living weapon (When this Equipment enters the battlefield, create a 0/0 black Germ creature token, then attach this to it.)\nEquipped creature gets +1/+1 for each Swamp you control.\nEquip {B/P}{B/P} ({B/P} can be paid with either {B} or 2 life.)', 'mana_cost': '4'}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c389583(card.Card):
    "Loxodon Warhammer"
    def __init__(self):
        super(c389583, self).__init__(gameobject.Characteristics(**{'color': '', 'name': 'Loxodon Warhammer', 'subtype': ['Equipment'], 'text': 'Equipped creature gets +3/+0 and has trample and lifelink.\nEquip {3}', 'mana_cost': '3'}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c389596(card.Card):
    "Mind Stone"
    def __init__(self):
        super(c389596, self).__init__(gameobject.Characteristics(**{'color': '', 'name': 'Mind Stone', 'text': '{T}: Add {C} to your mana pool.\n{1}, {T}, Sacrifice Mind Stone: Draw a card.', 'mana_cost': '2'}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c389608(card.Card):
    "Myr Battlesphere"
    def __init__(self):
        super(c389608, self).__init__(gameobject.Characteristics(**{'color': '', 'text': 'When Myr Battlesphere enters the battlefield, create four 1/1 colorless Myr artifact creature tokens.\nWhenever Myr Battlesphere attacks, you may tap X untapped Myr you control. If you do, Myr Battlesphere gets +X/+0 until end of turn and deals X damage to defending player.', 'power': 4, 'mana_cost': '7', 'name': 'Myr Battlesphere', 'subtype': ['Myr', 'Construct'], 'toughness': 7}, supertype=[], types=[cardtype.CardType.ARTIFACT, cardtype.CardType.CREATURE], abilities=[]))

class c389609(card.Card):
    "Myr Retriever"
    def __init__(self):
        super(c389609, self).__init__(gameobject.Characteristics(**{'color': '', 'text': 'When Myr Retriever dies, return another target artifact card from your graveyard to your hand.', 'power': 1, 'mana_cost': '2', 'name': 'Myr Retriever', 'subtype': ['Myr'], 'toughness': 1}, supertype=[], types=[cardtype.CardType.ARTIFACT, cardtype.CardType.CREATURE], abilities=[]))

class c389632(card.Card):
    "Pilgrim's Eye"
    def __init__(self):
        super(c389632, self).__init__(gameobject.Characteristics(**{'color': '', 'text': "Flying\nWhen Pilgrim's Eye enters the battlefield, you may search your library for a basic land card, reveal it, put it into your hand, then shuffle your library.", 'power': 1, 'mana_cost': '3', 'name': "Pilgrim's Eye", 'subtype': ['Thopter'], 'toughness': 1}, supertype=[], types=[cardtype.CardType.ARTIFACT, cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Flying]))

class c389754(card.Card):
    "Worn Powerstone"
    def __init__(self):
        super(c389754, self).__init__(gameobject.Characteristics(**{'color': '', 'name': 'Worn Powerstone', 'text': 'Worn Powerstone enters the battlefield tapped.\n{T}: Add {C}{C} to your mana pool.', 'mana_cost': '3'}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c389756(card.Card):
    "Wurmcoil Engine"
    def __init__(self):
        super(c389756, self).__init__(gameobject.Characteristics(**{'color': '', 'text': 'Deathtouch, lifelink\nWhen Wurmcoil Engine dies, create a 3/3 colorless Wurm artifact creature token with deathtouch and a 3/3 colorless Wurm artifact creature token with lifelink.', 'power': 6, 'mana_cost': '6', 'name': 'Wurmcoil Engine', 'subtype': ['Wurm'], 'toughness': 6}, supertype=[], types=[cardtype.CardType.ARTIFACT, cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Deathtouch, abilities.StaticAbilities.Lifelink]))

class c426836(card.Card):
    "Glorybringer"
    def __init__(self):
        super(c426836, self).__init__(gameobject.Characteristics(**{'color': ['R'], 'text': "Flying, haste\nYou may exert Glorybringer as it attacks. When you do, it deals 4 damage to target non-Dragon creature an opponent controls. (An exerted creature won't untap during your next untap step.)", 'power': 4, 'mana_cost': '3RR', 'name': 'Glorybringer', 'subtype': ['Dragon'], 'toughness': 4}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Flying, abilities.StaticAbilities.Haste]))

class c426837(card.Card):
    "Harsh Mentor"
    def __init__(self):
        super(c426837, self).__init__(gameobject.Characteristics(**{'color': ['R'], 'text': "Whenever an opponent activates an ability of an artifact, creature, or land on the battlefield, if it isn't a mana ability, Harsh Mentor deals 2 damage to that player.", 'power': 2, 'mana_cost': '1R', 'name': 'Harsh Mentor', 'subtype': ['Human', 'Cleric'], 'toughness': 2}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c426851(card.Card):
    "Sweltering Suns"
    def __init__(self):
        super(c426851, self).__init__(gameobject.Characteristics(**{'color': ['R'], 'name': 'Sweltering Suns', 'text': 'Sweltering Suns deals 3 damage to each creature.\nCycling {3} ({3}, Discard this card: Draw a card.)', 'mana_cost': '1RR'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c426906(card.Card):
    "Nissa, Steward of Elements"
    def __init__(self):
        super(c426906, self).__init__(gameobject.Characteristics(**{'color': ['U', 'G'], 'name': 'Nissa, Steward of Elements', 'subtype': ['Nissa'], 'text': "+2: Scry 2.\n0: Look at the top card of your library. If it's a land card or a creature card with converted mana cost less than or equal to the number of loyalty counters on Nissa, Steward of Elements, you may put that card onto the battlefield.\n−6: Untap up to two target lands you control. They become 5/5 Elemental creatures with flying and haste until end of turn. They're still lands.", 'mana_cost': 'XGU'}, supertype=[], types=[cardtype.CardType.PLANESWALKER], abilities=[]))

class c426907(card.Card):
    "Samut, Voice of Dissent"
    def __init__(self):
        super(c426907, self).__init__(gameobject.Characteristics(**{'color': ['R', 'G', 'W'], 'text': 'Flash\nDouble strike, vigilance, haste\nOther creatures you control have haste.\n{W}, {T}: Untap another target creature.', 'power': 3, 'mana_cost': '3RG', 'name': 'Samut, Voice of Dissent', 'subtype': ['Human', 'Warrior'], 'toughness': 4}, supertype=[cardtype.SuperType.LEGENDARY], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Flash, abilities.StaticAbilities.Haste, abilities.StaticAbilities.Vigilance]))

class c426936(card.Card):
    "Oracle's Vault"
    def __init__(self):
        super(c426936, self).__init__(gameobject.Characteristics(**{'color': '', 'name': "Oracle's Vault", 'text': "{2}, {T}: Exile the top card of your library. Until end of turn, you may play that card. Put a brick counter on Oracle's Vault.\n{T}: Exile the top card of your library. Until end of turn, you may play that card without paying its mana cost. Activate this ability only if there are three or more brick counters on Oracle's Vault.", 'mana_cost': '4'}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c409784(card.Card):
    "Thraben Inspector"
    def __init__(self):
        super(c409784, self).__init__(gameobject.Characteristics(**{'color': ['W'], 'text': 'When Thraben Inspector enters the battlefield, investigate. (Create a colorless Clue artifact token with "{2}, Sacrifice this artifact: Draw a card.")', 'power': 1, 'mana_cost': 'W', 'name': 'Thraben Inspector', 'subtype': ['Human', 'Soldier'], 'toughness': 2}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c409831(card.Card):
    "Startled Awake"
    def __init__(self):
        super(c409831, self).__init__(gameobject.Characteristics(**{'color': ['U'], 'name': 'Startled Awake', 'text': 'Target opponent puts the top thirteen cards of his or her library into his or her graveyard.\n{3}{U}{U}: Put Startled Awake from your graveyard onto the battlefield transformed. Activate this ability only any time you could cast a sorcery.', 'mana_cost': '2UU'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c409836(card.Card):
    "Thing in the Ice"
    def __init__(self):
        super(c409836, self).__init__(gameobject.Characteristics(**{'color': ['U'], 'text': 'Defender\nThing in the Ice enters the battlefield with four ice counters on it.\nWhenever you cast an instant or sorcery spell, remove an ice counter from Thing in the Ice. Then if it has no ice counters on it, transform it.', 'power': 0, 'mana_cost': '1U', 'name': 'Thing in the Ice', 'subtype': ['Horror'], 'toughness': 4}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Defender]))

class c409855(card.Card):
    "Elusive Tormentor"
    def __init__(self):
        super(c409855, self).__init__(gameobject.Characteristics(**{'color': ['U', 'B'], 'text': '{1}, Discard a card: Transform Elusive Tormentor.', 'power': 4, 'mana_cost': '2BB', 'name': 'Elusive Tormentor', 'subtype': ['Vampire', 'Wizard'], 'toughness': 4}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c409907(card.Card):
    "Falkenrath Gorger"
    def __init__(self):
        super(c409907, self).__init__(gameobject.Characteristics(**{'color': ['R'], 'text': "Each Vampire creature card you own that isn't on the battlefield has madness. The madness cost is equal to its mana cost. (If you discard a card with madness, discard it into exile. When you do, cast it for its madness cost or put it into your graveyard.)", 'power': 2, 'mana_cost': 'R', 'name': 'Falkenrath Gorger', 'subtype': ['Vampire', 'Berserker'], 'toughness': 1}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c409997(card.Card):
    "Tireless Tracker"
    def __init__(self):
        super(c409997, self).__init__(gameobject.Characteristics(**{'color': ['G'], 'text': 'Whenever a land enters the battlefield under your control, investigate. (Create a colorless Clue artifact token with "{2}, Sacrifice this artifact: Draw a card.")\nWhenever you sacrifice a Clue, put a +1/+1 counter on Tireless Tracker.', 'power': 3, 'mana_cost': '2G', 'name': 'Tireless Tracker', 'subtype': ['Human', 'Scout'], 'toughness': 2}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c409998(card.Card):
    "Traverse the Ulvenwald"
    def __init__(self):
        super(c409998, self).__init__(gameobject.Characteristics(**{'color': ['G'], 'name': 'Traverse the Ulvenwald', 'text': 'Search your library for a basic land card, reveal it, put it into your hand, then shuffle your library.\nDelirium — If there are four or more card types among cards in your graveyard, instead search your library for a creature or land card, reveal it, put it into your hand, then shuffle your library.', 'mana_cost': 'G'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c410000(card.Card):
    "Ulvenwald Mysteries"
    def __init__(self):
        super(c410000, self).__init__(gameobject.Characteristics(**{'color': ['G'], 'name': 'Ulvenwald Mysteries', 'text': 'Whenever a nontoken creature you control dies, investigate. (Create a colorless Clue artifact token with "{2}, Sacrifice this artifact: Draw a card.")\nWhenever you sacrifice a Clue, create a 1/1 white Human Soldier creature token.', 'mana_cost': '2G'}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c410006(card.Card):
    "Anguished Unmaking"
    def __init__(self):
        super(c410006, self).__init__(gameobject.Characteristics(**{'color': ['W', 'B'], 'name': 'Anguished Unmaking', 'text': 'Exile target nonland permanent. You lose 3 life.', 'mana_cost': '1WB'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c410032(card.Card):
    "Tamiyo's Journal"
    def __init__(self):
        super(c410032, self).__init__(gameobject.Characteristics(**{'color': '', 'name': "Tamiyo's Journal", 'text': 'At the beginning of your upkeep, investigate. (Create a colorless Clue artifact token with "{2}, Sacrifice this artifact: Draw a card.")\n{T}, Sacrifice three Clues: Search your library for a card and put that card into your hand. Then shuffle your library.', 'mana_cost': '5'}, supertype=[cardtype.SuperType.LEGENDARY], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c410049(card.Card):
    "Westvale Abbey"
    def __init__(self):
        super(c410049, self).__init__(gameobject.Characteristics(**{'color': ['B'], 'name': 'Westvale Abbey', 'text': '{T}: Add {C} to your mana pool.\n{5}, {T}, Pay 1 life: Create a 1/1 white and black Human Cleric creature token.\n{5}, {T}, Sacrifice five creatures: Transform Westvale Abbey, then untap it.', 'mana_cost': ''}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c5182(card.Card):
    "Mana Leak"
    def __init__(self):
        super(c5182, self).__init__(gameobject.Characteristics(**{'color': ['U'], 'name': 'Mana Leak', 'text': 'Counter target spell unless its controller pays {3}.', 'mana_cost': '1U'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c83483(card.Card):
    "Wildfire"
    def __init__(self):
        super(c83483, self).__init__(gameobject.Characteristics(**{'color': ['R'], 'name': 'Wildfire', 'text': 'Each player sacrifices four lands. Wildfire deals 4 damage to each creature.', 'mana_cost': '4RR'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c84443(card.Card):
    "Battlefield Forge"
    def __init__(self):
        super(c84443, self).__init__(gameobject.Characteristics(**{'color': ['R', 'W'], 'name': 'Battlefield Forge', 'text': '{T}: Add {C} to your mana pool.\n{T}: Add {R} or {W} to your mana pool. Battlefield Forge deals 1 damage to you.', 'mana_cost': ''}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c84559(card.Card):
    "Karplusan Forest"
    def __init__(self):
        super(c84559, self).__init__(gameobject.Characteristics(**{'color': ['R', 'G'], 'name': 'Karplusan Forest', 'text': '{T}: Add {C} to your mana pool.\n{T}: Add {R} or {G} to your mana pool. Karplusan Forest deals 1 damage to you.', 'mana_cost': ''}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c84457(card.Card):
    "Shivan Reef"
    def __init__(self):
        super(c84457, self).__init__(gameobject.Characteristics(**{'color': ['U', 'R'], 'name': 'Shivan Reef', 'text': '{T}: Add {C} to your mana pool.\n{T}: Add {U} or {R} to your mana pool. Shivan Reef deals 1 damage to you.', 'mana_cost': ''}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c84566(card.Card):
    "Underground River"
    def __init__(self):
        super(c84566, self).__init__(gameobject.Characteristics(**{'color': ['U', 'B'], 'name': 'Underground River', 'text': '{T}: Add {C} to your mana pool.\n{T}: Add {U} or {B} to your mana pool. Underground River deals 1 damage to you.', 'mana_cost': ''}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c394079(card.Card):
    "Mastery of the Unseen"
    def __init__(self):
        super(c394079, self).__init__(gameobject.Characteristics(**{'color': ['W'], 'name': 'Mastery of the Unseen', 'text': "Whenever a permanent you control is turned face up, you gain 1 life for each creature you control.\n{3}{W}: Manifest the top card of your library. (Put it onto the battlefield face down as a 2/2 creature. Turn it face up any time for its mana cost if it's a creature card.)", 'mana_cost': '1W'}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c394075(card.Card):
    "Grim Haruspex"
    def __init__(self):
        super(c394075, self).__init__(gameobject.Characteristics(**{'color': ['B'], 'text': 'Morph {B} (You may cast this card face down as a 2/2 creature for {3}. Turn it face up any time for its morph cost.)\nWhenever another nontoken creature you control dies, draw a card.', 'power': 3, 'mana_cost': '2B', 'name': 'Grim Haruspex', 'subtype': ['Human', 'Wizard'], 'toughness': 2}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c96923(card.Card):
    "Steam Vents"
    def __init__(self):
        super(c96923, self).__init__(gameobject.Characteristics(**{'color': ['U', 'R'], 'name': 'Steam Vents', 'subtype': ['Island', 'Mountain'], 'text': "({T}: Add {U} or {R} to your mana pool.)\nAs Steam Vents enters the battlefield, you may pay 2 life. If you don't, Steam Vents enters the battlefield tapped.", 'mana_cost': ''}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c96896(card.Card):
    "Stomping Ground"
    def __init__(self):
        super(c96896, self).__init__(gameobject.Characteristics(**{'color': ['R', 'G'], 'name': 'Stomping Ground', 'subtype': ['Mountain', 'Forest'], 'text': "({T}: Add {R} or {G} to your mana pool.)\nAs Stomping Ground enters the battlefield, you may pay 2 life. If you don't, Stomping Ground enters the battlefield tapped.", 'mana_cost': ''}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c420595(card.Card):
    "Chromatic Lantern"
    def __init__(self):
        super(c420595, self).__init__(gameobject.Characteristics(**{'color': '', 'name': 'Chromatic Lantern', 'text': 'Lands you control have "{T}: Add one mana of any color to your mana pool."\n{T}: Add one mana of any color to your mana pool.', 'mana_cost': '3'}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c420600(card.Card):
    "Hangarback Walker"
    def __init__(self):
        super(c420600, self).__init__(gameobject.Characteristics(**{'color': '', 'text': 'Hangarback Walker enters the battlefield with X +1/+1 counters on it.\nWhen Hangarback Walker dies, create a 1/1 colorless Thopter artifact creature token with flying for each +1/+1 counter on Hangarback Walker.\n{1}, {T}: Put a +1/+1 counter on Hangarback Walker.', 'power': 0, 'mana_cost': 'XX', 'name': 'Hangarback Walker', 'subtype': ['Construct'], 'toughness': 0}, supertype=[], types=[cardtype.CardType.ARTIFACT, cardtype.CardType.CREATURE], abilities=[]))

class c420616(card.Card):
    "Sword of Fire and Ice"
    def __init__(self):
        super(c420616, self).__init__(gameobject.Characteristics(**{'color': '', 'name': 'Sword of Fire and Ice', 'subtype': ['Equipment'], 'text': 'Equipped creature gets +2/+2 and has protection from red and from blue.\nWhenever equipped creature deals combat damage to a player, Sword of Fire and Ice deals 2 damage to target creature or player and you draw a card.\nEquip {2}', 'mana_cost': '3'}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c425822(card.Card):
    "Sword of War and Peace"
    def __init__(self):
        super(c425822, self).__init__(gameobject.Characteristics(**{'color': '', 'name': 'Sword of War and Peace', 'subtype': ['Equipment'], 'text': 'Equipped creature gets +2/+2 and has protection from red and from white.\nWhenever equipped creature deals combat damage to a player, Sword of War and Peace deals damage to that player equal to the number of cards in his or her hand and you gain 1 life for each card in your hand.\nEquip {2}', 'mana_cost': '3'}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c425824(card.Card):
    "Vedalken Shackles"
    def __init__(self):
        super(c425824, self).__init__(gameobject.Characteristics(**{'color': '', 'name': 'Vedalken Shackles', 'text': 'You may choose not to untap Vedalken Shackles during your untap step.\n{2}, {T}: Gain control of target creature with power less than or equal to the number of Islands you control for as long as Vedalken Shackles remains tapped.', 'mana_cost': '3'}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c48(card.Card):
    "Animate Dead"
    def __init__(self):
        super(c48, self).__init__(gameobject.Characteristics(**{'color': ['B'], 'name': 'Animate Dead', 'subtype': ['Aura'], 'text': 'Enchant creature card in a graveyard\nWhen Animate Dead enters the battlefield, if it\'s on the battlefield, it loses "enchant creature card in a graveyard" and gains "enchant creature put onto the battlefield with Animate Dead." Return enchanted creature card to the battlefield under your control and attach Animate Dead to it. When Animate Dead leaves the battlefield, that creature\'s controller sacrifices it.\nEnchanted creature gets -1/-0.', 'mana_cost': '1B'}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c234(card.Card):
    "Balance"
    def __init__(self):
        super(c234, self).__init__(gameobject.Characteristics(**{'color': ['W'], 'name': 'Balance', 'text': 'Each player chooses a number of lands he or she controls equal to the number of lands controlled by the player who controls the fewest, then sacrifices the rest. Players discard cards and sacrifice creatures the same way.', 'mana_cost': '1W'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c144(card.Card):
    "Channel"
    def __init__(self):
        super(c144, self).__init__(gameobject.Characteristics(**{'color': ['G'], 'name': 'Channel', 'text': 'Until end of turn, any time you could activate a mana ability, you may pay 1 life. If you do, add {C} to your mana pool.', 'mana_cost': 'GG'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c100(card.Card):
    "Control Magic"
    def __init__(self):
        super(c100, self).__init__(gameobject.Characteristics(**{'color': ['U'], 'name': 'Control Magic', 'subtype': ['Aura'], 'text': 'Enchant creature\nYou control enchanted creature.', 'mana_cost': '2UU'}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c102(card.Card):
    "Counterspell"
    def __init__(self):
        super(c102, self).__init__(gameobject.Characteristics(**{'color': ['U'], 'name': 'Counterspell', 'text': 'Counter target spell.', 'mana_cost': 'UU'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c54(card.Card):
    "Dark Ritual"
    def __init__(self):
        super(c54, self).__init__(gameobject.Characteristics(**{'color': ['B'], 'name': 'Dark Ritual', 'text': 'Add {B}{B}{B} to your mana pool.', 'mana_cost': 'B'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c249(card.Card):
    "Disenchant"
    def __init__(self):
        super(c249, self).__init__(gameobject.Characteristics(**{'color': ['W'], 'name': 'Disenchant', 'text': 'Destroy target artifact or enchantment.', 'mana_cost': '1W'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c170(card.Card):
    "Regrowth"
    def __init__(self):
        super(c170, self).__init__(gameobject.Characteristics(**{'color': ['G'], 'name': 'Regrowth', 'text': 'Return target card from your graveyard to your hand.', 'mana_cost': '1G'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c85(card.Card):
    "Sinkhole"
    def __init__(self):
        super(c85, self).__init__(gameobject.Characteristics(**{'color': ['B'], 'name': 'Sinkhole', 'text': 'Destroy target land.', 'mana_cost': 'BB'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c271(card.Card):
    "Swords to Plowshares"
    def __init__(self):
        super(c271, self).__init__(gameobject.Characteristics(**{'color': ['W'], 'name': 'Swords to Plowshares', 'text': 'Exile target creature. Its controller gains life equal to its power.', 'mana_cost': 'W'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c46(card.Card):
    "Winter Orb"
    def __init__(self):
        super(c46, self).__init__(gameobject.Characteristics(**{'color': '', 'name': 'Winter Orb', 'text': "As long as Winter Orb is untapped, players can't untap more than one land during their untap steps.", 'mana_cost': '2'}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c79090(card.Card):
    "Gifts Ungiven"
    def __init__(self):
        super(c79090, self).__init__(gameobject.Characteristics(**{'color': ['U'], 'name': 'Gifts Ungiven', 'text': 'Search your library for up to four cards with different names and reveal them. Target opponent chooses two of those cards. Put the chosen cards into your graveyard and the rest into your hand. Then shuffle your library.', 'mana_cost': '3U'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c75268(card.Card):
    "Meloku the Clouded Mirror"
    def __init__(self):
        super(c75268, self).__init__(gameobject.Characteristics(**{'color': ['U'], 'text': "Flying\n{1}, Return a land you control to its owner's hand: Create a 1/1 blue Illusion creature token with flying.", 'power': 2, 'mana_cost': '4U', 'name': 'Meloku the Clouded Mirror', 'subtype': ['Moonfolk', 'Wizard'], 'toughness': 4}, supertype=[cardtype.SuperType.LEGENDARY], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Flying]))

class c50321(card.Card):
    "Kiki-Jiki, Mirror Breaker"
    def __init__(self):
        super(c50321, self).__init__(gameobject.Characteristics(**{'color': ['R'], 'text': "Haste\n{T}: Create a token that's a copy of target nonlegendary creature you control. That token has haste. Sacrifice it at the beginning of the next end step.", 'power': 2, 'mana_cost': '2RRR', 'name': 'Kiki-Jiki, Mirror Breaker', 'subtype': ['Goblin', 'Shaman'], 'toughness': 2}, supertype=[cardtype.SuperType.LEGENDARY], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Haste]))

class c220547(card.Card):
    "Torrent of Souls"
    def __init__(self):
        super(c220547, self).__init__(gameobject.Characteristics(**{'color': ['B', 'R'], 'name': 'Torrent of Souls', 'text': 'Return up to one target creature card from your graveyard to the battlefield if {B} was spent to cast Torrent of Souls. Creatures target player controls get +2/+0 and gain haste until end of turn if {R} was spent to cast Torrent of Souls. (Do both if {B}{R} was spent.)', 'mana_cost': '4B/R'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c220540(card.Card):
    "Azorius Signet"
    def __init__(self):
        super(c220540, self).__init__(gameobject.Characteristics(**{'color': ['W', 'U'], 'name': 'Azorius Signet', 'text': '{1}, {T}: Add {W}{U} to your mana pool.', 'mana_cost': '2'}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c220536(card.Card):
    "Lodestone Golem"
    def __init__(self):
        super(c220536, self).__init__(gameobject.Characteristics(**{'color': '', 'text': 'Nonartifact spells cost {1} more to cast.', 'power': 5, 'mana_cost': '4', 'name': 'Lodestone Golem', 'subtype': ['Golem'], 'toughness': 3}, supertype=[], types=[cardtype.CardType.ARTIFACT, cardtype.CardType.CREATURE], abilities=[]))

class c21284(card.Card):
    "Daze"
    def __init__(self):
        super(c21284, self).__init__(gameobject.Characteristics(**{'color': ['U'], 'name': 'Daze', 'text': "You may return an Island you control to its owner's hand rather than pay Daze's mana cost.\nCounter target spell unless its controller pays {1}.", 'mana_cost': '1U'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c21399(card.Card):
    "Tangle Wire"
    def __init__(self):
        super(c21399, self).__init__(gameobject.Characteristics(**{'color': '', 'name': 'Tangle Wire', 'text': "Fading 4 (This artifact enters the battlefield with four fade counters on it. At the beginning of your upkeep, remove a fade counter from it. If you can't, sacrifice it.)\nAt the beginning of each player's upkeep, that player taps an untapped artifact, creature, or land he or she controls for each fade counter on Tangle Wire.", 'mana_cost': '3'}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c386285(card.Card):
    "Burning of Xinye"
    def __init__(self):
        super(c386285, self).__init__(gameobject.Characteristics(**{'color': ['R'], 'name': 'Burning of Xinye', 'text': 'You destroy four lands you control, then target opponent destroys four lands he or she controls. Then Burning of Xinye deals 4 damage to each creature.', 'mana_cost': '4RR'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c386286(card.Card):
    "Cataclysm"
    def __init__(self):
        super(c386286, self).__init__(gameobject.Characteristics(**{'color': ['W'], 'name': 'Cataclysm', 'text': 'Each player chooses from among the permanents he or she controls an artifact, a creature, an enchantment, and a land, then sacrifices the rest.', 'mana_cost': '2WW'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c386295(card.Card):
    "Terminus"
    def __init__(self):
        super(c386295, self).__init__(gameobject.Characteristics(**{'color': ['W'], 'name': 'Terminus', 'text': "Put all creatures on the bottom of their owners' libraries.\nMiracle {W} (You may cast this card for its miracle cost when you draw it if it's the first card you drew this turn.)", 'mana_cost': '4WW'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c386296(card.Card):
    "Upheaval"
    def __init__(self):
        super(c386296, self).__init__(gameobject.Characteristics(**{'color': ['U'], 'name': 'Upheaval', 'text': "Return all permanents to their owners' hands.", 'mana_cost': '4UU'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c122423(card.Card):
    "Damnation"
    def __init__(self):
        super(c122423, self).__init__(gameobject.Characteristics(**{'color': ['B'], 'name': 'Damnation', 'text': "Destroy all creatures. They can't be regenerated.", 'mana_cost': '2BB'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c420691(card.Card):
    "Reveillark"
    def __init__(self):
        super(c420691, self).__init__(gameobject.Characteristics(**{'color': ['W'], 'text': "Flying\nWhen Reveillark leaves the battlefield, return up to two target creature cards with power 2 or less from your graveyard to the battlefield.\nEvoke {5}{W} (You may cast this spell for its evoke cost. If you do, it's sacrificed when it enters the battlefield.)", 'power': 4, 'mana_cost': '4W', 'name': 'Reveillark', 'subtype': ['Elemental'], 'toughness': 3}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Flying]))

class c420706(card.Card):
    "Etherium Sculptor"
    def __init__(self):
        super(c420706, self).__init__(gameobject.Characteristics(**{'color': ['U'], 'text': 'Artifact spells you cast cost {1} less to cast.', 'power': 1, 'mana_cost': '1U', 'name': 'Etherium Sculptor', 'subtype': ['Vedalken', 'Artificer'], 'toughness': 2}, supertype=[], types=[cardtype.CardType.ARTIFACT, cardtype.CardType.CREATURE], abilities=[]))

class c420718(card.Card):
    "Treasure Cruise"
    def __init__(self):
        super(c420718, self).__init__(gameobject.Characteristics(**{'color': ['U'], 'name': 'Treasure Cruise', 'text': 'Delve (Each card you exile from your graveyard while casting this spell pays for {1}.)\nDraw three cards.', 'mana_cost': '7U'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c420736(card.Card):
    "Alesha, Who Smiles at Death"
    def __init__(self):
        super(c420736, self).__init__(gameobject.Characteristics(**{'color': ['R', 'W', 'B'], 'text': 'First strike\nWhenever Alesha, Who Smiles at Death attacks, you may pay {W/B}{W/B}. If you do, return target creature card with power 2 or less from your graveyard to the battlefield tapped and attacking.', 'power': 3, 'mana_cost': '2R', 'name': 'Alesha, Who Smiles at Death', 'subtype': ['Human', 'Warrior'], 'toughness': 2}, supertype=[cardtype.SuperType.LEGENDARY], types=[cardtype.CardType.CREATURE], abilities=[]))

class c420764(card.Card):
    "Den Protector"
    def __init__(self):
        super(c420764, self).__init__(gameobject.Characteristics(**{'color': ['G'], 'text': "Creatures with power less than Den Protector's power can't block it.\nMegamorph {1}{G} (You may cast this card face down as a 2/2 creature for {3}. Turn it face up any time for its megamorph cost and put a +1/+1 counter on it.)\nWhen Den Protector is turned face up, return target card from your graveyard to your hand.", 'power': 2, 'mana_cost': '1G', 'name': 'Den Protector', 'subtype': ['Human', 'Warrior'], 'toughness': 1}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c420766(card.Card):
    "Farseek"
    def __init__(self):
        super(c420766, self).__init__(gameobject.Characteristics(**{'color': ['G'], 'name': 'Farseek', 'text': 'Search your library for a Plains, Island, Swamp, or Mountain card and put it onto the battlefield tapped. Then shuffle your library.', 'mana_cost': '1G'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c420782(card.Card):
    "Satyr Wayfinder"
    def __init__(self):
        super(c420782, self).__init__(gameobject.Characteristics(**{'color': ['G'], 'text': 'When Satyr Wayfinder enters the battlefield, reveal the top four cards of your library. You may put a land card from among them into your hand. Put the rest into your graveyard.', 'power': 1, 'mana_cost': '1G', 'name': 'Satyr Wayfinder', 'subtype': ['Satyr'], 'toughness': 1}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c420798(card.Card):
    "Baleful Strix"
    def __init__(self):
        super(c420798, self).__init__(gameobject.Characteristics(**{'color': ['U', 'B'], 'text': 'Flying, deathtouch\nWhen Baleful Strix enters the battlefield, draw a card.', 'power': 1, 'mana_cost': 'UB', 'name': 'Baleful Strix', 'subtype': ['Bird'], 'toughness': 1}, supertype=[], types=[cardtype.CardType.ARTIFACT, cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Deathtouch, abilities.StaticAbilities.Flying]))

class c420801(card.Card):
    "Bloodbraid Elf"
    def __init__(self):
        super(c420801, self).__init__(gameobject.Characteristics(**{'color': ['R', 'G'], 'text': 'Haste\nCascade (When you cast this spell, exile cards from the top of your library until you exile a nonland card that costs less. You may cast it without paying its mana cost. Put the exiled cards on the bottom of your library in a random order.)', 'power': 3, 'mana_cost': '2RG', 'name': 'Bloodbraid Elf', 'subtype': ['Elf', 'Berserker'], 'toughness': 2}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Haste]))

class c420834(card.Card):
    "Putrefy"
    def __init__(self):
        super(c420834, self).__init__(gameobject.Characteristics(**{'color': ['B', 'G'], 'name': 'Putrefy', 'text': "Destroy target artifact or creature. It can't be regenerated.", 'mana_cost': '1BG'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c420837(card.Card):
    "Selvala, Explorer Returned"
    def __init__(self):
        super(c420837, self).__init__(gameobject.Characteristics(**{'color': ['W', 'G'], 'text': 'Parley — {T}: Each player reveals the top card of his or her library. For each nonland card revealed this way, add {G} to your mana pool and you gain 1 life. Then each player draws a card.', 'power': 2, 'mana_cost': '1GW', 'name': 'Selvala, Explorer Returned', 'subtype': ['Elf', 'Scout'], 'toughness': 4}, supertype=[cardtype.SuperType.LEGENDARY], types=[cardtype.CardType.CREATURE], abilities=[]))

class c420854(card.Card):
    "Thopter Foundry"
    def __init__(self):
        super(c420854, self).__init__(gameobject.Characteristics(**{'color': ['W', 'U', 'B'], 'name': 'Thopter Foundry', 'text': '{1}, Sacrifice a nontoken artifact: Create a 1/1 blue Thopter artifact creature token with flying. You gain 1 life.', 'mana_cost': 'W/BU'}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c420886(card.Card):
    "Shimmer Myr"
    def __init__(self):
        super(c420886, self).__init__(gameobject.Characteristics(**{'color': '', 'text': 'Flash\nYou may cast artifact spells as though they had flash.', 'power': 2, 'mana_cost': '3', 'name': 'Shimmer Myr', 'subtype': ['Myr'], 'toughness': 2}, supertype=[], types=[cardtype.CardType.ARTIFACT, cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Flash]))

class c426592(card.Card):
    "Young Pyromancer"
    def __init__(self):
        super(c426592, self).__init__(gameobject.Characteristics(**{'color': ['R'], 'text': 'Whenever you cast an instant or sorcery spell, create a 1/1 red Elemental creature token.', 'power': 2, 'mana_cost': '1R', 'name': 'Young Pyromancer', 'subtype': ['Human', 'Shaman'], 'toughness': 1}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c243416(card.Card):
    "Knight of the Reliquary"
    def __init__(self):
        super(c243416, self).__init__(gameobject.Characteristics(**{'color': ['W', 'G'], 'text': 'Knight of the Reliquary gets +1/+1 for each land card in your graveyard.\n{T}, Sacrifice a Forest or Plains: Search your library for a land card, put it onto the battlefield, then shuffle your library.', 'power': 2, 'mana_cost': '1GW', 'name': 'Knight of the Reliquary', 'subtype': ['Human', 'Knight'], 'toughness': 2}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c5594(card.Card):
    "Sneak Attack"
    def __init__(self):
        super(c5594, self).__init__(gameobject.Characteristics(**{'color': ['R'], 'name': 'Sneak Attack', 'text': '{R}: You may put a creature card from your hand onto the battlefield. That creature gains haste. Sacrifice the creature at the beginning of the next end step.', 'mana_cost': '3R'}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c386301(card.Card):
    "Arc Trail"
    def __init__(self):
        super(c386301, self).__init__(gameobject.Characteristics(**{'color': ['R'], 'name': 'Arc Trail', 'text': 'Arc Trail deals 2 damage to target creature or player and 1 damage to another target creature or player.', 'mana_cost': '1R'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c222707(card.Card):
    "Razormane Masticore"
    def __init__(self):
        super(c222707, self).__init__(gameobject.Characteristics(**{'color': '', 'text': 'First strike (This creature deals combat damage before creatures without first strike.)\nAt the beginning of your upkeep, sacrifice Razormane Masticore unless you discard a card.\nAt the beginning of your draw step, you may have Razormane Masticore deal 3 damage to target creature.', 'power': 5, 'mana_cost': '5', 'name': 'Razormane Masticore', 'subtype': ['Masticore'], 'toughness': 5}, supertype=[], types=[cardtype.CardType.ARTIFACT, cardtype.CardType.CREATURE], abilities=[]))

class c222711(card.Card):
    "Elixir of Immortality"
    def __init__(self):
        super(c222711, self).__init__(gameobject.Characteristics(**{'color': '', 'name': 'Elixir of Immortality', 'text': "{2}, {T}: You gain 5 life. Shuffle Elixir of Immortality and your graveyard into their owner's library.", 'mana_cost': '1'}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c218580(card.Card):
    "Thirst for Knowledge"
    def __init__(self):
        super(c218580, self).__init__(gameobject.Characteristics(**{'color': ['U'], 'name': 'Thirst for Knowledge', 'text': 'Draw three cards. Then discard two cards unless you discard an artifact card.', 'mana_cost': '2U'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c218340(card.Card):
    "Mishra's Factory"
    def __init__(self):
        super(c218340, self).__init__(gameobject.Characteristics(**{'color': '', 'name': "Mishra's Factory", 'text': "{T}: Add {C} to your mana pool.\n{1}: Mishra's Factory becomes a 2/2 Assembly-Worker artifact creature until end of turn. It's still a land.\n{T}: Target Assembly-Worker creature gets +1/+1 until end of turn.", 'mana_cost': ''}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c338456(card.Card):
    "Sylvan Library"
    def __init__(self):
        super(c338456, self).__init__(gameobject.Characteristics(**{'color': ['G'], 'name': 'Sylvan Library', 'text': 'At the beginning of your draw step, you may draw two additional cards. If you do, choose two cards in your hand drawn this turn. For each of those cards, pay 4 life or put the card on top of your library.', 'mana_cost': '1G'}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c207884(card.Card):
    "Grand Architect"
    def __init__(self):
        super(c207884, self).__init__(gameobject.Characteristics(**{'color': ['U'], 'text': 'Other blue creatures you control get +1/+1.\n{U}: Target artifact creature becomes blue until end of turn.\nTap an untapped blue creature you control: Add {C}{C} to your mana pool. Spend this mana only to cast artifact spells or activate abilities of artifacts.', 'power': 1, 'mana_cost': '1UU', 'name': 'Grand Architect', 'subtype': ['Vedalken', 'Artificer'], 'toughness': 3}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c204958(card.Card):
    "Skinrender"
    def __init__(self):
        super(c204958, self).__init__(gameobject.Characteristics(**{'color': ['B'], 'text': 'When Skinrender enters the battlefield, put three -1/-1 counters on target creature.', 'power': 3, 'mana_cost': '2BB', 'name': 'Skinrender', 'subtype': ['Zombie'], 'toughness': 3}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c215099(card.Card):
    "Etched Champion"
    def __init__(self):
        super(c215099, self).__init__(gameobject.Characteristics(**{'color': '', 'text': 'Metalcraft — Etched Champion has protection from all colors as long as you control three or more artifacts.', 'power': 2, 'mana_cost': '3', 'name': 'Etched Champion', 'subtype': ['Soldier'], 'toughness': 2}, supertype=[], types=[cardtype.CardType.ARTIFACT, cardtype.CardType.CREATURE], abilities=[]))

class c209044(card.Card):
    "Mindslaver"
    def __init__(self):
        super(c209044, self).__init__(gameobject.Characteristics(**{'color': '', 'name': 'Mindslaver', 'text': "{4}, {T}, Sacrifice Mindslaver: You control target player during that player's next turn. (You see all cards that player could see and make all decisions for the player.)", 'mana_cost': '6'}, supertype=[cardtype.SuperType.LEGENDARY], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c394490(card.Card):
    "Anafenza, Kin-Tree Spirit"
    def __init__(self):
        super(c394490, self).__init__(gameobject.Characteristics(**{'color': ['W'], 'text': 'Whenever another nontoken creature enters the battlefield under your control, bolster 1. (Choose a creature with the least toughness among creatures you control and put a +1/+1 counter on it.)', 'power': 2, 'mana_cost': 'WW', 'name': 'Anafenza, Kin-Tree Spirit', 'subtype': ['Spirit', 'Soldier'], 'toughness': 2}, supertype=[cardtype.SuperType.LEGENDARY], types=[cardtype.CardType.CREATURE], abilities=[]))

class c394597(card.Card):
    "Hidden Dragonslayer"
    def __init__(self):
        super(c394597, self).__init__(gameobject.Characteristics(**{'color': ['W'], 'text': 'Lifelink\nMegamorph {2}{W} (You may cast this card face down as a 2/2 creature for {3}. Turn it face up any time for its megamorph cost and put a +1/+1 counter on it.)\nWhen Hidden Dragonslayer is turned face up, destroy target creature with power 4 or greater an opponent controls.', 'power': 2, 'mana_cost': '1W', 'name': 'Hidden Dragonslayer', 'subtype': ['Human', 'Warrior'], 'toughness': 1}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Lifelink]))

class c394714(card.Card):
    "Stratus Dancer"
    def __init__(self):
        super(c394714, self).__init__(gameobject.Characteristics(**{'color': ['U'], 'text': 'Flying\nMegamorph {1}{U} (You may cast this card face down as a 2/2 creature for {3}. Turn it face up any time for its megamorph cost and put a +1/+1 counter on it.)\nWhen Stratus Dancer is turned face up, counter target instant or sorcery spell.', 'power': 2, 'mana_cost': '1U', 'name': 'Stratus Dancer', 'subtype': ['Djinn', 'Monk'], 'toughness': 1}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Flying]))

class c394695(card.Card):
    "Sidisi, Undead Vizier"
    def __init__(self):
        super(c394695, self).__init__(gameobject.Characteristics(**{'color': ['B'], 'text': 'Deathtouch\nExploit (When this creature enters the battlefield, you may sacrifice a creature.)\nWhen Sidisi, Undead Vizier exploits a creature, you may search your library for a card, put it into your hand, then shuffle your library.', 'power': 4, 'mana_cost': '3BB', 'name': 'Sidisi, Undead Vizier', 'subtype': ['Zombie', 'Naga'], 'toughness': 6}, supertype=[cardtype.SuperType.LEGENDARY], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Deathtouch]))

class c394735(card.Card):
    "Ultimate Price"
    def __init__(self):
        super(c394735, self).__init__(gameobject.Characteristics(**{'color': ['B'], 'name': 'Ultimate Price', 'text': 'Destroy target monocolored creature.', 'mana_cost': '1B'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c205408(card.Card):
    "Search for Tomorrow"
    def __init__(self):
        super(c205408, self).__init__(gameobject.Characteristics(**{'color': ['G'], 'name': 'Search for Tomorrow', 'text': 'Search your library for a basic land card and put it onto the battlefield. Then shuffle your library.\nSuspend 2—{G} (Rather than cast this card from your hand, you may pay {G} and exile it with two time counters on it. At the beginning of your upkeep, remove a time counter. When the last is removed, cast it without paying its mana cost.)', 'mana_cost': '2G'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c265979(card.Card):
    "Preordain"
    def __init__(self):
        super(c265979, self).__init__(gameobject.Characteristics(**{'color': ['U'], 'name': 'Preordain', 'text': 'Scry 2, then draw a card. (To scry 2, look at the top two cards of your library, then put any number of them on the bottom of your library and the rest on top in any order.)', 'mana_cost': 'U'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c266210(card.Card):
    "Plated Geopede"
    def __init__(self):
        super(c266210, self).__init__(gameobject.Characteristics(**{'color': ['R'], 'text': 'First strike\nLandfall — Whenever a land enters the battlefield under your control, Plated Geopede gets +2/+2 until end of turn.', 'power': 1, 'mana_cost': '1R', 'name': 'Plated Geopede', 'subtype': ['Insect'], 'toughness': 1}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c270873(card.Card):
    "Searing Blaze"
    def __init__(self):
        super(c270873, self).__init__(gameobject.Characteristics(**{'color': ['R'], 'name': 'Searing Blaze', 'text': 'Searing Blaze deals 1 damage to target player and 1 damage to target creature that player controls.\nLandfall — If you had a land enter the battlefield under your control this turn, Searing Blaze deals 3 damage to that player and 3 damage to that creature instead.', 'mana_cost': 'RR'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c409577(card.Card):
    "Geist of Saint Traft"
    def __init__(self):
        super(c409577, self).__init__(gameobject.Characteristics(**{'color': ['W', 'U'], 'text': "Hexproof (This creature can't be the target of spells or abilities your opponents control.)\nWhenever Geist of Saint Traft attacks, create a 4/4 white Angel creature token with flying that's tapped and attacking. Exile that token at end of combat.", 'power': 2, 'mana_cost': '1WU', 'name': 'Geist of Saint Traft', 'subtype': ['Spirit', 'Cleric'], 'toughness': 2}, supertype=[cardtype.SuperType.LEGENDARY], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Hexproof]))

class c409580(card.Card):
    "Champion of the Parish"
    def __init__(self):
        super(c409580, self).__init__(gameobject.Characteristics(**{'color': ['W'], 'text': 'Whenever another Human enters the battlefield under your control, put a +1/+1 counter on Champion of the Parish.', 'power': 1, 'mana_cost': 'W', 'name': 'Champion of the Parish', 'subtype': ['Human', 'Soldier'], 'toughness': 1}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c409587(card.Card):
    "Fiend Hunter"
    def __init__(self):
        super(c409587, self).__init__(gameobject.Characteristics(**{'color': ['W'], 'text': "When Fiend Hunter enters the battlefield, you may exile another target creature.\nWhen Fiend Hunter leaves the battlefield, return the exiled card to the battlefield under its owner's control.", 'power': 1, 'mana_cost': '1WW', 'name': 'Fiend Hunter', 'subtype': ['Human', 'Cleric'], 'toughness': 3}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c409630(card.Card):
    "Diregraf Ghoul"
    def __init__(self):
        super(c409630, self).__init__(gameobject.Characteristics(**{'color': ['B'], 'text': 'Diregraf Ghoul enters the battlefield tapped.', 'power': 2, 'mana_cost': 'B', 'name': 'Diregraf Ghoul', 'subtype': ['Zombie'], 'toughness': 2}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c373649(card.Card):
    "Elspeth, Sun's Champion"
    def __init__(self):
        super(c373649, self).__init__(gameobject.Characteristics(**{'color': ['W'], 'name': "Elspeth, Sun's Champion", 'subtype': ['Elspeth'], 'text': '+1: Create three 1/1 white Soldier creature tokens.\n−3: Destroy all creatures with power 4 or greater.\n−7: You get an emblem with "Creatures you control get +2/+2 and have flying."', 'mana_cost': '4WW'}, supertype=[], types=[cardtype.CardType.PLANESWALKER], abilities=[]))

class c373529(card.Card):
    "Soldier of the Pantheon"
    def __init__(self):
        super(c373529, self).__init__(gameobject.Characteristics(**{'color': ['W'], 'text': 'Protection from multicolored\nWhenever an opponent casts a multicolored spell, you gain 1 life.', 'power': 2, 'mana_cost': 'W', 'name': 'Soldier of the Pantheon', 'subtype': ['Human', 'Soldier'], 'toughness': 1}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c373717(card.Card):
    "Spear of Heliod"
    def __init__(self):
        super(c373717, self).__init__(gameobject.Characteristics(**{'color': ['W'], 'name': 'Spear of Heliod', 'text': 'Creatures you control get +1/+1.\n{1}{W}{W}, {T}: Destroy target creature that dealt damage to you this turn.', 'mana_cost': '1WW'}, supertype=[cardtype.SuperType.LEGENDARY], types=[cardtype.CardType.ENCHANTMENT, cardtype.CardType.ARTIFACT], abilities=[]))

class c373661(card.Card):
    "Abhorrent Overlord"
    def __init__(self):
        super(c373661, self).__init__(gameobject.Characteristics(**{'color': ['B'], 'text': 'Flying\nWhen Abhorrent Overlord enters the battlefield, create a number of 1/1 black Harpy creature tokens with flying equal to your devotion to black. (Each {B} in the mana costs of permanents you control counts toward your devotion to black.)\nAt the beginning of your upkeep, sacrifice a creature.', 'power': 6, 'mana_cost': '5BB', 'name': 'Abhorrent Overlord', 'subtype': ['Demon'], 'toughness': 6}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Flying]))

class c373575(card.Card):
    "Hero's Downfall"
    def __init__(self):
        super(c373575, self).__init__(gameobject.Characteristics(**{'color': ['B'], 'name': "Hero's Downfall", 'text': 'Destroy target creature or planeswalker.', 'mana_cost': '1BB'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c373632(card.Card):
    "Thoughtseize"
    def __init__(self):
        super(c373632, self).__init__(gameobject.Characteristics(**{'color': ['B'], 'name': 'Thoughtseize', 'text': 'Target player reveals his or her hand. You choose a nonland card from it. That player discards that card. You lose 2 life.', 'mana_cost': 'B'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c373604(card.Card):
    "Anger of the Gods"
    def __init__(self):
        super(c373604, self).__init__(gameobject.Characteristics(**{'color': ['R'], 'name': 'Anger of the Gods', 'text': 'Anger of the Gods deals 3 damage to each creature. If a creature dealt damage this way would die this turn, exile it instead.', 'mana_cost': '1RR'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c373552(card.Card):
    "Firedrinker Satyr"
    def __init__(self):
        super(c373552, self).__init__(gameobject.Characteristics(**{'color': ['R'], 'text': 'Whenever Firedrinker Satyr is dealt damage, it deals that much damage to you.\n{1}{R}: Firedrinker Satyr gets +1/+0 until end of turn and deals 1 damage to you.', 'power': 2, 'mana_cost': 'R', 'name': 'Firedrinker Satyr', 'subtype': ['Satyr', 'Shaman'], 'toughness': 1}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c373704(card.Card):
    "Magma Jet"
    def __init__(self):
        super(c373704, self).__init__(gameobject.Characteristics(**{'color': ['R'], 'name': 'Magma Jet', 'text': 'Magma Jet deals 2 damage to target creature or player. Scry 2.', 'mana_cost': '1R'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c373549(card.Card):
    "Polukranos, World Eater"
    def __init__(self):
        super(c373549, self).__init__(gameobject.Characteristics(**{'color': ['G'], 'text': "{X}{X}{G}: Monstrosity X. (If this creature isn't monstrous, put X +1/+1 counters on it and it becomes monstrous.)\nWhen Polukranos, World Eater becomes monstrous, it deals X damage divided as you choose among any number of target creatures your opponents control. Each of those creatures deals damage equal to its power to Polukranos.", 'power': 5, 'mana_cost': '2GG', 'name': 'Polukranos, World Eater', 'subtype': ['Hydra'], 'toughness': 5}, supertype=[cardtype.SuperType.LEGENDARY], types=[cardtype.CardType.CREATURE], abilities=[]))

class c373624(card.Card):
    "Sylvan Caryatid"
    def __init__(self):
        super(c373624, self).__init__(gameobject.Characteristics(**{'color': ['G'], 'text': 'Defender, hexproof\n{T}: Add one mana of any color to your mana pool.', 'power': 0, 'mana_cost': '1G', 'name': 'Sylvan Caryatid', 'subtype': ['Plant'], 'toughness': 3}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Defender, abilities.StaticAbilities.Hexproof]))

class c373500(card.Card):
    "Ashiok, Nightmare Weaver"
    def __init__(self):
        super(c373500, self).__init__(gameobject.Characteristics(**{'color': ['U', 'B'], 'name': 'Ashiok, Nightmare Weaver', 'subtype': ['Ashiok'], 'text': "+2: Exile the top three cards of target opponent's library.\n−X: Put a creature card with converted mana cost X exiled with Ashiok, Nightmare Weaver onto the battlefield under your control. That creature is a Nightmare in addition to its other types.\n−10: Exile all cards from all opponents' hands and graveyards.", 'mana_cost': '1UB'}, supertype=[], types=[cardtype.CardType.PLANESWALKER], abilities=[]))

class c373562(card.Card):
    "Fleecemane Lion"
    def __init__(self):
        super(c373562, self).__init__(gameobject.Characteristics(**{'color': ['W', 'G'], 'text': "{3}{G}{W}: Monstrosity 1. (If this creature isn't monstrous, put a +1/+1 counter on it and it becomes monstrous.)\nAs long as Fleecemane Lion is monstrous, it has hexproof and indestructible.", 'power': 3, 'mana_cost': 'GW', 'name': 'Fleecemane Lion', 'subtype': ['Cat'], 'toughness': 3}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c373635(card.Card):
    "Prophet of Kruphix"
    def __init__(self):
        super(c373635, self).__init__(gameobject.Characteristics(**{'color': ['U', 'G'], 'text': "Untap all creatures and lands you control during each other player's untap step.\nYou may cast creature spells as though they had flash.", 'power': 2, 'mana_cost': '3GU', 'name': 'Prophet of Kruphix', 'subtype': ['Human', 'Wizard'], 'toughness': 3}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c373502(card.Card):
    "Xenagos, the Reveler"
    def __init__(self):
        super(c373502, self).__init__(gameobject.Characteristics(**{'color': ['R', 'G'], 'name': 'Xenagos, the Reveler', 'subtype': ['Xenagos'], 'text': '+1: Add X mana in any combination of {R} and/or {G} to your mana pool, where X is the number of creatures you control.\n0: Create a 2/2 red and green Satyr creature token with haste.\n−6: Exile the top seven cards of your library. You may put any number of creature and/or land cards from among them onto the battlefield.', 'mana_cost': '2RG'}, supertype=[], types=[cardtype.CardType.PLANESWALKER], abilities=[]))

class c220139(card.Card):
    "Day of Judgment"
    def __init__(self):
        super(c220139, self).__init__(gameobject.Characteristics(**{'color': ['W'], 'name': 'Day of Judgment', 'text': 'Destroy all creatures.', 'mana_cost': '2WW'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c220074(card.Card):
    "Timely Reinforcements"
    def __init__(self):
        super(c220074, self).__init__(gameobject.Characteristics(**{'color': ['W'], 'name': 'Timely Reinforcements', 'text': 'If you have less life than an opponent, you gain 6 life. If you control fewer creatures than an opponent, create three 1/1 white Soldier creature tokens.', 'mana_cost': '2W'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c220099(card.Card):
    "Phantasmal Image"
    def __init__(self):
        super(c220099, self).__init__(gameobject.Characteristics(**{'color': ['U'], 'text': 'You may have Phantasmal Image enter the battlefield as a copy of any creature on the battlefield, except it\'s an Illusion in addition to its other types and it gains "When this creature becomes the target of a spell or ability, sacrifice it."', 'power': 0, 'mana_cost': '1U', 'name': 'Phantasmal Image', 'subtype': ['Illusion'], 'toughness': 0}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c237010(card.Card):
    "Smallpox"
    def __init__(self):
        super(c237010, self).__init__(gameobject.Characteristics(**{'color': ['B'], 'name': 'Smallpox', 'text': 'Each player loses 1 life, discards a card, sacrifices a creature, then sacrifices a land.', 'mana_cost': 'BB'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c234075(card.Card):
    "Incinerate"
    def __init__(self):
        super(c234075, self).__init__(gameobject.Characteristics(**{'color': ['R'], 'name': 'Incinerate', 'text': "Incinerate deals 3 damage to target creature or player. A creature dealt damage this way can't be regenerated this turn.", 'mana_cost': '1R'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c235192(card.Card):
    "Inferno Titan"
    def __init__(self):
        super(c235192, self).__init__(gameobject.Characteristics(**{'color': ['R'], 'text': '{R}: Inferno Titan gets +1/+0 until end of turn.\nWhenever Inferno Titan enters the battlefield or attacks, it deals 3 damage divided as you choose among one, two, or three target creatures and/or players.', 'power': 6, 'mana_cost': '4RR', 'name': 'Inferno Titan', 'subtype': ['Giant'], 'toughness': 6}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c230764(card.Card):
    "Manic Vandal"
    def __init__(self):
        super(c230764, self).__init__(gameobject.Characteristics(**{'color': ['R'], 'text': 'When Manic Vandal enters the battlefield, destroy target artifact.', 'power': 2, 'mana_cost': '2R', 'name': 'Manic Vandal', 'subtype': ['Human', 'Warrior'], 'toughness': 2}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c152549(card.Card):
    "Vendilion Clique"
    def __init__(self):
        super(c152549, self).__init__(gameobject.Characteristics(**{'color': ['U'], 'text': "Flash\nFlying\nWhen Vendilion Clique enters the battlefield, look at target player's hand. You may choose a nonland card from it. If you do, that player reveals the chosen card, puts it on the bottom of his or her library, then draws a card.", 'power': 3, 'mana_cost': '1UU', 'name': 'Vendilion Clique', 'subtype': ['Faerie', 'Wizard'], 'toughness': 1}, supertype=[cardtype.SuperType.LEGENDARY], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Flash, abilities.StaticAbilities.Flying]))

class c152648(card.Card):
    "Bitterblossom"
    def __init__(self):
        super(c152648, self).__init__(gameobject.Characteristics(**{'color': ['B'], 'name': 'Bitterblossom', 'subtype': ['Faerie'], 'text': 'At the beginning of your upkeep, you lose 1 life and create a 1/1 black Faerie Rogue creature token with flying.', 'mana_cost': '1B'}, supertype=[], types=[cardtype.CardType.TRIBAL, cardtype.CardType.ENCHANTMENT], abilities=[]))

class c151987(card.Card):
    "Woodfall Primus"
    def __init__(self):
        super(c151987, self).__init__(gameobject.Characteristics(**{'color': ['G'], 'text': "Trample\nWhen Woodfall Primus enters the battlefield, destroy target noncreature permanent.\nPersist (When this creature dies, if it had no -1/-1 counters on it, return it to the battlefield under its owner's control with a -1/-1 counter on it.)", 'power': 6, 'mana_cost': '5GGG', 'name': 'Woodfall Primus', 'subtype': ['Treefolk', 'Shaman'], 'toughness': 6}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Trample]))

class c153298(card.Card):
    "Murderous Redcap"
    def __init__(self):
        super(c153298, self).__init__(gameobject.Characteristics(**{'color': ['B', 'R'], 'text': "When Murderous Redcap enters the battlefield, it deals damage equal to its power to target creature or player.\nPersist (When this creature dies, if it had no -1/-1 counters on it, return it to the battlefield under its owner's control with a -1/-1 counter on it.)", 'power': 2, 'mana_cost': '2B/RB/R', 'name': 'Murderous Redcap', 'subtype': ['Goblin', 'Assassin'], 'toughness': 2}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c398428(card.Card):
    "Kytheon, Hero of Akros"
    def __init__(self):
        super(c398428, self).__init__(gameobject.Characteristics(**{'color': ['W'], 'text': "At end of combat, if Kytheon, Hero of Akros and at least two other creatures attacked this combat, exile Kytheon, then return him to the battlefield transformed under his owner's control.\n{2}{W}: Kytheon gains indestructible until end of turn.", 'power': 2, 'mana_cost': 'W', 'name': 'Kytheon, Hero of Akros', 'subtype': ['Human', 'Soldier'], 'toughness': 1}, supertype=[cardtype.SuperType.LEGENDARY], types=[cardtype.CardType.CREATURE], abilities=[]))

class c398476(card.Card):
    "Relic Seeker"
    def __init__(self):
        super(c398476, self).__init__(gameobject.Characteristics(**{'color': ['W'], 'text': "Renown 1 (When this creature deals combat damage to a player, if it isn't renowned, put a +1/+1 counter on it and it becomes renowned.)\nWhen Relic Seeker becomes renowned, you may search your library for an Equipment card, reveal it, put it into your hand, then shuffle your library.", 'power': 2, 'mana_cost': '1W', 'name': 'Relic Seeker', 'subtype': ['Human', 'Soldier'], 'toughness': 2}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c398520(card.Card):
    "Sphinx's Tutelage"
    def __init__(self):
        super(c398520, self).__init__(gameobject.Characteristics(**{'color': ['U'], 'name': "Sphinx's Tutelage", 'text': "Whenever you draw a card, target opponent puts the top two cards of his or her library into his or her graveyard. If they're both nonland cards that share a color, repeat this process.\n{5}{U}: Draw a card, then discard a card.", 'mana_cost': '2U'}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c398519(card.Card):
    "Thopter Spy Network"
    def __init__(self):
        super(c398519, self).__init__(gameobject.Characteristics(**{'color': ['U'], 'name': 'Thopter Spy Network', 'text': 'At the beginning of your upkeep, if you control an artifact, create a 1/1 colorless Thopter artifact creature token with flying.\nWhenever one or more artifact creatures you control deal combat damage to a player, draw a card.', 'mana_cost': '2UU'}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c398410(card.Card):
    "Whirler Rogue"
    def __init__(self):
        super(c398410, self).__init__(gameobject.Characteristics(**{'color': ['U'], 'text': "When Whirler Rogue enters the battlefield, create two 1/1 colorless Thopter artifact creature tokens with flying.\nTap two untapped artifacts you control: Target creature can't be blocked this turn.", 'power': 2, 'mana_cost': '2UU', 'name': 'Whirler Rogue', 'subtype': ['Human', 'Rogue', 'Artificer'], 'toughness': 2}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c398495(card.Card):
    "Gilt-Leaf Winnower"
    def __init__(self):
        super(c398495, self).__init__(gameobject.Characteristics(**{'color': ['B'], 'text': "Menace (This creature can't be blocked except by two or more creatures.)\nWhen Gilt-Leaf Winnower enters the battlefield, you may destroy target non-Elf creature whose power and toughness aren't equal.", 'power': 4, 'mana_cost': '3BB', 'name': 'Gilt-Leaf Winnower', 'subtype': ['Elf', 'Warrior'], 'toughness': 3}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Menace]))

class c398411(card.Card):
    "Abbot of Keral Keep"
    def __init__(self):
        super(c398411, self).__init__(gameobject.Characteristics(**{'color': ['R'], 'text': 'Prowess (Whenever you cast a noncreature spell, this creature gets +1/+1 until end of turn.)\nWhen Abbot of Keral Keep enters the battlefield, exile the top card of your library. Until end of turn, you may play that card.', 'power': 2, 'mana_cost': '1R', 'name': 'Abbot of Keral Keep', 'subtype': ['Human', 'Monk'], 'toughness': 1}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c398453(card.Card):
    "Pia and Kiran Nalaar"
    def __init__(self):
        super(c398453, self).__init__(gameobject.Characteristics(**{'color': ['R'], 'text': 'When Pia and Kiran Nalaar enters the battlefield, create two 1/1 colorless Thopter artifact creature tokens with flying.\n{2}{R}, Sacrifice an artifact: Pia and Kiran Nalaar deals 2 damage to target creature or player.', 'power': 2, 'mana_cost': '2RR', 'name': 'Pia and Kiran Nalaar', 'subtype': ['Human', 'Artificer'], 'toughness': 2}, supertype=[cardtype.SuperType.LEGENDARY], types=[cardtype.CardType.CREATURE], abilities=[]))

class c398514(card.Card):
    "Thopter Engineer"
    def __init__(self):
        super(c398514, self).__init__(gameobject.Characteristics(**{'color': ['R'], 'text': 'When Thopter Engineer enters the battlefield, create a 1/1 colorless Thopter artifact creature token with flying.\nArtifact creatures you control have haste. (They can attack and {T} as soon as they come under your control.)', 'power': 1, 'mana_cost': '2R', 'name': 'Thopter Engineer', 'subtype': ['Human', 'Artificer'], 'toughness': 3}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c398573(card.Card):
    "Evolutionary Leap"
    def __init__(self):
        super(c398573, self).__init__(gameobject.Characteristics(**{'color': ['G'], 'name': 'Evolutionary Leap', 'text': '{G}, Sacrifice a creature: Reveal cards from the top of your library until you reveal a creature card. Put that card into your hand and the rest on the bottom of your library in a random order.', 'mana_cost': '1G'}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c398511(card.Card):
    "Woodland Bellower"
    def __init__(self):
        super(c398511, self).__init__(gameobject.Characteristics(**{'color': ['G'], 'text': 'When Woodland Bellower enters the battlefield, you may search your library for a nonlegendary green creature card with converted mana cost 3 or less, put it onto the battlefield, then shuffle your library.', 'power': 6, 'mana_cost': '4GG', 'name': 'Woodland Bellower', 'subtype': ['Beast'], 'toughness': 5}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c1849(card.Card):
    "Hymn to Tourach"
    def __init__(self):
        super(c1849, self).__init__(gameobject.Characteristics(**{'color': ['B'], 'name': 'Hymn to Tourach', 'text': 'Target player discards two cards at random.', 'mana_cost': 'BB'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c386660(card.Card):
    "Seeker of the Way"
    def __init__(self):
        super(c386660, self).__init__(gameobject.Characteristics(**{'color': ['W'], 'text': 'Prowess (Whenever you cast a noncreature spell, this creature gets +1/+1 until end of turn.)\nWhenever you cast a noncreature spell, Seeker of the Way gains lifelink until end of turn.', 'power': 2, 'mana_cost': '1W', 'name': 'Seeker of the Way', 'subtype': ['Human', 'Warrior'], 'toughness': 2}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c386518(card.Card):
    "Dig Through Time"
    def __init__(self):
        super(c386518, self).__init__(gameobject.Characteristics(**{'color': ['U'], 'name': 'Dig Through Time', 'text': 'Delve (Each card you exile from your graveyard while casting this spell pays for {1}.)\nLook at the top seven cards of your library. Put two of them into your hand and the rest on the bottom of your library in any order.', 'mana_cost': '6UU'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c386494(card.Card):
    "Bloodsoaked Champion"
    def __init__(self):
        super(c386494, self).__init__(gameobject.Characteristics(**{'color': ['B'], 'text': "Bloodsoaked Champion can't block.\nRaid — {1}{B}: Return Bloodsoaked Champion from your graveyard to the battlefield. Activate this ability only if you attacked with a creature this turn.", 'power': 2, 'mana_cost': 'B', 'name': 'Bloodsoaked Champion', 'subtype': ['Human', 'Warrior'], 'toughness': 1}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c386613(card.Card):
    "Murderous Cut"
    def __init__(self):
        super(c386613, self).__init__(gameobject.Characteristics(**{'color': ['B'], 'name': 'Murderous Cut', 'text': 'Delve (Each card you exile from your graveyard while casting this spell pays for {1}.)\nDestroy target creature.', 'mana_cost': '4B'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c386560(card.Card):
    "Hordeling Outburst"
    def __init__(self):
        super(c386560, self).__init__(gameobject.Characteristics(**{'color': ['R'], 'name': 'Hordeling Outburst', 'text': 'Create three 1/1 red Goblin creature tokens.', 'mana_cost': '1RR'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c386608(card.Card):
    "Monastery Swiftspear"
    def __init__(self):
        super(c386608, self).__init__(gameobject.Characteristics(**{'color': ['R'], 'text': 'Haste\nProwess (Whenever you cast a noncreature spell, this creature gets +1/+1 until end of turn.)', 'power': 1, 'mana_cost': 'R', 'name': 'Monastery Swiftspear', 'subtype': ['Human', 'Monk'], 'toughness': 2}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Haste]))

class c386562(card.Card):
    "Icefeather Aven"
    def __init__(self):
        super(c386562, self).__init__(gameobject.Characteristics(**{'color': ['U', 'G'], 'text': "Flying\nMorph {1}{G}{U} (You may cast this card face down as a 2/2 creature for {3}. Turn it face up any time for its morph cost.)\nWhen Icefeather Aven is turned face up, you may return another target creature to its owner's hand.", 'power': 2, 'mana_cost': 'GU', 'name': 'Icefeather Aven', 'subtype': ['Bird', 'Shaman'], 'toughness': 2}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Flying]))

class c386571(card.Card):
    "Jeskai Ascendancy"
    def __init__(self):
        super(c386571, self).__init__(gameobject.Characteristics(**{'color': ['W', 'U', 'R'], 'name': 'Jeskai Ascendancy', 'text': 'Whenever you cast a noncreature spell, creatures you control get +1/+1 until end of turn. Untap those creatures.\nWhenever you cast a noncreature spell, you may draw a card. If you do, discard a card.', 'mana_cost': 'URW'}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c386631(card.Card):
    "Rakshasa Deathdealer"
    def __init__(self):
        super(c386631, self).__init__(gameobject.Characteristics(**{'color': ['B', 'G'], 'text': '{B}{G}: Rakshasa Deathdealer gets +2/+2 until end of turn.\n{B}{G}: Regenerate Rakshasa Deathdealer.', 'power': 2, 'mana_cost': 'BG', 'name': 'Rakshasa Deathdealer', 'subtype': ['Cat', 'Demon'], 'toughness': 2}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c386495(card.Card):
    "Bloodstained Mire"
    def __init__(self):
        super(c386495, self).__init__(gameobject.Characteristics(**{'color': '', 'name': 'Bloodstained Mire', 'text': '{T}, Pay 1 life, Sacrifice Bloodstained Mire: Search your library for a Swamp or Mountain card and put it onto the battlefield. Then shuffle your library.', 'mana_cost': ''}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c386537(card.Card):
    "Flooded Strand"
    def __init__(self):
        super(c386537, self).__init__(gameobject.Characteristics(**{'color': '', 'name': 'Flooded Strand', 'text': '{T}, Pay 1 life, Sacrifice Flooded Strand: Search your library for a Plains or Island card and put it onto the battlefield. Then shuffle your library.', 'mana_cost': ''}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c386627(card.Card):
    "Polluted Delta"
    def __init__(self):
        super(c386627, self).__init__(gameobject.Characteristics(**{'color': '', 'name': 'Polluted Delta', 'text': '{T}, Pay 1 life, Sacrifice Polluted Delta: Search your library for an Island or Swamp card and put it onto the battlefield. Then shuffle your library.', 'mana_cost': ''}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c386725(card.Card):
    "Windswept Heath"
    def __init__(self):
        super(c386725, self).__init__(gameobject.Characteristics(**{'color': '', 'name': 'Windswept Heath', 'text': '{T}, Pay 1 life, Sacrifice Windswept Heath: Search your library for a Forest or Plains card and put it onto the battlefield. Then shuffle your library.', 'mana_cost': ''}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c386729(card.Card):
    "Wooded Foothills"
    def __init__(self):
        super(c386729, self).__init__(gameobject.Characteristics(**{'color': '', 'name': 'Wooded Foothills', 'text': '{T}, Pay 1 life, Sacrifice Wooded Foothills: Search your library for a Mountain or Forest card and put it onto the battlefield. Then shuffle your library.', 'mana_cost': ''}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c198294(card.Card):
    "Hyena Umbra"
    def __init__(self):
        super(c198294, self).__init__(gameobject.Characteristics(**{'color': ['W'], 'name': 'Hyena Umbra', 'subtype': ['Aura'], 'text': 'Enchant creature\nEnchanted creature gets +1/+1 and has first strike.\nTotem armor (If enchanted creature would be destroyed, instead remove all damage from it and destroy this Aura.)', 'mana_cost': 'W'}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c193474(card.Card):
    "Splinter Twin"
    def __init__(self):
        super(c193474, self).__init__(gameobject.Characteristics(**{'color': ['R'], 'name': 'Splinter Twin', 'subtype': ['Aura'], 'text': 'Enchant creature\nEnchanted creature has "{T}: Create a token that\'s a copy of this creature. That token has haste. Exile it at the beginning of the next end step."', 'mana_cost': '2RR'}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c193462(card.Card):
    "Joraga Treespeaker"
    def __init__(self):
        super(c193462, self).__init__(gameobject.Characteristics(**{'color': ['G'], 'text': 'Level up {1}{G} ({1}{G}: Put a level counter on this. Level up only as a sorcery.)\nLEVEL 1-4\n1/2\n{T}: Add {G}{G} to your mana pool.\nLEVEL 5+\n1/4\nElves you control have "{T}: Add {G}{G} to your mana pool."', 'power': 1, 'mana_cost': 'G', 'name': 'Joraga Treespeaker', 'subtype': ['Elf', 'Druid'], 'toughness': 1}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c270446(card.Card):
    "Sphinx of the Steel Wind"
    def __init__(self):
        super(c270446, self).__init__(gameobject.Characteristics(**{'color': ['W', 'U', 'B'], 'text': 'Flying, first strike, vigilance, lifelink, protection from red and from green', 'power': 6, 'mana_cost': '5WUB', 'name': 'Sphinx of the Steel Wind', 'subtype': ['Sphinx'], 'toughness': 6}, supertype=[], types=[cardtype.CardType.ARTIFACT, cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.First_Strike, abilities.StaticAbilities.Flying, abilities.StaticAbilities.Lifelink, abilities.StaticAbilities.Vigilance]))

class c270447(card.Card):
    "Inkwell Leviathan"
    def __init__(self):
        super(c270447, self).__init__(gameobject.Characteristics(**{'color': ['U'], 'text': "Islandwalk (This creature can't be blocked as long as defending player controls an Island.)\nTrample\nShroud (This creature can't be the target of spells or abilities.)", 'power': 7, 'mana_cost': '7UU', 'name': 'Inkwell Leviathan', 'subtype': ['Leviathan'], 'toughness': 11}, supertype=[], types=[cardtype.CardType.ARTIFACT, cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Shroud, abilities.StaticAbilities.Trample, abilities.StaticAbilities.Islandwalk]))

class c27080(card.Card):
    "Memory Lapse"
    def __init__(self):
        super(c27080, self).__init__(gameobject.Characteristics(**{'color': ['U'], 'name': 'Memory Lapse', 'text': "Counter target spell. If that spell is countered this way, put it on top of its owner's library instead of into that player's graveyard.", 'mana_cost': '1U'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c15796(card.Card):
    "Opposition"
    def __init__(self):
        super(c15796, self).__init__(gameobject.Characteristics(**{'color': ['U'], 'name': 'Opposition', 'text': 'Tap an untapped creature you control: Tap target artifact, creature, or land.', 'mana_cost': '2UU'}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c405126(card.Card):
    "Angel of Serenity"
    def __init__(self):
        super(c405126, self).__init__(gameobject.Characteristics(**{'color': ['W'], 'text': "Flying\nWhen Angel of Serenity enters the battlefield, you may exile up to three other target creatures from the battlefield and/or creature cards from graveyards.\nWhen Angel of Serenity leaves the battlefield, return the exiled cards to their owners' hands.", 'power': 5, 'mana_cost': '4WWW', 'name': 'Angel of Serenity', 'subtype': ['Angel'], 'toughness': 6}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Flying]))

class c405200(card.Card):
    "Dictate of Heliod"
    def __init__(self):
        super(c405200, self).__init__(gameobject.Characteristics(**{'color': ['W'], 'name': 'Dictate of Heliod', 'text': 'Flash\nCreatures you control get +2/+2.', 'mana_cost': '3WW'}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[abilities.StaticAbilities.Flash]))

class c405428(card.Card):
    "Underworld Connections"
    def __init__(self):
        super(c405428, self).__init__(gameobject.Characteristics(**{'color': ['B'], 'name': 'Underworld Connections', 'subtype': ['Aura'], 'text': 'Enchant land\nEnchanted land has "{T}, Pay 1 life: Draw a card."', 'mana_cost': '1BB'}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c405289(card.Card):
    "Lotleth Troll"
    def __init__(self):
        super(c405289, self).__init__(gameobject.Characteristics(**{'color': ['B', 'G'], 'text': 'Trample\nDiscard a creature card: Put a +1/+1 counter on Lotleth Troll.\n{B}: Regenerate Lotleth Troll.', 'power': 2, 'mana_cost': 'BG', 'name': 'Lotleth Troll', 'subtype': ['Zombie', 'Troll'], 'toughness': 1}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Trample]))

class c405100(card.Card):
    "Hallowed Fountain"
    def __init__(self):
        super(c405100, self).__init__(gameobject.Characteristics(**{'color': ['W', 'U'], 'name': 'Hallowed Fountain', 'subtype': ['Plains', 'Island'], 'text': "({T}: Add {W} or {U} to your mana pool.)\nAs Hallowed Fountain enters the battlefield, you may pay 2 life. If you don't, Hallowed Fountain enters the battlefield tapped.", 'mana_cost': ''}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c405093(card.Card):
    "Blood Crypt"
    def __init__(self):
        super(c405093, self).__init__(gameobject.Characteristics(**{'color': ['B', 'R'], 'name': 'Blood Crypt', 'subtype': ['Swamp', 'Mountain'], 'text': "({T}: Add {B} or {R} to your mana pool.)\nAs Blood Crypt enters the battlefield, you may pay 2 life. If you don't, Blood Crypt enters the battlefield tapped.", 'mana_cost': ''}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c405112(card.Card):
    "Temple Garden"
    def __init__(self):
        super(c405112, self).__init__(gameobject.Characteristics(**{'color': ['W', 'G'], 'name': 'Temple Garden', 'subtype': ['Forest', 'Plains'], 'text': "({T}: Add {G} or {W} to your mana pool.)\nAs Temple Garden enters the battlefield, you may pay 2 life. If you don't, Temple Garden enters the battlefield tapped.", 'mana_cost': ''}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c405103(card.Card):
    "Overgrown Tomb"
    def __init__(self):
        super(c405103, self).__init__(gameobject.Characteristics(**{'color': ['B', 'G'], 'name': 'Overgrown Tomb', 'subtype': ['Swamp', 'Forest'], 'text': "({T}: Add {B} or {G} to your mana pool.)\nAs Overgrown Tomb enters the battlefield, you may pay 2 life. If you don't, Overgrown Tomb enters the battlefield tapped.", 'mana_cost': ''}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c405106(card.Card):
    "Sacred Foundry"
    def __init__(self):
        super(c405106, self).__init__(gameobject.Characteristics(**{'color': ['W', 'R'], 'name': 'Sacred Foundry', 'subtype': ['Mountain', 'Plains'], 'text': "({T}: Add {R} or {W} to your mana pool.)\nAs Sacred Foundry enters the battlefield, you may pay 2 life. If you don't, Sacred Foundry enters the battlefield tapped.", 'mana_cost': ''}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c405095(card.Card):
    "Breeding Pool"
    def __init__(self):
        super(c405095, self).__init__(gameobject.Characteristics(**{'color': ['U', 'G'], 'name': 'Breeding Pool', 'subtype': ['Forest', 'Island'], 'text': "({T}: Add {G} or {U} to your mana pool.)\nAs Breeding Pool enters the battlefield, you may pay 2 life. If you don't, Breeding Pool enters the battlefield tapped.", 'mana_cost': ''}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c405101(card.Card):
    "Marsh Flats"
    def __init__(self):
        super(c405101, self).__init__(gameobject.Characteristics(**{'color': '', 'name': 'Marsh Flats', 'text': '{T}, Pay 1 life, Sacrifice Marsh Flats: Search your library for a Plains or Swamp card and put it onto the battlefield. Then shuffle your library.', 'mana_cost': ''}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c405107(card.Card):
    "Scalding Tarn"
    def __init__(self):
        super(c405107, self).__init__(gameobject.Characteristics(**{'color': '', 'name': 'Scalding Tarn', 'text': '{T}, Pay 1 life, Sacrifice Scalding Tarn: Search your library for an Island or Mountain card and put it onto the battlefield. Then shuffle your library.', 'mana_cost': ''}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c405113(card.Card):
    "Verdant Catacombs"
    def __init__(self):
        super(c405113, self).__init__(gameobject.Characteristics(**{'color': '', 'name': 'Verdant Catacombs', 'text': '{T}, Pay 1 life, Sacrifice Verdant Catacombs: Search your library for a Swamp or Forest card and put it onto the battlefield. Then shuffle your library.', 'mana_cost': ''}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c405092(card.Card):
    "Arid Mesa"
    def __init__(self):
        super(c405092, self).__init__(gameobject.Characteristics(**{'color': '', 'name': 'Arid Mesa', 'text': '{T}, Pay 1 life, Sacrifice Arid Mesa: Search your library for a Mountain or Plains card and put it onto the battlefield. Then shuffle your library.', 'mana_cost': ''}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c405102(card.Card):
    "Misty Rainforest"
    def __init__(self):
        super(c405102, self).__init__(gameobject.Characteristics(**{'color': '', 'name': 'Misty Rainforest', 'text': '{T}, Pay 1 life, Sacrifice Misty Rainforest: Search your library for a Forest or Island card and put it onto the battlefield. Then shuffle your library.', 'mana_cost': ''}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c409573(card.Card):
    "Mana Confluence"
    def __init__(self):
        super(c409573, self).__init__(gameobject.Characteristics(**{'color': '', 'name': 'Mana Confluence', 'text': '{T}, Pay 1 life: Add one mana of any color to your mana pool.', 'mana_cost': ''}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c430729(card.Card):
    "Nimble Obstructionist"
    def __init__(self):
        super(c430729, self).__init__(gameobject.Characteristics(**{'color': ['U'], 'text': "Flash\nFlying\nCycling {2}{U} ({2}{U}, Discard this card: Draw a card.)\nWhen you cycle Nimble Obstructionist, counter target activated or triggered ability you don't control.", 'power': 3, 'mana_cost': '2U', 'name': 'Nimble Obstructionist', 'subtype': ['Bird', 'Wizard'], 'toughness': 1}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Flash, abilities.StaticAbilities.Flying]))

class c430738(card.Card):
    "Supreme Will"
    def __init__(self):
        super(c430738, self).__init__(gameobject.Characteristics(**{'color': ['U'], 'name': 'Supreme Will', 'text': 'Choose one —\n• Counter target spell unless its controller pays {3}.\n• Look at the top four cards of your library. Put one of them into your hand and the rest on the bottom of your library in any order.', 'mana_cost': '2U'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c430779(card.Card):
    "Earthshaker Khenra"
    def __init__(self):
        super(c430779, self).__init__(gameobject.Characteristics(**{'color': ['R'], 'text': "Haste\nWhen Earthshaker Khenra enters the battlefield, target creature with power less than or equal to Earthshaker Khenra's power can't block this turn.\nEternalize {4}{R}{R} ({4}{R}{R}, Exile this card from your graveyard: Create a token that's a copy of it, except it's a 4/4 black Zombie Jackal Warrior with no mana cost. Eternalize only as a sorcery.)", 'power': 2, 'mana_cost': '1R', 'name': 'Earthshaker Khenra', 'subtype': ['Jackal', 'Warrior'], 'toughness': 1}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Haste]))

class c430818(card.Card):
    "Ramunap Excavator"
    def __init__(self):
        super(c430818, self).__init__(gameobject.Characteristics(**{'color': ['G'], 'text': 'You may play land cards from your graveyard.', 'power': 2, 'mana_cost': '2G', 'name': 'Ramunap Excavator', 'subtype': ['Naga', 'Cleric'], 'toughness': 3}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c430830(card.Card):
    "Obelisk Spider"
    def __init__(self):
        super(c430830, self).__init__(gameobject.Characteristics(**{'color': ['B', 'G'], 'text': 'Reach\nWhenever Obelisk Spider deals combat damage to a creature, put a -1/-1 counter on that creature.\nWhenever you put one or more -1/-1 counters on a creature, each opponent loses 1 life and you gain 1 life.', 'power': 1, 'mana_cost': '1BG', 'name': 'Obelisk Spider', 'subtype': ['Spider'], 'toughness': 4}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Reach]))

class c19135(card.Card):
    "Vindicate"
    def __init__(self):
        super(c19135, self).__init__(gameobject.Characteristics(**{'color': ['W', 'B'], 'name': 'Vindicate', 'text': 'Destroy target permanent.', 'mana_cost': '1WB'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c41280(card.Card):
    "Silent Specter"
    def __init__(self):
        super(c41280, self).__init__(gameobject.Characteristics(**{'color': ['B'], 'text': 'Flying\nWhenever Silent Specter deals combat damage to a player, that player discards two cards.\nMorph {3}{B}{B} (You may cast this card face down as a 2/2 creature for {3}. Turn it face up any time for its morph cost.)', 'power': 4, 'mana_cost': '4BB', 'name': 'Silent Specter', 'subtype': ['Specter'], 'toughness': 4}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Flying]))

class c292752(card.Card):
    "Isochron Scepter"
    def __init__(self):
        super(c292752, self).__init__(gameobject.Characteristics(**{'color': '', 'name': 'Isochron Scepter', 'text': 'Imprint — When Isochron Scepter enters the battlefield, you may exile an instant card with converted mana cost 2 or less from your hand.\n{2}, {T}: You may copy the exiled card. If you do, you may cast the copy without paying its mana cost.', 'mana_cost': '2'}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c338413(card.Card):
    "Izzet Charm"
    def __init__(self):
        super(c338413, self).__init__(gameobject.Characteristics(**{'color': ['U', 'R'], 'name': 'Izzet Charm', 'text': 'Choose one —\n• Counter target noncreature spell unless its controller pays {2}.\n• Izzet Charm deals 2 damage to target creature.\n• Draw two cards, then discard two cards.', 'mana_cost': 'UR'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c370439(card.Card):
    "Cryptic Command"
    def __init__(self):
        super(c370439, self).__init__(gameobject.Characteristics(**{'color': ['U'], 'name': 'Cryptic Command', 'text': "Choose two —\n• Counter target spell.\n• Return target permanent to its owner's hand.\n• Tap all creatures your opponents control.\n• Draw a card.", 'mana_cost': '1UUU'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c370440(card.Card):
    "Pestermite"
    def __init__(self):
        super(c370440, self).__init__(gameobject.Characteristics(**{'color': ['U'], 'text': 'Flash\nFlying\nWhen Pestermite enters the battlefield, you may tap or untap target permanent.', 'power': 2, 'mana_cost': '2U', 'name': 'Pestermite', 'subtype': ['Faerie', 'Rogue'], 'toughness': 1}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Flash, abilities.StaticAbilities.Flying]))

class c370560(card.Card):
    "Greater Gargadon"
    def __init__(self):
        super(c370560, self).__init__(gameobject.Characteristics(**{'color': ['R'], 'text': 'Suspend 10—{R}\nSacrifice an artifact, creature, or land: Remove a time counter from Greater Gargadon. Activate this ability only if Greater Gargadon is suspended.', 'power': 9, 'mana_cost': '9R', 'name': 'Greater Gargadon', 'subtype': ['Beast'], 'toughness': 7}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c370566(card.Card):
    "Sarkhan Vol"
    def __init__(self):
        super(c370566, self).__init__(gameobject.Characteristics(**{'color': ['R', 'G'], 'name': 'Sarkhan Vol', 'subtype': ['Sarkhan'], 'text': '+1: Creatures you control get +1/+1 and gain haste until end of turn.\n−2: Gain control of target creature until end of turn. Untap that creature. It gains haste until end of turn.\n−6: Create five 4/4 red Dragon creature tokens with flying.', 'mana_cost': '2RG'}, supertype=[], types=[cardtype.CardType.PLANESWALKER], abilities=[]))

class c370442(card.Card):
    "Bonesplitter"
    def __init__(self):
        super(c370442, self).__init__(gameobject.Characteristics(**{'color': '', 'name': 'Bonesplitter', 'subtype': ['Equipment'], 'text': 'Equipped creature gets +2/+0.\nEquip {1}', 'mana_cost': '1'}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c51221(card.Card):
    "All Suns' Dawn"
    def __init__(self):
        super(c51221, self).__init__(gameobject.Characteristics(**{'color': ['G'], 'name': "All Suns' Dawn", 'text': "For each color, return up to one target card of that color from your graveyard to your hand. Exile All Suns' Dawn.", 'mana_cost': '4G'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c378433(card.Card):
    "Bile Blight"
    def __init__(self):
        super(c378433, self).__init__(gameobject.Characteristics(**{'color': ['B'], 'name': 'Bile Blight', 'text': 'Target creature and all other creatures with the same name as that creature get -3/-3 until end of turn.', 'mana_cost': 'BB'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c240096(card.Card):
    "Restoration Angel"
    def __init__(self):
        super(c240096, self).__init__(gameobject.Characteristics(**{'color': ['W'], 'text': 'Flash\nFlying\nWhen Restoration Angel enters the battlefield, you may exile target non-Angel creature you control, then return that card to the battlefield under your control.', 'power': 3, 'mana_cost': '3W', 'name': 'Restoration Angel', 'subtype': ['Angel'], 'toughness': 4}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Flash, abilities.StaticAbilities.Flying]))

class c240022(card.Card):
    "Deadeye Navigator"
    def __init__(self):
        super(c240022, self).__init__(gameobject.Characteristics(**{'color': ['U'], 'text': 'Soulbond (You may pair this creature with another unpaired creature when either enters the battlefield. They remain paired for as long as you control both of them.)\nAs long as Deadeye Navigator is paired with another creature, each of those creatures has "{1}{U}: Exile this creature, then return it to the battlefield under your control."', 'power': 5, 'mana_cost': '4UU', 'name': 'Deadeye Navigator', 'subtype': ['Spirit'], 'toughness': 5}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c240178(card.Card):
    "Blood Artist"
    def __init__(self):
        super(c240178, self).__init__(gameobject.Characteristics(**{'color': ['B'], 'text': 'Whenever Blood Artist or another creature dies, target player loses 1 life and you gain 1 life.', 'power': 0, 'mana_cost': '1B', 'name': 'Blood Artist', 'subtype': ['Vampire'], 'toughness': 1}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c239995(card.Card):
    "Griselbrand"
    def __init__(self):
        super(c239995, self).__init__(gameobject.Characteristics(**{'color': ['B'], 'text': 'Flying, lifelink\nPay 7 life: Draw seven cards.', 'power': 7, 'mana_cost': '4BBBB', 'name': 'Griselbrand', 'subtype': ['Demon'], 'toughness': 7}, supertype=[cardtype.SuperType.LEGENDARY], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Flying, abilities.StaticAbilities.Lifelink]))

class c271095(card.Card):
    "Bonfire of the Damned"
    def __init__(self):
        super(c271095, self).__init__(gameobject.Characteristics(**{'color': ['R'], 'name': 'Bonfire of the Damned', 'text': "Bonfire of the Damned deals X damage to target player and each creature he or she controls.\nMiracle {X}{R} (You may cast this card for its miracle cost when you draw it if it's the first card you drew this turn.)", 'mana_cost': 'XXR'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c240082(card.Card):
    "Zealous Conscripts"
    def __init__(self):
        super(c240082, self).__init__(gameobject.Characteristics(**{'color': ['R'], 'text': 'Haste\nWhen Zealous Conscripts enters the battlefield, gain control of target permanent until end of turn. Untap that permanent. It gains haste until end of turn.', 'power': 3, 'mana_cost': '4R', 'name': 'Zealous Conscripts', 'subtype': ['Human', 'Warrior'], 'toughness': 3}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Haste]))

class c240033(card.Card):
    "Sigarda, Host of Herons"
    def __init__(self):
        super(c240033, self).__init__(gameobject.Characteristics(**{'color': ['W', 'G'], 'text': "Flying, hexproof\nSpells and abilities your opponents control can't cause you to sacrifice permanents.", 'power': 5, 'mana_cost': '2GWW', 'name': 'Sigarda, Host of Herons', 'subtype': ['Angel'], 'toughness': 5}, supertype=[cardtype.SuperType.LEGENDARY], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Flying, abilities.StaticAbilities.Hexproof]))

class c382209(card.Card):
    "Agent of Acquisitions"
    def __init__(self):
        super(c382209, self).__init__(gameobject.Characteristics(**{'color': '', 'text': "Draft Agent of Acquisitions face up.\nInstead of drafting a card from a booster pack, you may draft each card in that booster pack, one at a time. If you do, turn Agent of Acquisitions face down and you can't draft cards for the rest of this draft round. (You may look at booster packs passed to you.)", 'power': 2, 'mana_cost': '2', 'name': 'Agent of Acquisitions', 'subtype': ['Construct'], 'toughness': 1}, supertype=[], types=[cardtype.CardType.ARTIFACT, cardtype.CardType.CREATURE], abilities=[]))

class c382233(card.Card):
    "Cogwork Librarian"
    def __init__(self):
        super(c382233, self).__init__(gameobject.Characteristics(**{'color': '', 'text': 'Draft Cogwork Librarian face up.\nAs you draft a card, you may draft an additional card from that booster pack. If you do, put Cogwork Librarian into that booster pack.', 'power': 3, 'mana_cost': '4', 'name': 'Cogwork Librarian', 'subtype': ['Construct'], 'toughness': 3}, supertype=[], types=[cardtype.CardType.ARTIFACT, cardtype.CardType.CREATURE], abilities=[]))

class c382246(card.Card):
    "Deal Broker"
    def __init__(self):
        super(c382246, self).__init__(gameobject.Characteristics(**{'color': '', 'text': 'Draft Deal Broker face up.\nImmediately after the draft, you may reveal a card in your card pool. Each other player may offer you one card in his or her card pool in exchange. You may accept any one offer.\n{T}: Draw a card, then discard a card.', 'power': 2, 'mana_cost': '3', 'name': 'Deal Broker', 'subtype': ['Construct'], 'toughness': 3}, supertype=[], types=[cardtype.CardType.ARTIFACT, cardtype.CardType.CREATURE], abilities=[]))

class c382298(card.Card):
    "Lore Seeker"
    def __init__(self):
        super(c382298, self).__init__(gameobject.Characteristics(**{'color': '', 'text': "Reveal Lore Seeker as you draft it. After you draft Lore Seeker, you may add a booster pack to the draft. (Your next pick is from that booster pack. Pass it to the next player and it's drafted this draft round.)", 'power': 2, 'mana_cost': '2', 'name': 'Lore Seeker', 'subtype': ['Construct'], 'toughness': 2}, supertype=[], types=[cardtype.CardType.ARTIFACT, cardtype.CardType.CREATURE], abilities=[]))

class c382320(card.Card):
    "Paliano, the High City"
    def __init__(self):
        super(c382320, self).__init__(gameobject.Characteristics(**{'color': '', 'name': 'Paliano, the High City', 'text': 'Reveal Paliano, the High City as you draft it. The player to your right chooses a color, you choose another color, then the player to your left chooses a third color.\n{T}: Add one mana to your mana pool of any color chosen as you drafted cards named Paliano, the High City.', 'mana_cost': ''}, supertype=[cardtype.SuperType.LEGENDARY], types=[cardtype.CardType.LAND], abilities=[]))

class c382379(card.Card):
    "Sulfuric Vortex"
    def __init__(self):
        super(c382379, self).__init__(gameobject.Characteristics(**{'color': ['R'], 'name': 'Sulfuric Vortex', 'text': "At the beginning of each player's upkeep, Sulfuric Vortex deals 2 damage to that player.\nIf a player would gain life, that player gains no life instead.", 'mana_cost': '1RR'}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c382249(card.Card):
    "Deathrender"
    def __init__(self):
        super(c382249, self).__init__(gameobject.Characteristics(**{'color': '', 'name': 'Deathrender', 'subtype': ['Equipment'], 'text': 'Equipped creature gets +2/+2.\nWhenever equipped creature dies, you may put a creature card from your hand onto the battlefield and attach Deathrender to it.\nEquip {2}', 'mana_cost': '4'}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c259670(card.Card):
    "Odric, Master Tactician"
    def __init__(self):
        super(c259670, self).__init__(gameobject.Characteristics(**{'color': ['W'], 'text': 'First strike (This creature deals combat damage before creatures without first strike.)\nWhenever Odric, Master Tactician and at least three other creatures attack, you choose which creatures block this combat and how those creatures block.', 'power': 3, 'mana_cost': '2WW', 'name': 'Odric, Master Tactician', 'subtype': ['Human', 'Soldier'], 'toughness': 4}, supertype=[cardtype.SuperType.LEGENDARY], types=[cardtype.CardType.CREATURE], abilities=[]))

class c249676(card.Card):
    "Augur of Bolas"
    def __init__(self):
        super(c249676, self).__init__(gameobject.Characteristics(**{'color': ['U'], 'text': 'When Augur of Bolas enters the battlefield, look at the top three cards of your library. You may reveal an instant or sorcery card from among them and put it into your hand. Put the rest on the bottom of your library in any order.', 'power': 1, 'mana_cost': '1U', 'name': 'Augur of Bolas', 'subtype': ['Merfolk', 'Wizard'], 'toughness': 3}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c249685(card.Card):
    "Thragtusk"
    def __init__(self):
        super(c249685, self).__init__(gameobject.Characteristics(**{'color': ['G'], 'text': 'When Thragtusk enters the battlefield, you gain 5 life.\nWhen Thragtusk leaves the battlefield, create a 3/3 green Beast creature token.', 'power': 5, 'mana_cost': '4G', 'name': 'Thragtusk', 'subtype': ['Beast'], 'toughness': 3}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c249680(card.Card):
    "Yeva, Nature's Herald"
    def __init__(self):
        super(c249680, self).__init__(gameobject.Characteristics(**{'color': ['G'], 'text': 'Flash (You may cast this spell any time you could cast an instant.)\nYou may cast green creature spells as though they had flash.', 'power': 4, 'mana_cost': '2GG', 'name': "Yeva, Nature's Herald", 'subtype': ['Elf', 'Shaman'], 'toughness': 4}, supertype=[cardtype.SuperType.LEGENDARY], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Flash]))

class c249742(card.Card):
    "Gilded Lotus"
    def __init__(self):
        super(c249742, self).__init__(gameobject.Characteristics(**{'color': '', 'name': 'Gilded Lotus', 'text': '{T}: Add three mana of any one color to your mana pool.', 'mana_cost': '5'}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c192230(card.Card):
    "Bloodghast"
    def __init__(self):
        super(c192230, self).__init__(gameobject.Characteristics(**{'color': ['B'], 'text': "Bloodghast can't block.\nBloodghast has haste as long as an opponent has 10 or less life.\nLandfall — Whenever a land enters the battlefield under your control, you may return Bloodghast from your graveyard to the battlefield.", 'power': 2, 'mana_cost': 'BB', 'name': 'Bloodghast', 'subtype': ['Vampire', 'Spirit'], 'toughness': 1}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c185698(card.Card):
    "Gatekeeper of Malakir"
    def __init__(self):
        super(c185698, self).__init__(gameobject.Characteristics(**{'color': ['B'], 'text': 'Kicker {B} (You may pay an additional {B} as you cast this spell.)\nWhen Gatekeeper of Malakir enters the battlefield, if it was kicked, target player sacrifices a creature.', 'power': 2, 'mana_cost': 'BB', 'name': 'Gatekeeper of Malakir', 'subtype': ['Vampire', 'Warrior'], 'toughness': 2}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c192225(card.Card):
    "Vampire Lacerator"
    def __init__(self):
        super(c192225, self).__init__(gameobject.Characteristics(**{'color': ['B'], 'text': 'At the beginning of your upkeep, you lose 1 life unless an opponent has 10 or less life.', 'power': 2, 'mana_cost': 'B', 'name': 'Vampire Lacerator', 'subtype': ['Vampire', 'Warrior'], 'toughness': 2}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c177558(card.Card):
    "Burst Lightning"
    def __init__(self):
        super(c177558, self).__init__(gameobject.Characteristics(**{'color': ['R'], 'name': 'Burst Lightning', 'text': 'Kicker {4} (You may pay an additional {4} as you cast this spell.)\nBurst Lightning deals 2 damage to target creature or player. If Burst Lightning was kicked, it deals 4 damage to that creature or player instead.', 'mana_cost': 'R'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c170987(card.Card):
    "Goblin Guide"
    def __init__(self):
        super(c170987, self).__init__(gameobject.Characteristics(**{'color': ['R'], 'text': "Haste\nWhenever Goblin Guide attacks, defending player reveals the top card of his or her library. If it's a land card, that player puts it into his or her hand.", 'power': 2, 'mana_cost': 'R', 'name': 'Goblin Guide', 'subtype': ['Goblin', 'Scout'], 'toughness': 2}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Haste]))

class c185749(card.Card):
    "Lotus Cobra"
    def __init__(self):
        super(c185749, self).__init__(gameobject.Characteristics(**{'color': ['G'], 'text': 'Landfall — Whenever a land enters the battlefield under your control, you may add one mana of any color to your mana pool.', 'power': 2, 'mana_cost': '1G', 'name': 'Lotus Cobra', 'subtype': ['Snake'], 'toughness': 1}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c180455(card.Card):
    "Scute Mob"
    def __init__(self):
        super(c180455, self).__init__(gameobject.Characteristics(**{'color': ['G'], 'text': 'At the beginning of your upkeep, if you control five or more lands, put four +1/+1 counters on Scute Mob.', 'power': 1, 'mana_cost': 'G', 'name': 'Scute Mob', 'subtype': ['Insect'], 'toughness': 1}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c407614(card.Card):
    "Chandra, Flamecaller"
    def __init__(self):
        super(c407614, self).__init__(gameobject.Characteristics(**{'color': ['R'], 'name': 'Chandra, Flamecaller', 'subtype': ['Chandra'], 'text': '+1: Create two 3/1 red Elemental creature tokens with haste. Exile them at the beginning of the next end step.\n0: Discard all the cards in your hand, then draw that many cards plus one.\n−X: Chandra, Flamecaller deals X damage to each creature.', 'mana_cost': '4RR'}, supertype=[], types=[cardtype.CardType.PLANESWALKER], abilities=[]))

class c407654(card.Card):
    "Sylvan Advocate"
    def __init__(self):
        super(c407654, self).__init__(gameobject.Characteristics(**{'color': ['G'], 'text': 'Vigilance\nAs long as you control six or more lands, Sylvan Advocate and land creatures you control get +2/+2.', 'power': 2, 'mana_cost': '1G', 'name': 'Sylvan Advocate', 'subtype': ['Elf', 'Druid', 'Ally'], 'toughness': 3}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Vigilance]))

class c407667(card.Card):
    "Reflector Mage"
    def __init__(self):
        super(c407667, self).__init__(gameobject.Characteristics(**{'color': ['W', 'U'], 'text': "When Reflector Mage enters the battlefield, return target creature an opponent controls to its owner's hand. That creature's owner can't cast spells with the same name as that creature until your next turn.", 'power': 2, 'mana_cost': '1WU', 'name': 'Reflector Mage', 'subtype': ['Human', 'Wizard'], 'toughness': 3}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c370770(card.Card):
    "Imposing Sovereign"
    def __init__(self):
        super(c370770, self).__init__(gameobject.Characteristics(**{'color': ['W'], 'text': 'Creatures your opponents control enter the battlefield tapped.', 'power': 2, 'mana_cost': '1W', 'name': 'Imposing Sovereign', 'subtype': ['Human'], 'toughness': 1}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c382983(card.Card):
    "Karmic Guide"
    def __init__(self):
        super(c382983, self).__init__(gameobject.Characteristics(**{'color': ['W'], 'text': 'Flying, protection from black\nEcho {3}{W}{W} (At the beginning of your upkeep, if this came under your control since the beginning of your last upkeep, sacrifice it unless you pay its echo cost.)\nWhen Karmic Guide enters the battlefield, return target creature card from your graveyard to the battlefield.', 'power': 2, 'mana_cost': '3WW', 'name': 'Karmic Guide', 'subtype': ['Angel', 'Spirit'], 'toughness': 2}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Flying]))

class c383063(card.Card):
    "Recurring Nightmare"
    def __init__(self):
        super(c383063, self).__init__(gameobject.Characteristics(**{'color': ['B'], 'name': 'Recurring Nightmare', 'text': "Sacrifice a creature, Return Recurring Nightmare to its owner's hand: Return target creature card from your graveyard to the battlefield. Activate this ability only any time you could cast a sorcery.", 'mana_cost': '2B'}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c383056(card.Card):
    "Psychatog"
    def __init__(self):
        super(c383056, self).__init__(gameobject.Characteristics(**{'color': ['U', 'B'], 'text': 'Discard a card: Psychatog gets +1/+1 until end of turn.\nExile two cards from your graveyard: Psychatog gets +1/+1 until end of turn.', 'power': 1, 'mana_cost': '1UB', 'name': 'Psychatog', 'subtype': ['Atog'], 'toughness': 2}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c423686(card.Card):
    "Felidar Guardian"
    def __init__(self):
        super(c423686, self).__init__(gameobject.Characteristics(**{'color': ['W'], 'text': "When Felidar Guardian enters the battlefield, you may exile another target permanent you control, then return that card to the battlefield under its owner's control.", 'power': 1, 'mana_cost': '3W', 'name': 'Felidar Guardian', 'subtype': ['Cat', 'Beast'], 'toughness': 4}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c423696(card.Card):
    "Baral's Expertise"
    def __init__(self):
        super(c423696, self).__init__(gameobject.Characteristics(**{'color': ['U'], 'name': "Baral's Expertise", 'text': "Return up to three target artifacts and/or creatures to their owners' hands.\nYou may cast a card with converted mana cost 4 or less from your hand without paying its mana cost.", 'mana_cost': '3UU'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c423715(card.Card):
    "Trophy Mage"
    def __init__(self):
        super(c423715, self).__init__(gameobject.Characteristics(**{'color': ['U'], 'text': 'When Trophy Mage enters the battlefield, you may search your library for an artifact card with converted mana cost 3, reveal it, put it into your hand, then shuffle your library.', 'power': 2, 'mana_cost': '2U', 'name': 'Trophy Mage', 'subtype': ['Human', 'Wizard'], 'toughness': 2}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c423742(card.Card):
    "Yahenni's Expertise"
    def __init__(self):
        super(c423742, self).__init__(gameobject.Characteristics(**{'color': ['B'], 'name': "Yahenni's Expertise", 'text': 'All creatures get -3/-3 until end of turn.\nYou may cast a card with converted mana cost 3 or less from your hand without paying its mana cost.', 'mana_cost': '2BB'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c423754(card.Card):
    "Kari Zev, Skyship Raider"
    def __init__(self):
        super(c423754, self).__init__(gameobject.Characteristics(**{'color': ['R'], 'text': "First strike, menace\nWhenever Kari Zev, Skyship Raider attacks, create a legendary 2/1 red Monkey creature token named Ragavan that's tapped and attacking. Exile that token at end of combat.", 'power': 1, 'mana_cost': '1R', 'name': 'Kari Zev, Skyship Raider', 'subtype': ['Human', 'Pirate'], 'toughness': 3}, supertype=[cardtype.SuperType.LEGENDARY], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Menace]))

class c423842(card.Card):
    "Scrap Trawler"
    def __init__(self):
        super(c423842, self).__init__(gameobject.Characteristics(**{'color': '', 'text': 'Whenever Scrap Trawler or another artifact you control is put into a graveyard from the battlefield, return to your hand target artifact card in your graveyard with lesser converted mana cost.', 'power': 3, 'mana_cost': '3', 'name': 'Scrap Trawler', 'subtype': ['Construct'], 'toughness': 2}, supertype=[], types=[cardtype.CardType.ARTIFACT, cardtype.CardType.CREATURE], abilities=[]))

class c146178(card.Card):
    "Shelldock Isle"
    def __init__(self):
        super(c146178, self).__init__(gameobject.Characteristics(**{'color': ['U'], 'name': 'Shelldock Isle', 'text': 'Hideaway (This land enters the battlefield tapped. When it does, look at the top four cards of your library, exile one face down, then put the rest on the bottom of your library.)\n{T}: Add {U} to your mana pool.\n{U}, {T}: You may play the exiled card without paying its mana cost if a library has twenty or fewer cards in it.', 'mana_cost': ''}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c12383(card.Card):
    "Tinker"
    def __init__(self):
        super(c12383, self).__init__(gameobject.Characteristics(**{'color': ['U'], 'name': 'Tinker', 'text': 'As an additional cost to cast Tinker, sacrifice an artifact.\nSearch your library for an artifact card and put that card onto the battlefield. Then shuffle your library.', 'mana_cost': '2U'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c12418(card.Card):
    "Avalanche Riders"
    def __init__(self):
        super(c12418, self).__init__(gameobject.Characteristics(**{'color': ['R'], 'text': 'Haste\nEcho {3}{R} (At the beginning of your upkeep, if this came under your control since the beginning of your last upkeep, sacrifice it unless you pay its echo cost.)\nWhen Avalanche Riders enters the battlefield, destroy target land.', 'power': 2, 'mana_cost': '3R', 'name': 'Avalanche Riders', 'subtype': ['Human', 'Nomad'], 'toughness': 2}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Haste]))

class c397881(card.Card):
    "Remand"
    def __init__(self):
        super(c397881, self).__init__(gameobject.Characteristics(**{'color': ['U'], 'name': 'Remand', 'text': "Counter target spell. If that spell is countered this way, put it into its owner's hand instead of into that player's graveyard.\nDraw a card.", 'mana_cost': '1U'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c368961(card.Card):
    "Aetherling"
    def __init__(self):
        super(c368961, self).__init__(gameobject.Characteristics(**{'color': ['U'], 'text': "{U}: Exile Aetherling. Return it to the battlefield under its owner's control at the beginning of the next end step.\n{U}: Aetherling can't be blocked this turn.\n{1}: Aetherling gets +1/-1 until end of turn.\n{1}: Aetherling gets -1/+1 until end of turn.", 'power': 4, 'mana_cost': '4UU', 'name': 'Aetherling', 'subtype': ['Shapeshifter'], 'toughness': 5}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c368973(card.Card):
    "Notion Thief"
    def __init__(self):
        super(c368973, self).__init__(gameobject.Characteristics(**{'color': ['U', 'B'], 'text': 'Flash\nIf an opponent would draw a card except the first one he or she draws in each of his or her draw steps, instead that player skips that draw and you draw a card.', 'power': 3, 'mana_cost': '2UB', 'name': 'Notion Thief', 'subtype': ['Human', 'Rogue'], 'toughness': 1}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Flash]))

class c259296(card.Card):
    "Mikaeus, the Lunarch"
    def __init__(self):
        super(c259296, self).__init__(gameobject.Characteristics(**{'color': ['W'], 'text': 'Mikaeus, the Lunarch enters the battlefield with X +1/+1 counters on it.\n{T}: Put a +1/+1 counter on Mikaeus.\n{T}, Remove a +1/+1 counter from Mikaeus: Put a +1/+1 counter on each other creature you control.', 'power': 0, 'mana_cost': 'XW', 'name': 'Mikaeus, the Lunarch', 'subtype': ['Human', 'Cleric'], 'toughness': 0}, supertype=[cardtype.SuperType.LEGENDARY], types=[cardtype.CardType.CREATURE], abilities=[]))

class c233068(card.Card):
    "Blade Splicer"
    def __init__(self):
        super(c233068, self).__init__(gameobject.Characteristics(**{'color': ['W'], 'text': 'When Blade Splicer enters the battlefield, create a 3/3 colorless Golem artifact creature token.\nGolem creatures you control have first strike.', 'power': 1, 'mana_cost': '2W', 'name': 'Blade Splicer', 'subtype': ['Human', 'Artificer'], 'toughness': 1}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c218043(card.Card):
    "Porcelain Legionnaire"
    def __init__(self):
        super(c218043, self).__init__(gameobject.Characteristics(**{'color': ['W'], 'text': '({W/P} can be paid with either {W} or 2 life.)\nFirst strike', 'power': 3, 'mana_cost': '2W/P', 'name': 'Porcelain Legionnaire', 'subtype': ['Soldier'], 'toughness': 1}, supertype=[], types=[cardtype.CardType.ARTIFACT, cardtype.CardType.CREATURE], abilities=[]))

class c214365(card.Card):
    "Deceiver Exarch"
    def __init__(self):
        super(c214365, self).__init__(gameobject.Characteristics(**{'color': ['U'], 'text': 'Flash (You may cast this spell any time you could cast an instant.)\nWhen Deceiver Exarch enters the battlefield, choose one —\n• Untap target permanent you control.\n• Tap target permanent an opponent controls.', 'power': 1, 'mana_cost': '2U', 'name': 'Deceiver Exarch', 'subtype': ['Cleric'], 'toughness': 4}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Flash]))

class c214375(card.Card):
    "Phyrexian Metamorph"
    def __init__(self):
        super(c214375, self).__init__(gameobject.Characteristics(**{'color': ['U'], 'text': "({U/P} can be paid with either {U} or 2 life.)\nYou may have Phyrexian Metamorph enter the battlefield as a copy of any artifact or creature on the battlefield, except it's an artifact in addition to its other types.", 'power': 0, 'mana_cost': '3U/P', 'name': 'Phyrexian Metamorph', 'subtype': ['Shapeshifter'], 'toughness': 0}, supertype=[], types=[cardtype.CardType.ARTIFACT, cardtype.CardType.CREATURE], abilities=[]))

class c218006(card.Card):
    "Birthing Pod"
    def __init__(self):
        super(c218006, self).__init__(gameobject.Characteristics(**{'color': ['G'], 'name': 'Birthing Pod', 'text': "({G/P} can be paid with either {G} or 2 life.)\n{1}{G/P}, {T}, Sacrifice a creature: Search your library for a creature card with converted mana cost equal to 1 plus the sacrificed creature's converted mana cost, put that card onto the battlefield, then shuffle your library. Activate this ability only any time you could cast a sorcery.", 'mana_cost': '3G/P'}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c233055(card.Card):
    "Batterskull"
    def __init__(self):
        super(c233055, self).__init__(gameobject.Characteristics(**{'color': '', 'name': 'Batterskull', 'subtype': ['Equipment'], 'text': "Living weapon (When this Equipment enters the battlefield, create a 0/0 black Germ creature token, then attach this to it.)\nEquipped creature gets +4/+4 and has vigilance and lifelink.\n{3}: Return Batterskull to its owner's hand.\nEquip {5}", 'mana_cost': '5'}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c218018(card.Card):
    "Shrine of Burning Rage"
    def __init__(self):
        super(c218018, self).__init__(gameobject.Characteristics(**{'color': '', 'name': 'Shrine of Burning Rage', 'text': 'At the beginning of your upkeep or whenever you cast a red spell, put a charge counter on Shrine of Burning Rage.\n{3}, {T}, Sacrifice Shrine of Burning Rage: Shrine of Burning Rage deals damage equal to the number of charge counters on it to target creature or player.', 'mana_cost': '2'}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c89064(card.Card):
    "Chord of Calling"
    def __init__(self):
        super(c89064, self).__init__(gameobject.Characteristics(**{'color': ['G'], 'name': 'Chord of Calling', 'text': "Convoke (Your creatures can help cast this spell. Each creature you tap while casting this spell pays for {1} or one mana of that creature's color.)\nSearch your library for a creature card with converted mana cost X or less and put it onto the battlefield. Then shuffle your library.", 'mana_cost': 'XGGG'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[abilities.StaticAbilities.Convoke]))

class c244678(card.Card):
    "Heartless Summoning"
    def __init__(self):
        super(c244678, self).__init__(gameobject.Characteristics(**{'color': ['B'], 'name': 'Heartless Summoning', 'text': 'Creature spells you cast cost {2} less to cast.\nCreatures you control get -1/-1.', 'mana_cost': '1B'}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c227087(card.Card):
    "Unburial Rites"
    def __init__(self):
        super(c227087, self).__init__(gameobject.Characteristics(**{'color': ['B', 'W'], 'name': 'Unburial Rites', 'text': 'Return target creature card from your graveyard to the battlefield.\nFlashback {3}{W} (You may cast this card from your graveyard for its flashback cost. Then exile it.)', 'mana_cost': '4B'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[abilities.StaticAbilities.Flash]))

class c241980(card.Card):
    "Clifftop Retreat"
    def __init__(self):
        super(c241980, self).__init__(gameobject.Characteristics(**{'color': ['R', 'W'], 'name': 'Clifftop Retreat', 'text': 'Clifftop Retreat enters the battlefield tapped unless you control a Mountain or a Plains.\n{T}: Add {R} or {W} to your mana pool.', 'mana_cost': ''}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c241988(card.Card):
    "Hinterland Harbor"
    def __init__(self):
        super(c241988, self).__init__(gameobject.Characteristics(**{'color': ['G', 'U'], 'name': 'Hinterland Harbor', 'text': 'Hinterland Harbor enters the battlefield tapped unless you control a Forest or an Island.\n{T}: Add {G} or {U} to your mana pool.', 'mana_cost': ''}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c241987(card.Card):
    "Sulfur Falls"
    def __init__(self):
        super(c241987, self).__init__(gameobject.Characteristics(**{'color': ['U', 'R'], 'name': 'Sulfur Falls', 'text': 'Sulfur Falls enters the battlefield tapped unless you control an Island or a Mountain.\n{T}: Add {U} or {R} to your mana pool.', 'mana_cost': ''}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c241983(card.Card):
    "Woodland Cemetery"
    def __init__(self):
        super(c241983, self).__init__(gameobject.Characteristics(**{'color': ['B', 'G'], 'name': 'Woodland Cemetery', 'text': 'Woodland Cemetery enters the battlefield tapped unless you control a Swamp or a Forest.\n{T}: Add {B} or {G} to your mana pool.', 'mana_cost': ''}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c253624(card.Card):
    "Pack Rat"
    def __init__(self):
        super(c253624, self).__init__(gameobject.Characteristics(**{'color': ['B'], 'text': "Pack Rat's power and toughness are each equal to the number of Rats you control.\n{2}{B}, Discard a card: Create a token that's a copy of Pack Rat.", 'power': '*', 'mana_cost': '1B', 'name': 'Pack Rat', 'subtype': ['Rat'], 'toughness': '*'}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c265392(card.Card):
    "Guttersnipe"
    def __init__(self):
        super(c265392, self).__init__(gameobject.Characteristics(**{'color': ['R'], 'text': 'Whenever you cast an instant or sorcery spell, Guttersnipe deals 2 damage to each opponent.', 'power': 2, 'mana_cost': '2R', 'name': 'Guttersnipe', 'subtype': ['Goblin', 'Shaman'], 'toughness': 2}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c253561(card.Card):
    "Abrupt Decay"
    def __init__(self):
        super(c253561, self).__init__(gameobject.Characteristics(**{'color': ['B', 'G'], 'name': 'Abrupt Decay', 'text': "Abrupt Decay can't be countered by spells or abilities.\nDestroy target nonland permanent with converted mana cost 3 or less.", 'mana_cost': 'BG'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c270356(card.Card):
    "Detention Sphere"
    def __init__(self):
        super(c270356, self).__init__(gameobject.Characteristics(**{'color': ['W', 'U'], 'name': 'Detention Sphere', 'text': "When Detention Sphere enters the battlefield, you may exile target nonland permanent not named Detention Sphere and all other permanents with the same name as that permanent.\nWhen Detention Sphere leaves the battlefield, return the exiled cards to the battlefield under their owner's control.", 'mana_cost': '1WU'}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c253534(card.Card):
    "Sphinx's Revelation"
    def __init__(self):
        super(c253534, self).__init__(gameobject.Characteristics(**{'color': ['W', 'U'], 'name': "Sphinx's Revelation", 'text': 'You gain X life and draw X cards.', 'mana_cost': 'XWUU'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c253596(card.Card):
    "Rakdos Cackler"
    def __init__(self):
        super(c253596, self).__init__(gameobject.Characteristics(**{'color': ['B', 'R'], 'text': "Unleash (You may have this creature enter the battlefield with a +1/+1 counter on it. It can't block as long as it has a +1/+1 counter on it.)", 'power': 1, 'mana_cost': 'B/R', 'name': 'Rakdos Cackler', 'subtype': ['Devil'], 'toughness': 1}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c376563(card.Card):
    "Unexpectedly Absent"
    def __init__(self):
        super(c376563, self).__init__(gameobject.Characteristics(**{'color': ['W'], 'name': 'Unexpectedly Absent', 'text': "Put target nonland permanent into its owner's library just beneath the top X cards of that library.", 'mana_cost': 'XWW'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c376439(card.Card):
    "Ophiomancer"
    def __init__(self):
        super(c376439, self).__init__(gameobject.Characteristics(**{'color': ['B'], 'text': 'At the beginning of each upkeep, if you control no Snakes, create a 1/1 black Snake creature token with deathtouch.', 'power': 2, 'mana_cost': '2B', 'name': 'Ophiomancer', 'subtype': ['Human', 'Shaman'], 'toughness': 2}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c376546(card.Card):
    "Tempt with Vengeance"
    def __init__(self):
        super(c376546, self).__init__(gameobject.Characteristics(**{'color': ['R'], 'name': 'Tempt with Vengeance', 'text': 'Tempting offer — Create X 1/1 red Elemental creature tokens with haste. Each opponent may create X 1/1 red Elemental creature tokens with haste. For each player who does, create X 1/1 red Elemental creature tokens with haste.', 'mana_cost': 'XR'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c376253(card.Card):
    "Avenger of Zendikar"
    def __init__(self):
        super(c376253, self).__init__(gameobject.Characteristics(**{'color': ['G'], 'text': 'When Avenger of Zendikar enters the battlefield, create a 0/1 green Plant creature token for each land you control.\nLandfall — Whenever a land enters the battlefield under your control, you may put a +1/+1 counter on each Plant creature you control.', 'power': 5, 'mana_cost': '5GG', 'name': 'Avenger of Zendikar', 'subtype': ['Elemental'], 'toughness': 5}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c376293(card.Card):
    "Curse of Predation"
    def __init__(self):
        super(c376293, self).__init__(gameobject.Characteristics(**{'color': ['G'], 'name': 'Curse of Predation', 'subtype': ['Aura', 'Curse'], 'text': 'Enchant player\nWhenever a creature attacks enchanted player, put a +1/+1 counter on it.', 'mana_cost': '2G'}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c430667(card.Card):
    "Capsize"
    def __init__(self):
        super(c430667, self).__init__(gameobject.Characteristics(**{'color': ['U'], 'name': 'Capsize', 'text': "Buyback {3} (You may pay an additional {3} as you cast this spell. If you do, put this card into your hand as it resolves.)\nReturn target permanent to its owner's hand.", 'mana_cost': '1UU'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c430668(card.Card):
    "Forbid"
    def __init__(self):
        super(c430668, self).__init__(gameobject.Characteristics(**{'color': ['U'], 'name': 'Forbid', 'text': 'Buyback—Discard two cards. (You may discard two cards in addition to any other costs as you cast this spell. If you do, put this card into your hand as it resolves.)\nCounter target spell.', 'mana_cost': '1UU'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c383258(card.Card):
    "Goblin Rabblemaster"
    def __init__(self):
        super(c383258, self).__init__(gameobject.Characteristics(**{'color': ['R'], 'text': 'Other Goblin creatures you control attack each turn if able.\nAt the beginning of combat on your turn, create a 1/1 red Goblin creature token with haste.\nWhenever Goblin Rabblemaster attacks, it gets +1/+0 until end of turn for each other attacking Goblin.', 'power': 2, 'mana_cost': '2R', 'name': 'Goblin Rabblemaster', 'subtype': ['Goblin', 'Warrior'], 'toughness': 2}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383343(card.Card):
    "Phyrexian Revoker"
    def __init__(self):
        super(c383343, self).__init__(gameobject.Characteristics(**{'color': '', 'text': "As Phyrexian Revoker enters the battlefield, choose a nonland card name.\nActivated abilities of sources with the chosen name can't be activated.", 'power': 2, 'mana_cost': '2', 'name': 'Phyrexian Revoker', 'subtype': ['Horror'], 'toughness': 1}, supertype=[], types=[cardtype.CardType.ARTIFACT, cardtype.CardType.CREATURE], abilities=[]))

class c417577(card.Card):
    "Angel of Invention"
    def __init__(self):
        super(c417577, self).__init__(gameobject.Characteristics(**{'color': ['W'], 'text': 'Flying, vigilance, lifelink\nFabricate 2 (When this creature enters the battlefield, put two +1/+1 counters on it or create two 1/1 colorless Servo artifact creature tokens.)\nOther creatures you control get +1/+1.', 'power': 2, 'mana_cost': '3WW', 'name': 'Angel of Invention', 'subtype': ['Angel'], 'toughness': 1}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Flying, abilities.StaticAbilities.Lifelink, abilities.StaticAbilities.Vigilance]))

class c417632(card.Card):
    "Padeem, Consul of Innovation"
    def __init__(self):
        super(c417632, self).__init__(gameobject.Characteristics(**{'color': ['U'], 'text': 'Artifacts you control have hexproof.\nAt the beginning of your upkeep, if you control the artifact with the highest converted mana cost or tied for the highest converted mana cost, draw a card.', 'power': 1, 'mana_cost': '3U', 'name': 'Padeem, Consul of Innovation', 'subtype': ['Vedalken', 'Artificer'], 'toughness': 4}, supertype=[cardtype.SuperType.LEGENDARY], types=[cardtype.CardType.CREATURE], abilities=[]))

class c417752(card.Card):
    "Dovin Baan"
    def __init__(self):
        super(c417752, self).__init__(gameobject.Characteristics(**{'color': ['W', 'U'], 'name': 'Dovin Baan', 'subtype': ['Dovin'], 'text': '+1: Until your next turn, up to one target creature gets -3/-0 and its activated abilities can\'t be activated.\n−1: You gain 2 life and draw a card.\n−7: You get an emblem with "Your opponents can\'t untap more than two permanents during their untap steps."', 'mana_cost': '2WU'}, supertype=[], types=[cardtype.CardType.PLANESWALKER], abilities=[]))

class c417757(card.Card):
    "Rashmi, Eternities Crafter"
    def __init__(self):
        super(c417757, self).__init__(gameobject.Characteristics(**{'color': ['U', 'G'], 'text': "Whenever you cast your first spell each turn, reveal the top card of your library. If it's a nonland card with converted mana cost less than that spell's, you may cast it without paying its mana cost. If you don't cast the revealed card, put it into your hand.", 'power': 2, 'mana_cost': '2GU', 'name': 'Rashmi, Eternities Crafter', 'subtype': ['Elf', 'Druid'], 'toughness': 3}, supertype=[cardtype.SuperType.LEGENDARY], types=[cardtype.CardType.CREATURE], abilities=[]))

class c417759(card.Card):
    "Saheeli Rai"
    def __init__(self):
        super(c417759, self).__init__(gameobject.Characteristics(**{'color': ['U', 'R'], 'name': 'Saheeli Rai', 'subtype': ['Saheeli'], 'text': "+1: Scry 1. Saheeli Rai deals 1 damage to each opponent.\n−2: Create a token that's a copy of target artifact or creature you control, except it's an artifact in addition to its other types. That token gains haste. Exile it at the beginning of the next end step.\n−7: Search your library for up to three artifact cards with different names, put them onto the battlefield, then shuffle your library.", 'mana_cost': '1UR'}, supertype=[], types=[cardtype.CardType.PLANESWALKER], abilities=[]))

class c417788(card.Card):
    "Foundry Inspector"
    def __init__(self):
        super(c417788, self).__init__(gameobject.Characteristics(**{'color': '', 'text': 'Artifact spells you cast cost {1} less to cast.', 'power': 3, 'mana_cost': '3', 'name': 'Foundry Inspector', 'subtype': ['Construct'], 'toughness': 2}, supertype=[], types=[cardtype.CardType.ARTIFACT, cardtype.CardType.CREATURE], abilities=[]))

class c417795(card.Card):
    "Metalwork Colossus"
    def __init__(self):
        super(c417795, self).__init__(gameobject.Characteristics(**{'color': '', 'text': 'Metalwork Colossus costs {X} less to cast, where X is the total converted mana cost of noncreature artifacts you control.\nSacrifice two artifacts: Return Metalwork Colossus from your graveyard to your hand.', 'power': 10, 'mana_cost': '11', 'name': 'Metalwork Colossus', 'subtype': ['Construct'], 'toughness': 10}, supertype=[], types=[cardtype.CardType.ARTIFACT, cardtype.CardType.CREATURE], abilities=[]))

class c417808(card.Card):
    "Smuggler's Copter"
    def __init__(self):
        super(c417808, self).__init__(gameobject.Characteristics(**{'color': '', 'name': "Smuggler's Copter", 'subtype': ['Vehicle'], 'text': "Flying\nWhenever Smuggler's Copter attacks or blocks, you may draw a card. If you do, discard a card.\nCrew 1 (Tap any number of creatures you control with total power 1 or more: This Vehicle becomes an artifact creature until end of turn.)", 'mana_cost': '2'}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[abilities.StaticAbilities.Flying]))

class c417815(card.Card):
    "Aether Hub"
    def __init__(self):
        super(c417815, self).__init__(gameobject.Characteristics(**{'color': '', 'name': 'Aether Hub', 'text': 'When Aether Hub enters the battlefield, you get {E} (an energy counter).\n{T}: Add {C} to your mana pool.\n{T}, Pay {E}: Add one mana of any color to your mana pool.', 'mana_cost': ''}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c417820(card.Card):
    "Inventors' Fair"
    def __init__(self):
        super(c417820, self).__init__(gameobject.Characteristics(**{'color': '', 'name': "Inventors' Fair", 'text': "At the beginning of your upkeep, if you control three or more artifacts, you gain 1 life.\n{T}: Add {C} to your mana pool.\n{4}, {T}, Sacrifice Inventors' Fair: Search your library for an artifact card, reveal it, put it into your hand, then shuffle your library. Activate this ability only if you control three or more artifacts.", 'mana_cost': ''}, supertype=[cardtype.SuperType.LEGENDARY], types=[cardtype.CardType.LAND], abilities=[]))

class c391927(card.Card):
    "Soulfire Grand Master"
    def __init__(self):
        super(c391927, self).__init__(gameobject.Characteristics(**{'color': ['W', 'U', 'R'], 'text': 'Lifelink\nInstant and sorcery spells you control have lifelink.\n{2}{U/R}{U/R}: The next time you cast an instant or sorcery spell from your hand this turn, put that card into your hand instead of into your graveyard as it resolves.', 'power': 2, 'mana_cost': '1W', 'name': 'Soulfire Grand Master', 'subtype': ['Human', 'Monk'], 'toughness': 2}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Lifelink]))

class c391937(card.Card):
    "Tasigur, the Golden Fang"
    def __init__(self):
        super(c391937, self).__init__(gameobject.Characteristics(**{'color': ['B', 'G', 'U'], 'text': "Delve (Each card you exile from your graveyard while casting this spell pays for {1}.)\n{2}{G/U}{G/U}: Put the top two cards of your library into your graveyard, then return a nonland card of an opponent's choice from your graveyard to your hand.", 'power': 4, 'mana_cost': '5B', 'name': 'Tasigur, the Golden Fang', 'subtype': ['Human', 'Shaman'], 'toughness': 5}, supertype=[cardtype.SuperType.LEGENDARY], types=[cardtype.CardType.CREATURE], abilities=[]))

class c391958(card.Card):
    "Whisperwood Elemental"
    def __init__(self):
        super(c391958, self).__init__(gameobject.Characteristics(**{'color': ['G'], 'text': 'At the beginning of your end step, manifest the top card of your library. (Put it onto the battlefield face down as a 2/2 creature. Turn it face up any time for its mana cost if it\'s a creature card.)\nSacrifice Whisperwood Elemental: Until end of turn, face-up nontoken creatures you control gain "When this creature dies, manifest the top card of your library."', 'power': 4, 'mana_cost': '3GG', 'name': 'Whisperwood Elemental', 'subtype': ['Elemental'], 'toughness': 4}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c4642(card.Card):
    "Coffin Queen"
    def __init__(self):
        super(c4642, self).__init__(gameobject.Characteristics(**{'color': ['B'], 'text': 'You may choose not to untap Coffin Queen during your untap step.\n{2}{B}, {T}: Put target creature card from a graveyard onto the battlefield under your control. When Coffin Queen becomes untapped or you lose control of Coffin Queen, exile that creature.', 'power': 1, 'mana_cost': '2B', 'name': 'Coffin Queen', 'subtype': ['Zombie', 'Wizard'], 'toughness': 1}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c416784(card.Card):
    "Arcane Savant"
    def __init__(self):
        super(c416784, self).__init__(gameobject.Characteristics(**{'color': ['U'], 'text': "Before you shuffle your deck to start the game, you may reveal this card from your deck and exile an instant or sorcery card you drafted that isn't in your deck.\nWhen Arcane Savant enters the battlefield, copy a card you exiled with cards named Arcane Savant. You may cast the copy without paying its mana cost.", 'power': 3, 'mana_cost': '3UU', 'name': 'Arcane Savant', 'subtype': ['Human', 'Wizard'], 'toughness': 3}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c416798(card.Card):
    "Custodi Lich"
    def __init__(self):
        super(c416798, self).__init__(gameobject.Characteristics(**{'color': ['B'], 'text': 'When Custodi Lich enters the battlefield, you become the monarch.\nWhenever you become the monarch, target player sacrifices a creature.', 'power': 4, 'mana_cost': '3BB', 'name': 'Custodi Lich', 'subtype': ['Zombie', 'Cleric'], 'toughness': 2}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c416819(card.Card):
    "Caller of the Untamed"
    def __init__(self):
        super(c416819, self).__init__(gameobject.Characteristics(**{'color': ['G'], 'text': "Before you shuffle your deck to start the game, you may reveal this card from your deck and exile a creature card you drafted that isn't in your deck.\n{X}, {T}: Create a token that's a copy of a card you exiled with cards named Caller of the Untamed. X is the converted mana cost of that card.", 'power': 2, 'mana_cost': '3G', 'name': 'Caller of the Untamed', 'subtype': ['Elf', 'Shaman'], 'toughness': 4}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c416756(card.Card):
    "Umezawa's Jitte"
    def __init__(self):
        super(c416756, self).__init__(gameobject.Characteristics(**{'color': '', 'name': "Umezawa's Jitte", 'subtype': ['Equipment'], 'text': "Whenever equipped creature deals combat damage, put two charge counters on Umezawa's Jitte.\nRemove a charge counter from Umezawa's Jitte: Choose one —\n• Equipped creature gets +2/+2 until end of turn.\n• Target creature gets -1/-1 until end of turn.\n• You gain 2 life.\nEquip {2}", 'mana_cost': '2'}, supertype=[cardtype.SuperType.LEGENDARY], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c270445(card.Card):
    "Thalia, Guardian of Thraben"
    def __init__(self):
        super(c270445, self).__init__(gameobject.Characteristics(**{'color': ['W'], 'text': 'First strike\nNoncreature spells cost {1} more to cast.', 'power': 2, 'mana_cost': '1W', 'name': 'Thalia, Guardian of Thraben', 'subtype': ['Human', 'Soldier'], 'toughness': 1}, supertype=[cardtype.SuperType.LEGENDARY], types=[cardtype.CardType.CREATURE], abilities=[]))

class c243250(card.Card):
    "Geralf's Messenger"
    def __init__(self):
        super(c243250, self).__init__(gameobject.Characteristics(**{'color': ['B'], 'text': "Geralf's Messenger enters the battlefield tapped.\nWhen Geralf's Messenger enters the battlefield, target opponent loses 2 life.\nUndying (When this creature dies, if it had no +1/+1 counters on it, return it to the battlefield under its owner's control with a +1/+1 counter on it.)", 'power': 3, 'mana_cost': 'BBB', 'name': "Geralf's Messenger", 'subtype': ['Zombie'], 'toughness': 2}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c226874(card.Card):
    "Hellrider"
    def __init__(self):
        super(c226874, self).__init__(gameobject.Characteristics(**{'color': ['R'], 'text': 'Haste\nWhenever a creature you control attacks, Hellrider deals 1 damage to defending player.', 'power': 3, 'mana_cost': '2RR', 'name': 'Hellrider', 'subtype': ['Devil'], 'toughness': 3}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Haste]))

class c262671(card.Card):
    "Strangleroot Geist"
    def __init__(self):
        super(c262671, self).__init__(gameobject.Characteristics(**{'color': ['G'], 'text': "Haste\nUndying (When this creature dies, if it had no +1/+1 counters on it, return it to the battlefield under its owner's control with a +1/+1 counter on it.)", 'power': 2, 'mana_cost': 'GG', 'name': 'Strangleroot Geist', 'subtype': ['Spirit'], 'toughness': 1}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Haste]))

class c262847(card.Card):
    "Falkenrath Aristocrat"
    def __init__(self):
        super(c262847, self).__init__(gameobject.Characteristics(**{'color': ['B', 'R'], 'text': 'Flying, haste\nSacrifice a creature: Falkenrath Aristocrat gains indestructible until end of turn. If the sacrificed creature was a Human, put a +1/+1 counter on Falkenrath Aristocrat.', 'power': 4, 'mana_cost': '2BR', 'name': 'Falkenrath Aristocrat', 'subtype': ['Vampire'], 'toughness': 1}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Flying, abilities.StaticAbilities.Haste]))

class c118918(card.Card):
    "Looter il-Kor"
    def __init__(self):
        super(c118918, self).__init__(gameobject.Characteristics(**{'color': ['U'], 'text': 'Shadow (This creature can block or be blocked by only creatures with shadow.)\nWhenever Looter il-Kor deals damage to an opponent, draw a card, then discard a card.', 'power': 1, 'mana_cost': '1U', 'name': 'Looter il-Kor', 'subtype': ['Kor', 'Rogue'], 'toughness': 1}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c425986(card.Card):
    "Domri Rade"
    def __init__(self):
        super(c425986, self).__init__(gameobject.Characteristics(**{'color': ['R', 'G'], 'name': 'Domri Rade', 'subtype': ['Domri'], 'text': '+1: Look at the top card of your library. If it\'s a creature card, you may reveal it and put it into your hand.\n−2: Target creature you control fights another target creature.\n−7: You get an emblem with "Creatures you control have double strike, trample, hexproof, and haste."', 'mana_cost': '1RG'}, supertype=[], types=[cardtype.CardType.PLANESWALKER], abilities=[abilities.StaticAbilities.Hexproof, abilities.StaticAbilities.Trample]))

class c425990(card.Card):
    "Ghor-Clan Rampager"
    def __init__(self):
        super(c425990, self).__init__(gameobject.Characteristics(**{'color': ['R', 'G'], 'text': 'Trample\nBloodrush — {R}{G}, Discard Ghor-Clan Rampager: Target attacking creature gets +4/+4 and gains trample until end of turn.', 'power': 4, 'mana_cost': '2RG', 'name': 'Ghor-Clan Rampager', 'subtype': ['Beast'], 'toughness': 4}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Trample]))

class c426031(card.Card):
    "Boros Reckoner"
    def __init__(self):
        super(c426031, self).__init__(gameobject.Characteristics(**{'color': ['W', 'R'], 'text': 'Whenever Boros Reckoner is dealt damage, it deals that much damage to target creature or player.\n{R/W}: Boros Reckoner gains first strike until end of turn.', 'power': 3, 'mana_cost': 'R/WR/WR/W', 'name': 'Boros Reckoner', 'subtype': ['Minotaur', 'Wizard'], 'toughness': 3}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c74647(card.Card):
    "Hokori, Dust Drinker"
    def __init__(self):
        super(c74647, self).__init__(gameobject.Characteristics(**{'color': ['W'], 'text': "Lands don't untap during their controllers' untap steps.\nAt the beginning of each player's upkeep, that player untaps a land he or she controls.", 'power': 2, 'mana_cost': '2WW', 'name': 'Hokori, Dust Drinker', 'subtype': ['Spirit'], 'toughness': 2}, supertype=[cardtype.SuperType.LEGENDARY], types=[cardtype.CardType.CREATURE], abilities=[]))

class c366470(card.Card):
    "Assemble the Legion"
    def __init__(self):
        super(c366470, self).__init__(gameobject.Characteristics(**{'color': ['W', 'R'], 'name': 'Assemble the Legion', 'text': 'At the beginning of your upkeep, put a muster counter on Assemble the Legion. Then create a 1/1 red and white Soldier creature token with haste for each muster counter on Assemble the Legion.', 'mana_cost': '3RW'}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c366473(card.Card):
    "Dimir Charm"
    def __init__(self):
        super(c366473, self).__init__(gameobject.Characteristics(**{'color': ['U', 'B'], 'name': 'Dimir Charm', 'text': "Choose one —\n• Counter target sorcery spell.\n• Destroy target creature with power 2 or less.\n• Look at the top three cards of target player's library. Put one back and the rest into that player's graveyard.", 'mana_cost': 'UB'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c198383(card.Card):
    "Stoneforge Mystic"
    def __init__(self):
        super(c198383, self).__init__(gameobject.Characteristics(**{'color': ['W'], 'text': 'When Stoneforge Mystic enters the battlefield, you may search your library for an Equipment card, reveal it, put it into your hand, then shuffle your library.\n{1}{W}, {T}: You may put an Equipment card from your hand onto the battlefield.', 'power': 1, 'mana_cost': '1W', 'name': 'Stoneforge Mystic', 'subtype': ['Kor', 'Artificer'], 'toughness': 2}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c197854(card.Card):
    "Dragonmaster Outcast"
    def __init__(self):
        super(c197854, self).__init__(gameobject.Characteristics(**{'color': ['R'], 'text': 'At the beginning of your upkeep, if you control six or more lands, create a 5/5 red Dragon creature token with flying.', 'power': 1, 'mana_cost': 'R', 'name': 'Dragonmaster Outcast', 'subtype': ['Human', 'Shaman'], 'toughness': 1}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c177545(card.Card):
    "Celestial Colonnade"
    def __init__(self):
        super(c177545, self).__init__(gameobject.Characteristics(**{'color': ['W', 'U'], 'name': 'Celestial Colonnade', 'text': "Celestial Colonnade enters the battlefield tapped.\n{T}: Add {W} or {U} to your mana pool.\n{3}{W}{U}: Until end of turn, Celestial Colonnade becomes a 4/4 white and blue Elemental creature with flying and vigilance. It's still a land.", 'mana_cost': ''}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c177560(card.Card):
    "Stirring Wildwood"
    def __init__(self):
        super(c177560, self).__init__(gameobject.Characteristics(**{'color': ['G', 'W'], 'name': 'Stirring Wildwood', 'text': "Stirring Wildwood enters the battlefield tapped.\n{T}: Add {G} or {W} to your mana pool.\n{1}{G}{W}: Until end of turn, Stirring Wildwood becomes a 3/4 green and white Elemental creature with reach. It's still a land.", 'mana_cost': ''}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c213818(card.Card):
    "Accorder Paladin"
    def __init__(self):
        super(c213818, self).__init__(gameobject.Characteristics(**{'color': ['W'], 'text': 'Battle cry (Whenever this creature attacks, each other attacking creature gets +1/+0 until end of turn.)', 'power': 3, 'mana_cost': '1W', 'name': 'Accorder Paladin', 'subtype': ['Human', 'Knight'], 'toughness': 1}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c214064(card.Card):
    "Hero of Bladehold"
    def __init__(self):
        super(c214064, self).__init__(gameobject.Characteristics(**{'color': ['W'], 'text': 'Battle cry (Whenever this creature attacks, each other attacking creature gets +1/+0 until end of turn.)\nWhenever Hero of Bladehold attacks, create two 1/1 white Soldier creature tokens that are tapped and attacking.', 'power': 3, 'mana_cost': '2WW', 'name': 'Hero of Bladehold', 'subtype': ['Human', 'Knight'], 'toughness': 4}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c213799(card.Card):
    "Go for the Throat"
    def __init__(self):
        super(c213799, self).__init__(gameobject.Characteristics(**{'color': ['B'], 'name': 'Go for the Throat', 'text': 'Destroy target nonartifact creature.', 'mana_cost': '1B'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c221559(card.Card):
    "Green Sun's Zenith"
    def __init__(self):
        super(c221559, self).__init__(gameobject.Characteristics(**{'color': ['G'], 'name': "Green Sun's Zenith", 'text': "Search your library for a green creature card with converted mana cost X or less, put it onto the battlefield, then shuffle your library. Shuffle Green Sun's Zenith into its owner's library.", 'mana_cost': 'XG'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c413573(card.Card):
    "Squadron Hawk"
    def __init__(self):
        super(c413573, self).__init__(gameobject.Characteristics(**{'color': ['W'], 'text': 'Flying\nWhen Squadron Hawk enters the battlefield, you may search your library for up to three cards named Squadron Hawk, reveal them, put them into your hand, then shuffle your library.', 'power': 1, 'mana_cost': '1W', 'name': 'Squadron Hawk', 'subtype': ['Bird'], 'toughness': 1}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Flying]))

class c413624(card.Card):
    "Braids, Cabal Minion"
    def __init__(self):
        super(c413624, self).__init__(gameobject.Characteristics(**{'color': ['B'], 'text': "At the beginning of each player's upkeep, that player sacrifices an artifact, creature, or land.", 'power': 2, 'mana_cost': '2BB', 'name': 'Braids, Cabal Minion', 'subtype': ['Human', 'Minion'], 'toughness': 2}, supertype=[cardtype.SuperType.LEGENDARY], types=[cardtype.CardType.CREATURE], abilities=[]))

class c414292(card.Card):
    "Distended Mindbender"
    def __init__(self):
        super(c414292, self).__init__(gameobject.Characteristics(**{'color': ['B'], 'text': "Emerge {5}{B}{B} (You may cast this spell by sacrificing a creature and paying the emerge cost reduced by that creature's converted mana cost.)\nWhen you cast Distended Mindbender, target opponent reveals his or her hand. You choose from it a nonland card with converted mana cost 3 or less and a card with converted mana cost 4 or greater. That player discards those cards.", 'power': 5, 'mana_cost': '8', 'name': 'Distended Mindbender', 'subtype': ['Eldrazi', 'Insect'], 'toughness': 5}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c414302(card.Card):
    "Blessed Alliance"
    def __init__(self):
        super(c414302, self).__init__(gameobject.Characteristics(**{'color': ['W'], 'name': 'Blessed Alliance', 'text': 'Escalate {2} (Pay this cost for each mode chosen beyond the first.)\nChoose one or more —\n• Target player gains 4 life.\n• Untap up to two target creatures.\n• Target opponent sacrifices an attacking creature.', 'mana_cost': '1W'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c414332(card.Card):
    "Selfless Spirit"
    def __init__(self):
        super(c414332, self).__init__(gameobject.Characteristics(**{'color': ['W'], 'text': 'Flying\nSacrifice Selfless Spirit: Creatures you control gain indestructible until end of turn.', 'power': 2, 'mana_cost': '1W', 'name': 'Selfless Spirit', 'subtype': ['Spirit', 'Cleric'], 'toughness': 1}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Flying]))

class c414338(card.Card):
    "Thalia, Heretic Cathar"
    def __init__(self):
        super(c414338, self).__init__(gameobject.Characteristics(**{'color': ['W'], 'text': 'First strike\nCreatures and nonbasic lands your opponents control enter the battlefield tapped.', 'power': 3, 'mana_cost': '2W', 'name': 'Thalia, Heretic Cathar', 'subtype': ['Human', 'Soldier'], 'toughness': 2}, supertype=[cardtype.SuperType.LEGENDARY], types=[cardtype.CardType.CREATURE], abilities=[]))

class c414375(card.Card):
    "Wharf Infiltrator"
    def __init__(self):
        super(c414375, self).__init__(gameobject.Characteristics(**{'color': ['U'], 'text': "Skulk (This creature can't be blocked by creatures with greater power.)\nWhenever Wharf Infiltrator deals combat damage to a player, you may draw a card. If you do, discard a card.\nWhenever you discard a creature card, you may pay {2}. If you do, create a 3/2 colorless Eldrazi Horror creature token.", 'power': 1, 'mana_cost': '1U', 'name': 'Wharf Infiltrator', 'subtype': ['Human', 'Horror'], 'toughness': 1}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c414463(card.Card):
    "Ishkanah, Grafwidow"
    def __init__(self):
        super(c414463, self).__init__(gameobject.Characteristics(**{'color': ['G', 'B'], 'text': 'Reach\nDelirium — When Ishkanah, Grafwidow enters the battlefield, if there are four or more card types among cards in your graveyard, create three 1/2 green Spider creature tokens with reach.\n{6}{B}: Target opponent loses 1 life for each Spider you control.', 'power': 3, 'mana_cost': '4G', 'name': 'Ishkanah, Grafwidow', 'subtype': ['Spider'], 'toughness': 5}, supertype=[cardtype.SuperType.LEGENDARY], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Reach]))

class c414467(card.Card):
    "Permeating Mass"
    def __init__(self):
        super(c414467, self).__init__(gameobject.Characteristics(**{'color': ['G'], 'text': 'Whenever Permeating Mass deals combat damage to a creature, that creature becomes a copy of Permeating Mass.', 'power': 1, 'mana_cost': 'G', 'name': 'Permeating Mass', 'subtype': ['Spirit'], 'toughness': 3}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c414489(card.Card):
    "Grim Flayer"
    def __init__(self):
        super(c414489, self).__init__(gameobject.Characteristics(**{'color': ['B', 'G'], 'text': 'Trample\nWhenever Grim Flayer deals combat damage to a player, look at the top three cards of your library. Put any number of them into your graveyard and the rest back on top of your library in any order.\nDelirium — Grim Flayer gets +2/+2 as long as there are four or more card types among cards in your graveyard.', 'power': 2, 'mana_cost': 'BG', 'name': 'Grim Flayer', 'subtype': ['Human', 'Warrior'], 'toughness': 2}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Trample]))

class c205059(card.Card):
    "Fauna Shaman"
    def __init__(self):
        super(c205059, self).__init__(gameobject.Characteristics(**{'color': ['G'], 'text': '{G}, {T}, Discard a creature card: Search your library for a creature card, reveal it, and put it into your hand. Then shuffle your library.', 'power': 2, 'mana_cost': '1G', 'name': 'Fauna Shaman', 'subtype': ['Elf', 'Shaman'], 'toughness': 2}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c433145(card.Card):
    "Hedron Archive"
    def __init__(self):
        super(c433145, self).__init__(gameobject.Characteristics(**{'color': '', 'name': 'Hedron Archive', 'text': '{T}: Add {C}{C} to your mana pool.\n{2}, {T}, Sacrifice Hedron Archive: Draw two cards.', 'mana_cost': '4'}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c380410(card.Card):
    "Eidolon of the Great Revel"
    def __init__(self):
        super(c380410, self).__init__(gameobject.Characteristics(**{'color': ['R'], 'text': 'Whenever a player casts a spell with converted mana cost 3 or less, Eidolon of the Great Revel deals 2 damage to that player.', 'power': 2, 'mana_cost': 'RR', 'name': 'Eidolon of the Great Revel', 'subtype': ['Spirit'], 'toughness': 2}, supertype=[], types=[cardtype.CardType.ENCHANTMENT, cardtype.CardType.CREATURE], abilities=[]))

class c380495(card.Card):
    "Setessan Tactics"
    def __init__(self):
        super(c380495, self).__init__(gameobject.Characteristics(**{'color': ['G'], 'name': 'Setessan Tactics', 'text': 'Strive — Setessan Tactics costs {G} more to cast for each target beyond the first.\nUntil end of turn, any number of target creatures each get +1/+1 and gain "{T}: This creature fights another target creature."', 'mana_cost': '1G'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c402001(card.Card):
    "Quarantine Field"
    def __init__(self):
        super(c402001, self).__init__(gameobject.Characteristics(**{'color': ['W'], 'name': 'Quarantine Field', 'text': 'Quarantine Field enters the battlefield with X isolation counters on it.\nWhen Quarantine Field enters the battlefield, for each isolation counter on it, exile up to one target nonland permanent an opponent controls until Quarantine Field leaves the battlefield.', 'mana_cost': 'XXWW'}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c402101(card.Card):
    "Zulaport Cutthroat"
    def __init__(self):
        super(c402101, self).__init__(gameobject.Characteristics(**{'color': ['B'], 'text': 'Whenever Zulaport Cutthroat or another creature you control dies, each opponent loses 1 life and you gain 1 life.', 'power': 1, 'mana_cost': '1B', 'name': 'Zulaport Cutthroat', 'subtype': ['Human', 'Rogue', 'Ally'], 'toughness': 1}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c401912(card.Card):
    "Herald of Kozilek"
    def __init__(self):
        super(c401912, self).__init__(gameobject.Characteristics(**{'color': ['U', 'R'], 'text': 'Devoid (This card has no color.)\nColorless spells you cast cost {1} less to cast.', 'power': 2, 'mana_cost': '1UR', 'name': 'Herald of Kozilek', 'subtype': ['Eldrazi', 'Drone'], 'toughness': 4}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c401931(card.Card):
    "Kiora, Master of the Depths"
    def __init__(self):
        super(c401931, self).__init__(gameobject.Characteristics(**{'color': ['U', 'G'], 'name': 'Kiora, Master of the Depths', 'subtype': ['Kiora'], 'text': '+1: Untap up to one target creature and up to one target land.\n−2: Reveal the top four cards of your library. You may put a creature card and/or a land card from among them into your hand. Put the rest into your graveyard.\n−8: You get an emblem with "Whenever a creature enters the battlefield under your control, you may have it fight target creature." Then create three 8/8 blue Octopus creature tokens.', 'mana_cost': '2GU'}, supertype=[], types=[cardtype.CardType.PLANESWALKER], abilities=[]))

class c401943(card.Card):
    "Lumbering Falls"
    def __init__(self):
        super(c401943, self).__init__(gameobject.Characteristics(**{'color': ['G', 'U'], 'name': 'Lumbering Falls', 'text': "Lumbering Falls enters the battlefield tapped.\n{T}: Add {G} or {U} to your mana pool.\n{2}{G}{U}: Lumbering Falls becomes a 3/3 green and blue Elemental creature with hexproof until end of turn. It's still a land.", 'mana_cost': ''}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c402031(card.Card):
    "Shambling Vent"
    def __init__(self):
        super(c402031, self).__init__(gameobject.Characteristics(**{'color': ['W', 'B'], 'name': 'Shambling Vent', 'text': "Shambling Vent enters the battlefield tapped.\n{T}: Add {W} or {B} to your mana pool.\n{1}{W}{B}: Shambling Vent becomes a 2/3 white and black Elemental creature with lifelink until end of turn. It's still a land.", 'mana_cost': ''}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

