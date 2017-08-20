from MTG import card
from MTG import gameobject
from MTG import cardtype
from MTG import abilities
from MTG import mana

class c27255(card.Card):
    "Lightning Bolt"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c27255, self).__init__(gameobject.Characteristics(**{'color': ['R'], 'text': 'Lightning Bolt deals 3 damage to target creature or player.', 'name': 'Lightning Bolt', 'mana_cost': 'R'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c221309(card.Card):
    "Plains"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c221309, self).__init__(gameobject.Characteristics(**{'subtype': ['Plains'], 'color': [], 'text': 'W', 'name': 'Plains', 'mana_cost': ''}, supertype=[cardtype.SuperType.BASIC], types=[cardtype.CardType.LAND], abilities=[]))

class c221300(card.Card):
    "Island"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c221300, self).__init__(gameobject.Characteristics(**{'subtype': ['Island'], 'color': [], 'text': 'U', 'name': 'Island', 'mana_cost': ''}, supertype=[cardtype.SuperType.BASIC], types=[cardtype.CardType.LAND], abilities=[]))

class c221311(card.Card):
    "Swamp"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c221311, self).__init__(gameobject.Characteristics(**{'subtype': ['Swamp'], 'color': [], 'text': 'B', 'name': 'Swamp', 'mana_cost': ''}, supertype=[cardtype.SuperType.BASIC], types=[cardtype.CardType.LAND], abilities=[]))

class c221297(card.Card):
    "Forest"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c221297, self).__init__(gameobject.Characteristics(**{'subtype': ['Forest'], 'color': [], 'text': 'G', 'name': 'Forest', 'mana_cost': ''}, supertype=[cardtype.SuperType.BASIC], types=[cardtype.CardType.LAND], abilities=[]))

class c983(card.Card):
    "Mountain"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c983, self).__init__(gameobject.Characteristics(**{'subtype': ['Mountain'], 'color': [], 'text': 'R', 'name': 'Mountain', 'mana_cost': ''}, supertype=[cardtype.SuperType.BASIC], types=[cardtype.CardType.LAND], abilities=[]))

class c26805(card.Card):
    "Tundra Kavu"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c26805, self).__init__(gameobject.Characteristics(**{'name': 'Tundra Kavu', 'power': 2, 'subtype': ['Kavu'], 'text': '{T}: Target land becomes a Plains or an Island until end of turn.', 'toughness': 2, 'color': ['R'], 'mana_cost': '2R'}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c79145(card.Card):
    "Hundred-Talon Kami"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c79145, self).__init__(gameobject.Characteristics(**{'name': 'Hundred-Talon Kami', 'power': 2, 'subtype': ['Spirit'], 'text': 'Flying\nSoulshift 4 (When this creature dies, you may return target Spirit card with converted mana cost 4 or less from your graveyard to your hand.)', 'toughness': 3, 'color': ['W'], 'mana_cost': '4W'}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Flying]))

class c370698(card.Card):
    "Blood Bairn"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c370698, self).__init__(gameobject.Characteristics(**{'name': 'Blood Bairn', 'power': 2, 'subtype': ['Vampire'], 'text': 'Sacrifice another creature: Blood Bairn gets +2/+2 until end of turn.', 'toughness': 2, 'color': ['B'], 'mana_cost': '2B'}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c3060(card.Card):
    "Soldevi Sentry"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c3060, self).__init__(gameobject.Characteristics(**{'name': 'Soldevi Sentry', 'power': 1, 'subtype': ['Soldier'], 'text': '{1}: Choose target opponent. Regenerate Soldevi Sentry. When it regenerates this way, that player may draw a card.', 'toughness': 1, 'color': [], 'mana_cost': '1'}, supertype=[], types=[cardtype.CardType.ARTIFACT, cardtype.CardType.CREATURE], abilities=[]))

class c34243(card.Card):
    "Ancestor's Chosen"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c34243, self).__init__(gameobject.Characteristics(**{'name': "Ancestor's Chosen", 'power': 4, 'subtype': ['Human', 'Cleric'], 'text': "First strike (This creature deals combat damage before creatures without first strike.)\nWhen Ancestor's Chosen enters the battlefield, you gain 1 life for each card in your graveyard.", 'toughness': 4, 'color': ['W'], 'mana_cost': '5WW'}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c174799(card.Card):
    "Hellspark Elemental"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c174799, self).__init__(gameobject.Characteristics(**{'name': 'Hellspark Elemental', 'power': 3, 'subtype': ['Elemental'], 'text': 'Trample, haste\nAt the beginning of the end step, sacrifice Hellspark Elemental.\nUnearth {1}{R} ({1}{R}: Return this card from your graveyard to the battlefield. It gains haste. Exile it at the beginning of the next end step or if it would leave the battlefield. Unearth only as a sorcery.)', 'toughness': 1, 'color': ['R'], 'mana_cost': '1R'}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Haste, abilities.StaticAbilities.Trample]))

class c179594(card.Card):
    "Sewn-Eye Drake"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c179594, self).__init__(gameobject.Characteristics(**{'name': 'Sewn-Eye Drake', 'power': 3, 'subtype': ['Zombie', 'Drake'], 'text': 'Flying, haste', 'toughness': 1, 'color': ['U', 'B', 'R'], 'mana_cost': '2(U/R)B'}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Flying, abilities.StaticAbilities.Haste]))

class c29973(card.Card):
    "Price of Glory"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c29973, self).__init__(gameobject.Characteristics(**{'color': ['R'], 'text': "Whenever a player taps a land for mana, if it's not that player's turn, destroy that land.", 'name': 'Price of Glory', 'mana_cost': '2R'}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c21190(card.Card):
    "Sun Clasp"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c21190, self).__init__(gameobject.Characteristics(**{'subtype': ['Aura'], 'color': ['W'], 'text': "Enchant creature\nEnchanted creature gets +1/+3.\n{W}: Return enchanted creature to its owner's hand.", 'name': 'Sun Clasp', 'mana_cost': '1W'}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c2473(card.Card):
    "Mind Whip"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c2473, self).__init__(gameobject.Characteristics(**{'subtype': ['Aura'], 'color': ['B'], 'text': "Enchant creature\nAt the beginning of the upkeep of enchanted creature's controller, that player may pay {3}. If he or she doesn't, Mind Whip deals 2 damage to that player and you tap that creature.", 'name': 'Mind Whip', 'mana_cost': '2BB'}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c5806(card.Card):
    "Fluctuator"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c5806, self).__init__(gameobject.Characteristics(**{'color': [], 'text': 'Cycling abilities you activate cost you up to {2} less to activate.', 'name': 'Fluctuator', 'mana_cost': '2'}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c230762(card.Card):
    "Slaughter Cry"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c230762, self).__init__(gameobject.Characteristics(**{'color': ['R'], 'text': 'Target creature gets +3/+0 and gains first strike until end of turn. (It deals combat damage before creatures without first strike.)', 'name': 'Slaughter Cry', 'mana_cost': '2R'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c24615(card.Card):
    "Despoil"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c24615, self).__init__(gameobject.Characteristics(**{'color': ['B'], 'text': 'Destroy target land. Its controller loses 2 life.', 'name': 'Despoil', 'mana_cost': '3B'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c22061(card.Card):
    "Overlaid Terrain"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c22061, self).__init__(gameobject.Characteristics(**{'color': ['G'], 'text': 'As Overlaid Terrain enters the battlefield, sacrifice all lands you control.\nLands you control have "{T}: Add two mana of any one color to your mana pool."', 'name': 'Overlaid Terrain', 'mana_cost': '2GG'}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c215101(card.Card):
    "Ogre Geargrabber"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c215101, self).__init__(gameobject.Characteristics(**{'name': 'Ogre Geargrabber', 'power': 4, 'subtype': ['Ogre', 'Warrior'], 'text': 'Whenever Ogre Geargrabber attacks, gain control of target Equipment an opponent controls until end of turn. Attach it to Ogre Geargrabber. When you lose control of that Equipment, unattach it.', 'toughness': 4, 'color': ['R'], 'mana_cost': '4RR'}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c96920(card.Card):
    "Vedalken Plotter"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c96920, self).__init__(gameobject.Characteristics(**{'name': 'Vedalken Plotter', 'power': 1, 'subtype': ['Vedalken', 'Wizard'], 'text': 'When Vedalken Plotter enters the battlefield, exchange control of target land you control and target land an opponent controls.', 'toughness': 1, 'color': ['U'], 'mana_cost': '2U'}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c1476(card.Card):
    "Devouring Deep"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c1476, self).__init__(gameobject.Characteristics(**{'name': 'Devouring Deep', 'power': 1, 'subtype': ['Fish'], 'text': 'Islandwalk', 'toughness': 2, 'color': ['U'], 'mana_cost': '2U'}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Islandwalk]))

class c49055(card.Card):
    "Temporal Cascade"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c49055, self).__init__(gameobject.Characteristics(**{'color': ['U'], 'text': 'Choose one - Each player shuffles his or her hand and graveyard into his or her library; or each player draws seven cards.\nEntwine {2} (Choose both if you pay the entwine cost.)', 'name': 'Temporal Cascade', 'mana_cost': '5UU'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c50176(card.Card):
    "Myr Quadropod"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c50176, self).__init__(gameobject.Characteristics(**{'name': 'Myr Quadropod', 'power': 1, 'subtype': ['Myr'], 'text': "{3}: Switch Myr Quadropod's power and toughness until end of turn.", 'toughness': 4, 'color': [], 'mana_cost': '4'}, supertype=[], types=[cardtype.CardType.ARTIFACT, cardtype.CardType.CREATURE], abilities=[]))

class c233086(card.Card):
    "Flameborn Viron"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c233086, self).__init__(gameobject.Characteristics(**{'name': 'Flameborn Viron', 'power': 6, 'subtype': ['Insect'], 'text': '', 'toughness': 4, 'color': ['R'], 'mana_cost': '4RR'}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c226561(card.Card):
    "Taste of Blood"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c226561, self).__init__(gameobject.Characteristics(**{'color': ['B'], 'text': 'Taste of Blood deals 1 damage to target player and you gain 1 life.', 'name': 'Taste of Blood', 'mana_cost': 'B'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c240039(card.Card):
    "Homicidal Seclusion"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c240039, self).__init__(gameobject.Characteristics(**{'color': ['B'], 'text': 'As long as you control exactly one creature, that creature gets +3/+1 and has lifelink.', 'name': 'Homicidal Seclusion', 'mana_cost': '4B'}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c3610(card.Card):
    "Brood of Cockroaches"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c3610, self).__init__(gameobject.Characteristics(**{'name': 'Brood of Cockroaches', 'power': 1, 'subtype': ['Insect'], 'text': 'When Brood of Cockroaches is put into your graveyard from the battlefield, at the beginning of the next end step, you lose 1 life and return Brood of Cockroaches to your hand.', 'toughness': 1, 'color': ['B'], 'mana_cost': '1B'}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c73960(card.Card):
    "Orcish Paratroopers"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c73960, self).__init__(gameobject.Characteristics(**{'name': 'Orcish Paratroopers', 'power': 4, 'subtype': ['Orc', 'Paratrooper'], 'text': 'When Orcish Paratroopers comes into play, flip it from a height of at least one foot. Sacrifice Orcish Paratroopers unless it lands face up after turning over completely.', 'toughness': 4, 'color': ['R'], 'mana_cost': '2R'}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c19647(card.Card):
    "Cho-Arrim Alchemist"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c19647, self).__init__(gameobject.Characteristics(**{'name': 'Cho-Arrim Alchemist', 'power': 1, 'subtype': ['Human', 'Spellshaper'], 'text': '{1}{W}{W}, {T}, Discard a card: The next time a source of your choice would deal damage to you this turn, prevent that damage. You gain life equal to the damage prevented this way.', 'toughness': 1, 'color': ['W'], 'mana_cost': 'W'}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c193467(card.Card):
    "Near-Death Experience"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c193467, self).__init__(gameobject.Characteristics(**{'color': ['W'], 'text': 'At the beginning of your upkeep, if you have exactly 1 life, you win the game.', 'name': 'Near-Death Experience', 'mana_cost': '2WWW'}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c74238(card.Card):
    "Persecute Artist"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c74238, self).__init__(gameobject.Characteristics(**{'color': ['B'], 'text': 'Choose an artist other than Rebecca Guay. Target player reveals his or her hand and discards all nonland cards by the chosen artist.', 'name': 'Persecute Artist', 'mana_cost': '1BB'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c369080(card.Card):
    "Turn // Burn"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c369080, self).__init__(gameobject.Characteristics(**{'color': ['R'], 'text': 'Burn deals 2 damage to target creature or player.\nFuse (You may cast one or both halves of this card from your hand.)\n---\nTarget creature loses all abilities and becomes a 0/1 red Weird until end of turn.\nFuse (You may cast one or both halves of this card from your hand.)', 'name': 'Turn // Burn', 'mana_cost': '1R'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c142027(card.Card):
    "Silkbind Faerie"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c142027, self).__init__(gameobject.Characteristics(**{'name': 'Silkbind Faerie', 'power': 1, 'subtype': ['Faerie', 'Rogue'], 'text': 'Flying\n{1}{(w/u)}, {Q}: Tap target creature. ({Q} is the untap symbol.)', 'toughness': 3, 'color': ['W', 'U'], 'mana_cost': '2(W/U)'}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Flying]))

class c21320(card.Card):
    "Battlefield Percher"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c21320, self).__init__(gameobject.Characteristics(**{'name': 'Battlefield Percher', 'power': 2, 'subtype': ['Bird'], 'text': 'Flying\nBattlefield Percher can block only creatures with flying.\n{1}{B}: Battlefield Percher gets +1/+1 until end of turn.', 'toughness': 2, 'color': ['B'], 'mana_cost': '3BB'}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Flying]))

class c212614(card.Card):
    "I Bask in Your Silent Awe"
    activated_abilities = []
    _activated_abilities_costs = []
    _activated_abilities_effects = []
    _activated_abilities_costs_validation = []
    def __init__(self):
        super(c212614, self).__init__(gameobject.Characteristics(**{'color': [], 'text': "(An ongoing scheme remains face up until it's abandoned.)\nEach opponent can't cast more than one spell each turn.\nAt the beginning of your upkeep, if no opponent cast a spell since your last turn ended, abandon this scheme.", 'name': 'I Bask in Your Silent Awe', 'mana_cost': ''}, supertype=[], types=[cardtype.CardType.ONGOING, cardtype.CardType.SCHEME], abilities=[]))

