from MTG.card import *
from MTG.gameObject import *


class c221309(Card):
    "Plains"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c221309, self).__init__(Characteristics(**{'name': 'Plains', 'subtype': ['Plains'], 'mana_cost': '', 'text': 'W', 'color': []}, supertype=[SuperType.BASIC], types=[CardType.LAND], abilities=[]))


class c221300(Card):
    "Island"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c221300, self).__init__(Characteristics(**{'name': 'Island', 'subtype': ['Island'], 'mana_cost': '', 'text': 'U', 'color': []}, supertype=[SuperType.BASIC], types=[CardType.LAND], abilities=[]))


class c26805(Card):
    "Tundra Kavu"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c26805, self).__init__(Characteristics(**{'power': 2, 'text': '{T}: Target land becomes a Plains or an Island until end of turn.', 'color': ['R'], 'name': 'Tundra Kavu', 'toughness': 2, 'subtype': ['Kavu'], 'mana_cost': '2R'}, supertype=[], types=[CardType.CREATURE], abilities=[]))


class c79145(Card):
    "Hundred-Talon Kami"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c79145, self).__init__(Characteristics(**{'power': 2, 'text': 'Flying\nSoulshift 4 (When this creature dies, you may return target Spirit card with converted mana cost 4 or less from your graveyard to your hand.)', 'color': ['W'], 'name': 'Hundred-Talon Kami', 'toughness': 3, 'subtype': ['Spirit'], 'mana_cost': '4W'}, supertype=[], types=[CardType.CREATURE], abilities=[StaticAbilities.Flying]))


class c370698(Card):
    "Blood Bairn"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c370698, self).__init__(Characteristics(**{'power': 2, 'text': 'Sacrifice another creature: Blood Bairn gets +2/+2 until end of turn.', 'color': ['B'], 'name': 'Blood Bairn', 'toughness': 2, 'subtype': ['Vampire'], 'mana_cost': '2B'}, supertype=[], types=[CardType.CREATURE], abilities=[]))


class c3060(Card):
    "Soldevi Sentry"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c3060, self).__init__(Characteristics(**{'power': 1, 'text': '{1}: Choose target opponent. Regenerate Soldevi Sentry. When it regenerates this way, that player may draw a card.', 'color': [], 'name': 'Soldevi Sentry', 'toughness': 1, 'subtype': ['Soldier'], 'mana_cost': '1'}, supertype=[], types=[CardType.ARTIFACT, CardType.CREATURE], abilities=[]))


class c34243(Card):
    "Ancestor's Chosen"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c34243, self).__init__(Characteristics(**{'power': 4, 'text': "First strike (This creature deals combat damage before creatures without first strike.)\nWhen Ancestor's Chosen enters the battlefield, you gain 1 life for each card in your graveyard.", 'color': ['W'], 'name': "Ancestor's Chosen", 'toughness': 4, 'subtype': ['Human', 'Cleric'], 'mana_cost': '5WW'}, supertype=[], types=[CardType.CREATURE], abilities=[]))


class c174799(Card):
    "Hellspark Elemental"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c174799, self).__init__(Characteristics(**{'power': 3, 'text': 'Trample, haste\nAt the beginning of the end step, sacrifice Hellspark Elemental.\nUnearth {1}{R} ({1}{R}: Return this card from your graveyard to the battlefield. It gains haste. Exile it at the beginning of the next end step or if it would leave the battlefield. Unearth only as a sorcery.)', 'color': ['R'], 'name': 'Hellspark Elemental', 'toughness': 1, 'subtype': ['Elemental'], 'mana_cost': '1R'}, supertype=[], types=[CardType.CREATURE], abilities=[StaticAbilities.Haste, StaticAbilities.Trample]))


class c179594(Card):
    "Sewn-Eye Drake"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c179594, self).__init__(Characteristics(**{'power': 3, 'text': 'Flying, haste', 'color': ['U', 'B', 'R'], 'name': 'Sewn-Eye Drake', 'toughness': 1, 'subtype': ['Zombie', 'Drake'], 'mana_cost': '2(U/R)B'}, supertype=[], types=[CardType.CREATURE], abilities=[StaticAbilities.Flying, StaticAbilities.Haste]))


class c29973(Card):
    "Price of Glory"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c29973, self).__init__(Characteristics(**{'name': 'Price of Glory', 'mana_cost': '2R', 'text': "Whenever a player taps a land for mana, if it's not that player's turn, destroy that land.", 'color': ['R']}, supertype=[], types=[CardType.ENCHANTMENT], abilities=[]))


class c21190(Card):
    "Sun Clasp"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c21190, self).__init__(Characteristics(**{'name': 'Sun Clasp', 'subtype': ['Aura'], 'mana_cost': '1W', 'text': "Enchant creature\nEnchanted creature gets +1/+3.\n{W}: Return enchanted creature to its owner's hand.", 'color': ['W']}, supertype=[], types=[CardType.ENCHANTMENT], abilities=[]))


class c2473(Card):
    "Mind Whip"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c2473, self).__init__(Characteristics(**{'name': 'Mind Whip', 'subtype': ['Aura'], 'mana_cost': '2BB', 'text': "Enchant creature\nAt the beginning of the upkeep of enchanted creature's controller, that player may pay {3}. If he or she doesn't, Mind Whip deals 2 damage to that player and you tap that creature.", 'color': ['B']}, supertype=[], types=[CardType.ENCHANTMENT], abilities=[]))


class c5806(Card):
    "Fluctuator"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c5806, self).__init__(Characteristics(**{'name': 'Fluctuator', 'mana_cost': '2', 'text': 'Cycling abilities you activate cost you up to {2} less to activate.', 'color': []}, supertype=[], types=[CardType.ARTIFACT], abilities=[]))


class c230762(Card):
    "Slaughter Cry"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c230762, self).__init__(Characteristics(**{'name': 'Slaughter Cry', 'mana_cost': '2R', 'text': 'Target creature gets +3/+0 and gains first strike until end of turn. (It deals combat damage before creatures without first strike.)', 'color': ['R']}, supertype=[], types=[CardType.INSTANT], abilities=[]))


class c24615(Card):
    "Despoil"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c24615, self).__init__(Characteristics(**{'name': 'Despoil', 'mana_cost': '3B', 'text': 'Destroy target land. Its controller loses 2 life.', 'color': ['B']}, supertype=[], types=[CardType.SORCERY], abilities=[]))


class c22061(Card):
    "Overlaid Terrain"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c22061, self).__init__(Characteristics(**{'name': 'Overlaid Terrain', 'mana_cost': '2GG', 'text': 'As Overlaid Terrain enters the battlefield, sacrifice all lands you control.\nLands you control have "{T}: Add two mana of any one color to your mana pool."', 'color': ['G']}, supertype=[], types=[CardType.ENCHANTMENT], abilities=[]))


class c215101(Card):
    "Ogre Geargrabber"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c215101, self).__init__(Characteristics(**{'power': 4, 'text': 'Whenever Ogre Geargrabber attacks, gain control of target Equipment an opponent controls until end of turn. Attach it to Ogre Geargrabber. When you lose control of that Equipment, unattach it.', 'color': ['R'], 'name': 'Ogre Geargrabber', 'toughness': 4, 'subtype': ['Ogre', 'Warrior'], 'mana_cost': '4RR'}, supertype=[], types=[CardType.CREATURE], abilities=[]))


class c96920(Card):
    "Vedalken Plotter"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c96920, self).__init__(Characteristics(**{'power': 1, 'text': 'When Vedalken Plotter enters the battlefield, exchange control of target land you control and target land an opponent controls.', 'color': ['U'], 'name': 'Vedalken Plotter', 'toughness': 1, 'subtype': ['Vedalken', 'Wizard'], 'mana_cost': '2U'}, supertype=[], types=[CardType.CREATURE], abilities=[]))


class c1476(Card):
    "Devouring Deep"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c1476, self).__init__(Characteristics(**{'power': 1, 'text': 'Islandwalk', 'color': ['U'], 'name': 'Devouring Deep', 'toughness': 2, 'subtype': ['Fish'], 'mana_cost': '2U'}, supertype=[], types=[CardType.CREATURE], abilities=[StaticAbilities.Islandwalk]))


class c49055(Card):
    "Temporal Cascade"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c49055, self).__init__(Characteristics(**{'name': 'Temporal Cascade', 'mana_cost': '5UU', 'text': 'Choose one - Each player shuffles his or her hand and graveyard into his or her library; or each player draws seven cards.\nEntwine {2} (Choose both if you pay the entwine cost.)', 'color': ['U']}, supertype=[], types=[CardType.SORCERY], abilities=[]))


class c50176(Card):
    "Myr Quadropod"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c50176, self).__init__(Characteristics(**{'power': 1, 'text': "{3}: Switch Myr Quadropod's power and toughness until end of turn.", 'color': [], 'name': 'Myr Quadropod', 'toughness': 4, 'subtype': ['Myr'], 'mana_cost': '4'}, supertype=[], types=[CardType.ARTIFACT, CardType.CREATURE], abilities=[]))


class c233086(Card):
    "Flameborn Viron"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c233086, self).__init__(Characteristics(**{'power': 6, 'text': '', 'color': ['R'], 'name': 'Flameborn Viron', 'toughness': 4, 'subtype': ['Insect'], 'mana_cost': '4RR'}, supertype=[], types=[CardType.CREATURE], abilities=[]))


class c226561(Card):
    "Taste of Blood"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c226561, self).__init__(Characteristics(**{'name': 'Taste of Blood', 'mana_cost': 'B', 'text': 'Taste of Blood deals 1 damage to target player and you gain 1 life.', 'color': ['B']}, supertype=[], types=[CardType.SORCERY], abilities=[]))


class c240039(Card):
    "Homicidal Seclusion"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c240039, self).__init__(Characteristics(**{'name': 'Homicidal Seclusion', 'mana_cost': '4B', 'text': 'As long as you control exactly one creature, that creature gets +3/+1 and has lifelink.', 'color': ['B']}, supertype=[], types=[CardType.ENCHANTMENT], abilities=[]))


class c3610(Card):
    "Brood of Cockroaches"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c3610, self).__init__(Characteristics(**{'power': 1, 'text': 'When Brood of Cockroaches is put into your graveyard from the battlefield, at the beginning of the next end step, you lose 1 life and return Brood of Cockroaches to your hand.', 'color': ['B'], 'name': 'Brood of Cockroaches', 'toughness': 1, 'subtype': ['Insect'], 'mana_cost': '1B'}, supertype=[], types=[CardType.CREATURE], abilities=[]))


class c73960(Card):
    "Orcish Paratroopers"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c73960, self).__init__(Characteristics(**{'power': 4, 'text': 'When Orcish Paratroopers comes into play, flip it from a height of at least one foot. Sacrifice Orcish Paratroopers unless it lands face up after turning over completely.', 'color': ['R'], 'name': 'Orcish Paratroopers', 'toughness': 4, 'subtype': ['Orc', 'Paratrooper'], 'mana_cost': '2R'}, supertype=[], types=[CardType.CREATURE], abilities=[]))


class c19647(Card):
    "Cho-Arrim Alchemist"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c19647, self).__init__(Characteristics(**{'power': 1, 'text': '{1}{W}{W}, {T}, Discard a card: The next time a source of your choice would deal damage to you this turn, prevent that damage. You gain life equal to the damage prevented this way.', 'color': ['W'], 'name': 'Cho-Arrim Alchemist', 'toughness': 1, 'subtype': ['Human', 'Spellshaper'], 'mana_cost': 'W'}, supertype=[], types=[CardType.CREATURE], abilities=[]))


class c193467(Card):
    "Near-Death Experience"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c193467, self).__init__(Characteristics(**{'name': 'Near-Death Experience', 'mana_cost': '2WWW', 'text': 'At the beginning of your upkeep, if you have exactly 1 life, you win the game.', 'color': ['W']}, supertype=[], types=[CardType.ENCHANTMENT], abilities=[]))


class c74238(Card):
    "Persecute Artist"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c74238, self).__init__(Characteristics(**{'name': 'Persecute Artist', 'mana_cost': '1BB', 'text': 'Choose an artist other than Rebecca Guay. Target player reveals his or her hand and discards all nonland cards by the chosen artist.', 'color': ['B']}, supertype=[], types=[CardType.SORCERY], abilities=[]))


class c369080(Card):
    "Turn // Burn"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c369080, self).__init__(Characteristics(**{'name': 'Turn // Burn', 'mana_cost': '1R', 'text': 'Burn deals 2 damage to target creature or player.\nFuse (You may cast one or both halves of this card from your hand.)\n---\nTarget creature loses all abilities and becomes a 0/1 red Weird until end of turn.\nFuse (You may cast one or both halves of this card from your hand.)', 'color': ['R']}, supertype=[], types=[CardType.INSTANT], abilities=[]))


class c142027(Card):
    "Silkbind Faerie"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c142027, self).__init__(Characteristics(**{'power': 1, 'text': 'Flying\n{1}{(w/u)}, {Q}: Tap target creature. ({Q} is the untap symbol.)', 'color': ['W', 'U'], 'name': 'Silkbind Faerie', 'toughness': 3, 'subtype': ['Faerie', 'Rogue'], 'mana_cost': '2(W/U)'}, supertype=[], types=[CardType.CREATURE], abilities=[StaticAbilities.Flying]))


class c21320(Card):
    "Battlefield Percher"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c21320, self).__init__(Characteristics(**{'power': 2, 'text': 'Flying\nBattlefield Percher can block only creatures with flying.\n{1}{B}: Battlefield Percher gets +1/+1 until end of turn.', 'color': ['B'], 'name': 'Battlefield Percher', 'toughness': 2, 'subtype': ['Bird'], 'mana_cost': '3BB'}, supertype=[], types=[CardType.CREATURE], abilities=[StaticAbilities.Flying]))


class c212614(Card):
    "I Bask in Your Silent Awe"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c212614, self).__init__(Characteristics(**{'name': 'I Bask in Your Silent Awe', 'mana_cost': '', 'text': "(An ongoing scheme remains face up until it's abandoned.)\nEach opponent can't cast more than one spell each turn.\nAt the beginning of your upkeep, if no opponent cast a spell since your last turn ended, abandon this scheme.", 'color': []}, supertype=[], types=[CardType.ONGOING, CardType.SCHEME], abilities=[]))


id_to_name_dict = {'c21320': 'Battlefield Percher', 'c240039': 'Homicidal Seclusion', 'c3610': 'Brood of Cockroaches', 'c73960': 'Orcish Paratroopers', 'c1476': 'Devouring Deep', 'c50176': 'Myr Quadropod', 'c22061': 'Overlaid Terrain', 'c79145': 'Hundred-Talon Kami', 'c26805': 'Tundra Kavu', 'c212614': 'I Bask in Your Silent Awe', 'c34243': "Ancestor's Chosen", 'c179594': 'Sewn-Eye Drake', 'c370698': 'Blood Bairn', 'c29973': 'Price of Glory', 'c221300': 'Island', 'c215101': 'Ogre Geargrabber', 'c24615': 'Despoil', 'c49055': 'Temporal Cascade', 'c193467': 'Near-Death Experience', 'c233086': 'Flameborn Viron', 'c221309': 'Plains', 'c142027': 'Silkbind Faerie', 'c21190': 'Sun Clasp', 'c19647': 'Cho-Arrim Alchemist', 'c3060': 'Soldevi Sentry', 'c174799': 'Hellspark Elemental', 'c369080': 'Turn // Burn', 'c5806': 'Fluctuator', 'c2473': 'Mind Whip', 'c74238': 'Persecute Artist', 'c226561': 'Taste of Blood', 'c96920': 'Vedalken Plotter', 'c230762': 'Slaughter Cry'}

name_to_id_dict = {'Tundra Kavu': 'c26805', 'I Bask in Your Silent Awe': 'c212614', 'Homicidal Seclusion': 'c240039', 'Blood Bairn': 'c370698', 'Ogre Geargrabber': 'c215101', 'Hellspark Elemental': 'c174799', 'Fluctuator': 'c5806', 'Myr Quadropod': 'c50176', 'Overlaid Terrain': 'c22061', 'Vedalken Plotter': 'c96920', 'Soldevi Sentry': 'c3060', 'Brood of Cockroaches': 'c3610', 'Cho-Arrim Alchemist': 'c19647', 'Near-Death Experience': 'c193467', 'Silkbind Faerie': 'c142027', 'Taste of Blood': 'c226561', 'Devouring Deep': 'c1476', 'Turn // Burn': 'c369080', 'Mind Whip': 'c2473', 'Orcish Paratroopers': 'c73960', 'Plains': 'c221309', 'Temporal Cascade': 'c49055', 'Hundred-Talon Kami': 'c79145', 'Despoil': 'c24615', 'Sun Clasp': 'c21190', 'Price of Glory': 'c29973', 'Persecute Artist': 'c74238', 'Flameborn Viron': 'c233086', 'Slaughter Cry': 'c230762', "Ancestor's Chosen": 'c34243', 'Battlefield Percher': 'c21320', 'Island': 'c221300', 'Sewn-Eye Drake': 'c179594'}


