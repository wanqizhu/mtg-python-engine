from MTG.card import *
from MTG.gameObject import *


class c221309(Card):
    "Plains"
    def __init__(self):
        super(c221309, self).__init__(Characteristics(**{'name': 'Plains', 'text': 'W', 'mana_cost': '', 'subtype': ['Plains'], 'color': []}, supertype=[SuperType.BASIC], types=[CardType.LAND]))


class c221300(Card):
    "Island"
    def __init__(self):
        super(c221300, self).__init__(Characteristics(**{'name': 'Island', 'text': 'U', 'mana_cost': '', 'subtype': ['Island'], 'color': []}, supertype=[SuperType.BASIC], types=[CardType.LAND]))


class c26805(Card):
    "Tundra Kavu"
    def __init__(self):
        super(c26805, self).__init__(Characteristics(**{'name': 'Tundra Kavu', 'text': '{T}: Target land becomes a Plains or an Island until end of turn.', 'mana_cost': '2R', 'subtype': ['Kavu'], 'color': ['R']}, supertype=[], types=[CardType.CREATURE]))


class c79145(Card):
    "Hundred-Talon Kami"
    def __init__(self):
        super(c79145, self).__init__(Characteristics(**{'name': 'Hundred-Talon Kami', 'text': 'Flying\nSoulshift 4 (When this creature dies, you may return target Spirit card with converted mana cost 4 or less from your graveyard to your hand.)', 'mana_cost': '4W', 'subtype': ['Spirit'], 'color': ['W']}, supertype=[], types=[CardType.CREATURE]))


class c370698(Card):
    "Blood Bairn"
    def __init__(self):
        super(c370698, self).__init__(Characteristics(**{'name': 'Blood Bairn', 'text': 'Sacrifice another creature: Blood Bairn gets +2/+2 until end of turn.', 'mana_cost': '2B', 'subtype': ['Vampire'], 'color': ['B']}, supertype=[], types=[CardType.CREATURE]))


class c3060(Card):
    "Soldevi Sentry"
    def __init__(self):
        super(c3060, self).__init__(Characteristics(**{'name': 'Soldevi Sentry', 'text': '{1}: Choose target opponent. Regenerate Soldevi Sentry. When it regenerates this way, that player may draw a card.', 'mana_cost': '1', 'subtype': ['Soldier'], 'color': []}, supertype=[], types=[CardType.ARTIFACT, CardType.CREATURE]))


class c34243(Card):
    "Ancestor's Chosen"
    def __init__(self):
        super(c34243, self).__init__(Characteristics(**{'name': "Ancestor's Chosen", 'text': "First strike (This creature deals combat damage before creatures without first strike.)\nWhen Ancestor's Chosen enters the battlefield, you gain 1 life for each card in your graveyard.", 'mana_cost': '5WW', 'subtype': ['Human', 'Cleric'], 'color': ['W']}, supertype=[], types=[CardType.CREATURE]))


class c174799(Card):
    "Hellspark Elemental"
    def __init__(self):
        super(c174799, self).__init__(Characteristics(**{'name': 'Hellspark Elemental', 'text': 'Trample, haste\nAt the beginning of the end step, sacrifice Hellspark Elemental.\nUnearth {1}{R} ({1}{R}: Return this card from your graveyard to the battlefield. It gains haste. Exile it at the beginning of the next end step or if it would leave the battlefield. Unearth only as a sorcery.)', 'mana_cost': '1R', 'subtype': ['Elemental'], 'color': ['R']}, supertype=[], types=[CardType.CREATURE]))


class c179594(Card):
    "Sewn-Eye Drake"
    def __init__(self):
        super(c179594, self).__init__(Characteristics(**{'name': 'Sewn-Eye Drake', 'text': 'Flying, haste', 'mana_cost': '2(U/R)B', 'subtype': ['Zombie', 'Drake'], 'color': ['U', 'B', 'R']}, supertype=[], types=[CardType.CREATURE]))


class c29973(Card):
    "Price of Glory"
    def __init__(self):
        super(c29973, self).__init__(Characteristics(**{'name': 'Price of Glory', 'text': "Whenever a player taps a land for mana, if it's not that player's turn, destroy that land.", 'mana_cost': '2R', 'color': ['R']}, supertype=[], types=[CardType.ENCHANTMENT]))


class c21190(Card):
    "Sun Clasp"
    def __init__(self):
        super(c21190, self).__init__(Characteristics(**{'name': 'Sun Clasp', 'text': "Enchant creature\nEnchanted creature gets +1/+3.\n{W}: Return enchanted creature to its owner's hand.", 'mana_cost': '1W', 'subtype': ['Aura'], 'color': ['W']}, supertype=[], types=[CardType.ENCHANTMENT]))


class c2473(Card):
    "Mind Whip"
    def __init__(self):
        super(c2473, self).__init__(Characteristics(**{'name': 'Mind Whip', 'text': "Enchant creature\nAt the beginning of the upkeep of enchanted creature's controller, that player may pay {3}. If he or she doesn't, Mind Whip deals 2 damage to that player and you tap that creature.", 'mana_cost': '2BB', 'subtype': ['Aura'], 'color': ['B']}, supertype=[], types=[CardType.ENCHANTMENT]))


class c5806(Card):
    "Fluctuator"
    def __init__(self):
        super(c5806, self).__init__(Characteristics(**{'name': 'Fluctuator', 'text': 'Cycling abilities you activate cost you up to {2} less to activate.', 'mana_cost': '2', 'color': []}, supertype=[], types=[CardType.ARTIFACT]))


class c230762(Card):
    "Slaughter Cry"
    def __init__(self):
        super(c230762, self).__init__(Characteristics(**{'name': 'Slaughter Cry', 'text': 'Target creature gets +3/+0 and gains first strike until end of turn. (It deals combat damage before creatures without first strike.)', 'mana_cost': '2R', 'color': ['R']}, supertype=[], types=[CardType.INSTANT]))


class c24615(Card):
    "Despoil"
    def __init__(self):
        super(c24615, self).__init__(Characteristics(**{'name': 'Despoil', 'text': 'Destroy target land. Its controller loses 2 life.', 'mana_cost': '3B', 'color': ['B']}, supertype=[], types=[CardType.SORCERY]))


class c22061(Card):
    "Overlaid Terrain"
    def __init__(self):
        super(c22061, self).__init__(Characteristics(**{'name': 'Overlaid Terrain', 'text': 'As Overlaid Terrain enters the battlefield, sacrifice all lands you control.\nLands you control have "{T}: Add two mana of any one color to your mana pool."', 'mana_cost': '2GG', 'color': ['G']}, supertype=[], types=[CardType.ENCHANTMENT]))


class c215101(Card):
    "Ogre Geargrabber"
    def __init__(self):
        super(c215101, self).__init__(Characteristics(**{'name': 'Ogre Geargrabber', 'text': 'Whenever Ogre Geargrabber attacks, gain control of target Equipment an opponent controls until end of turn. Attach it to Ogre Geargrabber. When you lose control of that Equipment, unattach it.', 'mana_cost': '4RR', 'subtype': ['Ogre', 'Warrior'], 'color': ['R']}, supertype=[], types=[CardType.CREATURE]))


class c96920(Card):
    "Vedalken Plotter"
    def __init__(self):
        super(c96920, self).__init__(Characteristics(**{'name': 'Vedalken Plotter', 'text': 'When Vedalken Plotter enters the battlefield, exchange control of target land you control and target land an opponent controls.', 'mana_cost': '2U', 'subtype': ['Vedalken', 'Wizard'], 'color': ['U']}, supertype=[], types=[CardType.CREATURE]))


class c1476(Card):
    "Devouring Deep"
    def __init__(self):
        super(c1476, self).__init__(Characteristics(**{'name': 'Devouring Deep', 'text': 'Islandwalk', 'mana_cost': '2U', 'subtype': ['Fish'], 'color': ['U']}, supertype=[], types=[CardType.CREATURE]))


class c49055(Card):
    "Temporal Cascade"
    def __init__(self):
        super(c49055, self).__init__(Characteristics(**{'name': 'Temporal Cascade', 'text': 'Choose one - Each player shuffles his or her hand and graveyard into his or her library; or each player draws seven cards.\nEntwine {2} (Choose both if you pay the entwine cost.)', 'mana_cost': '5UU', 'color': ['U']}, supertype=[], types=[CardType.SORCERY]))


class c50176(Card):
    "Myr Quadropod"
    def __init__(self):
        super(c50176, self).__init__(Characteristics(**{'name': 'Myr Quadropod', 'text': "{3}: Switch Myr Quadropod's power and toughness until end of turn.", 'mana_cost': '4', 'subtype': ['Myr'], 'color': []}, supertype=[], types=[CardType.ARTIFACT, CardType.CREATURE]))


class c233086(Card):
    "Flameborn Viron"
    def __init__(self):
        super(c233086, self).__init__(Characteristics(**{'name': 'Flameborn Viron', 'text': '', 'mana_cost': '4RR', 'subtype': ['Insect'], 'color': ['R']}, supertype=[], types=[CardType.CREATURE]))


class c226561(Card):
    "Taste of Blood"
    def __init__(self):
        super(c226561, self).__init__(Characteristics(**{'name': 'Taste of Blood', 'text': 'Taste of Blood deals 1 damage to target player and you gain 1 life.', 'mana_cost': 'B', 'color': ['B']}, supertype=[], types=[CardType.SORCERY]))


class c240039(Card):
    "Homicidal Seclusion"
    def __init__(self):
        super(c240039, self).__init__(Characteristics(**{'name': 'Homicidal Seclusion', 'text': 'As long as you control exactly one creature, that creature gets +3/+1 and has lifelink.', 'mana_cost': '4B', 'color': ['B']}, supertype=[], types=[CardType.ENCHANTMENT]))


class c3610(Card):
    "Brood of Cockroaches"
    def __init__(self):
        super(c3610, self).__init__(Characteristics(**{'name': 'Brood of Cockroaches', 'text': 'When Brood of Cockroaches is put into your graveyard from the battlefield, at the beginning of the next end step, you lose 1 life and return Brood of Cockroaches to your hand.', 'mana_cost': '1B', 'subtype': ['Insect'], 'color': ['B']}, supertype=[], types=[CardType.CREATURE]))


class c73960(Card):
    "Orcish Paratroopers"
    def __init__(self):
        super(c73960, self).__init__(Characteristics(**{'name': 'Orcish Paratroopers', 'text': 'When Orcish Paratroopers comes into play, flip it from a height of at least one foot. Sacrifice Orcish Paratroopers unless it lands face up after turning over completely.', 'mana_cost': '2R', 'subtype': ['Orc', 'Paratrooper'], 'color': ['R']}, supertype=[], types=[CardType.CREATURE]))


class c19647(Card):
    "Cho-Arrim Alchemist"
    def __init__(self):
        super(c19647, self).__init__(Characteristics(**{'name': 'Cho-Arrim Alchemist', 'text': '{1}{W}{W}, {T}, Discard a card: The next time a source of your choice would deal damage to you this turn, prevent that damage. You gain life equal to the damage prevented this way.', 'mana_cost': 'W', 'subtype': ['Human', 'Spellshaper'], 'color': ['W']}, supertype=[], types=[CardType.CREATURE]))


class c193467(Card):
    "Near-Death Experience"
    def __init__(self):
        super(c193467, self).__init__(Characteristics(**{'name': 'Near-Death Experience', 'text': 'At the beginning of your upkeep, if you have exactly 1 life, you win the game.', 'mana_cost': '2WWW', 'color': ['W']}, supertype=[], types=[CardType.ENCHANTMENT]))


class c74238(Card):
    "Persecute Artist"
    def __init__(self):
        super(c74238, self).__init__(Characteristics(**{'name': 'Persecute Artist', 'text': 'Choose an artist other than Rebecca Guay. Target player reveals his or her hand and discards all nonland cards by the chosen artist.', 'mana_cost': '1BB', 'color': ['B']}, supertype=[], types=[CardType.SORCERY]))


class c369080(Card):
    "Turn // Burn"
    def __init__(self):
        super(c369080, self).__init__(Characteristics(**{'name': 'Turn // Burn', 'text': 'Burn deals 2 damage to target creature or player.\nFuse (You may cast one or both halves of this card from your hand.)\n---\nTarget creature loses all abilities and becomes a 0/1 red Weird until end of turn.\nFuse (You may cast one or both halves of this card from your hand.)', 'mana_cost': '1R', 'color': ['R']}, supertype=[], types=[CardType.INSTANT]))


class c142027(Card):
    "Silkbind Faerie"
    def __init__(self):
        super(c142027, self).__init__(Characteristics(**{'name': 'Silkbind Faerie', 'text': 'Flying\n{1}{(w/u)}, {Q}: Tap target creature. ({Q} is the untap symbol.)', 'mana_cost': '2(W/U)', 'subtype': ['Faerie', 'Rogue'], 'color': ['W', 'U']}, supertype=[], types=[CardType.CREATURE]))


class c21320(Card):
    "Battlefield Percher"
    def __init__(self):
        super(c21320, self).__init__(Characteristics(**{'name': 'Battlefield Percher', 'text': 'Flying\nBattlefield Percher can block only creatures with flying.\n{1}{B}: Battlefield Percher gets +1/+1 until end of turn.', 'mana_cost': '3BB', 'subtype': ['Bird'], 'color': ['B']}, supertype=[], types=[CardType.CREATURE]))


class c212614(Card):
    "I Bask in Your Silent Awe"
    def __init__(self):
        super(c212614, self).__init__(Characteristics(**{'name': 'I Bask in Your Silent Awe', 'text': "(An ongoing scheme remains face up until it's abandoned.)\nEach opponent can't cast more than one spell each turn.\nAt the beginning of your upkeep, if no opponent cast a spell since your last turn ended, abandon this scheme.", 'mana_cost': '', 'color': []}, supertype=[], types=[CardType.ONGOING, CardType.SCHEME]))


id_to_name_dict = {'c369080': 'Turn // Burn', 'c26805': 'Tundra Kavu', 'c50176': 'Myr Quadropod', 'c240039': 'Homicidal Seclusion', 'c1476': 'Devouring Deep', 'c230762': 'Slaughter Cry', 'c21320': 'Battlefield Percher', 'c233086': 'Flameborn Viron', 'c212614': 'I Bask in Your Silent Awe', 'c193467': 'Near-Death Experience', 'c221309': 'Plains', 'c5806': 'Fluctuator', 'c174799': 'Hellspark Elemental', 'c179594': 'Sewn-Eye Drake', 'c142027': 'Silkbind Faerie', 'c74238': 'Persecute Artist', 'c34243': "Ancestor's Chosen", 'c24615': 'Despoil', 'c370698': 'Blood Bairn', 'c96920': 'Vedalken Plotter', 'c49055': 'Temporal Cascade', 'c3610': 'Brood of Cockroaches', 'c19647': 'Cho-Arrim Alchemist', 'c2473': 'Mind Whip', 'c73960': 'Orcish Paratroopers', 'c215101': 'Ogre Geargrabber', 'c3060': 'Soldevi Sentry', 'c221300': 'Island', 'c29973': 'Price of Glory', 'c226561': 'Taste of Blood', 'c79145': 'Hundred-Talon Kami', 'c22061': 'Overlaid Terrain', 'c21190': 'Sun Clasp'}

name_to_id_dict = {'I Bask in Your Silent Awe': 'c212614', 'Taste of Blood': 'c226561', 'Fluctuator': 'c5806', 'Soldevi Sentry': 'c3060', 'Overlaid Terrain': 'c22061', 'Sun Clasp': 'c21190', 'Despoil': 'c24615', 'Sewn-Eye Drake': 'c179594', 'Hundred-Talon Kami': 'c79145', 'Persecute Artist': 'c74238', 'Orcish Paratroopers': 'c73960', 'Devouring Deep': 'c1476', 'Turn // Burn': 'c369080', 'Tundra Kavu': 'c26805', 'Near-Death Experience': 'c193467', 'Ogre Geargrabber': 'c215101', 'Vedalken Plotter': 'c96920', 'Flameborn Viron': 'c233086', 'Price of Glory': 'c29973', 'Plains': 'c221309', "Ancestor's Chosen": 'c34243', 'Homicidal Seclusion': 'c240039', 'Silkbind Faerie': 'c142027', 'Brood of Cockroaches': 'c3610', 'Battlefield Percher': 'c21320', 'Mind Whip': 'c2473', 'Blood Bairn': 'c370698', 'Cho-Arrim Alchemist': 'c19647', 'Hellspark Elemental': 'c174799', 'Temporal Cascade': 'c49055', 'Myr Quadropod': 'c50176', 'Island': 'c221300', 'Slaughter Cry': 'c230762'}

def id_to_name(ID):
    return id_to_name_dict.get(ID, None)

def name_to_id(name):
    return name_to_id_dict.get(name, None)

def card_from_name(name):
    if name_to_id(name) is not None:
        return eval(name_to_id(name)+'()')
    else:
        return None
