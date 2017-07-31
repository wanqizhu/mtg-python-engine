from MTG.card import *
from MTG.gameObject import *


class c221309(Card):
    "Plains"
    def __init__(self):
        super(c221309, self).__init__(Characteristics(**{'subtype': ['Plains'], 'mana_cost': '', 'color': [], 'text': 'W', 'name': 'Plains'}, supertype=SuperType.BASIC, types=CardType.LAND))


class c221300(Card):
    "Island"
    def __init__(self):
        super(c221300, self).__init__(Characteristics(**{'subtype': ['Island'], 'mana_cost': '', 'color': [], 'text': 'U', 'name': 'Island'}, supertype=SuperType.BASIC, types=CardType.LAND))


class c26805(Card):
    "Tundra Kavu"
    def __init__(self):
        super(c26805, self).__init__(Characteristics(**{'subtype': ['Kavu'], 'mana_cost': '2R', 'color': ['R'], 'text': '{T}: Target land becomes a Plains or an Island until end of turn.', 'name': 'Tundra Kavu'}, supertype=None, types=CardType.CREATURE))


class c79145(Card):
    "Hundred-Talon Kami"
    def __init__(self):
        super(c79145, self).__init__(Characteristics(**{'subtype': ['Spirit'], 'mana_cost': '4W', 'color': ['W'], 'text': 'Flying\nSoulshift 4 (When this creature dies, you may return target Spirit card with converted mana cost 4 or less from your graveyard to your hand.)', 'name': 'Hundred-Talon Kami'}, supertype=None, types=CardType.CREATURE))


class c370698(Card):
    "Blood Bairn"
    def __init__(self):
        super(c370698, self).__init__(Characteristics(**{'subtype': ['Vampire'], 'mana_cost': '2B', 'color': ['B'], 'text': 'Sacrifice another creature: Blood Bairn gets +2/+2 until end of turn.', 'name': 'Blood Bairn'}, supertype=None, types=CardType.CREATURE))


class c3060(Card):
    "Soldevi Sentry"
    def __init__(self):
        super(c3060, self).__init__(Characteristics(**{'subtype': ['Soldier'], 'mana_cost': '1', 'color': [], 'text': '{1}: Choose target opponent. Regenerate Soldevi Sentry. When it regenerates this way, that player may draw a card.', 'name': 'Soldevi Sentry'}, supertype=SuperType.ARTIFACT, types=CardType.CREATURE))


class c34243(Card):
    "Ancestor's Chosen"
    def __init__(self):
        super(c34243, self).__init__(Characteristics(**{'subtype': ['Human', 'Cleric'], 'mana_cost': '5WW', 'color': ['W'], 'text': "First strike (This creature deals combat damage before creatures without first strike.)\nWhen Ancestor's Chosen enters the battlefield, you gain 1 life for each card in your graveyard.", 'name': "Ancestor's Chosen"}, supertype=None, types=CardType.CREATURE))


class c174799(Card):
    "Hellspark Elemental"
    def __init__(self):
        super(c174799, self).__init__(Characteristics(**{'subtype': ['Elemental'], 'mana_cost': '1R', 'color': ['R'], 'text': 'Trample, haste\nAt the beginning of the end step, sacrifice Hellspark Elemental.\nUnearth {1}{R} ({1}{R}: Return this card from your graveyard to the battlefield. It gains haste. Exile it at the beginning of the next end step or if it would leave the battlefield. Unearth only as a sorcery.)', 'name': 'Hellspark Elemental'}, supertype=None, types=CardType.CREATURE))


class c179594(Card):
    "Sewn-Eye Drake"
    def __init__(self):
        super(c179594, self).__init__(Characteristics(**{'subtype': ['Zombie', 'Drake'], 'mana_cost': '2(U/R)B', 'color': ['U', 'B', 'R'], 'text': 'Flying, haste', 'name': 'Sewn-Eye Drake'}, supertype=None, types=CardType.CREATURE))


class c29973(Card):
    "Price of Glory"
    def __init__(self):
        super(c29973, self).__init__(Characteristics(**{'mana_cost': '2R', 'color': ['R'], 'text': "Whenever a player taps a land for mana, if it's not that player's turn, destroy that land.", 'name': 'Price of Glory'}, supertype=None, types=CardType.ENCHANTMENT))


class c21190(Card):
    "Sun Clasp"
    def __init__(self):
        super(c21190, self).__init__(Characteristics(**{'subtype': ['Aura'], 'mana_cost': '1W', 'color': ['W'], 'text': "Enchant creature\nEnchanted creature gets +1/+3.\n{W}: Return enchanted creature to its owner's hand.", 'name': 'Sun Clasp'}, supertype=None, types=CardType.ENCHANTMENT))


class c2473(Card):
    "Mind Whip"
    def __init__(self):
        super(c2473, self).__init__(Characteristics(**{'subtype': ['Aura'], 'mana_cost': '2BB', 'color': ['B'], 'text': "Enchant creature\nAt the beginning of the upkeep of enchanted creature's controller, that player may pay {3}. If he or she doesn't, Mind Whip deals 2 damage to that player and you tap that creature.", 'name': 'Mind Whip'}, supertype=None, types=CardType.ENCHANTMENT))


class c5806(Card):
    "Fluctuator"
    def __init__(self):
        super(c5806, self).__init__(Characteristics(**{'mana_cost': '2', 'color': [], 'text': 'Cycling abilities you activate cost you up to {2} less to activate.', 'name': 'Fluctuator'}, supertype=None, types=CardType.ARTIFACT))


class c230762(Card):
    "Slaughter Cry"
    def __init__(self):
        super(c230762, self).__init__(Characteristics(**{'mana_cost': '2R', 'color': ['R'], 'text': 'Target creature gets +3/+0 and gains first strike until end of turn. (It deals combat damage before creatures without first strike.)', 'name': 'Slaughter Cry'}, supertype=None, types=CardType.INSTANT))


class c24615(Card):
    "Despoil"
    def __init__(self):
        super(c24615, self).__init__(Characteristics(**{'mana_cost': '3B', 'color': ['B'], 'text': 'Destroy target land. Its controller loses 2 life.', 'name': 'Despoil'}, supertype=None, types=CardType.SORCERY))


class c22061(Card):
    "Overlaid Terrain"
    def __init__(self):
        super(c22061, self).__init__(Characteristics(**{'mana_cost': '2GG', 'color': ['G'], 'text': 'As Overlaid Terrain enters the battlefield, sacrifice all lands you control.\nLands you control have "{T}: Add two mana of any one color to your mana pool."', 'name': 'Overlaid Terrain'}, supertype=None, types=CardType.ENCHANTMENT))


class c215101(Card):
    "Ogre Geargrabber"
    def __init__(self):
        super(c215101, self).__init__(Characteristics(**{'subtype': ['Ogre', 'Warrior'], 'mana_cost': '4RR', 'color': ['R'], 'text': 'Whenever Ogre Geargrabber attacks, gain control of target Equipment an opponent controls until end of turn. Attach it to Ogre Geargrabber. When you lose control of that Equipment, unattach it.', 'name': 'Ogre Geargrabber'}, supertype=None, types=CardType.CREATURE))


class c96920(Card):
    "Vedalken Plotter"
    def __init__(self):
        super(c96920, self).__init__(Characteristics(**{'subtype': ['Vedalken', 'Wizard'], 'mana_cost': '2U', 'color': ['U'], 'text': 'When Vedalken Plotter enters the battlefield, exchange control of target land you control and target land an opponent controls.', 'name': 'Vedalken Plotter'}, supertype=None, types=CardType.CREATURE))


class c1476(Card):
    "Devouring Deep"
    def __init__(self):
        super(c1476, self).__init__(Characteristics(**{'subtype': ['Fish'], 'mana_cost': '2U', 'color': ['U'], 'text': 'Islandwalk', 'name': 'Devouring Deep'}, supertype=None, types=CardType.CREATURE))


class c49055(Card):
    "Temporal Cascade"
    def __init__(self):
        super(c49055, self).__init__(Characteristics(**{'mana_cost': '5UU', 'color': ['U'], 'text': 'Choose one - Each player shuffles his or her hand and graveyard into his or her library; or each player draws seven cards.\nEntwine {2} (Choose both if you pay the entwine cost.)', 'name': 'Temporal Cascade'}, supertype=None, types=CardType.SORCERY))


class c50176(Card):
    "Myr Quadropod"
    def __init__(self):
        super(c50176, self).__init__(Characteristics(**{'subtype': ['Myr'], 'mana_cost': '4', 'color': [], 'text': "{3}: Switch Myr Quadropod's power and toughness until end of turn.", 'name': 'Myr Quadropod'}, supertype=SuperType.ARTIFACT, types=CardType.CREATURE))


class c233086(Card):
    "Flameborn Viron"
    def __init__(self):
        super(c233086, self).__init__(Characteristics(**{'subtype': ['Insect'], 'mana_cost': '4RR', 'color': ['R'], 'text': '', 'name': 'Flameborn Viron'}, supertype=None, types=CardType.CREATURE))


class c226561(Card):
    "Taste of Blood"
    def __init__(self):
        super(c226561, self).__init__(Characteristics(**{'mana_cost': 'B', 'color': ['B'], 'text': 'Taste of Blood deals 1 damage to target player and you gain 1 life.', 'name': 'Taste of Blood'}, supertype=None, types=CardType.SORCERY))


class c240039(Card):
    "Homicidal Seclusion"
    def __init__(self):
        super(c240039, self).__init__(Characteristics(**{'mana_cost': '4B', 'color': ['B'], 'text': 'As long as you control exactly one creature, that creature gets +3/+1 and has lifelink.', 'name': 'Homicidal Seclusion'}, supertype=None, types=CardType.ENCHANTMENT))


class c3610(Card):
    "Brood of Cockroaches"
    def __init__(self):
        super(c3610, self).__init__(Characteristics(**{'subtype': ['Insect'], 'mana_cost': '1B', 'color': ['B'], 'text': 'When Brood of Cockroaches is put into your graveyard from the battlefield, at the beginning of the next end step, you lose 1 life and return Brood of Cockroaches to your hand.', 'name': 'Brood of Cockroaches'}, supertype=None, types=CardType.CREATURE))


class c73960(Card):
    "Orcish Paratroopers"
    def __init__(self):
        super(c73960, self).__init__(Characteristics(**{'subtype': ['Orc', 'Paratrooper'], 'mana_cost': '2R', 'color': ['R'], 'text': 'When Orcish Paratroopers comes into play, flip it from a height of at least one foot. Sacrifice Orcish Paratroopers unless it lands face up after turning over completely.', 'name': 'Orcish Paratroopers'}, supertype=None, types=CardType.CREATURE))


class c19647(Card):
    "Cho-Arrim Alchemist"
    def __init__(self):
        super(c19647, self).__init__(Characteristics(**{'subtype': ['Human', 'Spellshaper'], 'mana_cost': 'W', 'color': ['W'], 'text': '{1}{W}{W}, {T}, Discard a card: The next time a source of your choice would deal damage to you this turn, prevent that damage. You gain life equal to the damage prevented this way.', 'name': 'Cho-Arrim Alchemist'}, supertype=None, types=CardType.CREATURE))


class c193467(Card):
    "Near-Death Experience"
    def __init__(self):
        super(c193467, self).__init__(Characteristics(**{'mana_cost': '2WWW', 'color': ['W'], 'text': 'At the beginning of your upkeep, if you have exactly 1 life, you win the game.', 'name': 'Near-Death Experience'}, supertype=None, types=CardType.ENCHANTMENT))


class c74238(Card):
    "Persecute Artist"
    def __init__(self):
        super(c74238, self).__init__(Characteristics(**{'mana_cost': '1BB', 'color': ['B'], 'text': 'Choose an artist other than Rebecca Guay. Target player reveals his or her hand and discards all nonland cards by the chosen artist.', 'name': 'Persecute Artist'}, supertype=None, types=CardType.SORCERY))


class c369080(Card):
    "Turn // Burn"
    def __init__(self):
        super(c369080, self).__init__(Characteristics(**{'mana_cost': '1R', 'color': ['R'], 'text': 'Burn deals 2 damage to target creature or player.\nFuse (You may cast one or both halves of this card from your hand.)\n---\nTarget creature loses all abilities and becomes a 0/1 red Weird until end of turn.\nFuse (You may cast one or both halves of this card from your hand.)', 'name': 'Turn // Burn'}, supertype=None, types=CardType.INSTANT))


class c142027(Card):
    "Silkbind Faerie"
    def __init__(self):
        super(c142027, self).__init__(Characteristics(**{'subtype': ['Faerie', 'Rogue'], 'mana_cost': '2(W/U)', 'color': ['W', 'U'], 'text': 'Flying\n{1}{(w/u)}, {Q}: Tap target creature. ({Q} is the untap symbol.)', 'name': 'Silkbind Faerie'}, supertype=None, types=CardType.CREATURE))


class c21320(Card):
    "Battlefield Percher"
    def __init__(self):
        super(c21320, self).__init__(Characteristics(**{'subtype': ['Bird'], 'mana_cost': '3BB', 'color': ['B'], 'text': 'Flying\nBattlefield Percher can block only creatures with flying.\n{1}{B}: Battlefield Percher gets +1/+1 until end of turn.', 'name': 'Battlefield Percher'}, supertype=None, types=CardType.CREATURE))


class c212614(Card):
    "I Bask in Your Silent Awe"
    def __init__(self):
        super(c212614, self).__init__(Characteristics(**{'mana_cost': '', 'color': [], 'text': "(An ongoing scheme remains face up until it's abandoned.)\nEach opponent can't cast more than one spell each turn.\nAt the beginning of your upkeep, if no opponent cast a spell since your last turn ended, abandon this scheme.", 'name': 'I Bask in Your Silent Awe'}, supertype=SuperType.ONGOING, types=CardType.SCHEME))


id_to_name_dict = {'c2473': 'Mind Whip', 'c221309': 'Plains', 'c212614': 'I Bask in Your Silent Awe', 'c1476': 'Devouring Deep', 'c193467': 'Near-Death Experience', 'c240039': 'Homicidal Seclusion', 'c215101': 'Ogre Geargrabber', 'c74238': 'Persecute Artist', 'c22061': 'Overlaid Terrain', 'c49055': 'Temporal Cascade', 'c26805': 'Tundra Kavu', 'c96920': 'Vedalken Plotter', 'c5806': 'Fluctuator', 'c21320': 'Battlefield Percher', 'c221300': 'Island', 'c79145': 'Hundred-Talon Kami', 'c3060': 'Soldevi Sentry', 'c50176': 'Myr Quadropod', 'c226561': 'Taste of Blood', 'c21190': 'Sun Clasp', 'c230762': 'Slaughter Cry', 'c73960': 'Orcish Paratroopers', 'c29973': 'Price of Glory', 'c233086': 'Flameborn Viron', 'c370698': 'Blood Bairn', 'c3610': 'Brood of Cockroaches', 'c179594': 'Sewn-Eye Drake', 'c34243': "Ancestor's Chosen", 'c369080': 'Turn // Burn', 'c142027': 'Silkbind Faerie', 'c174799': 'Hellspark Elemental', 'c24615': 'Despoil', 'c19647': 'Cho-Arrim Alchemist'}

name_to_id_dict = {'Ogre Geargrabber': 'c215101', 'Vedalken Plotter': 'c96920', 'Brood of Cockroaches': 'c3610', 'Island': 'c221300', 'Overlaid Terrain': 'c22061', 'Persecute Artist': 'c74238', 'Despoil': 'c24615', 'Soldevi Sentry': 'c3060', 'Turn // Burn': 'c369080', 'Myr Quadropod': 'c50176', 'Tundra Kavu': 'c26805', 'Near-Death Experience': 'c193467', 'Silkbind Faerie': 'c142027', 'Devouring Deep': 'c1476', 'Sewn-Eye Drake': 'c179594', 'Fluctuator': 'c5806', 'Orcish Paratroopers': 'c73960', "Ancestor's Chosen": 'c34243', 'Temporal Cascade': 'c49055', 'Cho-Arrim Alchemist': 'c19647', 'Hellspark Elemental': 'c174799', 'Blood Bairn': 'c370698', 'Flameborn Viron': 'c233086', 'Price of Glory': 'c29973', 'I Bask in Your Silent Awe': 'c212614', 'Hundred-Talon Kami': 'c79145', 'Taste of Blood': 'c226561', 'Sun Clasp': 'c21190', 'Mind Whip': 'c2473', 'Homicidal Seclusion': 'c240039', 'Plains': 'c221309', 'Battlefield Percher': 'c21320', 'Slaughter Cry': 'c230762'}

def id_to_name(ID):
    return id_to_name_dict.get(ID, None)

def name_to_id(name):
    return name_to_id_dict.get(name, None)

def card_from_name(name):
    if name_to_id(name) is not None:
        return eval(name_to_id(name)+'()')
    else:
        return None
