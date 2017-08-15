from MTG import card
from MTG import gameobject
from MTG import cardtype
from MTG import abilities
from MTG import mana

class c221309(card.Card):
    "Plains"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c221309, self).__init__(gameobject.Characteristics(**{'mana_cost': '', 'color': [], 'text': 'W', 'subtype': ['Plains'], 'name': 'Plains'}, supertype=[cardtype.SuperType.BASIC], types=[cardtype.CardType.LAND], abilities=[]))

class c221300(card.Card):
    "Island"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c221300, self).__init__(gameobject.Characteristics(**{'mana_cost': '', 'color': [], 'text': 'U', 'subtype': ['Island'], 'name': 'Island'}, supertype=[cardtype.SuperType.BASIC], types=[cardtype.CardType.LAND], abilities=[]))

class c221311(card.Card):
    "Swamp"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c221311, self).__init__(gameobject.Characteristics(**{'mana_cost': '', 'color': [], 'text': 'B', 'subtype': ['Swamp'], 'name': 'Swamp'}, supertype=[cardtype.SuperType.BASIC], types=[cardtype.CardType.LAND], abilities=[]))

class c221297(card.Card):
    "Forest"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c221297, self).__init__(gameobject.Characteristics(**{'mana_cost': '', 'color': [], 'text': 'G', 'subtype': ['Forest'], 'name': 'Forest'}, supertype=[cardtype.SuperType.BASIC], types=[cardtype.CardType.LAND], abilities=[]))

class c983(card.Card):
    "Mountain"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c983, self).__init__(gameobject.Characteristics(**{'mana_cost': '', 'color': [], 'text': 'R', 'subtype': ['Mountain'], 'name': 'Mountain'}, supertype=[cardtype.SuperType.BASIC], types=[cardtype.CardType.LAND], abilities=[]))

class c26805(card.Card):
    "Tundra Kavu"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c26805, self).__init__(gameobject.Characteristics(**{'subtype': ['Kavu'], 'color': ['R'], 'toughness': 2, 'mana_cost': '2R', 'text': '{T}: Target land becomes a Plains or an Island until end of turn.', 'power': 2, 'name': 'Tundra Kavu'}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c79145(card.Card):
    "Hundred-Talon Kami"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c79145, self).__init__(gameobject.Characteristics(**{'subtype': ['Spirit'], 'color': ['W'], 'toughness': 3, 'mana_cost': '4W', 'text': 'Flying\nSoulshift 4 (When this creature dies, you may return target Spirit card with converted mana cost 4 or less from your graveyard to your hand.)', 'power': 2, 'name': 'Hundred-Talon Kami'}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Flying]))

class c370698(card.Card):
    "Blood Bairn"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c370698, self).__init__(gameobject.Characteristics(**{'subtype': ['Vampire'], 'color': ['B'], 'toughness': 2, 'mana_cost': '2B', 'text': 'Sacrifice another creature: Blood Bairn gets +2/+2 until end of turn.', 'power': 2, 'name': 'Blood Bairn'}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c3060(card.Card):
    "Soldevi Sentry"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c3060, self).__init__(gameobject.Characteristics(**{'subtype': ['Soldier'], 'color': [], 'toughness': 1, 'mana_cost': '1', 'text': '{1}: Choose target opponent. Regenerate Soldevi Sentry. When it regenerates this way, that player may draw a card.', 'power': 1, 'name': 'Soldevi Sentry'}, supertype=[], types=[cardtype.CardType.ARTIFACT, cardtype.CardType.CREATURE], abilities=[]))

class c34243(card.Card):
    "Ancestor's Chosen"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c34243, self).__init__(gameobject.Characteristics(**{'subtype': ['Human', 'Cleric'], 'color': ['W'], 'toughness': 4, 'mana_cost': '5WW', 'text': "First strike (This creature deals combat damage before creatures without first strike.)\nWhen Ancestor's Chosen enters the battlefield, you gain 1 life for each card in your graveyard.", 'power': 4, 'name': "Ancestor's Chosen"}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c174799(card.Card):
    "Hellspark Elemental"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c174799, self).__init__(gameobject.Characteristics(**{'subtype': ['Elemental'], 'color': ['R'], 'toughness': 1, 'mana_cost': '1R', 'text': 'Trample, haste\nAt the beginning of the end step, sacrifice Hellspark Elemental.\nUnearth {1}{R} ({1}{R}: Return this card from your graveyard to the battlefield. It gains haste. Exile it at the beginning of the next end step or if it would leave the battlefield. Unearth only as a sorcery.)', 'power': 3, 'name': 'Hellspark Elemental'}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Haste, abilities.StaticAbilities.Trample]))

class c179594(card.Card):
    "Sewn-Eye Drake"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c179594, self).__init__(gameobject.Characteristics(**{'subtype': ['Zombie', 'Drake'], 'color': ['U', 'B', 'R'], 'toughness': 1, 'mana_cost': '2(U/R)B', 'text': 'Flying, haste', 'power': 3, 'name': 'Sewn-Eye Drake'}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Flying, abilities.StaticAbilities.Haste]))

class c29973(card.Card):
    "Price of Glory"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c29973, self).__init__(gameobject.Characteristics(**{'mana_cost': '2R', 'color': ['R'], 'text': "Whenever a player taps a land for mana, if it's not that player's turn, destroy that land.", 'name': 'Price of Glory'}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c21190(card.Card):
    "Sun Clasp"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c21190, self).__init__(gameobject.Characteristics(**{'mana_cost': '1W', 'color': ['W'], 'text': "Enchant creature\nEnchanted creature gets +1/+3.\n{W}: Return enchanted creature to its owner's hand.", 'subtype': ['Aura'], 'name': 'Sun Clasp'}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c2473(card.Card):
    "Mind Whip"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c2473, self).__init__(gameobject.Characteristics(**{'mana_cost': '2BB', 'color': ['B'], 'text': "Enchant creature\nAt the beginning of the upkeep of enchanted creature's controller, that player may pay {3}. If he or she doesn't, Mind Whip deals 2 damage to that player and you tap that creature.", 'subtype': ['Aura'], 'name': 'Mind Whip'}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c5806(card.Card):
    "Fluctuator"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c5806, self).__init__(gameobject.Characteristics(**{'mana_cost': '2', 'color': [], 'text': 'Cycling abilities you activate cost you up to {2} less to activate.', 'name': 'Fluctuator'}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c230762(card.Card):
    "Slaughter Cry"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c230762, self).__init__(gameobject.Characteristics(**{'mana_cost': '2R', 'color': ['R'], 'text': 'Target creature gets +3/+0 and gains first strike until end of turn. (It deals combat damage before creatures without first strike.)', 'name': 'Slaughter Cry'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c24615(card.Card):
    "Despoil"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c24615, self).__init__(gameobject.Characteristics(**{'mana_cost': '3B', 'color': ['B'], 'text': 'Destroy target land. Its controller loses 2 life.', 'name': 'Despoil'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c22061(card.Card):
    "Overlaid Terrain"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c22061, self).__init__(gameobject.Characteristics(**{'mana_cost': '2GG', 'color': ['G'], 'text': 'As Overlaid Terrain enters the battlefield, sacrifice all lands you control.\nLands you control have "{T}: Add two mana of any one color to your mana pool."', 'name': 'Overlaid Terrain'}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c215101(card.Card):
    "Ogre Geargrabber"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c215101, self).__init__(gameobject.Characteristics(**{'subtype': ['Ogre', 'Warrior'], 'color': ['R'], 'toughness': 4, 'mana_cost': '4RR', 'text': 'Whenever Ogre Geargrabber attacks, gain control of target Equipment an opponent controls until end of turn. Attach it to Ogre Geargrabber. When you lose control of that Equipment, unattach it.', 'power': 4, 'name': 'Ogre Geargrabber'}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c96920(card.Card):
    "Vedalken Plotter"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c96920, self).__init__(gameobject.Characteristics(**{'subtype': ['Vedalken', 'Wizard'], 'color': ['U'], 'toughness': 1, 'mana_cost': '2U', 'text': 'When Vedalken Plotter enters the battlefield, exchange control of target land you control and target land an opponent controls.', 'power': 1, 'name': 'Vedalken Plotter'}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c1476(card.Card):
    "Devouring Deep"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c1476, self).__init__(gameobject.Characteristics(**{'subtype': ['Fish'], 'color': ['U'], 'toughness': 2, 'mana_cost': '2U', 'text': 'Islandwalk', 'power': 1, 'name': 'Devouring Deep'}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Islandwalk]))

class c49055(card.Card):
    "Temporal Cascade"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c49055, self).__init__(gameobject.Characteristics(**{'mana_cost': '5UU', 'color': ['U'], 'text': 'Choose one - Each player shuffles his or her hand and graveyard into his or her library; or each player draws seven cards.\nEntwine {2} (Choose both if you pay the entwine cost.)', 'name': 'Temporal Cascade'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c50176(card.Card):
    "Myr Quadropod"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c50176, self).__init__(gameobject.Characteristics(**{'subtype': ['Myr'], 'color': [], 'toughness': 4, 'mana_cost': '4', 'text': "{3}: Switch Myr Quadropod's power and toughness until end of turn.", 'power': 1, 'name': 'Myr Quadropod'}, supertype=[], types=[cardtype.CardType.ARTIFACT, cardtype.CardType.CREATURE], abilities=[]))

class c233086(card.Card):
    "Flameborn Viron"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c233086, self).__init__(gameobject.Characteristics(**{'subtype': ['Insect'], 'color': ['R'], 'toughness': 4, 'mana_cost': '4RR', 'text': '', 'power': 6, 'name': 'Flameborn Viron'}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c226561(card.Card):
    "Taste of Blood"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c226561, self).__init__(gameobject.Characteristics(**{'mana_cost': 'B', 'color': ['B'], 'text': 'Taste of Blood deals 1 damage to target player and you gain 1 life.', 'name': 'Taste of Blood'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c240039(card.Card):
    "Homicidal Seclusion"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c240039, self).__init__(gameobject.Characteristics(**{'mana_cost': '4B', 'color': ['B'], 'text': 'As long as you control exactly one creature, that creature gets +3/+1 and has lifelink.', 'name': 'Homicidal Seclusion'}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c3610(card.Card):
    "Brood of Cockroaches"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c3610, self).__init__(gameobject.Characteristics(**{'subtype': ['Insect'], 'color': ['B'], 'toughness': 1, 'mana_cost': '1B', 'text': 'When Brood of Cockroaches is put into your graveyard from the battlefield, at the beginning of the next end step, you lose 1 life and return Brood of Cockroaches to your hand.', 'power': 1, 'name': 'Brood of Cockroaches'}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c73960(card.Card):
    "Orcish Paratroopers"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c73960, self).__init__(gameobject.Characteristics(**{'subtype': ['Orc', 'Paratrooper'], 'color': ['R'], 'toughness': 4, 'mana_cost': '2R', 'text': 'When Orcish Paratroopers comes into play, flip it from a height of at least one foot. Sacrifice Orcish Paratroopers unless it lands face up after turning over completely.', 'power': 4, 'name': 'Orcish Paratroopers'}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c19647(card.Card):
    "Cho-Arrim Alchemist"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c19647, self).__init__(gameobject.Characteristics(**{'subtype': ['Human', 'Spellshaper'], 'color': ['W'], 'toughness': 1, 'mana_cost': 'W', 'text': '{1}{W}{W}, {T}, Discard a card: The next time a source of your choice would deal damage to you this turn, prevent that damage. You gain life equal to the damage prevented this way.', 'power': 1, 'name': 'Cho-Arrim Alchemist'}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c193467(card.Card):
    "Near-Death Experience"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c193467, self).__init__(gameobject.Characteristics(**{'mana_cost': '2WWW', 'color': ['W'], 'text': 'At the beginning of your upkeep, if you have exactly 1 life, you win the game.', 'name': 'Near-Death Experience'}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c74238(card.Card):
    "Persecute Artist"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c74238, self).__init__(gameobject.Characteristics(**{'mana_cost': '1BB', 'color': ['B'], 'text': 'Choose an artist other than Rebecca Guay. Target player reveals his or her hand and discards all nonland cards by the chosen artist.', 'name': 'Persecute Artist'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c369080(card.Card):
    "Turn // Burn"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c369080, self).__init__(gameobject.Characteristics(**{'mana_cost': '1R', 'color': ['R'], 'text': 'Burn deals 2 damage to target creature or player.\nFuse (You may cast one or both halves of this card from your hand.)\n---\nTarget creature loses all abilities and becomes a 0/1 red Weird until end of turn.\nFuse (You may cast one or both halves of this card from your hand.)', 'name': 'Turn // Burn'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c142027(card.Card):
    "Silkbind Faerie"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c142027, self).__init__(gameobject.Characteristics(**{'subtype': ['Faerie', 'Rogue'], 'color': ['W', 'U'], 'toughness': 3, 'mana_cost': '2(W/U)', 'text': 'Flying\n{1}{(w/u)}, {Q}: Tap target creature. ({Q} is the untap symbol.)', 'power': 1, 'name': 'Silkbind Faerie'}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Flying]))

class c21320(card.Card):
    "Battlefield Percher"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c21320, self).__init__(gameobject.Characteristics(**{'subtype': ['Bird'], 'color': ['B'], 'toughness': 2, 'mana_cost': '3BB', 'text': 'Flying\nBattlefield Percher can block only creatures with flying.\n{1}{B}: Battlefield Percher gets +1/+1 until end of turn.', 'power': 2, 'name': 'Battlefield Percher'}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Flying]))

class c212614(card.Card):
    "I Bask in Your Silent Awe"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c212614, self).__init__(gameobject.Characteristics(**{'mana_cost': '', 'color': [], 'text': "(An ongoing scheme remains face up until it's abandoned.)\nEach opponent can't cast more than one spell each turn.\nAt the beginning of your upkeep, if no opponent cast a spell since your last turn ended, abandon this scheme.", 'name': 'I Bask in Your Silent Awe'}, supertype=[], types=[cardtype.CardType.ONGOING, cardtype.CardType.SCHEME], abilities=[]))

id_to_name_dict = {'c3610': 'Brood of Cockroaches', 'c5806': 'Fluctuator', 'c21190': 'Sun Clasp', 'c96920': 'Vedalken Plotter', 'c142027': 'Silkbind Faerie', 'c2473': 'Mind Whip', 'c240039': 'Homicidal Seclusion', 'c179594': 'Sewn-Eye Drake', 'c26805': 'Tundra Kavu', 'c230762': 'Slaughter Cry', 'c212614': 'I Bask in Your Silent Awe', 'c73960': 'Orcish Paratroopers', 'c369080': 'Turn // Burn', 'c74238': 'Persecute Artist', 'c221300': 'Island', 'c22061': 'Overlaid Terrain', 'c49055': 'Temporal Cascade', 'c221309': 'Plains', 'c79145': 'Hundred-Talon Kami', 'c221311': 'Swamp', 'c19647': 'Cho-Arrim Alchemist', 'c50176': 'Myr Quadropod', 'c3060': 'Soldevi Sentry', 'c24615': 'Despoil', 'c226561': 'Taste of Blood', 'c29973': 'Price of Glory', 'c34243': "Ancestor's Chosen", 'c233086': 'Flameborn Viron', 'c983': 'Mountain', 'c215101': 'Ogre Geargrabber', 'c370698': 'Blood Bairn', 'c193467': 'Near-Death Experience', 'c174799': 'Hellspark Elemental', 'c1476': 'Devouring Deep', 'c21320': 'Battlefield Percher', 'c221297': 'Forest'}

name_to_id_dict = {'Forest': 'c221297', 'Plains': 'c221309', 'Ogre Geargrabber': 'c215101', 'Flameborn Viron': 'c233086', 'I Bask in Your Silent Awe': 'c212614', 'Mind Whip': 'c2473', 'Despoil': 'c24615', 'Orcish Paratroopers': 'c73960', 'Fluctuator': 'c5806', 'Hellspark Elemental': 'c174799', 'Near-Death Experience': 'c193467', 'Cho-Arrim Alchemist': 'c19647', 'Devouring Deep': 'c1476', 'Slaughter Cry': 'c230762', 'Brood of Cockroaches': 'c3610', 'Tundra Kavu': 'c26805', 'Overlaid Terrain': 'c22061', 'Sewn-Eye Drake': 'c179594', 'Soldevi Sentry': 'c3060', 'Swamp': 'c221311', 'Temporal Cascade': 'c49055', 'Myr Quadropod': 'c50176', 'Hundred-Talon Kami': 'c79145', 'Turn // Burn': 'c369080', "Ancestor's Chosen": 'c34243', 'Price of Glory': 'c29973', 'Mountain': 'c983', 'Persecute Artist': 'c74238', 'Vedalken Plotter': 'c96920', 'Island': 'c221300', 'Homicidal Seclusion': 'c240039', 'Blood Bairn': 'c370698', 'Taste of Blood': 'c226561', 'Sun Clasp': 'c21190', 'Silkbind Faerie': 'c142027', 'Battlefield Percher': 'c21320'}


