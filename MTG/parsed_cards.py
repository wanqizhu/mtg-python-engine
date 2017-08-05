from MTG.card import *
from MTG.gameObject import *


class c221309(Card):
    "Plains"
    def __init__(self):
        super(c221309, self).__init__(Characteristics(**{'text': 'W', 'color': [], 'name': 'Plains', 'mana_cost': '', 'subtype': ['Plains']}, supertype=[SuperType.BASIC], types=[CardType.LAND]))


class c221300(Card):
    "Island"
    def __init__(self):
        super(c221300, self).__init__(Characteristics(**{'text': 'U', 'color': [], 'name': 'Island', 'mana_cost': '', 'subtype': ['Island']}, supertype=[SuperType.BASIC], types=[CardType.LAND]))


class c26805(Card):
    "Tundra Kavu"
    def __init__(self):
        super(c26805, self).__init__(Characteristics(**{'text': '{T}: Target land becomes a Plains or an Island until end of turn.', 'color': ['R'], 'name': 'Tundra Kavu', 'mana_cost': '2R', 'subtype': ['Kavu']}, supertype=[], types=[CardType.CREATURE]))


class c79145(Card):
    "Hundred-Talon Kami"
    def __init__(self):
        super(c79145, self).__init__(Characteristics(**{'text': 'Flying\nSoulshift 4 (When this creature dies, you may return target Spirit card with converted mana cost 4 or less from your graveyard to your hand.)', 'color': ['W'], 'name': 'Hundred-Talon Kami', 'mana_cost': '4W', 'subtype': ['Spirit']}, supertype=[], types=[CardType.CREATURE]))


class c370698(Card):
    "Blood Bairn"
    def __init__(self):
        super(c370698, self).__init__(Characteristics(**{'text': 'Sacrifice another creature: Blood Bairn gets +2/+2 until end of turn.', 'color': ['B'], 'name': 'Blood Bairn', 'mana_cost': '2B', 'subtype': ['Vampire']}, supertype=[], types=[CardType.CREATURE]))


class c3060(Card):
    "Soldevi Sentry"
    def __init__(self):
        super(c3060, self).__init__(Characteristics(**{'text': '{1}: Choose target opponent. Regenerate Soldevi Sentry. When it regenerates this way, that player may draw a card.', 'color': [], 'name': 'Soldevi Sentry', 'mana_cost': '1', 'subtype': ['Soldier']}, supertype=[], types=[CardType.ARTIFACT, CardType.CREATURE]))


class c34243(Card):
    "Ancestor's Chosen"
    def __init__(self):
        super(c34243, self).__init__(Characteristics(**{'text': "First strike (This creature deals combat damage before creatures without first strike.)\nWhen Ancestor's Chosen enters the battlefield, you gain 1 life for each card in your graveyard.", 'color': ['W'], 'name': "Ancestor's Chosen", 'mana_cost': '5WW', 'subtype': ['Human', 'Cleric']}, supertype=[], types=[CardType.CREATURE]))


class c174799(Card):
    "Hellspark Elemental"
    def __init__(self):
        super(c174799, self).__init__(Characteristics(**{'text': 'Trample, haste\nAt the beginning of the end step, sacrifice Hellspark Elemental.\nUnearth {1}{R} ({1}{R}: Return this card from your graveyard to the battlefield. It gains haste. Exile it at the beginning of the next end step or if it would leave the battlefield. Unearth only as a sorcery.)', 'color': ['R'], 'name': 'Hellspark Elemental', 'mana_cost': '1R', 'subtype': ['Elemental']}, supertype=[], types=[CardType.CREATURE]))


class c179594(Card):
    "Sewn-Eye Drake"
    def __init__(self):
        super(c179594, self).__init__(Characteristics(**{'text': 'Flying, haste', 'color': ['U', 'B', 'R'], 'name': 'Sewn-Eye Drake', 'mana_cost': '2(U/R)B', 'subtype': ['Zombie', 'Drake']}, supertype=[], types=[CardType.CREATURE]))


class c29973(Card):
    "Price of Glory"
    def __init__(self):
        super(c29973, self).__init__(Characteristics(**{'text': "Whenever a player taps a land for mana, if it's not that player's turn, destroy that land.", 'color': ['R'], 'name': 'Price of Glory', 'mana_cost': '2R'}, supertype=[], types=[CardType.ENCHANTMENT]))


class c21190(Card):
    "Sun Clasp"
    def __init__(self):
        super(c21190, self).__init__(Characteristics(**{'text': "Enchant creature\nEnchanted creature gets +1/+3.\n{W}: Return enchanted creature to its owner's hand.", 'color': ['W'], 'name': 'Sun Clasp', 'mana_cost': '1W', 'subtype': ['Aura']}, supertype=[], types=[CardType.ENCHANTMENT]))


class c2473(Card):
    "Mind Whip"
    def __init__(self):
        super(c2473, self).__init__(Characteristics(**{'text': "Enchant creature\nAt the beginning of the upkeep of enchanted creature's controller, that player may pay {3}. If he or she doesn't, Mind Whip deals 2 damage to that player and you tap that creature.", 'color': ['B'], 'name': 'Mind Whip', 'mana_cost': '2BB', 'subtype': ['Aura']}, supertype=[], types=[CardType.ENCHANTMENT]))


class c5806(Card):
    "Fluctuator"
    def __init__(self):
        super(c5806, self).__init__(Characteristics(**{'text': 'Cycling abilities you activate cost you up to {2} less to activate.', 'color': [], 'name': 'Fluctuator', 'mana_cost': '2'}, supertype=[], types=[CardType.ARTIFACT]))


class c230762(Card):
    "Slaughter Cry"
    def __init__(self):
        super(c230762, self).__init__(Characteristics(**{'text': 'Target creature gets +3/+0 and gains first strike until end of turn. (It deals combat damage before creatures without first strike.)', 'color': ['R'], 'name': 'Slaughter Cry', 'mana_cost': '2R'}, supertype=[], types=[CardType.INSTANT]))


class c24615(Card):
    "Despoil"
    def __init__(self):
        super(c24615, self).__init__(Characteristics(**{'text': 'Destroy target land. Its controller loses 2 life.', 'color': ['B'], 'name': 'Despoil', 'mana_cost': '3B'}, supertype=[], types=[CardType.SORCERY]))


class c22061(Card):
    "Overlaid Terrain"
    def __init__(self):
        super(c22061, self).__init__(Characteristics(**{'text': 'As Overlaid Terrain enters the battlefield, sacrifice all lands you control.\nLands you control have "{T}: Add two mana of any one color to your mana pool."', 'color': ['G'], 'name': 'Overlaid Terrain', 'mana_cost': '2GG'}, supertype=[], types=[CardType.ENCHANTMENT]))


class c215101(Card):
    "Ogre Geargrabber"
    def __init__(self):
        super(c215101, self).__init__(Characteristics(**{'text': 'Whenever Ogre Geargrabber attacks, gain control of target Equipment an opponent controls until end of turn. Attach it to Ogre Geargrabber. When you lose control of that Equipment, unattach it.', 'color': ['R'], 'name': 'Ogre Geargrabber', 'mana_cost': '4RR', 'subtype': ['Ogre', 'Warrior']}, supertype=[], types=[CardType.CREATURE]))


class c96920(Card):
    "Vedalken Plotter"
    def __init__(self):
        super(c96920, self).__init__(Characteristics(**{'text': 'When Vedalken Plotter enters the battlefield, exchange control of target land you control and target land an opponent controls.', 'color': ['U'], 'name': 'Vedalken Plotter', 'mana_cost': '2U', 'subtype': ['Vedalken', 'Wizard']}, supertype=[], types=[CardType.CREATURE]))


class c1476(Card):
    "Devouring Deep"
    def __init__(self):
        super(c1476, self).__init__(Characteristics(**{'text': 'Islandwalk', 'color': ['U'], 'name': 'Devouring Deep', 'mana_cost': '2U', 'subtype': ['Fish']}, supertype=[], types=[CardType.CREATURE]))


class c49055(Card):
    "Temporal Cascade"
    def __init__(self):
        super(c49055, self).__init__(Characteristics(**{'text': 'Choose one - Each player shuffles his or her hand and graveyard into his or her library; or each player draws seven cards.\nEntwine {2} (Choose both if you pay the entwine cost.)', 'color': ['U'], 'name': 'Temporal Cascade', 'mana_cost': '5UU'}, supertype=[], types=[CardType.SORCERY]))


class c50176(Card):
    "Myr Quadropod"
    def __init__(self):
        super(c50176, self).__init__(Characteristics(**{'text': "{3}: Switch Myr Quadropod's power and toughness until end of turn.", 'color': [], 'name': 'Myr Quadropod', 'mana_cost': '4', 'subtype': ['Myr']}, supertype=[], types=[CardType.ARTIFACT, CardType.CREATURE]))


class c233086(Card):
    "Flameborn Viron"
    def __init__(self):
        super(c233086, self).__init__(Characteristics(**{'text': '', 'color': ['R'], 'name': 'Flameborn Viron', 'mana_cost': '4RR', 'subtype': ['Insect']}, supertype=[], types=[CardType.CREATURE]))


class c226561(Card):
    "Taste of Blood"
    def __init__(self):
        super(c226561, self).__init__(Characteristics(**{'text': 'Taste of Blood deals 1 damage to target player and you gain 1 life.', 'color': ['B'], 'name': 'Taste of Blood', 'mana_cost': 'B'}, supertype=[], types=[CardType.SORCERY]))


class c240039(Card):
    "Homicidal Seclusion"
    def __init__(self):
        super(c240039, self).__init__(Characteristics(**{'text': 'As long as you control exactly one creature, that creature gets +3/+1 and has lifelink.', 'color': ['B'], 'name': 'Homicidal Seclusion', 'mana_cost': '4B'}, supertype=[], types=[CardType.ENCHANTMENT]))


class c3610(Card):
    "Brood of Cockroaches"
    def __init__(self):
        super(c3610, self).__init__(Characteristics(**{'text': 'When Brood of Cockroaches is put into your graveyard from the battlefield, at the beginning of the next end step, you lose 1 life and return Brood of Cockroaches to your hand.', 'color': ['B'], 'name': 'Brood of Cockroaches', 'mana_cost': '1B', 'subtype': ['Insect']}, supertype=[], types=[CardType.CREATURE]))


class c73960(Card):
    "Orcish Paratroopers"
    def __init__(self):
        super(c73960, self).__init__(Characteristics(**{'text': 'When Orcish Paratroopers comes into play, flip it from a height of at least one foot. Sacrifice Orcish Paratroopers unless it lands face up after turning over completely.', 'color': ['R'], 'name': 'Orcish Paratroopers', 'mana_cost': '2R', 'subtype': ['Orc', 'Paratrooper']}, supertype=[], types=[CardType.CREATURE]))


class c19647(Card):
    "Cho-Arrim Alchemist"
    def __init__(self):
        super(c19647, self).__init__(Characteristics(**{'text': '{1}{W}{W}, {T}, Discard a card: The next time a source of your choice would deal damage to you this turn, prevent that damage. You gain life equal to the damage prevented this way.', 'color': ['W'], 'name': 'Cho-Arrim Alchemist', 'mana_cost': 'W', 'subtype': ['Human', 'Spellshaper']}, supertype=[], types=[CardType.CREATURE]))


class c193467(Card):
    "Near-Death Experience"
    def __init__(self):
        super(c193467, self).__init__(Characteristics(**{'text': 'At the beginning of your upkeep, if you have exactly 1 life, you win the game.', 'color': ['W'], 'name': 'Near-Death Experience', 'mana_cost': '2WWW'}, supertype=[], types=[CardType.ENCHANTMENT]))


class c74238(Card):
    "Persecute Artist"
    def __init__(self):
        super(c74238, self).__init__(Characteristics(**{'text': 'Choose an artist other than Rebecca Guay. Target player reveals his or her hand and discards all nonland cards by the chosen artist.', 'color': ['B'], 'name': 'Persecute Artist', 'mana_cost': '1BB'}, supertype=[], types=[CardType.SORCERY]))


class c369080(Card):
    "Turn // Burn"
    def __init__(self):
        super(c369080, self).__init__(Characteristics(**{'text': 'Burn deals 2 damage to target creature or player.\nFuse (You may cast one or both halves of this card from your hand.)\n---\nTarget creature loses all abilities and becomes a 0/1 red Weird until end of turn.\nFuse (You may cast one or both halves of this card from your hand.)', 'color': ['R'], 'name': 'Turn // Burn', 'mana_cost': '1R'}, supertype=[], types=[CardType.INSTANT]))


class c142027(Card):
    "Silkbind Faerie"
    def __init__(self):
        super(c142027, self).__init__(Characteristics(**{'text': 'Flying\n{1}{(w/u)}, {Q}: Tap target creature. ({Q} is the untap symbol.)', 'color': ['W', 'U'], 'name': 'Silkbind Faerie', 'mana_cost': '2(W/U)', 'subtype': ['Faerie', 'Rogue']}, supertype=[], types=[CardType.CREATURE]))


class c21320(Card):
    "Battlefield Percher"
    def __init__(self):
        super(c21320, self).__init__(Characteristics(**{'text': 'Flying\nBattlefield Percher can block only creatures with flying.\n{1}{B}: Battlefield Percher gets +1/+1 until end of turn.', 'color': ['B'], 'name': 'Battlefield Percher', 'mana_cost': '3BB', 'subtype': ['Bird']}, supertype=[], types=[CardType.CREATURE]))


class c212614(Card):
    "I Bask in Your Silent Awe"
    def __init__(self):
        super(c212614, self).__init__(Characteristics(**{'text': "(An ongoing scheme remains face up until it's abandoned.)\nEach opponent can't cast more than one spell each turn.\nAt the beginning of your upkeep, if no opponent cast a spell since your last turn ended, abandon this scheme.", 'color': [], 'name': 'I Bask in Your Silent Awe', 'mana_cost': ''}, supertype=[], types=[CardType.ONGOING, CardType.SCHEME]))


id_to_name_dict = {'c221300': 'Island', 'c215101': 'Ogre Geargrabber', 'c179594': 'Sewn-Eye Drake', 'c226561': 'Taste of Blood', 'c50176': 'Myr Quadropod', 'c24615': 'Despoil', 'c21190': 'Sun Clasp', 'c74238': 'Persecute Artist', 'c230762': 'Slaughter Cry', 'c1476': 'Devouring Deep', 'c96920': 'Vedalken Plotter', 'c49055': 'Temporal Cascade', 'c233086': 'Flameborn Viron', 'c3610': 'Brood of Cockroaches', 'c19647': 'Cho-Arrim Alchemist', 'c370698': 'Blood Bairn', 'c5806': 'Fluctuator', 'c212614': 'I Bask in Your Silent Awe', 'c193467': 'Near-Death Experience', 'c29973': 'Price of Glory', 'c221309': 'Plains', 'c2473': 'Mind Whip', 'c3060': 'Soldevi Sentry', 'c26805': 'Tundra Kavu', 'c22061': 'Overlaid Terrain', 'c34243': "Ancestor's Chosen", 'c21320': 'Battlefield Percher', 'c73960': 'Orcish Paratroopers', 'c174799': 'Hellspark Elemental', 'c240039': 'Homicidal Seclusion', 'c79145': 'Hundred-Talon Kami', 'c369080': 'Turn // Burn', 'c142027': 'Silkbind Faerie'}

name_to_id_dict = {'Brood of Cockroaches': 'c3610', 'Plains': 'c221309', 'Hellspark Elemental': 'c174799', 'Persecute Artist': 'c74238', 'Slaughter Cry': 'c230762', 'Tundra Kavu': 'c26805', 'Sun Clasp': 'c21190', 'Fluctuator': 'c5806', 'Taste of Blood': 'c226561', 'Orcish Paratroopers': 'c73960', 'Vedalken Plotter': 'c96920', 'Mind Whip': 'c2473', "Ancestor's Chosen": 'c34243', 'Silkbind Faerie': 'c142027', 'Temporal Cascade': 'c49055', 'Flameborn Viron': 'c233086', 'Hundred-Talon Kami': 'c79145', 'Island': 'c221300', 'Blood Bairn': 'c370698', 'Turn // Burn': 'c369080', 'Overlaid Terrain': 'c22061', 'Devouring Deep': 'c1476', 'Cho-Arrim Alchemist': 'c19647', 'Price of Glory': 'c29973', 'Near-Death Experience': 'c193467', 'Soldevi Sentry': 'c3060', 'Ogre Geargrabber': 'c215101', 'Myr Quadropod': 'c50176', 'Battlefield Percher': 'c21320', 'I Bask in Your Silent Awe': 'c212614', 'Despoil': 'c24615', 'Sewn-Eye Drake': 'c179594', 'Homicidal Seclusion': 'c240039'}


