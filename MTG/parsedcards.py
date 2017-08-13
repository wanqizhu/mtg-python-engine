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
        super(c221309, self).__init__(gameobject.Characteristics(**{'text': 'W', 'mana_cost': '', 'color': [], 'name': 'Plains', 'subtype': ['Plains']}, supertype=[cardtype.SuperType.BASIC], types=[cardtype.CardType.LAND], abilities=[]))

class c221300(card.Card):
    "Island"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c221300, self).__init__(gameobject.Characteristics(**{'text': 'U', 'mana_cost': '', 'color': [], 'name': 'Island', 'subtype': ['Island']}, supertype=[cardtype.SuperType.BASIC], types=[cardtype.CardType.LAND], abilities=[]))

class c26805(card.Card):
    "Tundra Kavu"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c26805, self).__init__(gameobject.Characteristics(**{'mana_cost': '2R', 'toughness': 2, 'name': 'Tundra Kavu', 'text': '{T}: Target land becomes a Plains or an Island until end of turn.', 'color': ['R'], 'power': 2, 'subtype': ['Kavu']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c79145(card.Card):
    "Hundred-Talon Kami"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c79145, self).__init__(gameobject.Characteristics(**{'mana_cost': '4W', 'toughness': 3, 'name': 'Hundred-Talon Kami', 'text': 'Flying\nSoulshift 4 (When this creature dies, you may return target Spirit card with converted mana cost 4 or less from your graveyard to your hand.)', 'color': ['W'], 'power': 2, 'subtype': ['Spirit']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Flying]))

class c370698(card.Card):
    "Blood Bairn"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c370698, self).__init__(gameobject.Characteristics(**{'mana_cost': '2B', 'toughness': 2, 'name': 'Blood Bairn', 'text': 'Sacrifice another creature: Blood Bairn gets +2/+2 until end of turn.', 'color': ['B'], 'power': 2, 'subtype': ['Vampire']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c3060(card.Card):
    "Soldevi Sentry"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c3060, self).__init__(gameobject.Characteristics(**{'mana_cost': '1', 'toughness': 1, 'name': 'Soldevi Sentry', 'text': '{1}: Choose target opponent. Regenerate Soldevi Sentry. When it regenerates this way, that player may draw a card.', 'color': [], 'power': 1, 'subtype': ['Soldier']}, supertype=[], types=[cardtype.CardType.ARTIFACT, cardtype.CardType.CREATURE], abilities=[]))

class c34243(card.Card):
    "Ancestor's Chosen"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c34243, self).__init__(gameobject.Characteristics(**{'mana_cost': '5WW', 'toughness': 4, 'name': "Ancestor's Chosen", 'text': "First strike (This creature deals combat damage before creatures without first strike.)\nWhen Ancestor's Chosen enters the battlefield, you gain 1 life for each card in your graveyard.", 'color': ['W'], 'power': 4, 'subtype': ['Human', 'Cleric']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c174799(card.Card):
    "Hellspark Elemental"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c174799, self).__init__(gameobject.Characteristics(**{'mana_cost': '1R', 'toughness': 1, 'name': 'Hellspark Elemental', 'text': 'Trample, haste\nAt the beginning of the end step, sacrifice Hellspark Elemental.\nUnearth {1}{R} ({1}{R}: Return this card from your graveyard to the battlefield. It gains haste. Exile it at the beginning of the next end step or if it would leave the battlefield. Unearth only as a sorcery.)', 'color': ['R'], 'power': 3, 'subtype': ['Elemental']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Haste, abilities.StaticAbilities.Trample]))

class c179594(card.Card):
    "Sewn-Eye Drake"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c179594, self).__init__(gameobject.Characteristics(**{'mana_cost': '2(U/R)B', 'toughness': 1, 'name': 'Sewn-Eye Drake', 'text': 'Flying, haste', 'color': ['U', 'B', 'R'], 'power': 3, 'subtype': ['Zombie', 'Drake']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Flying, abilities.StaticAbilities.Haste]))

class c29973(card.Card):
    "Price of Glory"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c29973, self).__init__(gameobject.Characteristics(**{'text': "Whenever a player taps a land for mana, if it's not that player's turn, destroy that land.", 'mana_cost': '2R', 'color': ['R'], 'name': 'Price of Glory'}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c21190(card.Card):
    "Sun Clasp"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c21190, self).__init__(gameobject.Characteristics(**{'text': "Enchant creature\nEnchanted creature gets +1/+3.\n{W}: Return enchanted creature to its owner's hand.", 'mana_cost': '1W', 'color': ['W'], 'name': 'Sun Clasp', 'subtype': ['Aura']}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c2473(card.Card):
    "Mind Whip"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c2473, self).__init__(gameobject.Characteristics(**{'text': "Enchant creature\nAt the beginning of the upkeep of enchanted creature's controller, that player may pay {3}. If he or she doesn't, Mind Whip deals 2 damage to that player and you tap that creature.", 'mana_cost': '2BB', 'color': ['B'], 'name': 'Mind Whip', 'subtype': ['Aura']}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c5806(card.Card):
    "Fluctuator"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c5806, self).__init__(gameobject.Characteristics(**{'text': 'Cycling abilities you activate cost you up to {2} less to activate.', 'mana_cost': '2', 'color': [], 'name': 'Fluctuator'}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c230762(card.Card):
    "Slaughter Cry"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c230762, self).__init__(gameobject.Characteristics(**{'text': 'Target creature gets +3/+0 and gains first strike until end of turn. (It deals combat damage before creatures without first strike.)', 'mana_cost': '2R', 'color': ['R'], 'name': 'Slaughter Cry'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c24615(card.Card):
    "Despoil"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c24615, self).__init__(gameobject.Characteristics(**{'text': 'Destroy target land. Its controller loses 2 life.', 'mana_cost': '3B', 'color': ['B'], 'name': 'Despoil'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c22061(card.Card):
    "Overlaid Terrain"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c22061, self).__init__(gameobject.Characteristics(**{'text': 'As Overlaid Terrain enters the battlefield, sacrifice all lands you control.\nLands you control have "{T}: Add two mana of any one color to your mana pool."', 'mana_cost': '2GG', 'color': ['G'], 'name': 'Overlaid Terrain'}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c215101(card.Card):
    "Ogre Geargrabber"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c215101, self).__init__(gameobject.Characteristics(**{'mana_cost': '4RR', 'toughness': 4, 'name': 'Ogre Geargrabber', 'text': 'Whenever Ogre Geargrabber attacks, gain control of target Equipment an opponent controls until end of turn. Attach it to Ogre Geargrabber. When you lose control of that Equipment, unattach it.', 'color': ['R'], 'power': 4, 'subtype': ['Ogre', 'Warrior']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c96920(card.Card):
    "Vedalken Plotter"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c96920, self).__init__(gameobject.Characteristics(**{'mana_cost': '2U', 'toughness': 1, 'name': 'Vedalken Plotter', 'text': 'When Vedalken Plotter enters the battlefield, exchange control of target land you control and target land an opponent controls.', 'color': ['U'], 'power': 1, 'subtype': ['Vedalken', 'Wizard']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c1476(card.Card):
    "Devouring Deep"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c1476, self).__init__(gameobject.Characteristics(**{'mana_cost': '2U', 'toughness': 2, 'name': 'Devouring Deep', 'text': 'Islandwalk', 'color': ['U'], 'power': 1, 'subtype': ['Fish']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Islandwalk]))

class c49055(card.Card):
    "Temporal Cascade"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c49055, self).__init__(gameobject.Characteristics(**{'text': 'Choose one - Each player shuffles his or her hand and graveyard into his or her library; or each player draws seven cards.\nEntwine {2} (Choose both if you pay the entwine cost.)', 'mana_cost': '5UU', 'color': ['U'], 'name': 'Temporal Cascade'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c50176(card.Card):
    "Myr Quadropod"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c50176, self).__init__(gameobject.Characteristics(**{'mana_cost': '4', 'toughness': 4, 'name': 'Myr Quadropod', 'text': "{3}: Switch Myr Quadropod's power and toughness until end of turn.", 'color': [], 'power': 1, 'subtype': ['Myr']}, supertype=[], types=[cardtype.CardType.ARTIFACT, cardtype.CardType.CREATURE], abilities=[]))

class c233086(card.Card):
    "Flameborn Viron"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c233086, self).__init__(gameobject.Characteristics(**{'mana_cost': '4RR', 'toughness': 4, 'name': 'Flameborn Viron', 'text': '', 'color': ['R'], 'power': 6, 'subtype': ['Insect']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c226561(card.Card):
    "Taste of Blood"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c226561, self).__init__(gameobject.Characteristics(**{'text': 'Taste of Blood deals 1 damage to target player and you gain 1 life.', 'mana_cost': 'B', 'color': ['B'], 'name': 'Taste of Blood'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c240039(card.Card):
    "Homicidal Seclusion"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c240039, self).__init__(gameobject.Characteristics(**{'text': 'As long as you control exactly one creature, that creature gets +3/+1 and has lifelink.', 'mana_cost': '4B', 'color': ['B'], 'name': 'Homicidal Seclusion'}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c3610(card.Card):
    "Brood of Cockroaches"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c3610, self).__init__(gameobject.Characteristics(**{'mana_cost': '1B', 'toughness': 1, 'name': 'Brood of Cockroaches', 'text': 'When Brood of Cockroaches is put into your graveyard from the battlefield, at the beginning of the next end step, you lose 1 life and return Brood of Cockroaches to your hand.', 'color': ['B'], 'power': 1, 'subtype': ['Insect']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c73960(card.Card):
    "Orcish Paratroopers"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c73960, self).__init__(gameobject.Characteristics(**{'mana_cost': '2R', 'toughness': 4, 'name': 'Orcish Paratroopers', 'text': 'When Orcish Paratroopers comes into play, flip it from a height of at least one foot. Sacrifice Orcish Paratroopers unless it lands face up after turning over completely.', 'color': ['R'], 'power': 4, 'subtype': ['Orc', 'Paratrooper']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c19647(card.Card):
    "Cho-Arrim Alchemist"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c19647, self).__init__(gameobject.Characteristics(**{'mana_cost': 'W', 'toughness': 1, 'name': 'Cho-Arrim Alchemist', 'text': '{1}{W}{W}, {T}, Discard a card: The next time a source of your choice would deal damage to you this turn, prevent that damage. You gain life equal to the damage prevented this way.', 'color': ['W'], 'power': 1, 'subtype': ['Human', 'Spellshaper']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c193467(card.Card):
    "Near-Death Experience"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c193467, self).__init__(gameobject.Characteristics(**{'text': 'At the beginning of your upkeep, if you have exactly 1 life, you win the game.', 'mana_cost': '2WWW', 'color': ['W'], 'name': 'Near-Death Experience'}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c74238(card.Card):
    "Persecute Artist"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c74238, self).__init__(gameobject.Characteristics(**{'text': 'Choose an artist other than Rebecca Guay. Target player reveals his or her hand and discards all nonland cards by the chosen artist.', 'mana_cost': '1BB', 'color': ['B'], 'name': 'Persecute Artist'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c369080(card.Card):
    "Turn // Burn"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c369080, self).__init__(gameobject.Characteristics(**{'text': 'Burn deals 2 damage to target creature or player.\nFuse (You may cast one or both halves of this card from your hand.)\n---\nTarget creature loses all abilities and becomes a 0/1 red Weird until end of turn.\nFuse (You may cast one or both halves of this card from your hand.)', 'mana_cost': '1R', 'color': ['R'], 'name': 'Turn // Burn'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c142027(card.Card):
    "Silkbind Faerie"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c142027, self).__init__(gameobject.Characteristics(**{'mana_cost': '2(W/U)', 'toughness': 3, 'name': 'Silkbind Faerie', 'text': 'Flying\n{1}{(w/u)}, {Q}: Tap target creature. ({Q} is the untap symbol.)', 'color': ['W', 'U'], 'power': 1, 'subtype': ['Faerie', 'Rogue']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Flying]))

class c21320(card.Card):
    "Battlefield Percher"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c21320, self).__init__(gameobject.Characteristics(**{'mana_cost': '3BB', 'toughness': 2, 'name': 'Battlefield Percher', 'text': 'Flying\nBattlefield Percher can block only creatures with flying.\n{1}{B}: Battlefield Percher gets +1/+1 until end of turn.', 'color': ['B'], 'power': 2, 'subtype': ['Bird']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Flying]))

class c212614(card.Card):
    "I Bask in Your Silent Awe"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c212614, self).__init__(gameobject.Characteristics(**{'text': "(An ongoing scheme remains face up until it's abandoned.)\nEach opponent can't cast more than one spell each turn.\nAt the beginning of your upkeep, if no opponent cast a spell since your last turn ended, abandon this scheme.", 'mana_cost': '', 'color': [], 'name': 'I Bask in Your Silent Awe'}, supertype=[], types=[cardtype.CardType.ONGOING, cardtype.CardType.SCHEME], abilities=[]))

id_to_name_dict = {'c5806': 'Fluctuator', 'c221309': 'Plains', 'c21190': 'Sun Clasp', 'c3610': 'Brood of Cockroaches', 'c74238': 'Persecute Artist', 'c26805': 'Tundra Kavu', 'c230762': 'Slaughter Cry', 'c49055': 'Temporal Cascade', 'c29973': 'Price of Glory', 'c212614': 'I Bask in Your Silent Awe', 'c2473': 'Mind Whip', 'c240039': 'Homicidal Seclusion', 'c179594': 'Sewn-Eye Drake', 'c221300': 'Island', 'c370698': 'Blood Bairn', 'c22061': 'Overlaid Terrain', 'c226561': 'Taste of Blood', 'c215101': 'Ogre Geargrabber', 'c50176': 'Myr Quadropod', 'c193467': 'Near-Death Experience', 'c24615': 'Despoil', 'c1476': 'Devouring Deep', 'c34243': "Ancestor's Chosen", 'c233086': 'Flameborn Viron', 'c96920': 'Vedalken Plotter', 'c369080': 'Turn // Burn', 'c174799': 'Hellspark Elemental', 'c79145': 'Hundred-Talon Kami', 'c21320': 'Battlefield Percher', 'c3060': 'Soldevi Sentry', 'c73960': 'Orcish Paratroopers', 'c19647': 'Cho-Arrim Alchemist', 'c142027': 'Silkbind Faerie'}

name_to_id_dict = {'Brood of Cockroaches': 'c3610', 'Devouring Deep': 'c1476', 'Fluctuator': 'c5806', 'Plains': 'c221309', 'Near-Death Experience': 'c193467', "Ancestor's Chosen": 'c34243', 'Price of Glory': 'c29973', 'Soldevi Sentry': 'c3060', 'Ogre Geargrabber': 'c215101', 'Flameborn Viron': 'c233086', 'Despoil': 'c24615', 'Taste of Blood': 'c226561', 'Island': 'c221300', 'Silkbind Faerie': 'c142027', 'Cho-Arrim Alchemist': 'c19647', 'Persecute Artist': 'c74238', 'Hellspark Elemental': 'c174799', 'Blood Bairn': 'c370698', 'Orcish Paratroopers': 'c73960', 'Hundred-Talon Kami': 'c79145', 'Slaughter Cry': 'c230762', 'Myr Quadropod': 'c50176', 'Battlefield Percher': 'c21320', 'Sun Clasp': 'c21190', 'Vedalken Plotter': 'c96920', 'Tundra Kavu': 'c26805', 'Sewn-Eye Drake': 'c179594', 'I Bask in Your Silent Awe': 'c212614', 'Homicidal Seclusion': 'c240039', 'Turn // Burn': 'c369080', 'Temporal Cascade': 'c49055', 'Mind Whip': 'c2473', 'Overlaid Terrain': 'c22061'}


