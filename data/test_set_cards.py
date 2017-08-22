from MTG import card
from MTG import gameobject
from MTG import cardtype
from MTG import abilities
from MTG import mana

class c27255(card.Card):
    "Lightning Bolt"
    def __init__(self):
        super(c27255, self).__init__(gameobject.Characteristics(**{'mana_cost': 'R', 'name': 'Lightning Bolt', 'color': ['R'], 'text': 'Lightning Bolt deals 3 damage to target creature or player.'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c221309(card.Card):
    "Plains"
    def __init__(self):
        super(c221309, self).__init__(gameobject.Characteristics(**{'subtype': ['Plains'], 'mana_cost': '', 'name': 'Plains', 'color': [], 'text': 'W'}, supertype=[cardtype.SuperType.BASIC], types=[cardtype.CardType.LAND], abilities=[]))

class c221300(card.Card):
    "Island"
    def __init__(self):
        super(c221300, self).__init__(gameobject.Characteristics(**{'subtype': ['Island'], 'mana_cost': '', 'name': 'Island', 'color': [], 'text': 'U'}, supertype=[cardtype.SuperType.BASIC], types=[cardtype.CardType.LAND], abilities=[]))

class c221311(card.Card):
    "Swamp"
    def __init__(self):
        super(c221311, self).__init__(gameobject.Characteristics(**{'subtype': ['Swamp'], 'mana_cost': '', 'name': 'Swamp', 'color': [], 'text': 'B'}, supertype=[cardtype.SuperType.BASIC], types=[cardtype.CardType.LAND], abilities=[]))

class c221297(card.Card):
    "Forest"
    def __init__(self):
        super(c221297, self).__init__(gameobject.Characteristics(**{'subtype': ['Forest'], 'mana_cost': '', 'name': 'Forest', 'color': [], 'text': 'G'}, supertype=[cardtype.SuperType.BASIC], types=[cardtype.CardType.LAND], abilities=[]))

class c983(card.Card):
    "Mountain"
    def __init__(self):
        super(c983, self).__init__(gameobject.Characteristics(**{'subtype': ['Mountain'], 'mana_cost': '', 'name': 'Mountain', 'color': [], 'text': 'R'}, supertype=[cardtype.SuperType.BASIC], types=[cardtype.CardType.LAND], abilities=[]))

class c26805(card.Card):
    "Tundra Kavu"
    def __init__(self):
        super(c26805, self).__init__(gameobject.Characteristics(**{'subtype': ['Kavu'], 'mana_cost': '2R', 'toughness': 2, 'power': 2, 'name': 'Tundra Kavu', 'color': ['R'], 'text': '{T}: Target land becomes a Plains or an Island until end of turn.'}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c79145(card.Card):
    "Hundred-Talon Kami"
    def __init__(self):
        super(c79145, self).__init__(gameobject.Characteristics(**{'subtype': ['Spirit'], 'mana_cost': '4W', 'toughness': 3, 'power': 2, 'name': 'Hundred-Talon Kami', 'color': ['W'], 'text': 'Flying\nSoulshift 4 (When this creature dies, you may return target Spirit card with converted mana cost 4 or less from your graveyard to your hand.)'}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Flying]))

class c370698(card.Card):
    "Blood Bairn"
    def __init__(self):
        super(c370698, self).__init__(gameobject.Characteristics(**{'subtype': ['Vampire'], 'mana_cost': '2B', 'toughness': 2, 'power': 2, 'name': 'Blood Bairn', 'color': ['B'], 'text': 'Sacrifice another creature: Blood Bairn gets +2/+2 until end of turn.'}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c3060(card.Card):
    "Soldevi Sentry"
    def __init__(self):
        super(c3060, self).__init__(gameobject.Characteristics(**{'subtype': ['Soldier'], 'mana_cost': '1', 'toughness': 1, 'power': 1, 'name': 'Soldevi Sentry', 'color': [], 'text': '{1}: Choose target opponent. Regenerate Soldevi Sentry. When it regenerates this way, that player may draw a card.'}, supertype=[], types=[cardtype.CardType.ARTIFACT, cardtype.CardType.CREATURE], abilities=[]))

class c34243(card.Card):
    "Ancestor's Chosen"
    def __init__(self):
        super(c34243, self).__init__(gameobject.Characteristics(**{'subtype': ['Human', 'Cleric'], 'mana_cost': '5WW', 'toughness': 4, 'power': 4, 'name': "Ancestor's Chosen", 'color': ['W'], 'text': "First strike (This creature deals combat damage before creatures without first strike.)\nWhen Ancestor's Chosen enters the battlefield, you gain 1 life for each card in your graveyard."}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c174799(card.Card):
    "Hellspark Elemental"
    def __init__(self):
        super(c174799, self).__init__(gameobject.Characteristics(**{'subtype': ['Elemental'], 'mana_cost': '1R', 'toughness': 1, 'power': 3, 'name': 'Hellspark Elemental', 'color': ['R'], 'text': 'Trample, haste\nAt the beginning of the end step, sacrifice Hellspark Elemental.\nUnearth {1}{R} ({1}{R}: Return this card from your graveyard to the battlefield. It gains haste. Exile it at the beginning of the next end step or if it would leave the battlefield. Unearth only as a sorcery.)'}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Haste, abilities.StaticAbilities.Trample]))

class c179594(card.Card):
    "Sewn-Eye Drake"
    def __init__(self):
        super(c179594, self).__init__(gameobject.Characteristics(**{'subtype': ['Zombie', 'Drake'], 'mana_cost': '2(U/R)B', 'toughness': 1, 'power': 3, 'name': 'Sewn-Eye Drake', 'color': ['U', 'B', 'R'], 'text': 'Flying, haste'}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Flying, abilities.StaticAbilities.Haste]))

class c29973(card.Card):
    "Price of Glory"
    def __init__(self):
        super(c29973, self).__init__(gameobject.Characteristics(**{'mana_cost': '2R', 'name': 'Price of Glory', 'color': ['R'], 'text': "Whenever a player taps a land for mana, if it's not that player's turn, destroy that land."}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c21190(card.Card):
    "Sun Clasp"
    def __init__(self):
        super(c21190, self).__init__(gameobject.Characteristics(**{'subtype': ['Aura'], 'mana_cost': '1W', 'name': 'Sun Clasp', 'color': ['W'], 'text': "Enchant creature\nEnchanted creature gets +1/+3.\n{W}: Return enchanted creature to its owner's hand."}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c2473(card.Card):
    "Mind Whip"
    def __init__(self):
        super(c2473, self).__init__(gameobject.Characteristics(**{'subtype': ['Aura'], 'mana_cost': '2BB', 'name': 'Mind Whip', 'color': ['B'], 'text': "Enchant creature\nAt the beginning of the upkeep of enchanted creature's controller, that player may pay {3}. If he or she doesn't, Mind Whip deals 2 damage to that player and you tap that creature."}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c5806(card.Card):
    "Fluctuator"
    def __init__(self):
        super(c5806, self).__init__(gameobject.Characteristics(**{'mana_cost': '2', 'name': 'Fluctuator', 'color': [], 'text': 'Cycling abilities you activate cost you up to {2} less to activate.'}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c230762(card.Card):
    "Slaughter Cry"
    def __init__(self):
        super(c230762, self).__init__(gameobject.Characteristics(**{'mana_cost': '2R', 'name': 'Slaughter Cry', 'color': ['R'], 'text': 'Target creature gets +3/+0 and gains first strike until end of turn. (It deals combat damage before creatures without first strike.)'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c24615(card.Card):
    "Despoil"
    def __init__(self):
        super(c24615, self).__init__(gameobject.Characteristics(**{'mana_cost': '3B', 'name': 'Despoil', 'color': ['B'], 'text': 'Destroy target land. Its controller loses 2 life.'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c22061(card.Card):
    "Overlaid Terrain"
    def __init__(self):
        super(c22061, self).__init__(gameobject.Characteristics(**{'mana_cost': '2GG', 'name': 'Overlaid Terrain', 'color': ['G'], 'text': 'As Overlaid Terrain enters the battlefield, sacrifice all lands you control.\nLands you control have "{T}: Add two mana of any one color to your mana pool."'}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c215101(card.Card):
    "Ogre Geargrabber"
    def __init__(self):
        super(c215101, self).__init__(gameobject.Characteristics(**{'subtype': ['Ogre', 'Warrior'], 'mana_cost': '4RR', 'toughness': 4, 'power': 4, 'name': 'Ogre Geargrabber', 'color': ['R'], 'text': 'Whenever Ogre Geargrabber attacks, gain control of target Equipment an opponent controls until end of turn. Attach it to Ogre Geargrabber. When you lose control of that Equipment, unattach it.'}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c96920(card.Card):
    "Vedalken Plotter"
    def __init__(self):
        super(c96920, self).__init__(gameobject.Characteristics(**{'subtype': ['Vedalken', 'Wizard'], 'mana_cost': '2U', 'toughness': 1, 'power': 1, 'name': 'Vedalken Plotter', 'color': ['U'], 'text': 'When Vedalken Plotter enters the battlefield, exchange control of target land you control and target land an opponent controls.'}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c1476(card.Card):
    "Devouring Deep"
    def __init__(self):
        super(c1476, self).__init__(gameobject.Characteristics(**{'subtype': ['Fish'], 'mana_cost': '2U', 'toughness': 2, 'power': 1, 'name': 'Devouring Deep', 'color': ['U'], 'text': 'Islandwalk'}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Islandwalk]))

class c49055(card.Card):
    "Temporal Cascade"
    def __init__(self):
        super(c49055, self).__init__(gameobject.Characteristics(**{'mana_cost': '5UU', 'name': 'Temporal Cascade', 'color': ['U'], 'text': 'Choose one - Each player shuffles his or her hand and graveyard into his or her library; or each player draws seven cards.\nEntwine {2} (Choose both if you pay the entwine cost.)'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c50176(card.Card):
    "Myr Quadropod"
    def __init__(self):
        super(c50176, self).__init__(gameobject.Characteristics(**{'subtype': ['Myr'], 'mana_cost': '4', 'toughness': 4, 'power': 1, 'name': 'Myr Quadropod', 'color': [], 'text': "{3}: Switch Myr Quadropod's power and toughness until end of turn."}, supertype=[], types=[cardtype.CardType.ARTIFACT, cardtype.CardType.CREATURE], abilities=[]))

class c233086(card.Card):
    "Flameborn Viron"
    def __init__(self):
        super(c233086, self).__init__(gameobject.Characteristics(**{'subtype': ['Insect'], 'mana_cost': '4RR', 'toughness': 4, 'power': 6, 'name': 'Flameborn Viron', 'color': ['R'], 'text': ''}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c226561(card.Card):
    "Taste of Blood"
    def __init__(self):
        super(c226561, self).__init__(gameobject.Characteristics(**{'mana_cost': 'B', 'name': 'Taste of Blood', 'color': ['B'], 'text': 'Taste of Blood deals 1 damage to target player and you gain 1 life.'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c240039(card.Card):
    "Homicidal Seclusion"
    def __init__(self):
        super(c240039, self).__init__(gameobject.Characteristics(**{'mana_cost': '4B', 'name': 'Homicidal Seclusion', 'color': ['B'], 'text': 'As long as you control exactly one creature, that creature gets +3/+1 and has lifelink.'}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c3610(card.Card):
    "Brood of Cockroaches"
    def __init__(self):
        super(c3610, self).__init__(gameobject.Characteristics(**{'subtype': ['Insect'], 'mana_cost': '1B', 'toughness': 1, 'power': 1, 'name': 'Brood of Cockroaches', 'color': ['B'], 'text': 'When Brood of Cockroaches is put into your graveyard from the battlefield, at the beginning of the next end step, you lose 1 life and return Brood of Cockroaches to your hand.'}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c73960(card.Card):
    "Orcish Paratroopers"
    def __init__(self):
        super(c73960, self).__init__(gameobject.Characteristics(**{'subtype': ['Orc', 'Paratrooper'], 'mana_cost': '2R', 'toughness': 4, 'power': 4, 'name': 'Orcish Paratroopers', 'color': ['R'], 'text': 'When Orcish Paratroopers comes into play, flip it from a height of at least one foot. Sacrifice Orcish Paratroopers unless it lands face up after turning over completely.'}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c19647(card.Card):
    "Cho-Arrim Alchemist"
    def __init__(self):
        super(c19647, self).__init__(gameobject.Characteristics(**{'subtype': ['Human', 'Spellshaper'], 'mana_cost': 'W', 'toughness': 1, 'power': 1, 'name': 'Cho-Arrim Alchemist', 'color': ['W'], 'text': '{1}{W}{W}, {T}, Discard a card: The next time a source of your choice would deal damage to you this turn, prevent that damage. You gain life equal to the damage prevented this way.'}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c193467(card.Card):
    "Near-Death Experience"
    def __init__(self):
        super(c193467, self).__init__(gameobject.Characteristics(**{'mana_cost': '2WWW', 'name': 'Near-Death Experience', 'color': ['W'], 'text': 'At the beginning of your upkeep, if you have exactly 1 life, you win the game.'}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c74238(card.Card):
    "Persecute Artist"
    def __init__(self):
        super(c74238, self).__init__(gameobject.Characteristics(**{'mana_cost': '1BB', 'name': 'Persecute Artist', 'color': ['B'], 'text': 'Choose an artist other than Rebecca Guay. Target player reveals his or her hand and discards all nonland cards by the chosen artist.'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c369080(card.Card):
    "Turn // Burn"
    def __init__(self):
        super(c369080, self).__init__(gameobject.Characteristics(**{'mana_cost': '1R', 'name': 'Turn // Burn', 'color': ['R'], 'text': 'Burn deals 2 damage to target creature or player.\nFuse (You may cast one or both halves of this card from your hand.)\n---\nTarget creature loses all abilities and becomes a 0/1 red Weird until end of turn.\nFuse (You may cast one or both halves of this card from your hand.)'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c142027(card.Card):
    "Silkbind Faerie"
    def __init__(self):
        super(c142027, self).__init__(gameobject.Characteristics(**{'subtype': ['Faerie', 'Rogue'], 'mana_cost': '2(W/U)', 'toughness': 3, 'power': 1, 'name': 'Silkbind Faerie', 'color': ['W', 'U'], 'text': 'Flying\n{1}{(w/u)}, {Q}: Tap target creature. ({Q} is the untap symbol.)'}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Flying]))

class c21320(card.Card):
    "Battlefield Percher"
    def __init__(self):
        super(c21320, self).__init__(gameobject.Characteristics(**{'subtype': ['Bird'], 'mana_cost': '3BB', 'toughness': 2, 'power': 2, 'name': 'Battlefield Percher', 'color': ['B'], 'text': 'Flying\nBattlefield Percher can block only creatures with flying.\n{1}{B}: Battlefield Percher gets +1/+1 until end of turn.'}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Flying]))

class c212614(card.Card):
    "I Bask in Your Silent Awe"
    def __init__(self):
        super(c212614, self).__init__(gameobject.Characteristics(**{'mana_cost': '', 'name': 'I Bask in Your Silent Awe', 'color': [], 'text': "(An ongoing scheme remains face up until it's abandoned.)\nEach opponent can't cast more than one spell each turn.\nAt the beginning of your upkeep, if no opponent cast a spell since your last turn ended, abandon this scheme."}, supertype=[], types=[cardtype.CardType.ONGOING, cardtype.CardType.SCHEME], abilities=[]))

