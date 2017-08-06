from MTG.card import *
from MTG.gameObject import *


class c221309(Card):
    "Plains"
    def __init__(self):
        super(c221309, self).__init__(Characteristics(**{'color': [], 'text': 'W', 'mana_cost': '', 'name': 'Plains', 'subtype': ['Plains']}, supertype=[SuperType.BASIC], types=[CardType.LAND], abilities=[]))


class c221300(Card):
    "Island"
    def __init__(self):
        super(c221300, self).__init__(Characteristics(**{'color': [], 'text': 'U', 'mana_cost': '', 'name': 'Island', 'subtype': ['Island']}, supertype=[SuperType.BASIC], types=[CardType.LAND], abilities=[]))


class c26805(Card):
    "Tundra Kavu"
    def __init__(self):
        super(c26805, self).__init__(Characteristics(**{'subtype': ['Kavu'], 'toughness': 2, 'name': 'Tundra Kavu', 'power': 2, 'color': ['R'], 'text': '{T}: Target land becomes a Plains or an Island until end of turn.', 'mana_cost': '2R'}, supertype=[], types=[CardType.CREATURE], abilities=[]))


class c79145(Card):
    "Hundred-Talon Kami"
    def __init__(self):
        super(c79145, self).__init__(Characteristics(**{'subtype': ['Spirit'], 'toughness': 3, 'name': 'Hundred-Talon Kami', 'power': 2, 'color': ['W'], 'text': 'Flying\nSoulshift 4 (When this creature dies, you may return target Spirit card with converted mana cost 4 or less from your graveyard to your hand.)', 'mana_cost': '4W'}, supertype=[], types=[CardType.CREATURE], abilities=[StaticAbilities.Flying]))


class c370698(Card):
    "Blood Bairn"
    def __init__(self):
        super(c370698, self).__init__(Characteristics(**{'subtype': ['Vampire'], 'toughness': 2, 'name': 'Blood Bairn', 'power': 2, 'color': ['B'], 'text': 'Sacrifice another creature: Blood Bairn gets +2/+2 until end of turn.', 'mana_cost': '2B'}, supertype=[], types=[CardType.CREATURE], abilities=[]))


class c3060(Card):
    "Soldevi Sentry"
    def __init__(self):
        super(c3060, self).__init__(Characteristics(**{'subtype': ['Soldier'], 'toughness': 1, 'name': 'Soldevi Sentry', 'power': 1, 'color': [], 'text': '{1}: Choose target opponent. Regenerate Soldevi Sentry. When it regenerates this way, that player may draw a card.', 'mana_cost': '1'}, supertype=[], types=[CardType.ARTIFACT, CardType.CREATURE], abilities=[]))


class c34243(Card):
    "Ancestor's Chosen"
    def __init__(self):
        super(c34243, self).__init__(Characteristics(**{'subtype': ['Human', 'Cleric'], 'toughness': 4, 'name': "Ancestor's Chosen", 'power': 4, 'color': ['W'], 'text': "First strike (This creature deals combat damage before creatures without first strike.)\nWhen Ancestor's Chosen enters the battlefield, you gain 1 life for each card in your graveyard.", 'mana_cost': '5WW'}, supertype=[], types=[CardType.CREATURE], abilities=[]))


class c174799(Card):
    "Hellspark Elemental"
    def __init__(self):
        super(c174799, self).__init__(Characteristics(**{'subtype': ['Elemental'], 'toughness': 1, 'name': 'Hellspark Elemental', 'power': 3, 'color': ['R'], 'text': 'Trample, haste\nAt the beginning of the end step, sacrifice Hellspark Elemental.\nUnearth {1}{R} ({1}{R}: Return this card from your graveyard to the battlefield. It gains haste. Exile it at the beginning of the next end step or if it would leave the battlefield. Unearth only as a sorcery.)', 'mana_cost': '1R'}, supertype=[], types=[CardType.CREATURE], abilities=[StaticAbilities.Haste, StaticAbilities.Trample]))


class c179594(Card):
    "Sewn-Eye Drake"
    def __init__(self):
        super(c179594, self).__init__(Characteristics(**{'subtype': ['Zombie', 'Drake'], 'toughness': 1, 'name': 'Sewn-Eye Drake', 'power': 3, 'color': ['U', 'B', 'R'], 'text': 'Flying, haste', 'mana_cost': '2(U/R)B'}, supertype=[], types=[CardType.CREATURE], abilities=[StaticAbilities.Flying, StaticAbilities.Haste]))


class c29973(Card):
    "Price of Glory"
    def __init__(self):
        super(c29973, self).__init__(Characteristics(**{'color': ['R'], 'text': "Whenever a player taps a land for mana, if it's not that player's turn, destroy that land.", 'mana_cost': '2R', 'name': 'Price of Glory'}, supertype=[], types=[CardType.ENCHANTMENT], abilities=[]))


class c21190(Card):
    "Sun Clasp"
    def __init__(self):
        super(c21190, self).__init__(Characteristics(**{'color': ['W'], 'text': "Enchant creature\nEnchanted creature gets +1/+3.\n{W}: Return enchanted creature to its owner's hand.", 'mana_cost': '1W', 'name': 'Sun Clasp', 'subtype': ['Aura']}, supertype=[], types=[CardType.ENCHANTMENT], abilities=[]))


class c2473(Card):
    "Mind Whip"
    def __init__(self):
        super(c2473, self).__init__(Characteristics(**{'color': ['B'], 'text': "Enchant creature\nAt the beginning of the upkeep of enchanted creature's controller, that player may pay {3}. If he or she doesn't, Mind Whip deals 2 damage to that player and you tap that creature.", 'mana_cost': '2BB', 'name': 'Mind Whip', 'subtype': ['Aura']}, supertype=[], types=[CardType.ENCHANTMENT], abilities=[]))


class c5806(Card):
    "Fluctuator"
    def __init__(self):
        super(c5806, self).__init__(Characteristics(**{'color': [], 'text': 'Cycling abilities you activate cost you up to {2} less to activate.', 'mana_cost': '2', 'name': 'Fluctuator'}, supertype=[], types=[CardType.ARTIFACT], abilities=[]))


class c230762(Card):
    "Slaughter Cry"
    def __init__(self):
        super(c230762, self).__init__(Characteristics(**{'color': ['R'], 'text': 'Target creature gets +3/+0 and gains first strike until end of turn. (It deals combat damage before creatures without first strike.)', 'mana_cost': '2R', 'name': 'Slaughter Cry'}, supertype=[], types=[CardType.INSTANT], abilities=[]))


class c24615(Card):
    "Despoil"
    def __init__(self):
        super(c24615, self).__init__(Characteristics(**{'color': ['B'], 'text': 'Destroy target land. Its controller loses 2 life.', 'mana_cost': '3B', 'name': 'Despoil'}, supertype=[], types=[CardType.SORCERY], abilities=[]))


class c22061(Card):
    "Overlaid Terrain"
    def __init__(self):
        super(c22061, self).__init__(Characteristics(**{'color': ['G'], 'text': 'As Overlaid Terrain enters the battlefield, sacrifice all lands you control.\nLands you control have "{T}: Add two mana of any one color to your mana pool."', 'mana_cost': '2GG', 'name': 'Overlaid Terrain'}, supertype=[], types=[CardType.ENCHANTMENT], abilities=[]))


class c215101(Card):
    "Ogre Geargrabber"
    def __init__(self):
        super(c215101, self).__init__(Characteristics(**{'subtype': ['Ogre', 'Warrior'], 'toughness': 4, 'name': 'Ogre Geargrabber', 'power': 4, 'color': ['R'], 'text': 'Whenever Ogre Geargrabber attacks, gain control of target Equipment an opponent controls until end of turn. Attach it to Ogre Geargrabber. When you lose control of that Equipment, unattach it.', 'mana_cost': '4RR'}, supertype=[], types=[CardType.CREATURE], abilities=[]))


class c96920(Card):
    "Vedalken Plotter"
    def __init__(self):
        super(c96920, self).__init__(Characteristics(**{'subtype': ['Vedalken', 'Wizard'], 'toughness': 1, 'name': 'Vedalken Plotter', 'power': 1, 'color': ['U'], 'text': 'When Vedalken Plotter enters the battlefield, exchange control of target land you control and target land an opponent controls.', 'mana_cost': '2U'}, supertype=[], types=[CardType.CREATURE], abilities=[]))


class c1476(Card):
    "Devouring Deep"
    def __init__(self):
        super(c1476, self).__init__(Characteristics(**{'subtype': ['Fish'], 'toughness': 2, 'name': 'Devouring Deep', 'power': 1, 'color': ['U'], 'text': 'Islandwalk', 'mana_cost': '2U'}, supertype=[], types=[CardType.CREATURE], abilities=[StaticAbilities.Islandwalk]))


class c49055(Card):
    "Temporal Cascade"
    def __init__(self):
        super(c49055, self).__init__(Characteristics(**{'color': ['U'], 'text': 'Choose one - Each player shuffles his or her hand and graveyard into his or her library; or each player draws seven cards.\nEntwine {2} (Choose both if you pay the entwine cost.)', 'mana_cost': '5UU', 'name': 'Temporal Cascade'}, supertype=[], types=[CardType.SORCERY], abilities=[]))


class c50176(Card):
    "Myr Quadropod"
    def __init__(self):
        super(c50176, self).__init__(Characteristics(**{'subtype': ['Myr'], 'toughness': 4, 'name': 'Myr Quadropod', 'power': 1, 'color': [], 'text': "{3}: Switch Myr Quadropod's power and toughness until end of turn.", 'mana_cost': '4'}, supertype=[], types=[CardType.ARTIFACT, CardType.CREATURE], abilities=[]))


class c233086(Card):
    "Flameborn Viron"
    def __init__(self):
        super(c233086, self).__init__(Characteristics(**{'subtype': ['Insect'], 'toughness': 4, 'name': 'Flameborn Viron', 'power': 6, 'color': ['R'], 'text': '', 'mana_cost': '4RR'}, supertype=[], types=[CardType.CREATURE], abilities=[]))


class c226561(Card):
    "Taste of Blood"
    def __init__(self):
        super(c226561, self).__init__(Characteristics(**{'color': ['B'], 'text': 'Taste of Blood deals 1 damage to target player and you gain 1 life.', 'mana_cost': 'B', 'name': 'Taste of Blood'}, supertype=[], types=[CardType.SORCERY], abilities=[]))


class c240039(Card):
    "Homicidal Seclusion"
    def __init__(self):
        super(c240039, self).__init__(Characteristics(**{'color': ['B'], 'text': 'As long as you control exactly one creature, that creature gets +3/+1 and has lifelink.', 'mana_cost': '4B', 'name': 'Homicidal Seclusion'}, supertype=[], types=[CardType.ENCHANTMENT], abilities=[]))


class c3610(Card):
    "Brood of Cockroaches"
    def __init__(self):
        super(c3610, self).__init__(Characteristics(**{'subtype': ['Insect'], 'toughness': 1, 'name': 'Brood of Cockroaches', 'power': 1, 'color': ['B'], 'text': 'When Brood of Cockroaches is put into your graveyard from the battlefield, at the beginning of the next end step, you lose 1 life and return Brood of Cockroaches to your hand.', 'mana_cost': '1B'}, supertype=[], types=[CardType.CREATURE], abilities=[]))


class c73960(Card):
    "Orcish Paratroopers"
    def __init__(self):
        super(c73960, self).__init__(Characteristics(**{'subtype': ['Orc', 'Paratrooper'], 'toughness': 4, 'name': 'Orcish Paratroopers', 'power': 4, 'color': ['R'], 'text': 'When Orcish Paratroopers comes into play, flip it from a height of at least one foot. Sacrifice Orcish Paratroopers unless it lands face up after turning over completely.', 'mana_cost': '2R'}, supertype=[], types=[CardType.CREATURE], abilities=[]))


class c19647(Card):
    "Cho-Arrim Alchemist"
    def __init__(self):
        super(c19647, self).__init__(Characteristics(**{'subtype': ['Human', 'Spellshaper'], 'toughness': 1, 'name': 'Cho-Arrim Alchemist', 'power': 1, 'color': ['W'], 'text': '{1}{W}{W}, {T}, Discard a card: The next time a source of your choice would deal damage to you this turn, prevent that damage. You gain life equal to the damage prevented this way.', 'mana_cost': 'W'}, supertype=[], types=[CardType.CREATURE], abilities=[]))


class c193467(Card):
    "Near-Death Experience"
    def __init__(self):
        super(c193467, self).__init__(Characteristics(**{'color': ['W'], 'text': 'At the beginning of your upkeep, if you have exactly 1 life, you win the game.', 'mana_cost': '2WWW', 'name': 'Near-Death Experience'}, supertype=[], types=[CardType.ENCHANTMENT], abilities=[]))


class c74238(Card):
    "Persecute Artist"
    def __init__(self):
        super(c74238, self).__init__(Characteristics(**{'color': ['B'], 'text': 'Choose an artist other than Rebecca Guay. Target player reveals his or her hand and discards all nonland cards by the chosen artist.', 'mana_cost': '1BB', 'name': 'Persecute Artist'}, supertype=[], types=[CardType.SORCERY], abilities=[]))


class c369080(Card):
    "Turn // Burn"
    def __init__(self):
        super(c369080, self).__init__(Characteristics(**{'color': ['R'], 'text': 'Burn deals 2 damage to target creature or player.\nFuse (You may cast one or both halves of this card from your hand.)\n---\nTarget creature loses all abilities and becomes a 0/1 red Weird until end of turn.\nFuse (You may cast one or both halves of this card from your hand.)', 'mana_cost': '1R', 'name': 'Turn // Burn'}, supertype=[], types=[CardType.INSTANT], abilities=[]))


class c142027(Card):
    "Silkbind Faerie"
    def __init__(self):
        super(c142027, self).__init__(Characteristics(**{'subtype': ['Faerie', 'Rogue'], 'toughness': 3, 'name': 'Silkbind Faerie', 'power': 1, 'color': ['W', 'U'], 'text': 'Flying\n{1}{(w/u)}, {Q}: Tap target creature. ({Q} is the untap symbol.)', 'mana_cost': '2(W/U)'}, supertype=[], types=[CardType.CREATURE], abilities=[StaticAbilities.Flying]))


class c21320(Card):
    "Battlefield Percher"
    def __init__(self):
        super(c21320, self).__init__(Characteristics(**{'subtype': ['Bird'], 'toughness': 2, 'name': 'Battlefield Percher', 'power': 2, 'color': ['B'], 'text': 'Flying\nBattlefield Percher can block only creatures with flying.\n{1}{B}: Battlefield Percher gets +1/+1 until end of turn.', 'mana_cost': '3BB'}, supertype=[], types=[CardType.CREATURE], abilities=[StaticAbilities.Flying]))


class c212614(Card):
    "I Bask in Your Silent Awe"
    def __init__(self):
        super(c212614, self).__init__(Characteristics(**{'color': [], 'text': "(An ongoing scheme remains face up until it's abandoned.)\nEach opponent can't cast more than one spell each turn.\nAt the beginning of your upkeep, if no opponent cast a spell since your last turn ended, abandon this scheme.", 'mana_cost': '', 'name': 'I Bask in Your Silent Awe'}, supertype=[], types=[CardType.ONGOING, CardType.SCHEME], abilities=[]))


id_to_name_dict = {'c240039': 'Homicidal Seclusion', 'c212614': 'I Bask in Your Silent Awe', 'c79145': 'Hundred-Talon Kami', 'c19647': 'Cho-Arrim Alchemist', 'c142027': 'Silkbind Faerie', 'c21320': 'Battlefield Percher', 'c5806': 'Fluctuator', 'c174799': 'Hellspark Elemental', 'c24615': 'Despoil', 'c49055': 'Temporal Cascade', 'c369080': 'Turn // Burn', 'c2473': 'Mind Whip', 'c22061': 'Overlaid Terrain', 'c193467': 'Near-Death Experience', 'c226561': 'Taste of Blood', 'c233086': 'Flameborn Viron', 'c34243': "Ancestor's Chosen", 'c221309': 'Plains', 'c21190': 'Sun Clasp', 'c26805': 'Tundra Kavu', 'c370698': 'Blood Bairn', 'c3060': 'Soldevi Sentry', 'c96920': 'Vedalken Plotter', 'c230762': 'Slaughter Cry', 'c29973': 'Price of Glory', 'c74238': 'Persecute Artist', 'c215101': 'Ogre Geargrabber', 'c221300': 'Island', 'c3610': 'Brood of Cockroaches', 'c50176': 'Myr Quadropod', 'c179594': 'Sewn-Eye Drake', 'c73960': 'Orcish Paratroopers', 'c1476': 'Devouring Deep'}

name_to_id_dict = {'Orcish Paratroopers': 'c73960', 'Island': 'c221300', 'Sun Clasp': 'c21190', 'Battlefield Percher': 'c21320', 'Sewn-Eye Drake': 'c179594', 'Persecute Artist': 'c74238', 'Overlaid Terrain': 'c22061', 'Homicidal Seclusion': 'c240039', 'Mind Whip': 'c2473', 'Fluctuator': 'c5806', 'Myr Quadropod': 'c50176', 'Plains': 'c221309', 'Near-Death Experience': 'c193467', 'Turn // Burn': 'c369080', 'Devouring Deep': 'c1476', 'Brood of Cockroaches': 'c3610', 'Soldevi Sentry': 'c3060', 'Vedalken Plotter': 'c96920', 'Taste of Blood': 'c226561', 'Slaughter Cry': 'c230762', 'Temporal Cascade': 'c49055', 'Cho-Arrim Alchemist': 'c19647', 'Hellspark Elemental': 'c174799', "Ancestor's Chosen": 'c34243', 'Hundred-Talon Kami': 'c79145', 'Flameborn Viron': 'c233086', 'Tundra Kavu': 'c26805', 'Silkbind Faerie': 'c142027', 'I Bask in Your Silent Awe': 'c212614', 'Price of Glory': 'c29973', 'Blood Bairn': 'c370698', 'Despoil': 'c24615', 'Ogre Geargrabber': 'c215101'}


