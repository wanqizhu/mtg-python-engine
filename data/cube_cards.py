from MTG import card
from MTG import gameobject
from MTG import cardtype
from MTG import static_abilities
from MTG import mana

class c270446(card.Card):
    "Sphinx of the Steel Wind"
    def __init__(self):
        super(c270446, self).__init__(gameobject.Characteristics(**{'name': 'Sphinx of the Steel Wind', 'text': 'Flying, first strike, vigilance, lifelink, protection from red and from green', 'color': ['W', 'U', 'B'], 'mana_cost': '5WUB', 'power': 6, 'toughness': 6, 'subtype': ['Sphinx']}, supertype=[], types=[cardtype.CardType.ARTIFACT, cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.First_Strike, static_abilities.StaticAbilities.Flying, static_abilities.StaticAbilities.Lifelink, static_abilities.StaticAbilities.Vigilance]))

class c270447(card.Card):
    "Inkwell Leviathan"
    def __init__(self):
        super(c270447, self).__init__(gameobject.Characteristics(**{'name': 'Inkwell Leviathan', 'text': "Islandwalk (This creature can't be blocked as long as defending player controls an Island.)\nTrample\nShroud (This creature can't be the target of spells or abilities.)", 'color': ['U'], 'mana_cost': '7UU', 'power': 7, 'toughness': 11, 'subtype': ['Leviathan']}, supertype=[], types=[cardtype.CardType.ARTIFACT, cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Shroud, static_abilities.StaticAbilities.Trample, static_abilities.StaticAbilities.Islandwalk]))

class c265167(card.Card):
    "Animate Dead"
    def __init__(self):
        super(c265167, self).__init__(gameobject.Characteristics(**{'name': 'Animate Dead', 'text': 'Enchant creature card in a graveyard\nWhen Animate Dead enters the battlefield, if it\'s on the battlefield, it loses "enchant creature card in a graveyard" and gains "enchant creature put onto the battlefield with Animate Dead." Return enchanted creature card to the battlefield under your control and attach Animate Dead to it. When Animate Dead leaves the battlefield, that creature\'s controller sacrifices it.\nEnchanted creature gets -1/-0.', 'color': ['B'], 'mana_cost': '1B', 'subtype': ['Aura']}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c234706(card.Card):
    "Grim Lavamancer"
    def __init__(self):
        super(c234706, self).__init__(gameobject.Characteristics(**{'name': 'Grim Lavamancer', 'text': '{R}, {T}, Exile two cards from your graveyard: Grim Lavamancer deals 2 damage to target creature or player.', 'color': ['R'], 'mana_cost': 'R', 'power': 1, 'toughness': 1, 'subtype': ['Human', 'Wizard']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c236456(card.Card):
    "Figure of Destiny"
    def __init__(self):
        super(c236456, self).__init__(gameobject.Characteristics(**{'name': 'Figure of Destiny', 'text': '{R/W}: Figure of Destiny becomes a Kithkin Spirit with base power and toughness 2/2.\n{R/W}{R/W}{R/W}: If Figure of Destiny is a Spirit, it becomes a Kithkin Spirit Warrior with base power and toughness 4/4.\n{R/W}{R/W}{R/W}{R/W}{R/W}{R/W}: If Figure of Destiny is a Warrior, it becomes a Kithkin Spirit Warrior Avatar with base power and toughness 8/8, flying, and first strike.', 'color': ['W', 'R'], 'mana_cost': 'R/W', 'power': 1, 'toughness': 1, 'subtype': ['Kithkin']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Flying]))

class c234709(card.Card):
    "Keldon Marauders"
    def __init__(self):
        super(c234709, self).__init__(gameobject.Characteristics(**{'name': 'Keldon Marauders', 'text': 'Vanishing 2 (This creature enters the battlefield with two time counters on it. At the beginning of your upkeep, remove a time counter from it. When the last is removed, sacrifice it.)\nWhen Keldon Marauders enters the battlefield or leaves the battlefield, it deals 1 damage to target player.', 'color': ['R'], 'mana_cost': '1R', 'power': 3, 'toughness': 3, 'subtype': ['Human', 'Warrior']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c217977(card.Card):
    "Chain Lightning"
    def __init__(self):
        super(c217977, self).__init__(gameobject.Characteristics(**{'name': 'Chain Lightning', 'text': "Chain Lightning deals 3 damage to target creature or player. Then that player or that creature's controller may pay {R}{R}. If the player does, he or she may copy this spell and may choose a new target for that copy.", 'color': ['R'], 'mana_cost': 'R'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c234704(card.Card):
    "Lightning Bolt"
    def __init__(self):
        super(c234704, self).__init__(gameobject.Characteristics(**{'name': 'Lightning Bolt', 'text': 'Lightning Bolt deals 3 damage to target creature or player.', 'color': ['R'], 'mana_cost': 'R'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c234736(card.Card):
    "Fireblast"
    def __init__(self):
        super(c234736, self).__init__(gameobject.Characteristics(**{'name': 'Fireblast', 'text': "You may sacrifice two Mountains rather than pay Fireblast's mana cost.\nFireblast deals 4 damage to target creature or player.", 'color': ['R'], 'mana_cost': '4RR'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c207928(card.Card):
    "Terramorphic Expanse"
    def __init__(self):
        super(c207928, self).__init__(gameobject.Characteristics(**{'name': 'Terramorphic Expanse', 'text': '{T}, Sacrifice Terramorphic Expanse: Search your library for a basic land card and put it onto the battlefield tapped. Then shuffle your library.', 'color': '', 'mana_cost': ''}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c10637(card.Card):
    "Burning of Xinye"
    def __init__(self):
        super(c10637, self).__init__(gameobject.Characteristics(**{'name': 'Burning of Xinye', 'text': 'You destroy four lands you control, then target opponent destroys four lands he or she controls. Then Burning of Xinye deals 4 damage to each creature.', 'color': ['R'], 'mana_cost': '4RR'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c6610(card.Card):
    "Wildfire"
    def __init__(self):
        super(c6610, self).__init__(gameobject.Characteristics(**{'name': 'Wildfire', 'text': 'Each player sacrifices four lands. Wildfire deals 4 damage to each creature.', 'color': ['R'], 'mana_cost': '4RR'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c423433(card.Card):
    "Hyena Umbra"
    def __init__(self):
        super(c423433, self).__init__(gameobject.Characteristics(**{'name': 'Hyena Umbra', 'text': 'Enchant creature\nEnchanted creature gets +1/+1 and has first strike.\nTotem armor (If enchanted creature would be destroyed, instead remove all damage from it and destroy this Aura.)', 'color': ['W'], 'mana_cost': 'W', 'subtype': ['Aura']}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c423464(card.Card):
    "Arc Trail"
    def __init__(self):
        super(c423464, self).__init__(gameobject.Characteristics(**{'name': 'Arc Trail', 'text': 'Arc Trail deals 2 damage to target creature or player and 1 damage to another target creature or player.', 'color': ['R'], 'mana_cost': '1R'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c423501(card.Card):
    "Rancor"
    def __init__(self):
        super(c423501, self).__init__(gameobject.Characteristics(**{'name': 'Rancor', 'text': "Enchant creature\nEnchanted creature gets +2/+0 and has trample.\nWhen Rancor is put into a graveyard from the battlefield, return Rancor to its owner's hand.", 'color': ['G'], 'mana_cost': 'G', 'subtype': ['Aura']}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c423507(card.Card):
    "Baleful Strix"
    def __init__(self):
        super(c423507, self).__init__(gameobject.Characteristics(**{'name': 'Baleful Strix', 'text': 'Flying, deathtouch\nWhen Baleful Strix enters the battlefield, draw a card.', 'color': ['U', 'B'], 'mana_cost': 'UB', 'power': 1, 'toughness': 1, 'subtype': ['Bird']}, supertype=[], types=[cardtype.CardType.ARTIFACT, cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Deathtouch, static_abilities.StaticAbilities.Flying]))

class c423509(card.Card):
    "Bloodbraid Elf"
    def __init__(self):
        super(c423509, self).__init__(gameobject.Characteristics(**{'name': 'Bloodbraid Elf', 'text': 'Haste\nCascade (When you cast this spell, exile cards from the top of your library until you exile a nonland card that costs less. You may cast it without paying its mana cost. Put the exiled cards on the bottom of your library in a random order.)', 'color': ['R', 'G'], 'mana_cost': '2RG', 'power': 3, 'toughness': 2, 'subtype': ['Elf', 'Berserker']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Haste]))

class c205396(card.Card):
    "Oblivion Ring"
    def __init__(self):
        super(c205396, self).__init__(gameobject.Characteristics(**{'name': 'Oblivion Ring', 'text': "When Oblivion Ring enters the battlefield, exile another target nonland permanent.\nWhen Oblivion Ring leaves the battlefield, return the exiled card to the battlefield under its owner's control.", 'color': ['W'], 'mana_cost': '2W'}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c205311(card.Card):
    "Thirst for Knowledge"
    def __init__(self):
        super(c205311, self).__init__(gameobject.Characteristics(**{'name': 'Thirst for Knowledge', 'text': 'Draw three cards. Then discard two cards unless you discard an artifact card.', 'color': ['U'], 'mana_cost': '2U'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c205422(card.Card):
    "Dark Ritual"
    def __init__(self):
        super(c205422, self).__init__(gameobject.Characteristics(**{'name': 'Dark Ritual', 'text': 'Add {B}{B}{B} to your mana pool.', 'color': ['B'], 'mana_cost': 'B'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c205392(card.Card):
    "Flametongue Kavu"
    def __init__(self):
        super(c205392, self).__init__(gameobject.Characteristics(**{'name': 'Flametongue Kavu', 'text': 'When Flametongue Kavu enters the battlefield, it deals 4 damage to target creature.', 'color': ['R'], 'mana_cost': '3R', 'power': 4, 'toughness': 2, 'subtype': ['Kavu']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c205393(card.Card):
    "Briarhorn"
    def __init__(self):
        super(c205393, self).__init__(gameobject.Characteristics(**{'name': 'Briarhorn', 'text': "Flash\nWhen Briarhorn enters the battlefield, target creature gets +3/+3 until end of turn.\nEvoke {1}{G} (You may cast this spell for its evoke cost. If you do, it's sacrificed when it enters the battlefield.)", 'color': ['G'], 'mana_cost': '3G', 'power': 3, 'toughness': 3, 'subtype': ['Elemental']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Flash]))

class c205350(card.Card):
    "Rampant Growth"
    def __init__(self):
        super(c205350, self).__init__(gameobject.Characteristics(**{'name': 'Rampant Growth', 'text': 'Search your library for a basic land card and put that card onto the battlefield tapped. Then shuffle your library.', 'color': ['G'], 'mana_cost': '1G'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c205408(card.Card):
    "Search for Tomorrow"
    def __init__(self):
        super(c205408, self).__init__(gameobject.Characteristics(**{'name': 'Search for Tomorrow', 'text': 'Search your library for a basic land card and put it onto the battlefield. Then shuffle your library.\nSuspend 2—{G} (Rather than cast this card from your hand, you may pay {G} and exile it with two time counters on it. At the beginning of your upkeep, remove a time counter. When the last is removed, cast it without paying its mana cost.)', 'color': ['G'], 'mana_cost': '2G'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c205361(card.Card):
    "Lightning Helix"
    def __init__(self):
        super(c205361, self).__init__(gameobject.Characteristics(**{'name': 'Lightning Helix', 'text': 'Lightning Helix deals 3 damage to target creature or player and you gain 3 life.', 'color': ['W', 'R'], 'mana_cost': 'RW'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c205358(card.Card):
    "Boros Signet"
    def __init__(self):
        super(c205358, self).__init__(gameobject.Characteristics(**{'name': 'Boros Signet', 'text': '{1}, {T}: Add {R}{W} to your mana pool.', 'color': ['R', 'W'], 'mana_cost': '2'}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c205270(card.Card):
    "Loxodon Warhammer"
    def __init__(self):
        super(c205270, self).__init__(gameobject.Characteristics(**{'name': 'Loxodon Warhammer', 'text': 'Equipped creature gets +3/+0 and has trample and lifelink.\nEquip {3}', 'color': '', 'mana_cost': '3', 'subtype': ['Equipment']}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c382853(card.Card):
    "Balance"
    def __init__(self):
        super(c382853, self).__init__(gameobject.Characteristics(**{'name': 'Balance', 'text': 'Each player chooses a number of lands he or she controls equal to the number of lands controlled by the player who controls the fewest, then sacrifices the rest. Players discard cards and sacrifice creatures the same way.', 'color': ['W'], 'mana_cost': '1W'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c382983(card.Card):
    "Karmic Guide"
    def __init__(self):
        super(c382983, self).__init__(gameobject.Characteristics(**{'name': 'Karmic Guide', 'text': 'Flying, protection from black\nEcho {3}{W}{W} (At the beginning of your upkeep, if this came under your control since the beginning of your last upkeep, sacrifice it unless you pay its echo cost.)\nWhen Karmic Guide enters the battlefield, return target creature card from your graveyard to the battlefield.', 'color': ['W'], 'mana_cost': '3WW', 'power': 2, 'toughness': 2, 'subtype': ['Angel', 'Spirit']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Flying]))

class c383119(card.Card):
    "Swords to Plowshares"
    def __init__(self):
        super(c383119, self).__init__(gameobject.Characteristics(**{'name': 'Swords to Plowshares', 'text': 'Exile target creature. Its controller gains life equal to its power.', 'color': ['W'], 'mana_cost': 'W'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c382871(card.Card):
    "Brainstorm"
    def __init__(self):
        super(c382871, self).__init__(gameobject.Characteristics(**{'name': 'Brainstorm', 'text': 'Draw three cards, then put two cards from your hand on top of your library in any order.', 'color': ['U'], 'mana_cost': 'U'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c382895(card.Card):
    "Control Magic"
    def __init__(self):
        super(c382895, self).__init__(gameobject.Characteristics(**{'name': 'Control Magic', 'text': 'Enchant creature\nYou control enchanted creature.', 'color': ['U'], 'mana_cost': '2UU', 'subtype': ['Aura']}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c382897(card.Card):
    "Counterspell"
    def __init__(self):
        super(c382897, self).__init__(gameobject.Characteristics(**{'name': 'Counterspell', 'text': 'Counter target spell.', 'color': ['U'], 'mana_cost': 'UU'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c382912(card.Card):
    "Deep Analysis"
    def __init__(self):
        super(c382912, self).__init__(gameobject.Characteristics(**{'name': 'Deep Analysis', 'text': 'Target player draws two cards.\nFlashback—{1}{U}, Pay 3 life. (You may cast this card from your graveyard for its flashback cost. Then exile it.)', 'color': ['U'], 'mana_cost': '3U'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[static_abilities.StaticAbilities.Flash]))

class c382930(card.Card):
    "Fact or Fiction"
    def __init__(self):
        super(c382930, self).__init__(gameobject.Characteristics(**{'name': 'Fact or Fiction', 'text': 'Reveal the top five cards of your library. An opponent separates those cards into two piles. Put one pile into your hand and the other into your graveyard.', 'color': ['U'], 'mana_cost': '3U'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c383143(card.Card):
    "Upheaval"
    def __init__(self):
        super(c383143, self).__init__(gameobject.Characteristics(**{'name': 'Upheaval', 'text': "Return all permanents to their owners' hands.", 'color': ['U'], 'mana_cost': '4UU'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c382976(card.Card):
    "Hymn to Tourach"
    def __init__(self):
        super(c382976, self).__init__(gameobject.Characteristics(**{'name': 'Hymn to Tourach', 'text': 'Target player discards two cards at random.', 'color': ['B'], 'mana_cost': 'BB'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c383063(card.Card):
    "Recurring Nightmare"
    def __init__(self):
        super(c383063, self).__init__(gameobject.Characteristics(**{'name': 'Recurring Nightmare', 'text': "Sacrifice a creature, Return Recurring Nightmare to its owner's hand: Return target creature card from your graveyard to the battlefield. Activate this ability only any time you could cast a sorcery.", 'color': ['B'], 'mana_cost': '2B'}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c383117(card.Card):
    "Sulfuric Vortex"
    def __init__(self):
        super(c383117, self).__init__(gameobject.Characteristics(**{'name': 'Sulfuric Vortex', 'text': "At the beginning of each player's upkeep, Sulfuric Vortex deals 2 damage to that player.\nIf a player would gain life, that player gains no life instead.", 'color': ['R'], 'mana_cost': '1RR'}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c382882(card.Card):
    "Channel"
    def __init__(self):
        super(c382882, self).__init__(gameobject.Characteristics(**{'name': 'Channel', 'text': 'Until end of turn, any time you could activate a mana ability, you may pay 1 life. If you do, add {C} to your mana pool.', 'color': ['G'], 'mana_cost': 'GG'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c383064(card.Card):
    "Regrowth"
    def __init__(self):
        super(c383064, self).__init__(gameobject.Characteristics(**{'name': 'Regrowth', 'text': 'Return target card from your graveyard to your hand.', 'color': ['G'], 'mana_cost': '1G'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c383120(card.Card):
    "Sylvan Library"
    def __init__(self):
        super(c383120, self).__init__(gameobject.Characteristics(**{'name': 'Sylvan Library', 'text': 'At the beginning of your draw step, you may draw two additional cards. If you do, choose two cards in your hand drawn this turn. For each of those cards, pay 4 life or put the card on top of your library.', 'color': ['G'], 'mana_cost': '1G'}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c382868(card.Card):
    "Blazing Specter"
    def __init__(self):
        super(c382868, self).__init__(gameobject.Characteristics(**{'name': 'Blazing Specter', 'text': 'Flying, haste\nWhenever Blazing Specter deals combat damage to a player, that player discards a card.', 'color': ['B', 'R'], 'mana_cost': '2BR', 'power': 2, 'toughness': 2, 'subtype': ['Specter']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Flying, static_abilities.StaticAbilities.Haste]))

class c383056(card.Card):
    "Psychatog"
    def __init__(self):
        super(c383056, self).__init__(gameobject.Characteristics(**{'name': 'Psychatog', 'text': 'Discard a card: Psychatog gets +1/+1 until end of turn.\nExile two cards from your graveyard: Psychatog gets +1/+1 until end of turn.', 'color': ['U', 'B'], 'mana_cost': '1UB', 'power': 1, 'toughness': 2, 'subtype': ['Atog']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383087(card.Card):
    "Selvala, Explorer Returned"
    def __init__(self):
        super(c383087, self).__init__(gameobject.Characteristics(**{'name': 'Selvala, Explorer Returned', 'text': 'Parley — {T}: Each player reveals the top card of his or her library. For each nonland card revealed this way, add {G} to your mana pool and you gain 1 life. Then each player draws a card.', 'color': ['W', 'G'], 'mana_cost': '1GW', 'power': 2, 'toughness': 4, 'subtype': ['Elf', 'Scout']}, supertype=[cardtype.SuperType.LEGENDARY], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383097(card.Card):
    "Skullclamp"
    def __init__(self):
        super(c383097, self).__init__(gameobject.Characteristics(**{'name': 'Skullclamp', 'text': 'Equipped creature gets +1/-1.\nWhenever equipped creature dies, draw two cards.\nEquip {1}', 'color': '', 'mana_cost': '1', 'subtype': ['Equipment']}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c370449(card.Card):
    "Flickerwisp"
    def __init__(self):
        super(c370449, self).__init__(gameobject.Characteristics(**{'name': 'Flickerwisp', 'text': "Flying\nWhen Flickerwisp enters the battlefield, exile another target permanent. Return that card to the battlefield under its owner's control at the beginning of the next end step.", 'color': ['W'], 'mana_cost': '1WW', 'power': 3, 'toughness': 1, 'subtype': ['Elemental']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Flying]))

class c370408(card.Card):
    "Path to Exile"
    def __init__(self):
        super(c370408, self).__init__(gameobject.Characteristics(**{'name': 'Path to Exile', 'text': 'Exile target creature. Its controller may search his or her library for a basic land card, put that card onto the battlefield tapped, then shuffle his or her library.', 'color': ['W'], 'mana_cost': 'W'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c370493(card.Card):
    "Reveillark"
    def __init__(self):
        super(c370493, self).__init__(gameobject.Characteristics(**{'name': 'Reveillark', 'text': "Flying\nWhen Reveillark leaves the battlefield, return up to two target creature cards with power 2 or less from your graveyard to the battlefield.\nEvoke {5}{W} (You may cast this spell for its evoke cost. If you do, it's sacrificed when it enters the battlefield.)", 'color': ['W'], 'mana_cost': '4W', 'power': 4, 'toughness': 3, 'subtype': ['Elemental']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Flying]))

class c370439(card.Card):
    "Cryptic Command"
    def __init__(self):
        super(c370439, self).__init__(gameobject.Characteristics(**{'name': 'Cryptic Command', 'text': "Choose two —\n• Counter target spell.\n• Return target permanent to its owner's hand.\n• Tap all creatures your opponents control.\n• Draw a card.", 'color': ['U'], 'mana_cost': '1UUU'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c370378(card.Card):
    "Etherium Sculptor"
    def __init__(self):
        super(c370378, self).__init__(gameobject.Characteristics(**{'name': 'Etherium Sculptor', 'text': 'Artifact spells you cast cost {1} less to cast.', 'color': ['U'], 'mana_cost': '1U', 'power': 1, 'toughness': 2, 'subtype': ['Vedalken', 'Artificer']}, supertype=[], types=[cardtype.CardType.ARTIFACT, cardtype.CardType.CREATURE], abilities=[]))

class c370368(card.Card):
    "Gifts Ungiven"
    def __init__(self):
        super(c370368, self).__init__(gameobject.Characteristics(**{'name': 'Gifts Ungiven', 'text': 'Search your library for up to four cards with different names and reveal them. Target opponent chooses two of those cards. Put the chosen cards into your graveyard and the rest into your hand. Then shuffle your library.', 'color': ['U'], 'mana_cost': '3U'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c370385(card.Card):
    "Meloku the Clouded Mirror"
    def __init__(self):
        super(c370385, self).__init__(gameobject.Characteristics(**{'name': 'Meloku the Clouded Mirror', 'text': "Flying\n{1}, Return a land you control to its owner's hand: Create a 1/1 blue Illusion creature token with flying.", 'color': ['U'], 'mana_cost': '4U', 'power': 2, 'toughness': 4, 'subtype': ['Moonfolk', 'Wizard']}, supertype=[cardtype.SuperType.LEGENDARY], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Flying]))

class c370535(card.Card):
    "Mulldrifter"
    def __init__(self):
        super(c370535, self).__init__(gameobject.Characteristics(**{'name': 'Mulldrifter', 'text': "Flying\nWhen Mulldrifter enters the battlefield, draw two cards.\nEvoke {2}{U} (You may cast this spell for its evoke cost. If you do, it's sacrificed when it enters the battlefield.)", 'color': ['U'], 'mana_cost': '4U', 'power': 2, 'toughness': 2, 'subtype': ['Elemental']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Flying]))

class c370440(card.Card):
    "Pestermite"
    def __init__(self):
        super(c370440, self).__init__(gameobject.Characteristics(**{'name': 'Pestermite', 'text': 'Flash\nFlying\nWhen Pestermite enters the battlefield, you may tap or untap target permanent.', 'color': ['U'], 'mana_cost': '2U', 'power': 2, 'toughness': 1, 'subtype': ['Faerie', 'Rogue']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Flash, static_abilities.StaticAbilities.Flying]))

class c370390(card.Card):
    "Vendilion Clique"
    def __init__(self):
        super(c370390, self).__init__(gameobject.Characteristics(**{'name': 'Vendilion Clique', 'text': "Flash\nFlying\nWhen Vendilion Clique enters the battlefield, look at target player's hand. You may choose a nonland card from it. If you do, that player reveals the chosen card, puts it on the bottom of his or her library, then draws a card.", 'color': ['U'], 'mana_cost': '1UU', 'power': 3, 'toughness': 1, 'subtype': ['Faerie', 'Wizard']}, supertype=[cardtype.SuperType.LEGENDARY], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Flash, static_abilities.StaticAbilities.Flying]))

class c370560(card.Card):
    "Greater Gargadon"
    def __init__(self):
        super(c370560, self).__init__(gameobject.Characteristics(**{'name': 'Greater Gargadon', 'text': 'Suspend 10—{R}\nSacrifice an artifact, creature, or land: Remove a time counter from Greater Gargadon. Activate this ability only if Greater Gargadon is suspended.', 'color': ['R'], 'mana_cost': '9R', 'power': 9, 'toughness': 7, 'subtype': ['Beast']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c370534(card.Card):
    "Kiki-Jiki, Mirror Breaker"
    def __init__(self):
        super(c370534, self).__init__(gameobject.Characteristics(**{'name': 'Kiki-Jiki, Mirror Breaker', 'text': "Haste\n{T}: Create a token that's a copy of target nonlegendary creature you control. That token has haste. Sacrifice it at the beginning of the next end step.", 'color': ['R'], 'mana_cost': '2RRR', 'power': 2, 'toughness': 2, 'subtype': ['Goblin', 'Shaman']}, supertype=[cardtype.SuperType.LEGENDARY], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Haste]))

class c370427(card.Card):
    "Eternal Witness"
    def __init__(self):
        super(c370427, self).__init__(gameobject.Characteristics(**{'name': 'Eternal Witness', 'text': 'When Eternal Witness enters the battlefield, you may return target card from your graveyard to your hand.', 'color': ['G'], 'mana_cost': '1GG', 'power': 2, 'toughness': 1, 'subtype': ['Human', 'Shaman']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c370406(card.Card):
    "Woodfall Primus"
    def __init__(self):
        super(c370406, self).__init__(gameobject.Characteristics(**{'name': 'Woodfall Primus', 'text': "Trample\nWhen Woodfall Primus enters the battlefield, destroy target noncreature permanent.\nPersist (When this creature dies, if it had no -1/-1 counters on it, return it to the battlefield under its owner's control with a -1/-1 counter on it.)", 'color': ['G'], 'mana_cost': '5GGG', 'power': 6, 'toughness': 6, 'subtype': ['Treefolk', 'Shaman']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Trample]))

class c370376(card.Card):
    "Electrolyze"
    def __init__(self):
        super(c370376, self).__init__(gameobject.Characteristics(**{'name': 'Electrolyze', 'text': 'Electrolyze deals 2 damage divided as you choose among one or two target creatures and/or players.\nDraw a card.', 'color': ['U', 'R'], 'mana_cost': '1UR'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c370379(card.Card):
    "Knight of the Reliquary"
    def __init__(self):
        super(c370379, self).__init__(gameobject.Characteristics(**{'name': 'Knight of the Reliquary', 'text': 'Knight of the Reliquary gets +1/+1 for each land card in your graveyard.\n{T}, Sacrifice a Forest or Plains: Search your library for a land card, put it onto the battlefield, then shuffle your library.', 'color': ['W', 'G'], 'mana_cost': '1GW', 'power': 2, 'toughness': 2, 'subtype': ['Human', 'Knight']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c370566(card.Card):
    "Sarkhan Vol"
    def __init__(self):
        super(c370566, self).__init__(gameobject.Characteristics(**{'name': 'Sarkhan Vol', 'text': '+1: Creatures you control get +1/+1 and gain haste until end of turn.\n−2: Gain control of target creature until end of turn. Untap that creature. It gains haste until end of turn.\n−6: Create five 4/4 red Dragon creature tokens with flying.', 'color': ['R', 'G'], 'mana_cost': '2RG', 'subtype': ['Sarkhan']}, supertype=[], types=[cardtype.CardType.PLANESWALKER], abilities=[]))

class c370518(card.Card):
    "Murderous Redcap"
    def __init__(self):
        super(c370518, self).__init__(gameobject.Characteristics(**{'name': 'Murderous Redcap', 'text': "When Murderous Redcap enters the battlefield, it deals damage equal to its power to target creature or player.\nPersist (When this creature dies, if it had no -1/-1 counters on it, return it to the battlefield under its owner's control with a -1/-1 counter on it.)", 'color': ['B', 'R'], 'mana_cost': '2B/RB/R', 'power': 2, 'toughness': 2, 'subtype': ['Goblin', 'Assassin']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c370442(card.Card):
    "Bonesplitter"
    def __init__(self):
        super(c370442, self).__init__(gameobject.Characteristics(**{'name': 'Bonesplitter', 'text': 'Equipped creature gets +2/+0.\nEquip {1}', 'color': '', 'mana_cost': '1', 'subtype': ['Equipment']}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c370520(card.Card):
    "Myr Retriever"
    def __init__(self):
        super(c370520, self).__init__(gameobject.Characteristics(**{'name': 'Myr Retriever', 'text': 'When Myr Retriever dies, return another target artifact card from your graveyard to your hand.', 'color': '', 'mana_cost': '2', 'power': 1, 'toughness': 1, 'subtype': ['Myr']}, supertype=[], types=[cardtype.CardType.ARTIFACT, cardtype.CardType.CREATURE], abilities=[]))

class c370471(card.Card):
    "Sword of Fire and Ice"
    def __init__(self):
        super(c370471, self).__init__(gameobject.Characteristics(**{'name': 'Sword of Fire and Ice', 'text': 'Equipped creature gets +2/+2 and has protection from red and from blue.\nWhenever equipped creature deals combat damage to a player, Sword of Fire and Ice deals 2 damage to target creature or player and you draw a card.\nEquip {2}', 'color': '', 'mana_cost': '3', 'subtype': ['Equipment']}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c370366(card.Card):
    "Vedalken Shackles"
    def __init__(self):
        super(c370366, self).__init__(gameobject.Characteristics(**{'name': 'Vedalken Shackles', 'text': 'You may choose not to untap Vedalken Shackles during your untap step.\n{2}, {T}: Gain control of target creature with power less than or equal to the number of Islands you control for as long as Vedalken Shackles remains tapped.', 'color': '', 'mana_cost': '3'}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c425828(card.Card):
    "Blade Splicer"
    def __init__(self):
        super(c425828, self).__init__(gameobject.Characteristics(**{'name': 'Blade Splicer', 'text': 'When Blade Splicer enters the battlefield, create a 3/3 colorless Golem artifact creature token.\nGolem creatures you control have first strike.', 'color': ['W'], 'mana_cost': '2W', 'power': 1, 'toughness': 1, 'subtype': ['Human', 'Artificer']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c425837(card.Card):
    "Lingering Souls"
    def __init__(self):
        super(c425837, self).__init__(gameobject.Characteristics(**{'name': 'Lingering Souls', 'text': 'Create two 1/1 white Spirit creature tokens with flying.\nFlashback {1}{B} (You may cast this card from your graveyard for its flashback cost. Then exile it.)', 'color': ['W', 'B'], 'mana_cost': '2W'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[static_abilities.StaticAbilities.Flash]))

class c425845(card.Card):
    "Restoration Angel"
    def __init__(self):
        super(c425845, self).__init__(gameobject.Characteristics(**{'name': 'Restoration Angel', 'text': 'Flash\nFlying\nWhen Restoration Angel enters the battlefield, you may exile target non-Angel creature you control, then return that card to the battlefield under your control.', 'color': ['W'], 'mana_cost': '3W', 'power': 3, 'toughness': 4, 'subtype': ['Angel']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Flash, static_abilities.StaticAbilities.Flying]))

class c425851(card.Card):
    "Terminus"
    def __init__(self):
        super(c425851, self).__init__(gameobject.Characteristics(**{'name': 'Terminus', 'text': "Put all creatures on the bottom of their owners' libraries.\nMiracle {W} (You may cast this card for its miracle cost when you draw it if it's the first card you drew this turn.)", 'color': ['W'], 'mana_cost': '4WW'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c425855(card.Card):
    "Augur of Bolas"
    def __init__(self):
        super(c425855, self).__init__(gameobject.Characteristics(**{'name': 'Augur of Bolas', 'text': 'When Augur of Bolas enters the battlefield, look at the top three cards of your library. You may reveal an instant or sorcery card from among them and put it into your hand. Put the rest on the bottom of your library in any order.', 'color': ['U'], 'mana_cost': '1U', 'power': 1, 'toughness': 3, 'subtype': ['Merfolk', 'Wizard']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c425861(card.Card):
    "Deadeye Navigator"
    def __init__(self):
        super(c425861, self).__init__(gameobject.Characteristics(**{'name': 'Deadeye Navigator', 'text': 'Soulbond (You may pair this creature with another unpaired creature when either enters the battlefield. They remain paired for as long as you control both of them.)\nAs long as Deadeye Navigator is paired with another creature, each of those creatures has "{1}{U}: Exile this creature, then return it to the battlefield under your control."', 'color': ['U'], 'mana_cost': '4UU', 'power': 5, 'toughness': 5, 'subtype': ['Spirit']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c425871(card.Card):
    "Phantasmal Image"
    def __init__(self):
        super(c425871, self).__init__(gameobject.Characteristics(**{'name': 'Phantasmal Image', 'text': 'You may have Phantasmal Image enter the battlefield as a copy of any creature on the battlefield, except it\'s an Illusion in addition to its other types and it gains "When this creature becomes the target of a spell or ability, sacrifice it."', 'color': ['U'], 'mana_cost': '1U', 'power': 0, 'toughness': 0, 'subtype': ['Illusion']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c425880(card.Card):
    "Venser, Shaper Savant"
    def __init__(self):
        super(c425880, self).__init__(gameobject.Characteristics(**{'name': 'Venser, Shaper Savant', 'text': "Flash\nWhen Venser, Shaper Savant enters the battlefield, return target spell or permanent to its owner's hand.", 'color': ['U'], 'mana_cost': '2UU', 'power': 2, 'toughness': 2, 'subtype': ['Human', 'Wizard']}, supertype=[cardtype.SuperType.LEGENDARY], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Flash]))

class c425888(card.Card):
    "Damnation"
    def __init__(self):
        super(c425888, self).__init__(gameobject.Characteristics(**{'name': 'Damnation', 'text': "Destroy all creatures. They can't be regenerated.", 'color': ['B'], 'mana_cost': '2BB'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c425897(card.Card):
    "Griselbrand"
    def __init__(self):
        super(c425897, self).__init__(gameobject.Characteristics(**{'name': 'Griselbrand', 'text': 'Flying, lifelink\nPay 7 life: Draw seven cards.', 'color': ['B'], 'mana_cost': '4BBBB', 'power': 7, 'toughness': 7, 'subtype': ['Demon']}, supertype=[cardtype.SuperType.LEGENDARY], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Flying, static_abilities.StaticAbilities.Lifelink]))

class c425900(card.Card):
    "Inquisition of Kozilek"
    def __init__(self):
        super(c425900, self).__init__(gameobject.Characteristics(**{'name': 'Inquisition of Kozilek', 'text': 'Target player reveals his or her hand. You choose a nonland card from it with converted mana cost 3 or less. That player discards that card.', 'color': ['B'], 'mana_cost': 'B'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c425910(card.Card):
    "Unburial Rites"
    def __init__(self):
        super(c425910, self).__init__(gameobject.Characteristics(**{'name': 'Unburial Rites', 'text': 'Return target creature card from your graveyard to the battlefield.\nFlashback {3}{W} (You may cast this card from your graveyard for its flashback cost. Then exile it.)', 'color': ['B', 'W'], 'mana_cost': '4B'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[static_abilities.StaticAbilities.Flash]))

class c425912(card.Card):
    "Vampire Nighthawk"
    def __init__(self):
        super(c425912, self).__init__(gameobject.Characteristics(**{'name': 'Vampire Nighthawk', 'text': 'Flying, deathtouch, lifelink', 'color': ['B'], 'mana_cost': '1BB', 'power': 2, 'toughness': 3, 'subtype': ['Vampire', 'Shaman']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Deathtouch, static_abilities.StaticAbilities.Flying, static_abilities.StaticAbilities.Lifelink]))

class c425916(card.Card):
    "Bonfire of the Damned"
    def __init__(self):
        super(c425916, self).__init__(gameobject.Characteristics(**{'name': 'Bonfire of the Damned', 'text': "Bonfire of the Damned deals X damage to target player and each creature he or she controls.\nMiracle {X}{R} (You may cast this card for its miracle cost when you draw it if it's the first card you drew this turn.)", 'color': ['R'], 'mana_cost': 'XXR'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c425921(card.Card):
    "Goblin Guide"
    def __init__(self):
        super(c425921, self).__init__(gameobject.Characteristics(**{'name': 'Goblin Guide', 'text': "Haste\nWhenever Goblin Guide attacks, defending player reveals the top card of his or her library. If it's a land card, that player puts it into his or her hand.", 'color': ['R'], 'mana_cost': 'R', 'power': 2, 'toughness': 2, 'subtype': ['Goblin', 'Scout']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Haste]))

class c425923(card.Card):
    "Hellrider"
    def __init__(self):
        super(c425923, self).__init__(gameobject.Characteristics(**{'name': 'Hellrider', 'text': 'Haste\nWhenever a creature you control attacks, Hellrider deals 1 damage to defending player.', 'color': ['R'], 'mana_cost': '2RR', 'power': 3, 'toughness': 3, 'subtype': ['Devil']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Haste]))

class c425925(card.Card):
    "Magma Jet"
    def __init__(self):
        super(c425925, self).__init__(gameobject.Characteristics(**{'name': 'Magma Jet', 'text': 'Magma Jet deals 2 damage to target creature or player. Scry 2.', 'color': ['R'], 'mana_cost': '1R'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c425941(card.Card):
    "Zealous Conscripts"
    def __init__(self):
        super(c425941, self).__init__(gameobject.Characteristics(**{'name': 'Zealous Conscripts', 'text': 'Haste\nWhen Zealous Conscripts enters the battlefield, gain control of target permanent until end of turn. Untap that permanent. It gains haste until end of turn.', 'color': ['R'], 'mana_cost': '4R', 'power': 3, 'toughness': 3, 'subtype': ['Human', 'Warrior']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Haste]))

class c425959(card.Card):
    "Scavenging Ooze"
    def __init__(self):
        super(c425959, self).__init__(gameobject.Characteristics(**{'name': 'Scavenging Ooze', 'text': '{G}: Exile target card from a graveyard. If it was a creature card, put a +1/+1 counter on Scavenging Ooze and you gain 1 life.', 'color': ['G'], 'mana_cost': '1G', 'power': 2, 'toughness': 2, 'subtype': ['Ooze']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c425968(card.Card):
    "Thragtusk"
    def __init__(self):
        super(c425968, self).__init__(gameobject.Characteristics(**{'name': 'Thragtusk', 'text': 'When Thragtusk enters the battlefield, you gain 5 life.\nWhen Thragtusk leaves the battlefield, create a 3/3 green Beast creature token.', 'color': ['G'], 'mana_cost': '4G', 'power': 5, 'toughness': 3, 'subtype': ['Beast']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c425971(card.Card):
    "Abrupt Decay"
    def __init__(self):
        super(c425971, self).__init__(gameobject.Characteristics(**{'name': 'Abrupt Decay', 'text': "Abrupt Decay can't be countered by spells or abilities.\nDestroy target nonland permanent with converted mana cost 3 or less.", 'color': ['B', 'G'], 'mana_cost': 'BG'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c425983(card.Card):
    "Cruel Ultimatum"
    def __init__(self):
        super(c425983, self).__init__(gameobject.Characteristics(**{'name': 'Cruel Ultimatum', 'text': 'Target opponent sacrifices a creature, discards three cards, then loses 5 life. You return a creature card from your graveyard to your hand, draw three cards, then gain 5 life.', 'color': ['U', 'B', 'R'], 'mana_cost': 'UUBBBRR'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c425986(card.Card):
    "Domri Rade"
    def __init__(self):
        super(c425986, self).__init__(gameobject.Characteristics(**{'name': 'Domri Rade', 'text': '+1: Look at the top card of your library. If it\'s a creature card, you may reveal it and put it into your hand.\n−2: Target creature you control fights another target creature.\n−7: You get an emblem with "Creatures you control have double strike, trample, hexproof, and haste."', 'color': ['R', 'G'], 'mana_cost': '1RG', 'subtype': ['Domri']}, supertype=[], types=[cardtype.CardType.PLANESWALKER], abilities=[static_abilities.StaticAbilities.Hexproof, static_abilities.StaticAbilities.Trample]))

class c425988(card.Card):
    "Falkenrath Aristocrat"
    def __init__(self):
        super(c425988, self).__init__(gameobject.Characteristics(**{'name': 'Falkenrath Aristocrat', 'text': 'Flying, haste\nSacrifice a creature: Falkenrath Aristocrat gains indestructible until end of turn. If the sacrificed creature was a Human, put a +1/+1 counter on Falkenrath Aristocrat.', 'color': ['B', 'R'], 'mana_cost': '2BR', 'power': 4, 'toughness': 1, 'subtype': ['Vampire']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Flying, static_abilities.StaticAbilities.Haste]))

class c425990(card.Card):
    "Ghor-Clan Rampager"
    def __init__(self):
        super(c425990, self).__init__(gameobject.Characteristics(**{'name': 'Ghor-Clan Rampager', 'text': 'Trample\nBloodrush — {R}{G}, Discard Ghor-Clan Rampager: Target attacking creature gets +4/+4 and gains trample until end of turn.', 'color': ['R', 'G'], 'mana_cost': '2RG', 'power': 4, 'toughness': 4, 'subtype': ['Beast']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Trample]))

class c425996(card.Card):
    "Izzet Charm"
    def __init__(self):
        super(c425996, self).__init__(gameobject.Characteristics(**{'name': 'Izzet Charm', 'text': 'Choose one —\n• Counter target noncreature spell unless its controller pays {2}.\n• Izzet Charm deals 2 damage to target creature.\n• Draw two cards, then discard two cards.', 'color': ['U', 'R'], 'mana_cost': 'UR'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c426004(card.Card):
    "Putrefy"
    def __init__(self):
        super(c426004, self).__init__(gameobject.Characteristics(**{'name': 'Putrefy', 'text': "Destroy target artifact or creature. It can't be regenerated.", 'color': ['B', 'G'], 'mana_cost': '1BG'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c426012(card.Card):
    "Sphinx's Revelation"
    def __init__(self):
        super(c426012, self).__init__(gameobject.Characteristics(**{'name': "Sphinx's Revelation", 'text': 'You gain X life and draw X cards.', 'color': ['W', 'U'], 'mana_cost': 'XWUU'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c426031(card.Card):
    "Boros Reckoner"
    def __init__(self):
        super(c426031, self).__init__(gameobject.Characteristics(**{'name': 'Boros Reckoner', 'text': 'Whenever Boros Reckoner is dealt damage, it deals that much damage to target creature or player.\n{R/W}: Boros Reckoner gains first strike until end of turn.', 'color': ['W', 'R'], 'mana_cost': 'R/WR/WR/W', 'power': 3, 'toughness': 3, 'subtype': ['Minotaur', 'Wizard']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c426038(card.Card):
    "Torrent of Souls"
    def __init__(self):
        super(c426038, self).__init__(gameobject.Characteristics(**{'name': 'Torrent of Souls', 'text': 'Return up to one target creature card from your graveyard to the battlefield if {B} was spent to cast Torrent of Souls. Creatures target player controls get +2/+0 and gain haste until end of turn if {R} was spent to cast Torrent of Souls. (Do both if {B}{R} was spent.)', 'color': ['B', 'R'], 'mana_cost': '4B/R'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c426040(card.Card):
    "Azorius Signet"
    def __init__(self):
        super(c426040, self).__init__(gameobject.Characteristics(**{'name': 'Azorius Signet', 'text': '{1}, {T}: Add {W}{U} to your mana pool.', 'color': ['W', 'U'], 'mana_cost': '2'}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c426044(card.Card):
    "Dimir Signet"
    def __init__(self):
        super(c426044, self).__init__(gameobject.Characteristics(**{'name': 'Dimir Signet', 'text': '{1}, {T}: Add {U}{B} to your mana pool.', 'color': ['U', 'B'], 'mana_cost': '2'}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c426045(card.Card):
    "Golgari Signet"
    def __init__(self):
        super(c426045, self).__init__(gameobject.Characteristics(**{'name': 'Golgari Signet', 'text': '{1}, {T}: Add {B}{G} to your mana pool.', 'color': ['B', 'G'], 'mana_cost': '2'}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c426047(card.Card):
    "Gruul Signet"
    def __init__(self):
        super(c426047, self).__init__(gameobject.Characteristics(**{'name': 'Gruul Signet', 'text': '{1}, {T}: Add {R}{G} to your mana pool.', 'color': ['R', 'G'], 'mana_cost': '2'}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c426048(card.Card):
    "Izzet Signet"
    def __init__(self):
        super(c426048, self).__init__(gameobject.Characteristics(**{'name': 'Izzet Signet', 'text': '{1}, {T}: Add {U}{R} to your mana pool.', 'color': ['U', 'R'], 'mana_cost': '2'}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c426049(card.Card):
    "Orzhov Signet"
    def __init__(self):
        super(c426049, self).__init__(gameobject.Characteristics(**{'name': 'Orzhov Signet', 'text': '{1}, {T}: Add {W}{B} to your mana pool.', 'color': ['W', 'B'], 'mana_cost': '2'}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c426050(card.Card):
    "Rakdos Signet"
    def __init__(self):
        super(c426050, self).__init__(gameobject.Characteristics(**{'name': 'Rakdos Signet', 'text': '{1}, {T}: Add {B}{R} to your mana pool.', 'color': ['B', 'R'], 'mana_cost': '2'}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c426051(card.Card):
    "Selesnya Signet"
    def __init__(self):
        super(c426051, self).__init__(gameobject.Characteristics(**{'name': 'Selesnya Signet', 'text': '{1}, {T}: Add {G}{W} to your mana pool.', 'color': ['G', 'W'], 'mana_cost': '2'}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c426052(card.Card):
    "Simic Signet"
    def __init__(self):
        super(c426052, self).__init__(gameobject.Characteristics(**{'name': 'Simic Signet', 'text': '{1}, {T}: Add {G}{U} to your mana pool.', 'color': ['G', 'U'], 'mana_cost': '2'}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c426054(card.Card):
    "Arid Mesa"
    def __init__(self):
        super(c426054, self).__init__(gameobject.Characteristics(**{'name': 'Arid Mesa', 'text': '{T}, Pay 1 life, Sacrifice Arid Mesa: Search your library for a Mountain or Plains card and put it onto the battlefield. Then shuffle your library.', 'color': '', 'mana_cost': ''}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c426064(card.Card):
    "Marsh Flats"
    def __init__(self):
        super(c426064, self).__init__(gameobject.Characteristics(**{'name': 'Marsh Flats', 'text': '{T}, Pay 1 life, Sacrifice Marsh Flats: Search your library for a Plains or Swamp card and put it onto the battlefield. Then shuffle your library.', 'color': '', 'mana_cost': ''}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c426065(card.Card):
    "Misty Rainforest"
    def __init__(self):
        super(c426065, self).__init__(gameobject.Characteristics(**{'name': 'Misty Rainforest', 'text': '{T}, Pay 1 life, Sacrifice Misty Rainforest: Search your library for a Forest or Island card and put it onto the battlefield. Then shuffle your library.', 'color': '', 'mana_cost': ''}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c426069(card.Card):
    "Scalding Tarn"
    def __init__(self):
        super(c426069, self).__init__(gameobject.Characteristics(**{'name': 'Scalding Tarn', 'text': '{T}, Pay 1 life, Sacrifice Scalding Tarn: Search your library for an Island or Mountain card and put it onto the battlefield. Then shuffle your library.', 'color': '', 'mana_cost': ''}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c426074(card.Card):
    "Verdant Catacombs"
    def __init__(self):
        super(c426074, self).__init__(gameobject.Characteristics(**{'name': 'Verdant Catacombs', 'text': '{T}, Pay 1 life, Sacrifice Verdant Catacombs: Search your library for a Swamp or Forest card and put it onto the battlefield. Then shuffle your library.', 'color': '', 'mana_cost': ''}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c397841(card.Card):
    "Spectral Procession"
    def __init__(self):
        super(c397841, self).__init__(gameobject.Characteristics(**{'name': 'Spectral Procession', 'text': 'Create three 1/1 white Spirit creature tokens with flying.', 'color': ['W'], 'mana_cost': '2/W2/W2/W'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c397773(card.Card):
    "Mana Leak"
    def __init__(self):
        super(c397773, self).__init__(gameobject.Characteristics(**{'name': 'Mana Leak', 'text': 'Counter target spell unless its controller pays {3}.', 'color': ['U'], 'mana_cost': '1U'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c397881(card.Card):
    "Remand"
    def __init__(self):
        super(c397881, self).__init__(gameobject.Characteristics(**{'name': 'Remand', 'text': "Counter target spell. If that spell is countered this way, put it into its owner's hand instead of into that player's graveyard.\nDraw a card.", 'color': ['U'], 'mana_cost': '1U'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c397701(card.Card):
    "Bitterblossom"
    def __init__(self):
        super(c397701, self).__init__(gameobject.Characteristics(**{'name': 'Bitterblossom', 'text': 'At the beginning of your upkeep, you lose 1 life and create a 1/1 black Faerie Rogue creature token with flying.', 'color': ['B'], 'mana_cost': '1B', 'subtype': ['Faerie']}, supertype=[], types=[cardtype.CardType.TRIBAL, cardtype.CardType.ENCHANTMENT], abilities=[]))

class c397830(card.Card):
    "Dismember"
    def __init__(self):
        super(c397830, self).__init__(gameobject.Characteristics(**{'name': 'Dismember', 'text': '({B/P} can be paid with either {B} or 2 life.)\nTarget creature gets -5/-5 until end of turn.', 'color': ['B'], 'mana_cost': '1B/PB/P'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c397845(card.Card):
    "Vampire Lacerator"
    def __init__(self):
        super(c397845, self).__init__(gameobject.Characteristics(**{'name': 'Vampire Lacerator', 'text': 'At the beginning of your upkeep, you lose 1 life unless an opponent has 10 or less life.', 'color': ['B'], 'mana_cost': 'B', 'power': 2, 'toughness': 2, 'subtype': ['Vampire', 'Warrior']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c397662(card.Card):
    "Burst Lightning"
    def __init__(self):
        super(c397662, self).__init__(gameobject.Characteristics(**{'name': 'Burst Lightning', 'text': 'Kicker {4} (You may pay an additional {4} as you cast this spell.)\nBurst Lightning deals 2 damage to target creature or player. If Burst Lightning was kicked, it deals 4 damage to that creature or player instead.', 'color': ['R'], 'mana_cost': 'R'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c397758(card.Card):
    "Comet Storm"
    def __init__(self):
        super(c397758, self).__init__(gameobject.Characteristics(**{'name': 'Comet Storm', 'text': 'Multikicker {1} (You may pay an additional {1} any number of times as you cast this spell.)\nChoose target creature or player, then choose another target creature or player for each time Comet Storm was kicked. Comet Storm deals X damage to each of them.', 'color': ['R'], 'mana_cost': 'XRR'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c397816(card.Card):
    "Splinter Twin"
    def __init__(self):
        super(c397816, self).__init__(gameobject.Characteristics(**{'name': 'Splinter Twin', 'text': 'Enchant creature\nEnchanted creature has "{T}: Create a token that\'s a copy of this creature. That token has haste. Exile it at the beginning of the next end step."', 'color': ['R'], 'mana_cost': '2RR', 'subtype': ['Aura']}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c397741(card.Card):
    "All Suns' Dawn"
    def __init__(self):
        super(c397741, self).__init__(gameobject.Characteristics(**{'name': "All Suns' Dawn", 'text': "For each color, return up to one target card of that color from your graveyard to your hand. Exile All Suns' Dawn.", 'color': ['G'], 'mana_cost': '4G'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c397788(card.Card):
    "Overwhelming Stampede"
    def __init__(self):
        super(c397788, self).__init__(gameobject.Characteristics(**{'name': 'Overwhelming Stampede', 'text': 'Until end of turn, creatures you control gain trample and get +X/+X, where X is the greatest power among creatures you control.', 'color': ['G'], 'mana_cost': '3GG'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c397751(card.Card):
    "Scute Mob"
    def __init__(self):
        super(c397751, self).__init__(gameobject.Characteristics(**{'name': 'Scute Mob', 'text': 'At the beginning of your upkeep, if you control five or more lands, put four +1/+1 counters on Scute Mob.', 'color': ['G'], 'mana_cost': 'G', 'power': 1, 'toughness': 1, 'subtype': ['Insect']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c397710(card.Card):
    "Etched Champion"
    def __init__(self):
        super(c397710, self).__init__(gameobject.Characteristics(**{'name': 'Etched Champion', 'text': 'Metalcraft — Etched Champion has protection from all colors as long as you control three or more artifacts.', 'color': '', 'mana_cost': '3', 'power': 2, 'toughness': 2, 'subtype': ['Soldier']}, supertype=[], types=[cardtype.CardType.ARTIFACT, cardtype.CardType.CREATURE], abilities=[]))

class c397679(card.Card):
    "Everflowing Chalice"
    def __init__(self):
        super(c397679, self).__init__(gameobject.Characteristics(**{'name': 'Everflowing Chalice', 'text': 'Multikicker {2} (You may pay an additional {2} any number of times as you cast this spell.)\nEverflowing Chalice enters the battlefield with a charge counter on it for each time it was kicked.\n{T}: Add {C} to your mana pool for each charge counter on Everflowing Chalice.', 'color': '', 'mana_cost': '0'}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c397736(card.Card):
    "Lodestone Golem"
    def __init__(self):
        super(c397736, self).__init__(gameobject.Characteristics(**{'name': 'Lodestone Golem', 'text': 'Nonartifact spells cost {1} more to cast.', 'color': '', 'mana_cost': '4', 'power': 5, 'toughness': 3, 'subtype': ['Golem']}, supertype=[], types=[cardtype.CardType.ARTIFACT, cardtype.CardType.CREATURE], abilities=[]))

class c397871(card.Card):
    "Evolving Wilds"
    def __init__(self):
        super(c397871, self).__init__(gameobject.Characteristics(**{'name': 'Evolving Wilds', 'text': '{T}, Sacrifice Evolving Wilds: Search your library for a basic land card and put it onto the battlefield tapped. Then shuffle your library.', 'color': '', 'mana_cost': ''}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c159277(card.Card):
    "Winter Orb"
    def __init__(self):
        super(c159277, self).__init__(gameobject.Characteristics(**{'name': 'Winter Orb', 'text': "As long as Winter Orb is untapped, players can't untap more than one land during their untap steps.", 'color': '', 'mana_cost': '2'}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c159114(card.Card):
    "Mishra's Factory"
    def __init__(self):
        super(c159114, self).__init__(gameobject.Characteristics(**{'name': "Mishra's Factory", 'text': "{T}: Add {C} to your mana pool.\n{1}: Mishra's Factory becomes a 2/2 Assembly-Worker artifact creature until end of turn. It's still a land.\n{T}: Target Assembly-Worker creature gets +1/+1 until end of turn.", 'color': '', 'mana_cost': ''}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c202439(card.Card):
    "Sinkhole"
    def __init__(self):
        super(c202439, self).__init__(gameobject.Characteristics(**{'name': 'Sinkhole', 'text': 'Destroy target land.', 'color': ['B'], 'mana_cost': 'BB'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c221108(card.Card):
    "Icy Manipulator"
    def __init__(self):
        super(c221108, self).__init__(gameobject.Characteristics(**{'name': 'Icy Manipulator', 'text': '{1}, {T}: Tap target artifact, creature, or land.', 'color': '', 'mana_cost': '4'}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c201162(card.Card):
    "Disenchant"
    def __init__(self):
        super(c201162, self).__init__(gameobject.Characteristics(**{'name': 'Disenchant', 'text': 'Destroy target artifact or enchantment.', 'color': ['W'], 'mana_cost': '1W'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c184636(card.Card):
    "Incinerate"
    def __init__(self):
        super(c184636, self).__init__(gameobject.Characteristics(**{'name': 'Incinerate', 'text': "Incinerate deals 3 damage to target creature or player. A creature dealt damage this way can't be regenerated this turn.", 'color': ['R'], 'mana_cost': '1R'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c413550(card.Card):
    "Elite Vanguard"
    def __init__(self):
        super(c413550, self).__init__(gameobject.Characteristics(**{'name': 'Elite Vanguard', 'text': '', 'color': ['W'], 'mana_cost': 'W', 'power': 2, 'toughness': 1, 'subtype': ['Human', 'Soldier']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c413564(card.Card):
    "Mother of Runes"
    def __init__(self):
        super(c413564, self).__init__(gameobject.Characteristics(**{'name': 'Mother of Runes', 'text': '{T}: Target creature you control gains protection from the color of your choice until end of turn.', 'color': ['W'], 'mana_cost': 'W', 'power': 1, 'toughness': 1, 'subtype': ['Human', 'Cleric']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c413573(card.Card):
    "Squadron Hawk"
    def __init__(self):
        super(c413573, self).__init__(gameobject.Characteristics(**{'name': 'Squadron Hawk', 'text': 'Flying\nWhen Squadron Hawk enters the battlefield, you may search your library for up to three cards named Squadron Hawk, reveal them, put them into your hand, then shuffle your library.', 'color': ['W'], 'mana_cost': '1W', 'power': 1, 'toughness': 1, 'subtype': ['Bird']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Flying]))

class c413575(card.Card):
    "Unexpectedly Absent"
    def __init__(self):
        super(c413575, self).__init__(gameobject.Characteristics(**{'name': 'Unexpectedly Absent', 'text': "Put target nonland permanent into its owner's library just beneath the top X cards of that library.", 'color': ['W'], 'mana_cost': 'XWW'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c413576(card.Card):
    "Wall of Omens"
    def __init__(self):
        super(c413576, self).__init__(gameobject.Characteristics(**{'name': 'Wall of Omens', 'text': 'Defender\nWhen Wall of Omens enters the battlefield, draw a card.', 'color': ['W'], 'mana_cost': '1W', 'power': 0, 'toughness': 4, 'subtype': ['Wall']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Defender]))

class c413586(card.Card):
    "Daze"
    def __init__(self):
        super(c413586, self).__init__(gameobject.Characteristics(**{'name': 'Daze', 'text': "You may return an Island you control to its owner's hand rather than pay Daze's mana cost.\nCounter target spell unless its controller pays {1}.", 'color': ['U'], 'mana_cost': '1U'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c413602(card.Card):
    "Memory Lapse"
    def __init__(self):
        super(c413602, self).__init__(gameobject.Characteristics(**{'name': 'Memory Lapse', 'text': "Counter target spell. If that spell is countered this way, put it on top of its owner's library instead of into that player's graveyard.", 'color': ['U'], 'mana_cost': '1U'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c413623(card.Card):
    "Blood Artist"
    def __init__(self):
        super(c413623, self).__init__(gameobject.Characteristics(**{'name': 'Blood Artist', 'text': 'Whenever Blood Artist or another creature dies, target player loses 1 life and you gain 1 life.', 'color': ['B'], 'mana_cost': '1B', 'power': 0, 'toughness': 1, 'subtype': ['Vampire']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c413624(card.Card):
    "Braids, Cabal Minion"
    def __init__(self):
        super(c413624, self).__init__(gameobject.Characteristics(**{'name': 'Braids, Cabal Minion', 'text': "At the beginning of each player's upkeep, that player sacrifices an artifact, creature, or land.", 'color': ['B'], 'mana_cost': '2BB', 'power': 2, 'toughness': 2, 'subtype': ['Human', 'Minion']}, supertype=[cardtype.SuperType.LEGENDARY], types=[cardtype.CardType.CREATURE], abilities=[]))

class c413641(card.Card):
    "Nekrataal"
    def __init__(self):
        super(c413641, self).__init__(gameobject.Characteristics(**{'name': 'Nekrataal', 'text': "First strike\nWhen Nekrataal enters the battlefield, destroy target nonartifact, nonblack creature. That creature can't be regenerated.", 'color': ['B'], 'mana_cost': '2BB', 'power': 2, 'toughness': 1, 'subtype': ['Human', 'Assassin']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c413670(card.Card):
    "Faithless Looting"
    def __init__(self):
        super(c413670, self).__init__(gameobject.Characteristics(**{'name': 'Faithless Looting', 'text': 'Draw two cards, then discard two cards.\nFlashback {2}{R} (You may cast this card from your graveyard for its flashback cost. Then exile it.)', 'color': ['R'], 'mana_cost': 'R'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[static_abilities.StaticAbilities.Flash]))

class c413689(card.Card):
    "Siege-Gang Commander"
    def __init__(self):
        super(c413689, self).__init__(gameobject.Characteristics(**{'name': 'Siege-Gang Commander', 'text': 'When Siege-Gang Commander enters the battlefield, create three 1/1 red Goblin creature tokens.\n{1}{R}, Sacrifice a Goblin: Siege-Gang Commander deals 2 damage to target creature or player.', 'color': ['R'], 'mana_cost': '3RR', 'power': 2, 'toughness': 2, 'subtype': ['Goblin']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c413690(card.Card):
    "Sneak Attack"
    def __init__(self):
        super(c413690, self).__init__(gameobject.Characteristics(**{'name': 'Sneak Attack', 'text': '{R}: You may put a creature card from your hand onto the battlefield. That creature gains haste. Sacrifice the creature at the beginning of the next end step.', 'color': ['R'], 'mana_cost': '3R'}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c413697(card.Card):
    "Young Pyromancer"
    def __init__(self):
        super(c413697, self).__init__(gameobject.Characteristics(**{'name': 'Young Pyromancer', 'text': 'Whenever you cast an instant or sorcery spell, create a 1/1 red Elemental creature token.', 'color': ['R'], 'mana_cost': '1R', 'power': 2, 'toughness': 1, 'subtype': ['Human', 'Shaman']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c413711(card.Card):
    "Green Sun's Zenith"
    def __init__(self):
        super(c413711, self).__init__(gameobject.Characteristics(**{'name': "Green Sun's Zenith", 'text': "Search your library for a green creature card with converted mana cost X or less, put it onto the battlefield, then shuffle your library. Shuffle Green Sun's Zenith into its owner's library.", 'color': ['G'], 'mana_cost': 'XG'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c413717(card.Card):
    "Llanowar Elves"
    def __init__(self):
        super(c413717, self).__init__(gameobject.Characteristics(**{'name': 'Llanowar Elves', 'text': '{T}: Add {G} to your mana pool.', 'color': ['G'], 'mana_cost': 'G', 'power': 1, 'toughness': 1, 'subtype': ['Elf', 'Druid']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c413752(card.Card):
    "Vindicate"
    def __init__(self):
        super(c413752, self).__init__(gameobject.Characteristics(**{'name': 'Vindicate', 'text': 'Destroy target permanent.', 'color': ['W', 'B'], 'mana_cost': '1WB'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c413755(card.Card):
    "Zealous Persecution"
    def __init__(self):
        super(c413755, self).__init__(gameobject.Characteristics(**{'name': 'Zealous Persecution', 'text': 'Until end of turn, creatures you control get +1/+1 and creatures your opponents control get -1/-1.', 'color': ['W', 'B'], 'mana_cost': 'WB'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c413765(card.Card):
    "Isochron Scepter"
    def __init__(self):
        super(c413765, self).__init__(gameobject.Characteristics(**{'name': 'Isochron Scepter', 'text': 'Imprint — When Isochron Scepter enters the battlefield, you may exile an instant card with converted mana cost 2 or less from your hand.\n{2}, {T}: You may copy the exiled card. If you do, you may cast the copy without paying its mana cost.', 'color': '', 'mana_cost': '2'}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c413771(card.Card):
    "Pilgrim's Eye"
    def __init__(self):
        super(c413771, self).__init__(gameobject.Characteristics(**{'name': "Pilgrim's Eye", 'text': "Flying\nWhen Pilgrim's Eye enters the battlefield, you may search your library for a basic land card, reveal it, put it into your hand, then shuffle your library.", 'color': '', 'mana_cost': '3', 'power': 1, 'toughness': 1, 'subtype': ['Thopter']}, supertype=[], types=[cardtype.CardType.ARTIFACT, cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Flying]))

class c413777(card.Card):
    "Worn Powerstone"
    def __init__(self):
        super(c413777, self).__init__(gameobject.Characteristics(**{'name': 'Worn Powerstone', 'text': 'Worn Powerstone enters the battlefield tapped.\n{T}: Add {C}{C} to your mana pool.', 'color': '', 'mana_cost': '3'}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c430667(card.Card):
    "Capsize"
    def __init__(self):
        super(c430667, self).__init__(gameobject.Characteristics(**{'name': 'Capsize', 'text': "Buyback {3} (You may pay an additional {3} as you cast this spell. If you do, put this card into your hand as it resolves.)\nReturn target permanent to its owner's hand.", 'color': ['U'], 'mana_cost': '1UU'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c430668(card.Card):
    "Forbid"
    def __init__(self):
        super(c430668, self).__init__(gameobject.Characteristics(**{'name': 'Forbid', 'text': 'Buyback—Discard two cards. (You may discard two cards in addition to any other costs as you cast this spell. If you do, put this card into your hand as it resolves.)\nCounter target spell.', 'color': ['U'], 'mana_cost': '1UU'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c430670(card.Card):
    "Opposition"
    def __init__(self):
        super(c430670, self).__init__(gameobject.Characteristics(**{'name': 'Opposition', 'text': 'Tap an untapped creature you control: Tap target artifact, creature, or land.', 'color': ['U'], 'mana_cost': '2UU'}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c430680(card.Card):
    "Thoughtseize"
    def __init__(self):
        super(c430680, self).__init__(gameobject.Characteristics(**{'name': 'Thoughtseize', 'text': 'Target player reveals his or her hand. You choose a nonland card from it. That player discards that card. You lose 2 life.', 'color': ['B'], 'mana_cost': 'B'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c420595(card.Card):
    "Chromatic Lantern"
    def __init__(self):
        super(c420595, self).__init__(gameobject.Characteristics(**{'name': 'Chromatic Lantern', 'text': 'Lands you control have "{T}: Add one mana of any color to your mana pool."\n{T}: Add one mana of any color to your mana pool.', 'color': '', 'mana_cost': '3'}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c420600(card.Card):
    "Hangarback Walker"
    def __init__(self):
        super(c420600, self).__init__(gameobject.Characteristics(**{'name': 'Hangarback Walker', 'text': 'Hangarback Walker enters the battlefield with X +1/+1 counters on it.\nWhen Hangarback Walker dies, create a 1/1 colorless Thopter artifact creature token with flying for each +1/+1 counter on Hangarback Walker.\n{1}, {T}: Put a +1/+1 counter on Hangarback Walker.', 'color': '', 'mana_cost': 'XX', 'power': 0, 'toughness': 0, 'subtype': ['Construct']}, supertype=[], types=[cardtype.CardType.ARTIFACT, cardtype.CardType.CREATURE], abilities=[]))

class c420612(card.Card):
    "Solemn Simulacrum"
    def __init__(self):
        super(c420612, self).__init__(gameobject.Characteristics(**{'name': 'Solemn Simulacrum', 'text': 'When Solemn Simulacrum enters the battlefield, you may search your library for a basic land card, put that card onto the battlefield tapped, then shuffle your library.\nWhen Solemn Simulacrum dies, you may draw a card.', 'color': '', 'mana_cost': '4', 'power': 2, 'toughness': 2, 'subtype': ['Golem']}, supertype=[], types=[cardtype.CardType.ARTIFACT, cardtype.CardType.CREATURE], abilities=[]))

class c425822(card.Card):
    "Sword of War and Peace"
    def __init__(self):
        super(c425822, self).__init__(gameobject.Characteristics(**{'name': 'Sword of War and Peace', 'text': 'Equipped creature gets +2/+2 and has protection from red and from white.\nWhenever equipped creature deals combat damage to a player, Sword of War and Peace deals damage to that player equal to the number of cards in his or her hand and you gain 1 life for each card in your hand.\nEquip {2}', 'color': '', 'mana_cost': '3', 'subtype': ['Equipment']}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c425825(card.Card):
    "Wurmcoil Engine"
    def __init__(self):
        super(c425825, self).__init__(gameobject.Characteristics(**{'name': 'Wurmcoil Engine', 'text': 'Deathtouch, lifelink\nWhen Wurmcoil Engine dies, create a 3/3 colorless Wurm artifact creature token with deathtouch and a 3/3 colorless Wurm artifact creature token with lifelink.', 'color': '', 'mana_cost': '6', 'power': 6, 'toughness': 6, 'subtype': ['Wurm']}, supertype=[], types=[cardtype.CardType.ARTIFACT, cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Deathtouch, static_abilities.StaticAbilities.Lifelink]))

class c405100(card.Card):
    "Hallowed Fountain"
    def __init__(self):
        super(c405100, self).__init__(gameobject.Characteristics(**{'name': 'Hallowed Fountain', 'text': "({T}: Add {W} or {U} to your mana pool.)\nAs Hallowed Fountain enters the battlefield, you may pay 2 life. If you don't, Hallowed Fountain enters the battlefield tapped.", 'color': ['W', 'U'], 'mana_cost': '', 'subtype': ['Plains', 'Island']}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c405093(card.Card):
    "Blood Crypt"
    def __init__(self):
        super(c405093, self).__init__(gameobject.Characteristics(**{'name': 'Blood Crypt', 'text': "({T}: Add {B} or {R} to your mana pool.)\nAs Blood Crypt enters the battlefield, you may pay 2 life. If you don't, Blood Crypt enters the battlefield tapped.", 'color': ['B', 'R'], 'mana_cost': '', 'subtype': ['Swamp', 'Mountain']}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c405110(card.Card):
    "Stomping Ground"
    def __init__(self):
        super(c405110, self).__init__(gameobject.Characteristics(**{'name': 'Stomping Ground', 'text': "({T}: Add {R} or {G} to your mana pool.)\nAs Stomping Ground enters the battlefield, you may pay 2 life. If you don't, Stomping Ground enters the battlefield tapped.", 'color': ['R', 'G'], 'mana_cost': '', 'subtype': ['Mountain', 'Forest']}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c405112(card.Card):
    "Temple Garden"
    def __init__(self):
        super(c405112, self).__init__(gameobject.Characteristics(**{'name': 'Temple Garden', 'text': "({T}: Add {G} or {W} to your mana pool.)\nAs Temple Garden enters the battlefield, you may pay 2 life. If you don't, Temple Garden enters the battlefield tapped.", 'color': ['W', 'G'], 'mana_cost': '', 'subtype': ['Forest', 'Plains']}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c405109(card.Card):
    "Steam Vents"
    def __init__(self):
        super(c405109, self).__init__(gameobject.Characteristics(**{'name': 'Steam Vents', 'text': "({T}: Add {U} or {R} to your mana pool.)\nAs Steam Vents enters the battlefield, you may pay 2 life. If you don't, Steam Vents enters the battlefield tapped.", 'color': ['U', 'R'], 'mana_cost': '', 'subtype': ['Island', 'Mountain']}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c405103(card.Card):
    "Overgrown Tomb"
    def __init__(self):
        super(c405103, self).__init__(gameobject.Characteristics(**{'name': 'Overgrown Tomb', 'text': "({T}: Add {B} or {G} to your mana pool.)\nAs Overgrown Tomb enters the battlefield, you may pay 2 life. If you don't, Overgrown Tomb enters the battlefield tapped.", 'color': ['B', 'G'], 'mana_cost': '', 'subtype': ['Swamp', 'Forest']}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c405106(card.Card):
    "Sacred Foundry"
    def __init__(self):
        super(c405106, self).__init__(gameobject.Characteristics(**{'name': 'Sacred Foundry', 'text': "({T}: Add {R} or {W} to your mana pool.)\nAs Sacred Foundry enters the battlefield, you may pay 2 life. If you don't, Sacred Foundry enters the battlefield tapped.", 'color': ['W', 'R'], 'mana_cost': '', 'subtype': ['Mountain', 'Plains']}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c405095(card.Card):
    "Breeding Pool"
    def __init__(self):
        super(c405095, self).__init__(gameobject.Characteristics(**{'name': 'Breeding Pool', 'text': "({T}: Add {G} or {U} to your mana pool.)\nAs Breeding Pool enters the battlefield, you may pay 2 life. If you don't, Breeding Pool enters the battlefield tapped.", 'color': ['U', 'G'], 'mana_cost': '', 'subtype': ['Forest', 'Island']}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c405098(card.Card):
    "Flooded Strand"
    def __init__(self):
        super(c405098, self).__init__(gameobject.Characteristics(**{'name': 'Flooded Strand', 'text': '{T}, Pay 1 life, Sacrifice Flooded Strand: Search your library for a Plains or Island card and put it onto the battlefield. Then shuffle your library.', 'color': '', 'mana_cost': ''}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c405104(card.Card):
    "Polluted Delta"
    def __init__(self):
        super(c405104, self).__init__(gameobject.Characteristics(**{'name': 'Polluted Delta', 'text': '{T}, Pay 1 life, Sacrifice Polluted Delta: Search your library for an Island or Swamp card and put it onto the battlefield. Then shuffle your library.', 'color': '', 'mana_cost': ''}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c405094(card.Card):
    "Bloodstained Mire"
    def __init__(self):
        super(c405094, self).__init__(gameobject.Characteristics(**{'name': 'Bloodstained Mire', 'text': '{T}, Pay 1 life, Sacrifice Bloodstained Mire: Search your library for a Swamp or Mountain card and put it onto the battlefield. Then shuffle your library.', 'color': '', 'mana_cost': ''}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c405116(card.Card):
    "Wooded Foothills"
    def __init__(self):
        super(c405116, self).__init__(gameobject.Characteristics(**{'name': 'Wooded Foothills', 'text': '{T}, Pay 1 life, Sacrifice Wooded Foothills: Search your library for a Mountain or Forest card and put it onto the battlefield. Then shuffle your library.', 'color': '', 'mana_cost': ''}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c405115(card.Card):
    "Windswept Heath"
    def __init__(self):
        super(c405115, self).__init__(gameobject.Characteristics(**{'name': 'Windswept Heath', 'text': '{T}, Pay 1 life, Sacrifice Windswept Heath: Search your library for a Forest or Plains card and put it onto the battlefield. Then shuffle your library.', 'color': '', 'mana_cost': ''}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c409573(card.Card):
    "Mana Confluence"
    def __init__(self):
        super(c409573, self).__init__(gameobject.Characteristics(**{'name': 'Mana Confluence', 'text': '{T}, Pay 1 life: Add one mana of any color to your mana pool.', 'color': '', 'mana_cost': ''}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c416756(card.Card):
    "Umezawa's Jitte"
    def __init__(self):
        super(c416756, self).__init__(gameobject.Characteristics(**{'name': "Umezawa's Jitte", 'text': "Whenever equipped creature deals combat damage, put two charge counters on Umezawa's Jitte.\nRemove a charge counter from Umezawa's Jitte: Choose one —\n• Equipped creature gets +2/+2 until end of turn.\n• Target creature gets -1/-1 until end of turn.\n• You gain 2 life.\nEquip {2}", 'color': '', 'mana_cost': '2', 'subtype': ['Equipment']}, supertype=[cardtype.SuperType.LEGENDARY], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c386286(card.Card):
    "Cataclysm"
    def __init__(self):
        super(c386286, self).__init__(gameobject.Characteristics(**{'name': 'Cataclysm', 'text': 'Each player chooses from among the permanents he or she controls an artifact, a creature, an enchantment, and a land, then sacrifices the rest.', 'color': ['W'], 'mana_cost': '2WW'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c373322(card.Card):
    "Tangle Wire"
    def __init__(self):
        super(c373322, self).__init__(gameobject.Characteristics(**{'name': 'Tangle Wire', 'text': "Fading 4 (This artifact enters the battlefield with four fade counters on it. At the beginning of your upkeep, remove a fade counter from it. If you can't, sacrifice it.)\nAt the beginning of each player's upkeep, that player taps an untapped artifact, creature, or land he or she controls for each fade counter on Tangle Wire.", 'color': '', 'mana_cost': '3'}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c373335(card.Card):
    "Gilded Lotus"
    def __init__(self):
        super(c373335, self).__init__(gameobject.Characteristics(**{'name': 'Gilded Lotus', 'text': '{T}: Add three mana of any one color to your mana pool.', 'color': '', 'mana_cost': '5'}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c259296(card.Card):
    "Mikaeus, the Lunarch"
    def __init__(self):
        super(c259296, self).__init__(gameobject.Characteristics(**{'name': 'Mikaeus, the Lunarch', 'text': 'Mikaeus, the Lunarch enters the battlefield with X +1/+1 counters on it.\n{T}: Put a +1/+1 counter on Mikaeus.\n{T}, Remove a +1/+1 counter from Mikaeus: Put a +1/+1 counter on each other creature you control.', 'color': ['W'], 'mana_cost': 'XW', 'power': 0, 'toughness': 0, 'subtype': ['Human', 'Cleric']}, supertype=[cardtype.SuperType.LEGENDARY], types=[cardtype.CardType.CREATURE], abilities=[]))

class c194980(card.Card):
    "Tinker"
    def __init__(self):
        super(c194980, self).__init__(gameobject.Characteristics(**{'name': 'Tinker', 'text': 'As an additional cost to cast Tinker, sacrifice an artifact.\nSearch your library for an artifact card and put that card onto the battlefield. Then shuffle your library.', 'color': ['U'], 'mana_cost': '2U'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c417453(card.Card):
    "Treetop Village"
    def __init__(self):
        super(c417453, self).__init__(gameobject.Characteristics(**{'name': 'Treetop Village', 'text': "Treetop Village enters the battlefield tapped.\n{T}: Add {G} to your mana pool.\n{1}{G}: Treetop Village becomes a 3/3 green Ape creature with trample until end of turn. It's still a land. (If it would assign enough damage to its blockers to destroy them, you may have it assign the rest of its damage to defending player or planeswalker.)", 'color': ['G'], 'mana_cost': ''}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c417470(card.Card):
    "Doom Blade"
    def __init__(self):
        super(c417470, self).__init__(gameobject.Characteristics(**{'name': 'Doom Blade', 'text': 'Destroy target nonblack creature.', 'color': ['B'], 'mana_cost': '1B'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c417484(card.Card):
    "Smallpox"
    def __init__(self):
        super(c417484, self).__init__(gameobject.Characteristics(**{'name': 'Smallpox', 'text': 'Each player loses 1 life, discards a card, sacrifices a creature, then sacrifices a land.', 'color': ['B'], 'mana_cost': 'BB'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c409577(card.Card):
    "Geist of Saint Traft"
    def __init__(self):
        super(c409577, self).__init__(gameobject.Characteristics(**{'name': 'Geist of Saint Traft', 'text': "Hexproof (This creature can't be the target of spells or abilities your opponents control.)\nWhenever Geist of Saint Traft attacks, create a 4/4 white Angel creature token with flying that's tapped and attacking. Exile that token at end of combat.", 'color': ['W', 'U'], 'mana_cost': '1WU', 'power': 2, 'toughness': 2, 'subtype': ['Spirit', 'Cleric']}, supertype=[cardtype.SuperType.LEGENDARY], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Hexproof]))

class c409580(card.Card):
    "Champion of the Parish"
    def __init__(self):
        super(c409580, self).__init__(gameobject.Characteristics(**{'name': 'Champion of the Parish', 'text': 'Whenever another Human enters the battlefield under your control, put a +1/+1 counter on Champion of the Parish.', 'color': ['W'], 'mana_cost': 'W', 'power': 1, 'toughness': 1, 'subtype': ['Human', 'Soldier']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c409587(card.Card):
    "Fiend Hunter"
    def __init__(self):
        super(c409587, self).__init__(gameobject.Characteristics(**{'name': 'Fiend Hunter', 'text': "When Fiend Hunter enters the battlefield, you may exile another target creature.\nWhen Fiend Hunter leaves the battlefield, return the exiled card to the battlefield under its owner's control.", 'color': ['W'], 'mana_cost': '1WW', 'power': 1, 'toughness': 3, 'subtype': ['Human', 'Cleric']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c409630(card.Card):
    "Diregraf Ghoul"
    def __init__(self):
        super(c409630, self).__init__(gameobject.Characteristics(**{'name': 'Diregraf Ghoul', 'text': 'Diregraf Ghoul enters the battlefield tapped.', 'color': ['B'], 'mana_cost': 'B', 'power': 2, 'toughness': 2, 'subtype': ['Zombie']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c401643(card.Card):
    "Avenger of Zendikar"
    def __init__(self):
        super(c401643, self).__init__(gameobject.Characteristics(**{'name': 'Avenger of Zendikar', 'text': 'When Avenger of Zendikar enters the battlefield, create a 0/1 green Plant creature token for each land you control.\nLandfall — Whenever a land enters the battlefield under your control, you may put a +1/+1 counter on each Plant creature you control.', 'color': ['G'], 'mana_cost': '5GG', 'power': 5, 'toughness': 5, 'subtype': ['Elemental']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c401658(card.Card):
    "Harrow"
    def __init__(self):
        super(c401658, self).__init__(gameobject.Characteristics(**{'name': 'Harrow', 'text': 'As an additional cost to cast Harrow, sacrifice a land.\nSearch your library for up to two basic land cards and put them onto the battlefield. Then shuffle your library.', 'color': ['G'], 'mana_cost': '2G'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c401675(card.Card):
    "Stirring Wildwood"
    def __init__(self):
        super(c401675, self).__init__(gameobject.Characteristics(**{'name': 'Stirring Wildwood', 'text': "Stirring Wildwood enters the battlefield tapped.\n{T}: Add {G} or {W} to your mana pool.\n{1}{G}{W}: Until end of turn, Stirring Wildwood becomes a 3/4 green and white Elemental creature with reach. It's still a land.", 'color': ['G', 'W'], 'mana_cost': ''}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c401707(card.Card):
    "Mind Stone"
    def __init__(self):
        super(c401707, self).__init__(gameobject.Characteristics(**{'name': 'Mind Stone', 'text': '{T}: Add {C} to your mana pool.\n{1}, {T}, Sacrifice Mind Stone: Draw a card.', 'color': '', 'mana_cost': '2'}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c394361(card.Card):
    "Elspeth, Sun's Champion"
    def __init__(self):
        super(c394361, self).__init__(gameobject.Characteristics(**{'name': "Elspeth, Sun's Champion", 'text': '+1: Create three 1/1 white Soldier creature tokens.\n−3: Destroy all creatures with power 4 or greater.\n−7: You get an emblem with "Creatures you control get +2/+2 and have flying."', 'color': ['W'], 'mana_cost': '4WW', 'subtype': ['Elspeth']}, supertype=[], types=[cardtype.CardType.PLANESWALKER], abilities=[]))

class c394360(card.Card):
    "Dictate of Heliod"
    def __init__(self):
        super(c394360, self).__init__(gameobject.Characteristics(**{'name': 'Dictate of Heliod', 'text': 'Flash\nCreatures you control get +2/+2.', 'color': ['W'], 'mana_cost': '3WW'}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[static_abilities.StaticAbilities.Flash]))

class c380188(card.Card):
    "Into the Roil"
    def __init__(self):
        super(c380188, self).__init__(gameobject.Characteristics(**{'name': 'Into the Roil', 'text': "Kicker {1}{U} (You may pay an additional {1}{U} as you cast this spell.)\nReturn target nonland permanent to its owner's hand. If Into the Roil was kicked, draw a card.", 'color': ['U'], 'mana_cost': '1U'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c380236(card.Card):
    "Acidic Slime"
    def __init__(self):
        super(c380236, self).__init__(gameobject.Characteristics(**{'name': 'Acidic Slime', 'text': 'Deathtouch (Any amount of damage this deals to a creature is enough to destroy it.)\nWhen Acidic Slime enters the battlefield, destroy target artifact, enchantment, or land.', 'color': ['G'], 'mana_cost': '3GG', 'power': 2, 'toughness': 2, 'subtype': ['Ooze']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Deathtouch]))

class c380227(card.Card):
    "Underworld Connections"
    def __init__(self):
        super(c380227, self).__init__(gameobject.Characteristics(**{'name': 'Underworld Connections', 'text': 'Enchant land\nEnchanted land has "{T}, Pay 1 life: Draw a card."', 'color': ['B'], 'mana_cost': '1BB', 'subtype': ['Aura']}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c373379(card.Card):
    "Sun Titan"
    def __init__(self):
        super(c373379, self).__init__(gameobject.Characteristics(**{'name': 'Sun Titan', 'text': 'Vigilance\nWhenever Sun Titan enters the battlefield or attacks, you may return target permanent card with converted mana cost 3 or less from your graveyard to the battlefield.', 'color': ['W'], 'mana_cost': '4WW', 'power': 6, 'toughness': 6, 'subtype': ['Giant']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Vigilance]))

class c373384(card.Card):
    "Polukranos, World Eater"
    def __init__(self):
        super(c373384, self).__init__(gameobject.Characteristics(**{'name': 'Polukranos, World Eater', 'text': "{X}{X}{G}: Monstrosity X. (If this creature isn't monstrous, put X +1/+1 counters on it and it becomes monstrous.)\nWhen Polukranos, World Eater becomes monstrous, it deals X damage divided as you choose among any number of target creatures your opponents control. Each of those creatures deals damage equal to its power to Polukranos.", 'color': ['G'], 'mana_cost': '2GG', 'power': 5, 'toughness': 5, 'subtype': ['Hydra']}, supertype=[cardtype.SuperType.LEGENDARY], types=[cardtype.CardType.CREATURE], abilities=[]))

class c373416(card.Card):
    "Troll Ascetic"
    def __init__(self):
        super(c373416, self).__init__(gameobject.Characteristics(**{'name': 'Troll Ascetic', 'text': "Hexproof (This creature can't be the target of spells or abilities your opponents control.)\n{1}{G}: Regenerate Troll Ascetic.", 'color': ['G'], 'mana_cost': '1GG', 'power': 3, 'toughness': 2, 'subtype': ['Troll', 'Shaman']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Hexproof]))

class c368479(card.Card):
    "Gatekeeper of Malakir"
    def __init__(self):
        super(c368479, self).__init__(gameobject.Characteristics(**{'name': 'Gatekeeper of Malakir', 'text': 'Kicker {B} (You may pay an additional {B} as you cast this spell.)\nWhen Gatekeeper of Malakir enters the battlefield, if it was kicked, target player sacrifices a creature.', 'color': ['B'], 'mana_cost': 'BB', 'power': 2, 'toughness': 2, 'subtype': ['Vampire', 'Warrior']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c265979(card.Card):
    "Preordain"
    def __init__(self):
        super(c265979, self).__init__(gameobject.Characteristics(**{'name': 'Preordain', 'text': 'Scry 2, then draw a card. (To scry 2, look at the top two cards of your library, then put any number of them on the bottom of your library and the rest on top in any order.)', 'color': ['U'], 'mana_cost': 'U'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c266210(card.Card):
    "Plated Geopede"
    def __init__(self):
        super(c266210, self).__init__(gameobject.Characteristics(**{'name': 'Plated Geopede', 'text': 'First strike\nLandfall — Whenever a land enters the battlefield under your control, Plated Geopede gets +2/+2 until end of turn.', 'color': ['R'], 'mana_cost': '1R', 'power': 1, 'toughness': 1, 'subtype': ['Insect']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c270873(card.Card):
    "Searing Blaze"
    def __init__(self):
        super(c270873, self).__init__(gameobject.Characteristics(**{'name': 'Searing Blaze', 'text': 'Searing Blaze deals 1 damage to target player and 1 damage to target creature that player controls.\nLandfall — If you had a land enter the battlefield under your control this turn, Searing Blaze deals 3 damage to that player and 3 damage to that creature instead.', 'color': ['R'], 'mana_cost': 'RR'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c266299(card.Card):
    "Ajani Vengeant"
    def __init__(self):
        super(c266299, self).__init__(gameobject.Characteristics(**{'name': 'Ajani Vengeant', 'text': "+1: Target permanent doesn't untap during its controller's next untap step.\n−2: Ajani Vengeant deals 3 damage to target creature or player and you gain 3 life.\n−7: Destroy all lands target player controls.", 'color': ['W', 'R'], 'mana_cost': '2RW', 'subtype': ['Ajani']}, supertype=[], types=[cardtype.CardType.PLANESWALKER], abilities=[]))

class c249405(card.Card):
    "Qasali Pridemage"
    def __init__(self):
        super(c249405, self).__init__(gameobject.Characteristics(**{'name': 'Qasali Pridemage', 'text': 'Exalted (Whenever a creature you control attacks alone, that creature gets +1/+1 until end of turn.)\n{1}, Sacrifice Qasali Pridemage: Destroy target artifact or enchantment.', 'color': ['W', 'G'], 'mana_cost': 'GW', 'power': 2, 'toughness': 2, 'subtype': ['Cat', 'Wizard']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c222707(card.Card):
    "Razormane Masticore"
    def __init__(self):
        super(c222707, self).__init__(gameobject.Characteristics(**{'name': 'Razormane Masticore', 'text': 'First strike (This creature deals combat damage before creatures without first strike.)\nAt the beginning of your upkeep, sacrifice Razormane Masticore unless you discard a card.\nAt the beginning of your draw step, you may have Razormane Masticore deal 3 damage to target creature.', 'color': '', 'mana_cost': '5', 'power': 5, 'toughness': 5, 'subtype': ['Masticore']}, supertype=[], types=[cardtype.CardType.ARTIFACT, cardtype.CardType.CREATURE], abilities=[]))

class c222711(card.Card):
    "Elixir of Immortality"
    def __init__(self):
        super(c222711, self).__init__(gameobject.Characteristics(**{'name': 'Elixir of Immortality', 'text': "{2}, {T}: You gain 5 life. Shuffle Elixir of Immortality and your graveyard into their owner's library.", 'color': '', 'mana_cost': '1'}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c393851(card.Card):
    "Jace Beleren"
    def __init__(self):
        super(c393851, self).__init__(gameobject.Characteristics(**{'name': 'Jace Beleren', 'text': '+2: Each player draws a card.\n−1: Target player draws a card.\n−10: Target player puts the top twenty cards of his or her library into his or her graveyard.', 'color': ['U'], 'mana_cost': '1UU', 'subtype': ['Jace']}, supertype=[], types=[cardtype.CardType.PLANESWALKER], abilities=[]))

class c382209(card.Card):
    "Agent of Acquisitions"
    def __init__(self):
        super(c382209, self).__init__(gameobject.Characteristics(**{'name': 'Agent of Acquisitions', 'text': "Draft Agent of Acquisitions face up.\nInstead of drafting a card from a booster pack, you may draft each card in that booster pack, one at a time. If you do, turn Agent of Acquisitions face down and you can't draft cards for the rest of this draft round. (You may look at booster packs passed to you.)", 'color': '', 'mana_cost': '2', 'power': 2, 'toughness': 1, 'subtype': ['Construct']}, supertype=[], types=[cardtype.CardType.ARTIFACT, cardtype.CardType.CREATURE], abilities=[]))

class c382233(card.Card):
    "Cogwork Librarian"
    def __init__(self):
        super(c382233, self).__init__(gameobject.Characteristics(**{'name': 'Cogwork Librarian', 'text': 'Draft Cogwork Librarian face up.\nAs you draft a card, you may draft an additional card from that booster pack. If you do, put Cogwork Librarian into that booster pack.', 'color': '', 'mana_cost': '4', 'power': 3, 'toughness': 3, 'subtype': ['Construct']}, supertype=[], types=[cardtype.CardType.ARTIFACT, cardtype.CardType.CREATURE], abilities=[]))

class c382246(card.Card):
    "Deal Broker"
    def __init__(self):
        super(c382246, self).__init__(gameobject.Characteristics(**{'name': 'Deal Broker', 'text': 'Draft Deal Broker face up.\nImmediately after the draft, you may reveal a card in your card pool. Each other player may offer you one card in his or her card pool in exchange. You may accept any one offer.\n{T}: Draw a card, then discard a card.', 'color': '', 'mana_cost': '3', 'power': 2, 'toughness': 3, 'subtype': ['Construct']}, supertype=[], types=[cardtype.CardType.ARTIFACT, cardtype.CardType.CREATURE], abilities=[]))

class c382298(card.Card):
    "Lore Seeker"
    def __init__(self):
        super(c382298, self).__init__(gameobject.Characteristics(**{'name': 'Lore Seeker', 'text': "Reveal Lore Seeker as you draft it. After you draft Lore Seeker, you may add a booster pack to the draft. (Your next pick is from that booster pack. Pass it to the next player and it's drafted this draft round.)", 'color': '', 'mana_cost': '2', 'power': 2, 'toughness': 2, 'subtype': ['Construct']}, supertype=[], types=[cardtype.CardType.ARTIFACT, cardtype.CardType.CREATURE], abilities=[]))

class c382320(card.Card):
    "Paliano, the High City"
    def __init__(self):
        super(c382320, self).__init__(gameobject.Characteristics(**{'name': 'Paliano, the High City', 'text': 'Reveal Paliano, the High City as you draft it. The player to your right chooses a color, you choose another color, then the player to your left chooses a third color.\n{T}: Add one mana to your mana pool of any color chosen as you drafted cards named Paliano, the High City.', 'color': '', 'mana_cost': ''}, supertype=[cardtype.SuperType.LEGENDARY], types=[cardtype.CardType.LAND], abilities=[]))

class c382397(card.Card):
    "Vampire Hexmage"
    def __init__(self):
        super(c382397, self).__init__(gameobject.Characteristics(**{'name': 'Vampire Hexmage', 'text': 'First strike\nSacrifice Vampire Hexmage: Remove all counters from target permanent.', 'color': ['B'], 'mana_cost': 'BB', 'power': 2, 'toughness': 1, 'subtype': ['Vampire', 'Shaman']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c382351(card.Card):
    "Sakura-Tribe Elder"
    def __init__(self):
        super(c382351, self).__init__(gameobject.Characteristics(**{'name': 'Sakura-Tribe Elder', 'text': 'Sacrifice Sakura-Tribe Elder: Search your library for a basic land card, put that card onto the battlefield tapped, then shuffle your library.', 'color': ['G'], 'mana_cost': '1G', 'power': 1, 'toughness': 1, 'subtype': ['Snake', 'Shaman']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c382249(card.Card):
    "Deathrender"
    def __init__(self):
        super(c382249, self).__init__(gameobject.Characteristics(**{'name': 'Deathrender', 'text': 'Equipped creature gets +2/+2.\nWhenever equipped creature dies, you may put a creature card from your hand onto the battlefield and attach Deathrender to it.\nEquip {2}', 'color': '', 'mana_cost': '4', 'subtype': ['Equipment']}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c416784(card.Card):
    "Arcane Savant"
    def __init__(self):
        super(c416784, self).__init__(gameobject.Characteristics(**{'name': 'Arcane Savant', 'text': "Before you shuffle your deck to start the game, you may reveal this card from your deck and exile an instant or sorcery card you drafted that isn't in your deck.\nWhen Arcane Savant enters the battlefield, copy a card you exiled with cards named Arcane Savant. You may cast the copy without paying its mana cost.", 'color': ['U'], 'mana_cost': '3UU', 'power': 3, 'toughness': 3, 'subtype': ['Human', 'Wizard']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c416798(card.Card):
    "Custodi Lich"
    def __init__(self):
        super(c416798, self).__init__(gameobject.Characteristics(**{'name': 'Custodi Lich', 'text': 'When Custodi Lich enters the battlefield, you become the monarch.\nWhenever you become the monarch, target player sacrifices a creature.', 'color': ['B'], 'mana_cost': '3BB', 'power': 4, 'toughness': 2, 'subtype': ['Zombie', 'Cleric']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c416819(card.Card):
    "Caller of the Untamed"
    def __init__(self):
        super(c416819, self).__init__(gameobject.Characteristics(**{'name': 'Caller of the Untamed', 'text': "Before you shuffle your deck to start the game, you may reveal this card from your deck and exile a creature card you drafted that isn't in your deck.\n{X}, {T}: Create a token that's a copy of a card you exiled with cards named Caller of the Untamed. X is the converted mana cost of that card.", 'color': ['G'], 'mana_cost': '3G', 'power': 2, 'toughness': 4, 'subtype': ['Elf', 'Shaman']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c416863(card.Card):
    "Deceiver Exarch"
    def __init__(self):
        super(c416863, self).__init__(gameobject.Characteristics(**{'name': 'Deceiver Exarch', 'text': 'Flash (You may cast this spell any time you could cast an instant.)\nWhen Deceiver Exarch enters the battlefield, choose one —\n• Untap target permanent you control.\n• Tap target permanent an opponent controls.', 'color': ['U'], 'mana_cost': '2U', 'power': 1, 'toughness': 4, 'subtype': ['Cleric']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Flash]))

class c416919(card.Card):
    "Guttersnipe"
    def __init__(self):
        super(c416919, self).__init__(gameobject.Characteristics(**{'name': 'Guttersnipe', 'text': 'Whenever you cast an instant or sorcery spell, Guttersnipe deals 2 damage to each opponent.', 'color': ['R'], 'mana_cost': '2R', 'power': 2, 'toughness': 2, 'subtype': ['Goblin', 'Shaman']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c416933(card.Card):
    "Birds of Paradise"
    def __init__(self):
        super(c416933, self).__init__(gameobject.Characteristics(**{'name': 'Birds of Paradise', 'text': 'Flying\n{T}: Add one mana of any color to your mana pool.', 'color': ['G'], 'mana_cost': 'G', 'power': 0, 'toughness': 1, 'subtype': ['Bird']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Flying]))

class c238141(card.Card):
    "Hornet Queen"
    def __init__(self):
        super(c238141, self).__init__(gameobject.Characteristics(**{'name': 'Hornet Queen', 'text': 'Flying\nDeathtouch (Any amount of damage this deals to a creature is enough to destroy it.)\nWhen Hornet Queen enters the battlefield, create four 1/1 green Insect creature tokens with flying and deathtouch.', 'color': ['G'], 'mana_cost': '4GGG', 'power': 2, 'toughness': 2, 'subtype': ['Insect']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Deathtouch, static_abilities.StaticAbilities.Flying]))

class c247316(card.Card):
    "Howling Mine"
    def __init__(self):
        super(c247316, self).__init__(gameobject.Characteristics(**{'name': 'Howling Mine', 'text': "At the beginning of each player's draw step, if Howling Mine is untapped, that player draws an additional card.", 'color': '', 'mana_cost': '2'}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c430318(card.Card):
    "Curse of Predation"
    def __init__(self):
        super(c430318, self).__init__(gameobject.Characteristics(**{'name': 'Curse of Predation', 'text': 'Enchant player\nWhenever a creature attacks enchanted player, put a +1/+1 counter on it.', 'color': ['G'], 'mana_cost': '2G', 'subtype': ['Aura', 'Curse']}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c430322(card.Card):
    "Elvish Mystic"
    def __init__(self):
        super(c430322, self).__init__(gameobject.Characteristics(**{'name': 'Elvish Mystic', 'text': '{T}: Add {G} to your mana pool.', 'color': ['G'], 'mana_cost': 'G', 'power': 1, 'toughness': 1, 'subtype': ['Elf', 'Druid']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c430358(card.Card):
    "Rampaging Baloths"
    def __init__(self):
        super(c430358, self).__init__(gameobject.Characteristics(**{'name': 'Rampaging Baloths', 'text': 'Trample\nLandfall — Whenever a land enters the battlefield under your control, you may create a 4/4 green Beast creature token.', 'color': ['G'], 'mana_cost': '4GG', 'power': 6, 'toughness': 6, 'subtype': ['Beast']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Trample]))

class c430359(card.Card):
    "Reclamation Sage"
    def __init__(self):
        super(c430359, self).__init__(gameobject.Characteristics(**{'name': 'Reclamation Sage', 'text': 'When Reclamation Sage enters the battlefield, you may destroy target artifact or enchantment.', 'color': ['G'], 'mana_cost': '2G', 'power': 2, 'toughness': 1, 'subtype': ['Elf', 'Shaman']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c430362(card.Card):
    "Satyr Wayfinder"
    def __init__(self):
        super(c430362, self).__init__(gameobject.Characteristics(**{'name': 'Satyr Wayfinder', 'text': 'When Satyr Wayfinder enters the battlefield, reveal the top four cards of your library. You may put a land card from among them into your hand. Put the rest into your graveyard.', 'color': ['G'], 'mana_cost': '1G', 'power': 1, 'toughness': 1, 'subtype': ['Satyr']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c430402(card.Card):
    "Lotleth Troll"
    def __init__(self):
        super(c430402, self).__init__(gameobject.Characteristics(**{'name': 'Lotleth Troll', 'text': 'Trample\nDiscard a creature card: Put a +1/+1 counter on Lotleth Troll.\n{B}: Regenerate Lotleth Troll.', 'color': ['B', 'G'], 'mana_cost': 'BG', 'power': 2, 'toughness': 1, 'subtype': ['Zombie', 'Troll']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Trample]))

class c433046(card.Card):
    "Go for the Throat"
    def __init__(self):
        super(c433046, self).__init__(gameobject.Characteristics(**{'name': 'Go for the Throat', 'text': 'Destroy target nonartifact creature.', 'color': ['B'], 'mana_cost': '1B'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c433081(card.Card):
    "Farseek"
    def __init__(self):
        super(c433081, self).__init__(gameobject.Characteristics(**{'name': 'Farseek', 'text': 'Search your library for a Plains, Island, Swamp, or Mountain card and put it onto the battlefield tapped. Then shuffle your library.', 'color': ['G'], 'mana_cost': '1G'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c433104(card.Card):
    "Fleecemane Lion"
    def __init__(self):
        super(c433104, self).__init__(gameobject.Characteristics(**{'name': 'Fleecemane Lion', 'text': "{3}{G}{W}: Monstrosity 1. (If this creature isn't monstrous, put a +1/+1 counter on it and it becomes monstrous.)\nAs long as Fleecemane Lion is monstrous, it has hexproof and indestructible.", 'color': ['W', 'G'], 'mana_cost': 'GW', 'power': 3, 'toughness': 3, 'subtype': ['Cat']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c433145(card.Card):
    "Hedron Archive"
    def __init__(self):
        super(c433145, self).__init__(gameobject.Characteristics(**{'name': 'Hedron Archive', 'text': '{T}: Add {C}{C} to your mana pool.\n{2}, {T}, Sacrifice Hedron Archive: Draw two cards.', 'color': '', 'mana_cost': '4'}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c420686(card.Card):
    "Mentor of the Meek"
    def __init__(self):
        super(c420686, self).__init__(gameobject.Characteristics(**{'name': 'Mentor of the Meek', 'text': 'Whenever another creature with power 2 or less enters the battlefield under your control, you may pay {1}. If you do, draw a card.', 'color': ['W'], 'mana_cost': '2W', 'power': 2, 'toughness': 2, 'subtype': ['Human', 'Soldier']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c420718(card.Card):
    "Treasure Cruise"
    def __init__(self):
        super(c420718, self).__init__(gameobject.Characteristics(**{'name': 'Treasure Cruise', 'text': 'Delve (Each card you exile from your graveyard while casting this spell pays for {1}.)\nDraw three cards.', 'color': ['U'], 'mana_cost': '7U'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c420736(card.Card):
    "Alesha, Who Smiles at Death"
    def __init__(self):
        super(c420736, self).__init__(gameobject.Characteristics(**{'name': 'Alesha, Who Smiles at Death', 'text': 'First strike\nWhenever Alesha, Who Smiles at Death attacks, you may pay {W/B}{W/B}. If you do, return target creature card with power 2 or less from your graveyard to the battlefield tapped and attacking.', 'color': ['R', 'W', 'B'], 'mana_cost': '2R', 'power': 3, 'toughness': 2, 'subtype': ['Human', 'Warrior']}, supertype=[cardtype.SuperType.LEGENDARY], types=[cardtype.CardType.CREATURE], abilities=[]))

class c420764(card.Card):
    "Den Protector"
    def __init__(self):
        super(c420764, self).__init__(gameobject.Characteristics(**{'name': 'Den Protector', 'text': "Creatures with power less than Den Protector's power can't block it.\nMegamorph {1}{G} (You may cast this card face down as a 2/2 creature for {3}. Turn it face up any time for its megamorph cost and put a +1/+1 counter on it.)\nWhen Den Protector is turned face up, return target card from your graveyard to your hand.", 'color': ['G'], 'mana_cost': '1G', 'power': 2, 'toughness': 1, 'subtype': ['Human', 'Warrior']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c420854(card.Card):
    "Thopter Foundry"
    def __init__(self):
        super(c420854, self).__init__(gameobject.Characteristics(**{'name': 'Thopter Foundry', 'text': '{1}, Sacrifice a nontoken artifact: Create a 1/1 blue Thopter artifact creature token with flying. You gain 1 life.', 'color': ['W', 'U', 'B'], 'mana_cost': 'W/BU'}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c420880(card.Card):
    "Myr Battlesphere"
    def __init__(self):
        super(c420880, self).__init__(gameobject.Characteristics(**{'name': 'Myr Battlesphere', 'text': 'When Myr Battlesphere enters the battlefield, create four 1/1 colorless Myr artifact creature tokens.\nWhenever Myr Battlesphere attacks, you may tap X untapped Myr you control. If you do, Myr Battlesphere gets +X/+0 until end of turn and deals X damage to defending player.', 'color': '', 'mana_cost': '7', 'power': 4, 'toughness': 7, 'subtype': ['Myr', 'Construct']}, supertype=[], types=[cardtype.CardType.ARTIFACT, cardtype.CardType.CREATURE], abilities=[]))

class c420886(card.Card):
    "Shimmer Myr"
    def __init__(self):
        super(c420886, self).__init__(gameobject.Characteristics(**{'name': 'Shimmer Myr', 'text': 'Flash\nYou may cast artifact spells as though they had flash.', 'color': '', 'mana_cost': '3', 'power': 2, 'toughness': 2, 'subtype': ['Myr']}, supertype=[], types=[cardtype.CardType.ARTIFACT, cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Flash]))

class c420909(card.Card):
    "Dragonskull Summit"
    def __init__(self):
        super(c420909, self).__init__(gameobject.Characteristics(**{'name': 'Dragonskull Summit', 'text': 'Dragonskull Summit enters the battlefield tapped unless you control a Swamp or a Mountain.\n{T}: Add {B} or {R} to your mana pool.', 'color': ['B', 'R'], 'mana_cost': ''}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c420922(card.Card):
    "Karplusan Forest"
    def __init__(self):
        super(c420922, self).__init__(gameobject.Characteristics(**{'name': 'Karplusan Forest', 'text': '{T}: Add {C} to your mana pool.\n{T}: Add {R} or {G} to your mana pool. Karplusan Forest deals 1 damage to you.', 'color': ['R', 'G'], 'mana_cost': ''}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c420946(card.Card):
    "Sunpetal Grove"
    def __init__(self):
        super(c420946, self).__init__(gameobject.Characteristics(**{'name': 'Sunpetal Grove', 'text': 'Sunpetal Grove enters the battlefield tapped unless you control a Forest or a Plains.\n{T}: Add {G} or {W} to your mana pool.', 'color': ['G', 'W'], 'mana_cost': ''}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c420952(card.Card):
    "Underground River"
    def __init__(self):
        super(c420952, self).__init__(gameobject.Characteristics(**{'name': 'Underground River', 'text': '{T}: Add {C} to your mana pool.\n{T}: Add {U} or {B} to your mana pool. Underground River deals 1 damage to you.', 'color': ['U', 'B'], 'mana_cost': ''}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c405126(card.Card):
    "Angel of Serenity"
    def __init__(self):
        super(c405126, self).__init__(gameobject.Characteristics(**{'name': 'Angel of Serenity', 'text': "Flying\nWhen Angel of Serenity enters the battlefield, you may exile up to three other target creatures from the battlefield and/or creature cards from graveyards.\nWhen Angel of Serenity leaves the battlefield, return the exiled cards to their owners' hands.", 'color': ['W'], 'mana_cost': '4WWW', 'power': 5, 'toughness': 6, 'subtype': ['Angel']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Flying]))

class c405262(card.Card):
    "Inferno Titan"
    def __init__(self):
        super(c405262, self).__init__(gameobject.Characteristics(**{'name': 'Inferno Titan', 'text': '{R}: Inferno Titan gets +1/+0 until end of turn.\nWhenever Inferno Titan enters the battlefield or attacks, it deals 3 damage divided as you choose among one, two, or three target creatures and/or players.', 'color': ['R'], 'mana_cost': '4RR', 'power': 6, 'toughness': 6, 'subtype': ['Giant']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c389515(card.Card):
    "Feldon of the Third Path"
    def __init__(self):
        super(c389515, self).__init__(gameobject.Characteristics(**{'name': 'Feldon of the Third Path', 'text': "{2}{R}, {T}: Create a token that's a copy of target creature card in your graveyard, except it's an artifact in addition to its other types. It gains haste. Sacrifice it at the beginning of the next end step.", 'color': ['R'], 'mana_cost': '1RR', 'power': 2, 'toughness': 3, 'subtype': ['Human', 'Artificer']}, supertype=[cardtype.SuperType.LEGENDARY], types=[cardtype.CardType.CREATURE], abilities=[]))

class c389422(card.Card):
    "Abyssal Persecutor"
    def __init__(self):
        super(c389422, self).__init__(gameobject.Characteristics(**{'name': 'Abyssal Persecutor', 'text': "Flying, trample\nYou can't win the game and your opponents can't lose the game.", 'color': ['B'], 'mana_cost': '2BB', 'power': 6, 'toughness': 6, 'subtype': ['Demon']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Flying, static_abilities.StaticAbilities.Trample]))

class c389474(card.Card):
    "Crypt Ghast"
    def __init__(self):
        super(c389474, self).__init__(gameobject.Characteristics(**{'name': 'Crypt Ghast', 'text': 'Extort (Whenever you cast a spell, you may pay {W/B}. If you do, each opponent loses 1 life and you gain that much life.)\nWhenever you tap a Swamp for mana, add {B} to your mana pool (in addition to the mana the land produces).', 'color': ['B'], 'mana_cost': '3B', 'power': 2, 'toughness': 2, 'subtype': ['Spirit']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c389540(card.Card):
    "Grave Titan"
    def __init__(self):
        super(c389540, self).__init__(gameobject.Characteristics(**{'name': 'Grave Titan', 'text': 'Deathtouch\nWhenever Grave Titan enters the battlefield or attacks, create two 2/2 black Zombie creature tokens.', 'color': ['B'], 'mana_cost': '4BB', 'power': 6, 'toughness': 6, 'subtype': ['Giant']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Deathtouch]))

class c389541(card.Card):
    "Gray Merchant of Asphodel"
    def __init__(self):
        super(c389541, self).__init__(gameobject.Characteristics(**{'name': 'Gray Merchant of Asphodel', 'text': 'When Gray Merchant of Asphodel enters the battlefield, each opponent loses X life, where X is your devotion to black. You gain life equal to the life lost this way. (Each {B} in the mana costs of permanents you control counts toward your devotion to black.)', 'color': ['B'], 'mana_cost': '3BB', 'power': 2, 'toughness': 4, 'subtype': ['Zombie']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c389675(card.Card):
    "Skirsdag High Priest"
    def __init__(self):
        super(c389675, self).__init__(gameobject.Characteristics(**{'name': 'Skirsdag High Priest', 'text': 'Morbid — {T}, Tap two untapped creatures you control: Create a 5/5 black Demon creature token with flying. Activate this ability only if a creature died this turn.', 'color': ['B'], 'mana_cost': '1B', 'power': 1, 'toughness': 2, 'subtype': ['Human', 'Cleric']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c389537(card.Card):
    "Goblin Welder"
    def __init__(self):
        super(c389537, self).__init__(gameobject.Characteristics(**{'name': 'Goblin Welder', 'text': "{T}: Choose target artifact a player controls and target artifact card in that player's graveyard. If both targets are still legal as this ability resolves, that player simultaneously sacrifices the artifact and returns the artifact card to the battlefield.", 'color': ['R'], 'mana_cost': 'R', 'power': 1, 'toughness': 1, 'subtype': ['Goblin', 'Artificer']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c389575(card.Card):
    "Lashwrithe"
    def __init__(self):
        super(c389575, self).__init__(gameobject.Characteristics(**{'name': 'Lashwrithe', 'text': 'Living weapon (When this Equipment enters the battlefield, create a 0/0 black Germ creature token, then attach this to it.)\nEquipped creature gets +1/+1 for each Swamp you control.\nEquip {B/P}{B/P} ({B/P} can be paid with either {B} or 2 life.)', 'color': ['B'], 'mana_cost': '4', 'subtype': ['Equipment']}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c376439(card.Card):
    "Ophiomancer"
    def __init__(self):
        super(c376439, self).__init__(gameobject.Characteristics(**{'name': 'Ophiomancer', 'text': 'At the beginning of each upkeep, if you control no Snakes, create a 1/1 black Snake creature token with deathtouch.', 'color': ['B'], 'mana_cost': '2B', 'power': 2, 'toughness': 2, 'subtype': ['Human', 'Shaman']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c376546(card.Card):
    "Tempt with Vengeance"
    def __init__(self):
        super(c376546, self).__init__(gameobject.Characteristics(**{'name': 'Tempt with Vengeance', 'text': 'Tempting offer — Create X 1/1 red Elemental creature tokens with haste. Each opponent may create X 1/1 red Elemental creature tokens with haste. For each player who does, create X 1/1 red Elemental creature tokens with haste.', 'color': ['R'], 'mana_cost': 'XR'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c430556(card.Card):
    "Odric, Master Tactician"
    def __init__(self):
        super(c430556, self).__init__(gameobject.Characteristics(**{'name': 'Odric, Master Tactician', 'text': 'First strike (This creature deals combat damage before creatures without first strike.)\nWhenever Odric, Master Tactician and at least three other creatures attack, you choose which creatures block this combat and how those creatures block.', 'color': ['W'], 'mana_cost': '2WW', 'power': 3, 'toughness': 4, 'subtype': ['Human', 'Soldier']}, supertype=[cardtype.SuperType.LEGENDARY], types=[cardtype.CardType.CREATURE], abilities=[]))

class c430633(card.Card):
    "Drowned Catacomb"
    def __init__(self):
        super(c430633, self).__init__(gameobject.Characteristics(**{'name': 'Drowned Catacomb', 'text': 'Drowned Catacomb enters the battlefield tapped unless you control an Island or a Swamp.\n{T}: Add {U} or {B} to your mana pool.', 'color': ['U', 'B'], 'mana_cost': ''}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c220476(card.Card):
    "Cemetery Reaper"
    def __init__(self):
        super(c220476, self).__init__(gameobject.Characteristics(**{'name': 'Cemetery Reaper', 'text': 'Other Zombie creatures you control get +1/+1.\n{2}{B}, {T}: Exile target creature card from a graveyard. Create a 2/2 black Zombie creature token.', 'color': ['B'], 'mana_cost': '1BB', 'power': 2, 'toughness': 2, 'subtype': ['Zombie']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c186309(card.Card):
    "Day of Judgment"
    def __init__(self):
        super(c186309, self).__init__(gameobject.Characteristics(**{'name': 'Day of Judgment', 'text': 'Destroy all creatures.', 'color': ['W'], 'mana_cost': '2WW'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c192230(card.Card):
    "Bloodghast"
    def __init__(self):
        super(c192230, self).__init__(gameobject.Characteristics(**{'name': 'Bloodghast', 'text': "Bloodghast can't block.\nBloodghast has haste as long as an opponent has 10 or less life.\nLandfall — Whenever a land enters the battlefield under your control, you may return Bloodghast from your graveyard to the battlefield.", 'color': ['B'], 'mana_cost': 'BB', 'power': 2, 'toughness': 1, 'subtype': ['Vampire', 'Spirit']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c185749(card.Card):
    "Lotus Cobra"
    def __init__(self):
        super(c185749, self).__init__(gameobject.Characteristics(**{'name': 'Lotus Cobra', 'text': 'Landfall — Whenever a land enters the battlefield under your control, you may add one mana of any color to your mana pool.', 'color': ['G'], 'mana_cost': '1G', 'power': 2, 'toughness': 1, 'subtype': ['Snake']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c198383(card.Card):
    "Stoneforge Mystic"
    def __init__(self):
        super(c198383, self).__init__(gameobject.Characteristics(**{'name': 'Stoneforge Mystic', 'text': 'When Stoneforge Mystic enters the battlefield, you may search your library for an Equipment card, reveal it, put it into your hand, then shuffle your library.\n{1}{W}, {T}: You may put an Equipment card from your hand onto the battlefield.', 'color': ['W'], 'mana_cost': '1W', 'power': 1, 'toughness': 2, 'subtype': ['Kor', 'Artificer']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c197854(card.Card):
    "Dragonmaster Outcast"
    def __init__(self):
        super(c197854, self).__init__(gameobject.Characteristics(**{'name': 'Dragonmaster Outcast', 'text': 'At the beginning of your upkeep, if you control six or more lands, create a 5/5 red Dragon creature token with flying.', 'color': ['R'], 'mana_cost': 'R', 'power': 1, 'toughness': 1, 'subtype': ['Human', 'Shaman']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c177545(card.Card):
    "Celestial Colonnade"
    def __init__(self):
        super(c177545, self).__init__(gameobject.Characteristics(**{'name': 'Celestial Colonnade', 'text': "Celestial Colonnade enters the battlefield tapped.\n{T}: Add {W} or {U} to your mana pool.\n{3}{W}{U}: Until end of turn, Celestial Colonnade becomes a 4/4 white and blue Elemental creature with flying and vigilance. It's still a land.", 'color': ['W', 'U'], 'mana_cost': ''}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c12418(card.Card):
    "Avalanche Riders"
    def __init__(self):
        super(c12418, self).__init__(gameobject.Characteristics(**{'name': 'Avalanche Riders', 'text': 'Haste\nEcho {3}{R} (At the beginning of your upkeep, if this came under your control since the beginning of your last upkeep, sacrifice it unless you pay its echo cost.)\nWhen Avalanche Riders enters the battlefield, destroy target land.', 'color': ['R'], 'mana_cost': '3R', 'power': 2, 'toughness': 2, 'subtype': ['Human', 'Nomad']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Haste]))

class c118918(card.Card):
    "Looter il-Kor"
    def __init__(self):
        super(c118918, self).__init__(gameobject.Characteristics(**{'name': 'Looter il-Kor', 'text': 'Shadow (This creature can block or be blocked by only creatures with shadow.)\nWhenever Looter il-Kor deals damage to an opponent, draw a card, then discard a card.', 'color': ['U'], 'mana_cost': '1U', 'power': 1, 'toughness': 1, 'subtype': ['Kor', 'Rogue']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c397562(card.Card):
    "Coffin Queen"
    def __init__(self):
        super(c397562, self).__init__(gameobject.Characteristics(**{'name': 'Coffin Queen', 'text': 'You may choose not to untap Coffin Queen during your untap step.\n{2}{B}, {T}: Put target creature card from a graveyard onto the battlefield under your control. When Coffin Queen becomes untapped or you lose control of Coffin Queen, exile that creature.', 'color': ['B'], 'mana_cost': '2B', 'power': 1, 'toughness': 1, 'subtype': ['Zombie', 'Wizard']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c373529(card.Card):
    "Soldier of the Pantheon"
    def __init__(self):
        super(c373529, self).__init__(gameobject.Characteristics(**{'name': 'Soldier of the Pantheon', 'text': 'Protection from multicolored\nWhenever an opponent casts a multicolored spell, you gain 1 life.', 'color': ['W'], 'mana_cost': 'W', 'power': 2, 'toughness': 1, 'subtype': ['Human', 'Soldier']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c373717(card.Card):
    "Spear of Heliod"
    def __init__(self):
        super(c373717, self).__init__(gameobject.Characteristics(**{'name': 'Spear of Heliod', 'text': 'Creatures you control get +1/+1.\n{1}{W}{W}, {T}: Destroy target creature that dealt damage to you this turn.', 'color': ['W'], 'mana_cost': '1WW'}, supertype=[cardtype.SuperType.LEGENDARY], types=[cardtype.CardType.ENCHANTMENT, cardtype.CardType.ARTIFACT], abilities=[]))

class c373661(card.Card):
    "Abhorrent Overlord"
    def __init__(self):
        super(c373661, self).__init__(gameobject.Characteristics(**{'name': 'Abhorrent Overlord', 'text': 'Flying\nWhen Abhorrent Overlord enters the battlefield, create a number of 1/1 black Harpy creature tokens with flying equal to your devotion to black. (Each {B} in the mana costs of permanents you control counts toward your devotion to black.)\nAt the beginning of your upkeep, sacrifice a creature.', 'color': ['B'], 'mana_cost': '5BB', 'power': 6, 'toughness': 6, 'subtype': ['Demon']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Flying]))

class c373575(card.Card):
    "Hero's Downfall"
    def __init__(self):
        super(c373575, self).__init__(gameobject.Characteristics(**{'name': "Hero's Downfall", 'text': 'Destroy target creature or planeswalker.', 'color': ['B'], 'mana_cost': '1BB'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c373604(card.Card):
    "Anger of the Gods"
    def __init__(self):
        super(c373604, self).__init__(gameobject.Characteristics(**{'name': 'Anger of the Gods', 'text': 'Anger of the Gods deals 3 damage to each creature. If a creature dealt damage this way would die this turn, exile it instead.', 'color': ['R'], 'mana_cost': '1RR'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c373552(card.Card):
    "Firedrinker Satyr"
    def __init__(self):
        super(c373552, self).__init__(gameobject.Characteristics(**{'name': 'Firedrinker Satyr', 'text': 'Whenever Firedrinker Satyr is dealt damage, it deals that much damage to you.\n{1}{R}: Firedrinker Satyr gets +1/+0 until end of turn and deals 1 damage to you.', 'color': ['R'], 'mana_cost': 'R', 'power': 2, 'toughness': 1, 'subtype': ['Satyr', 'Shaman']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c373624(card.Card):
    "Sylvan Caryatid"
    def __init__(self):
        super(c373624, self).__init__(gameobject.Characteristics(**{'name': 'Sylvan Caryatid', 'text': 'Defender, hexproof\n{T}: Add one mana of any color to your mana pool.', 'color': ['G'], 'mana_cost': '1G', 'power': 0, 'toughness': 3, 'subtype': ['Plant']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Defender, static_abilities.StaticAbilities.Hexproof]))

class c373500(card.Card):
    "Ashiok, Nightmare Weaver"
    def __init__(self):
        super(c373500, self).__init__(gameobject.Characteristics(**{'name': 'Ashiok, Nightmare Weaver', 'text': "+2: Exile the top three cards of target opponent's library.\n−X: Put a creature card with converted mana cost X exiled with Ashiok, Nightmare Weaver onto the battlefield under your control. That creature is a Nightmare in addition to its other types.\n−10: Exile all cards from all opponents' hands and graveyards.", 'color': ['U', 'B'], 'mana_cost': '1UB', 'subtype': ['Ashiok']}, supertype=[], types=[cardtype.CardType.PLANESWALKER], abilities=[]))

class c373635(card.Card):
    "Prophet of Kruphix"
    def __init__(self):
        super(c373635, self).__init__(gameobject.Characteristics(**{'name': 'Prophet of Kruphix', 'text': "Untap all creatures and lands you control during each other player's untap step.\nYou may cast creature spells as though they had flash.", 'color': ['U', 'G'], 'mana_cost': '3GU', 'power': 2, 'toughness': 3, 'subtype': ['Human', 'Wizard']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c373502(card.Card):
    "Xenagos, the Reveler"
    def __init__(self):
        super(c373502, self).__init__(gameobject.Characteristics(**{'name': 'Xenagos, the Reveler', 'text': '+1: Add X mana in any combination of {R} and/or {G} to your mana pool, where X is the number of creatures you control.\n0: Create a 2/2 red and green Satyr creature token with haste.\n−6: Exile the top seven cards of your library. You may put any number of creature and/or land cards from among them onto the battlefield.', 'color': ['R', 'G'], 'mana_cost': '2RG', 'subtype': ['Xenagos']}, supertype=[], types=[cardtype.CardType.PLANESWALKER], abilities=[]))

class c207884(card.Card):
    "Grand Architect"
    def __init__(self):
        super(c207884, self).__init__(gameobject.Characteristics(**{'name': 'Grand Architect', 'text': 'Other blue creatures you control get +1/+1.\n{U}: Target artifact creature becomes blue until end of turn.\nTap an untapped blue creature you control: Add {C}{C} to your mana pool. Spend this mana only to cast artifact spells or activate abilities of artifacts.', 'color': ['U'], 'mana_cost': '1UU', 'power': 1, 'toughness': 3, 'subtype': ['Vedalken', 'Artificer']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c204958(card.Card):
    "Skinrender"
    def __init__(self):
        super(c204958, self).__init__(gameobject.Characteristics(**{'name': 'Skinrender', 'text': 'When Skinrender enters the battlefield, put three -1/-1 counters on target creature.', 'color': ['B'], 'mana_cost': '2BB', 'power': 3, 'toughness': 3, 'subtype': ['Zombie']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c209044(card.Card):
    "Mindslaver"
    def __init__(self):
        super(c209044, self).__init__(gameobject.Characteristics(**{'name': 'Mindslaver', 'text': "{4}, {T}, Sacrifice Mindslaver: You control target player during that player's next turn. (You see all cards that player could see and make all decisions for the player.)", 'color': '', 'mana_cost': '6'}, supertype=[cardtype.SuperType.LEGENDARY], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c409784(card.Card):
    "Thraben Inspector"
    def __init__(self):
        super(c409784, self).__init__(gameobject.Characteristics(**{'name': 'Thraben Inspector', 'text': 'When Thraben Inspector enters the battlefield, investigate. (Create a colorless Clue artifact token with "{2}, Sacrifice this artifact: Draw a card.")', 'color': ['W'], 'mana_cost': 'W', 'power': 1, 'toughness': 2, 'subtype': ['Human', 'Soldier']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c409831(card.Card):
    "Startled Awake"
    def __init__(self):
        super(c409831, self).__init__(gameobject.Characteristics(**{'name': 'Startled Awake', 'text': 'Target opponent puts the top thirteen cards of his or her library into his or her graveyard.\n{3}{U}{U}: Put Startled Awake from your graveyard onto the battlefield transformed. Activate this ability only any time you could cast a sorcery.', 'color': ['U'], 'mana_cost': '2UU'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c409836(card.Card):
    "Thing in the Ice"
    def __init__(self):
        super(c409836, self).__init__(gameobject.Characteristics(**{'name': 'Thing in the Ice', 'text': 'Defender\nThing in the Ice enters the battlefield with four ice counters on it.\nWhenever you cast an instant or sorcery spell, remove an ice counter from Thing in the Ice. Then if it has no ice counters on it, transform it.', 'color': ['U'], 'mana_cost': '1U', 'power': 0, 'toughness': 4, 'subtype': ['Horror']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Defender]))

class c409855(card.Card):
    "Elusive Tormentor"
    def __init__(self):
        super(c409855, self).__init__(gameobject.Characteristics(**{'name': 'Elusive Tormentor', 'text': '{1}, Discard a card: Transform Elusive Tormentor.', 'color': ['U', 'B'], 'mana_cost': '2BB', 'power': 4, 'toughness': 4, 'subtype': ['Vampire', 'Wizard']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c409907(card.Card):
    "Falkenrath Gorger"
    def __init__(self):
        super(c409907, self).__init__(gameobject.Characteristics(**{'name': 'Falkenrath Gorger', 'text': "Each Vampire creature card you own that isn't on the battlefield has madness. The madness cost is equal to its mana cost. (If you discard a card with madness, discard it into exile. When you do, cast it for its madness cost or put it into your graveyard.)", 'color': ['R'], 'mana_cost': 'R', 'power': 2, 'toughness': 1, 'subtype': ['Vampire', 'Berserker']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c409997(card.Card):
    "Tireless Tracker"
    def __init__(self):
        super(c409997, self).__init__(gameobject.Characteristics(**{'name': 'Tireless Tracker', 'text': 'Whenever a land enters the battlefield under your control, investigate. (Create a colorless Clue artifact token with "{2}, Sacrifice this artifact: Draw a card.")\nWhenever you sacrifice a Clue, put a +1/+1 counter on Tireless Tracker.', 'color': ['G'], 'mana_cost': '2G', 'power': 3, 'toughness': 2, 'subtype': ['Human', 'Scout']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c409998(card.Card):
    "Traverse the Ulvenwald"
    def __init__(self):
        super(c409998, self).__init__(gameobject.Characteristics(**{'name': 'Traverse the Ulvenwald', 'text': 'Search your library for a basic land card, reveal it, put it into your hand, then shuffle your library.\nDelirium — If there are four or more card types among cards in your graveyard, instead search your library for a creature or land card, reveal it, put it into your hand, then shuffle your library.', 'color': ['G'], 'mana_cost': 'G'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c410000(card.Card):
    "Ulvenwald Mysteries"
    def __init__(self):
        super(c410000, self).__init__(gameobject.Characteristics(**{'name': 'Ulvenwald Mysteries', 'text': 'Whenever a nontoken creature you control dies, investigate. (Create a colorless Clue artifact token with "{2}, Sacrifice this artifact: Draw a card.")\nWhenever you sacrifice a Clue, create a 1/1 white Human Soldier creature token.', 'color': ['G'], 'mana_cost': '2G'}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c410006(card.Card):
    "Anguished Unmaking"
    def __init__(self):
        super(c410006, self).__init__(gameobject.Characteristics(**{'name': 'Anguished Unmaking', 'text': 'Exile target nonland permanent. You lose 3 life.', 'color': ['W', 'B'], 'mana_cost': '1WB'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c410032(card.Card):
    "Tamiyo's Journal"
    def __init__(self):
        super(c410032, self).__init__(gameobject.Characteristics(**{'name': "Tamiyo's Journal", 'text': 'At the beginning of your upkeep, investigate. (Create a colorless Clue artifact token with "{2}, Sacrifice this artifact: Draw a card.")\n{T}, Sacrifice three Clues: Search your library for a card and put that card into your hand. Then shuffle your library.', 'color': '', 'mana_cost': '5'}, supertype=[cardtype.SuperType.LEGENDARY], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c410049(card.Card):
    "Westvale Abbey"
    def __init__(self):
        super(c410049, self).__init__(gameobject.Characteristics(**{'name': 'Westvale Abbey', 'text': '{T}: Add {C} to your mana pool.\n{5}, {T}, Pay 1 life: Create a 1/1 white and black Human Cleric creature token.\n{5}, {T}, Sacrifice five creatures: Transform Westvale Abbey, then untap it.', 'color': ['B'], 'mana_cost': ''}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c253624(card.Card):
    "Pack Rat"
    def __init__(self):
        super(c253624, self).__init__(gameobject.Characteristics(**{'name': 'Pack Rat', 'text': "Pack Rat's power and toughness are each equal to the number of Rats you control.\n{2}{B}, Discard a card: Create a token that's a copy of Pack Rat.", 'color': ['B'], 'mana_cost': '1B', 'power': '*', 'toughness': '*', 'subtype': ['Rat']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c253538(card.Card):
    "Ultimate Price"
    def __init__(self):
        super(c253538, self).__init__(gameobject.Characteristics(**{'name': 'Ultimate Price', 'text': 'Destroy target monocolored creature.', 'color': ['B'], 'mana_cost': '1B'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c270356(card.Card):
    "Detention Sphere"
    def __init__(self):
        super(c270356, self).__init__(gameobject.Characteristics(**{'name': 'Detention Sphere', 'text': "When Detention Sphere enters the battlefield, you may exile target nonland permanent not named Detention Sphere and all other permanents with the same name as that permanent.\nWhen Detention Sphere leaves the battlefield, return the exiled cards to the battlefield under their owner's control.", 'color': ['W', 'U'], 'mana_cost': '1WU'}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c253596(card.Card):
    "Rakdos Cackler"
    def __init__(self):
        super(c253596, self).__init__(gameobject.Characteristics(**{'name': 'Rakdos Cackler', 'text': "Unleash (You may have this creature enter the battlefield with a +1/+1 counter on it. It can't block as long as it has a +1/+1 counter on it.)", 'color': ['B', 'R'], 'mana_cost': 'B/R', 'power': 1, 'toughness': 1, 'subtype': ['Devil']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c193462(card.Card):
    "Joraga Treespeaker"
    def __init__(self):
        super(c193462, self).__init__(gameobject.Characteristics(**{'name': 'Joraga Treespeaker', 'text': 'Level up {1}{G} ({1}{G}: Put a level counter on this. Level up only as a sorcery.)\nLEVEL 1-4\n1/2\n{T}: Add {G}{G} to your mana pool.\nLEVEL 5+\n1/4\nElves you control have "{T}: Add {G}{G} to your mana pool."', 'color': ['G'], 'mana_cost': 'G', 'power': 1, 'toughness': 1, 'subtype': ['Elf', 'Druid']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c89064(card.Card):
    "Chord of Calling"
    def __init__(self):
        super(c89064, self).__init__(gameobject.Characteristics(**{'name': 'Chord of Calling', 'text': "Convoke (Your creatures can help cast this spell. Each creature you tap while casting this spell pays for {1} or one mana of that creature's color.)\nSearch your library for a creature card with converted mana cost X or less and put it onto the battlefield. Then shuffle your library.", 'color': ['G'], 'mana_cost': 'XGGG'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[static_abilities.StaticAbilities.Convoke]))

class c398428(card.Card):
    "Kytheon, Hero of Akros"
    def __init__(self):
        super(c398428, self).__init__(gameobject.Characteristics(**{'name': 'Kytheon, Hero of Akros', 'text': "At end of combat, if Kytheon, Hero of Akros and at least two other creatures attacked this combat, exile Kytheon, then return him to the battlefield transformed under his owner's control.\n{2}{W}: Kytheon gains indestructible until end of turn.", 'color': ['W'], 'mana_cost': 'W', 'power': 2, 'toughness': 1, 'subtype': ['Human', 'Soldier']}, supertype=[cardtype.SuperType.LEGENDARY], types=[cardtype.CardType.CREATURE], abilities=[]))

class c398476(card.Card):
    "Relic Seeker"
    def __init__(self):
        super(c398476, self).__init__(gameobject.Characteristics(**{'name': 'Relic Seeker', 'text': "Renown 1 (When this creature deals combat damage to a player, if it isn't renowned, put a +1/+1 counter on it and it becomes renowned.)\nWhen Relic Seeker becomes renowned, you may search your library for an Equipment card, reveal it, put it into your hand, then shuffle your library.", 'color': ['W'], 'mana_cost': '1W', 'power': 2, 'toughness': 2, 'subtype': ['Human', 'Soldier']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c398520(card.Card):
    "Sphinx's Tutelage"
    def __init__(self):
        super(c398520, self).__init__(gameobject.Characteristics(**{'name': "Sphinx's Tutelage", 'text': "Whenever you draw a card, target opponent puts the top two cards of his or her library into his or her graveyard. If they're both nonland cards that share a color, repeat this process.\n{5}{U}: Draw a card, then discard a card.", 'color': ['U'], 'mana_cost': '2U'}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c398519(card.Card):
    "Thopter Spy Network"
    def __init__(self):
        super(c398519, self).__init__(gameobject.Characteristics(**{'name': 'Thopter Spy Network', 'text': 'At the beginning of your upkeep, if you control an artifact, create a 1/1 colorless Thopter artifact creature token with flying.\nWhenever one or more artifact creatures you control deal combat damage to a player, draw a card.', 'color': ['U'], 'mana_cost': '2UU'}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c398410(card.Card):
    "Whirler Rogue"
    def __init__(self):
        super(c398410, self).__init__(gameobject.Characteristics(**{'name': 'Whirler Rogue', 'text': "When Whirler Rogue enters the battlefield, create two 1/1 colorless Thopter artifact creature tokens with flying.\nTap two untapped artifacts you control: Target creature can't be blocked this turn.", 'color': ['U'], 'mana_cost': '2UU', 'power': 2, 'toughness': 2, 'subtype': ['Human', 'Rogue', 'Artificer']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c398495(card.Card):
    "Gilt-Leaf Winnower"
    def __init__(self):
        super(c398495, self).__init__(gameobject.Characteristics(**{'name': 'Gilt-Leaf Winnower', 'text': "Menace (This creature can't be blocked except by two or more creatures.)\nWhen Gilt-Leaf Winnower enters the battlefield, you may destroy target non-Elf creature whose power and toughness aren't equal.", 'color': ['B'], 'mana_cost': '3BB', 'power': 4, 'toughness': 3, 'subtype': ['Elf', 'Warrior']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Menace]))

class c398411(card.Card):
    "Abbot of Keral Keep"
    def __init__(self):
        super(c398411, self).__init__(gameobject.Characteristics(**{'name': 'Abbot of Keral Keep', 'text': 'Prowess (Whenever you cast a noncreature spell, this creature gets +1/+1 until end of turn.)\nWhen Abbot of Keral Keep enters the battlefield, exile the top card of your library. Until end of turn, you may play that card.', 'color': ['R'], 'mana_cost': '1R', 'power': 2, 'toughness': 1, 'subtype': ['Human', 'Monk']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c398453(card.Card):
    "Pia and Kiran Nalaar"
    def __init__(self):
        super(c398453, self).__init__(gameobject.Characteristics(**{'name': 'Pia and Kiran Nalaar', 'text': 'When Pia and Kiran Nalaar enters the battlefield, create two 1/1 colorless Thopter artifact creature tokens with flying.\n{2}{R}, Sacrifice an artifact: Pia and Kiran Nalaar deals 2 damage to target creature or player.', 'color': ['R'], 'mana_cost': '2RR', 'power': 2, 'toughness': 2, 'subtype': ['Human', 'Artificer']}, supertype=[cardtype.SuperType.LEGENDARY], types=[cardtype.CardType.CREATURE], abilities=[]))

class c398514(card.Card):
    "Thopter Engineer"
    def __init__(self):
        super(c398514, self).__init__(gameobject.Characteristics(**{'name': 'Thopter Engineer', 'text': 'When Thopter Engineer enters the battlefield, create a 1/1 colorless Thopter artifact creature token with flying.\nArtifact creatures you control have haste. (They can attack and {T} as soon as they come under your control.)', 'color': ['R'], 'mana_cost': '2R', 'power': 1, 'toughness': 3, 'subtype': ['Human', 'Artificer']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c398573(card.Card):
    "Evolutionary Leap"
    def __init__(self):
        super(c398573, self).__init__(gameobject.Characteristics(**{'name': 'Evolutionary Leap', 'text': '{G}, Sacrifice a creature: Reveal cards from the top of your library until you reveal a creature card. Put that card into your hand and the rest on the bottom of your library in a random order.', 'color': ['G'], 'mana_cost': '1G'}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c398511(card.Card):
    "Woodland Bellower"
    def __init__(self):
        super(c398511, self).__init__(gameobject.Characteristics(**{'name': 'Woodland Bellower', 'text': 'When Woodland Bellower enters the battlefield, you may search your library for a nonlegendary green creature card with converted mana cost 3 or less, put it onto the battlefield, then shuffle your library.', 'color': ['G'], 'mana_cost': '4GG', 'power': 6, 'toughness': 5, 'subtype': ['Beast']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c398417(card.Card):
    "Battlefield Forge"
    def __init__(self):
        super(c398417, self).__init__(gameobject.Characteristics(**{'name': 'Battlefield Forge', 'text': '{T}: Add {C} to your mana pool.\n{T}: Add {R} or {W} to your mana pool. Battlefield Forge deals 1 damage to you.', 'color': ['R', 'W'], 'mana_cost': ''}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c398444(card.Card):
    "Shivan Reef"
    def __init__(self):
        super(c398444, self).__init__(gameobject.Characteristics(**{'name': 'Shivan Reef', 'text': '{T}: Add {C} to your mana pool.\n{T}: Add {U} or {R} to your mana pool. Shivan Reef deals 1 damage to you.', 'color': ['U', 'R'], 'mana_cost': ''}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c41280(card.Card):
    "Silent Specter"
    def __init__(self):
        super(c41280, self).__init__(gameobject.Characteristics(**{'name': 'Silent Specter', 'text': 'Flying\nWhenever Silent Specter deals combat damage to a player, that player discards two cards.\nMorph {3}{B}{B} (You may cast this card face down as a 2/2 creature for {3}. Turn it face up any time for its morph cost.)', 'color': ['B'], 'mana_cost': '4BB', 'power': 4, 'toughness': 4, 'subtype': ['Specter']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Flying]))

class c407614(card.Card):
    "Chandra, Flamecaller"
    def __init__(self):
        super(c407614, self).__init__(gameobject.Characteristics(**{'name': 'Chandra, Flamecaller', 'text': '+1: Create two 3/1 red Elemental creature tokens with haste. Exile them at the beginning of the next end step.\n0: Discard all the cards in your hand, then draw that many cards plus one.\n−X: Chandra, Flamecaller deals X damage to each creature.', 'color': ['R'], 'mana_cost': '4RR', 'subtype': ['Chandra']}, supertype=[], types=[cardtype.CardType.PLANESWALKER], abilities=[]))

class c407654(card.Card):
    "Sylvan Advocate"
    def __init__(self):
        super(c407654, self).__init__(gameobject.Characteristics(**{'name': 'Sylvan Advocate', 'text': 'Vigilance\nAs long as you control six or more lands, Sylvan Advocate and land creatures you control get +2/+2.', 'color': ['G'], 'mana_cost': '1G', 'power': 2, 'toughness': 3, 'subtype': ['Elf', 'Druid', 'Ally']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Vigilance]))

class c407667(card.Card):
    "Reflector Mage"
    def __init__(self):
        super(c407667, self).__init__(gameobject.Characteristics(**{'name': 'Reflector Mage', 'text': "When Reflector Mage enters the battlefield, return target creature an opponent controls to its owner's hand. That creature's owner can't cast spells with the same name as that creature until your next turn.", 'color': ['W', 'U'], 'mana_cost': '1WU', 'power': 2, 'toughness': 3, 'subtype': ['Human', 'Wizard']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c218043(card.Card):
    "Porcelain Legionnaire"
    def __init__(self):
        super(c218043, self).__init__(gameobject.Characteristics(**{'name': 'Porcelain Legionnaire', 'text': '({W/P} can be paid with either {W} or 2 life.)\nFirst strike', 'color': ['W'], 'mana_cost': '2W/P', 'power': 3, 'toughness': 1, 'subtype': ['Soldier']}, supertype=[], types=[cardtype.CardType.ARTIFACT, cardtype.CardType.CREATURE], abilities=[]))

class c214375(card.Card):
    "Phyrexian Metamorph"
    def __init__(self):
        super(c214375, self).__init__(gameobject.Characteristics(**{'name': 'Phyrexian Metamorph', 'text': "({U/P} can be paid with either {U} or 2 life.)\nYou may have Phyrexian Metamorph enter the battlefield as a copy of any artifact or creature on the battlefield, except it's an artifact in addition to its other types.", 'color': ['U'], 'mana_cost': '3U/P', 'power': 0, 'toughness': 0, 'subtype': ['Shapeshifter']}, supertype=[], types=[cardtype.CardType.ARTIFACT, cardtype.CardType.CREATURE], abilities=[]))

class c218006(card.Card):
    "Birthing Pod"
    def __init__(self):
        super(c218006, self).__init__(gameobject.Characteristics(**{'name': 'Birthing Pod', 'text': "({G/P} can be paid with either {G} or 2 life.)\n{1}{G/P}, {T}, Sacrifice a creature: Search your library for a creature card with converted mana cost equal to 1 plus the sacrificed creature's converted mana cost, put that card onto the battlefield, then shuffle your library. Activate this ability only any time you could cast a sorcery.", 'color': ['G'], 'mana_cost': '3G/P'}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c233055(card.Card):
    "Batterskull"
    def __init__(self):
        super(c233055, self).__init__(gameobject.Characteristics(**{'name': 'Batterskull', 'text': "Living weapon (When this Equipment enters the battlefield, create a 0/0 black Germ creature token, then attach this to it.)\nEquipped creature gets +4/+4 and has vigilance and lifelink.\n{3}: Return Batterskull to its owner's hand.\nEquip {5}", 'color': '', 'mana_cost': '5', 'subtype': ['Equipment']}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c218018(card.Card):
    "Shrine of Burning Rage"
    def __init__(self):
        super(c218018, self).__init__(gameobject.Characteristics(**{'name': 'Shrine of Burning Rage', 'text': 'At the beginning of your upkeep or whenever you cast a red spell, put a charge counter on Shrine of Burning Rage.\n{3}, {T}, Sacrifice Shrine of Burning Rage: Shrine of Burning Rage deals damage equal to the number of charge counters on it to target creature or player.', 'color': '', 'mana_cost': '2'}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c206347(card.Card):
    "Shrine of Loyal Legions"
    def __init__(self):
        super(c206347, self).__init__(gameobject.Characteristics(**{'name': 'Shrine of Loyal Legions', 'text': 'At the beginning of your upkeep or whenever you cast a white spell, put a charge counter on Shrine of Loyal Legions.\n{3}, {T}, Sacrifice Shrine of Loyal Legions: Create a 1/1 colorless Myr artifact creature token for each charge counter on Shrine of Loyal Legions.', 'color': '', 'mana_cost': '2'}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c382189(card.Card):
    "Isolated Chapel"
    def __init__(self):
        super(c382189, self).__init__(gameobject.Characteristics(**{'name': 'Isolated Chapel', 'text': 'Isolated Chapel enters the battlefield tapped unless you control a Plains or a Swamp.\n{T}: Add {W} or {B} to your mana pool.', 'color': ['W', 'B'], 'mana_cost': ''}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c382202(card.Card):
    "Vault of the Archangel"
    def __init__(self):
        super(c382202, self).__init__(gameobject.Characteristics(**{'name': 'Vault of the Archangel', 'text': '{T}: Add {C} to your mana pool.\n{2}{W}{B}, {T}: Creatures you control gain deathtouch and lifelink until end of turn.', 'color': ['W', 'B'], 'mana_cost': ''}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c213818(card.Card):
    "Accorder Paladin"
    def __init__(self):
        super(c213818, self).__init__(gameobject.Characteristics(**{'name': 'Accorder Paladin', 'text': 'Battle cry (Whenever this creature attacks, each other attacking creature gets +1/+0 until end of turn.)', 'color': ['W'], 'mana_cost': '1W', 'power': 3, 'toughness': 1, 'subtype': ['Human', 'Knight']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c214064(card.Card):
    "Hero of Bladehold"
    def __init__(self):
        super(c214064, self).__init__(gameobject.Characteristics(**{'name': 'Hero of Bladehold', 'text': 'Battle cry (Whenever this creature attacks, each other attacking creature gets +1/+0 until end of turn.)\nWhenever Hero of Bladehold attacks, create two 1/1 white Soldier creature tokens that are tapped and attacking.', 'color': ['W'], 'mana_cost': '2WW', 'power': 3, 'toughness': 4, 'subtype': ['Human', 'Knight']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c220589(card.Card):
    "Phyrexian Revoker"
    def __init__(self):
        super(c220589, self).__init__(gameobject.Characteristics(**{'name': 'Phyrexian Revoker', 'text': "As Phyrexian Revoker enters the battlefield, choose a nonland card name.\nActivated abilities of sources with the chosen name can't be activated.", 'color': '', 'mana_cost': '2', 'power': 2, 'toughness': 1, 'subtype': ['Horror']}, supertype=[], types=[cardtype.CardType.ARTIFACT, cardtype.CardType.CREATURE], abilities=[]))

class c383258(card.Card):
    "Goblin Rabblemaster"
    def __init__(self):
        super(c383258, self).__init__(gameobject.Characteristics(**{'name': 'Goblin Rabblemaster', 'text': 'Other Goblin creatures you control attack each turn if able.\nAt the beginning of combat on your turn, create a 1/1 red Goblin creature token with haste.\nWhenever Goblin Rabblemaster attacks, it gets +1/+0 until end of turn for each other attacking Goblin.', 'color': ['R'], 'mana_cost': '2R', 'power': 2, 'toughness': 2, 'subtype': ['Goblin', 'Warrior']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c370770(card.Card):
    "Imposing Sovereign"
    def __init__(self):
        super(c370770, self).__init__(gameobject.Characteristics(**{'name': 'Imposing Sovereign', 'text': 'Creatures your opponents control enter the battlefield tapped.', 'color': ['W'], 'mana_cost': '1W', 'power': 2, 'toughness': 1, 'subtype': ['Human']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c249680(card.Card):
    "Yeva, Nature's Herald"
    def __init__(self):
        super(c249680, self).__init__(gameobject.Characteristics(**{'name': "Yeva, Nature's Herald", 'text': 'Flash (You may cast this spell any time you could cast an instant.)\nYou may cast green creature spells as though they had flash.', 'color': ['G'], 'mana_cost': '2GG', 'power': 4, 'toughness': 4, 'subtype': ['Elf', 'Shaman']}, supertype=[cardtype.SuperType.LEGENDARY], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Flash]))

class c249722(card.Card):
    "Glacial Fortress"
    def __init__(self):
        super(c249722, self).__init__(gameobject.Characteristics(**{'name': 'Glacial Fortress', 'text': 'Glacial Fortress enters the battlefield tapped unless you control a Plains or an Island.\n{T}: Add {W} or {U} to your mana pool.', 'color': ['W', 'U'], 'mana_cost': ''}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c220074(card.Card):
    "Timely Reinforcements"
    def __init__(self):
        super(c220074, self).__init__(gameobject.Characteristics(**{'name': 'Timely Reinforcements', 'text': 'If you have less life than an opponent, you gain 6 life. If you control fewer creatures than an opponent, create three 1/1 white Soldier creature tokens.', 'color': ['W'], 'mana_cost': '2W'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c244313(card.Card):
    "Ponder"
    def __init__(self):
        super(c244313, self).__init__(gameobject.Characteristics(**{'name': 'Ponder', 'text': 'Look at the top three cards of your library, then put them back in any order. You may shuffle your library.\nDraw a card.', 'color': ['U'], 'mana_cost': 'U'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c230764(card.Card):
    "Manic Vandal"
    def __init__(self):
        super(c230764, self).__init__(gameobject.Characteristics(**{'name': 'Manic Vandal', 'text': 'When Manic Vandal enters the battlefield, destroy target artifact.', 'color': ['R'], 'mana_cost': '2R', 'power': 2, 'toughness': 2, 'subtype': ['Human', 'Warrior']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c205059(card.Card):
    "Fauna Shaman"
    def __init__(self):
        super(c205059, self).__init__(gameobject.Characteristics(**{'name': 'Fauna Shaman', 'text': '{G}, {T}, Discard a creature card: Search your library for a creature card, reveal it, and put it into your hand. Then shuffle your library.', 'color': ['G'], 'mana_cost': '1G', 'power': 2, 'toughness': 2, 'subtype': ['Elf', 'Shaman']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c146178(card.Card):
    "Shelldock Isle"
    def __init__(self):
        super(c146178, self).__init__(gameobject.Characteristics(**{'name': 'Shelldock Isle', 'text': 'Hideaway (This land enters the battlefield tapped. When it does, look at the top four cards of your library, exile one face down, then put the rest on the bottom of your library.)\n{T}: Add {U} to your mana pool.\n{U}, {T}: You may play the exiled card without paying its mana cost if a library has twenty or fewer cards in it.', 'color': ['U'], 'mana_cost': ''}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c386660(card.Card):
    "Seeker of the Way"
    def __init__(self):
        super(c386660, self).__init__(gameobject.Characteristics(**{'name': 'Seeker of the Way', 'text': 'Prowess (Whenever you cast a noncreature spell, this creature gets +1/+1 until end of turn.)\nWhenever you cast a noncreature spell, Seeker of the Way gains lifelink until end of turn.', 'color': ['W'], 'mana_cost': '1W', 'power': 2, 'toughness': 2, 'subtype': ['Human', 'Warrior']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c386518(card.Card):
    "Dig Through Time"
    def __init__(self):
        super(c386518, self).__init__(gameobject.Characteristics(**{'name': 'Dig Through Time', 'text': 'Delve (Each card you exile from your graveyard while casting this spell pays for {1}.)\nLook at the top seven cards of your library. Put two of them into your hand and the rest on the bottom of your library in any order.', 'color': ['U'], 'mana_cost': '6UU'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c386494(card.Card):
    "Bloodsoaked Champion"
    def __init__(self):
        super(c386494, self).__init__(gameobject.Characteristics(**{'name': 'Bloodsoaked Champion', 'text': "Bloodsoaked Champion can't block.\nRaid — {1}{B}: Return Bloodsoaked Champion from your graveyard to the battlefield. Activate this ability only if you attacked with a creature this turn.", 'color': ['B'], 'mana_cost': 'B', 'power': 2, 'toughness': 1, 'subtype': ['Human', 'Warrior']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c386548(card.Card):
    "Grim Haruspex"
    def __init__(self):
        super(c386548, self).__init__(gameobject.Characteristics(**{'name': 'Grim Haruspex', 'text': 'Morph {B} (You may cast this card face down as a 2/2 creature for {3}. Turn it face up any time for its morph cost.)\nWhenever another nontoken creature you control dies, draw a card.', 'color': ['B'], 'mana_cost': '2B', 'power': 3, 'toughness': 2, 'subtype': ['Human', 'Wizard']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c386613(card.Card):
    "Murderous Cut"
    def __init__(self):
        super(c386613, self).__init__(gameobject.Characteristics(**{'name': 'Murderous Cut', 'text': 'Delve (Each card you exile from your graveyard while casting this spell pays for {1}.)\nDestroy target creature.', 'color': ['B'], 'mana_cost': '4B'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c386560(card.Card):
    "Hordeling Outburst"
    def __init__(self):
        super(c386560, self).__init__(gameobject.Characteristics(**{'name': 'Hordeling Outburst', 'text': 'Create three 1/1 red Goblin creature tokens.', 'color': ['R'], 'mana_cost': '1RR'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c386608(card.Card):
    "Monastery Swiftspear"
    def __init__(self):
        super(c386608, self).__init__(gameobject.Characteristics(**{'name': 'Monastery Swiftspear', 'text': 'Haste\nProwess (Whenever you cast a noncreature spell, this creature gets +1/+1 until end of turn.)', 'color': ['R'], 'mana_cost': 'R', 'power': 1, 'toughness': 2, 'subtype': ['Human', 'Monk']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Haste]))

class c386562(card.Card):
    "Icefeather Aven"
    def __init__(self):
        super(c386562, self).__init__(gameobject.Characteristics(**{'name': 'Icefeather Aven', 'text': "Flying\nMorph {1}{G}{U} (You may cast this card face down as a 2/2 creature for {3}. Turn it face up any time for its morph cost.)\nWhen Icefeather Aven is turned face up, you may return another target creature to its owner's hand.", 'color': ['U', 'G'], 'mana_cost': 'GU', 'power': 2, 'toughness': 2, 'subtype': ['Bird', 'Shaman']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Flying]))

class c386571(card.Card):
    "Jeskai Ascendancy"
    def __init__(self):
        super(c386571, self).__init__(gameobject.Characteristics(**{'name': 'Jeskai Ascendancy', 'text': 'Whenever you cast a noncreature spell, creatures you control get +1/+1 until end of turn. Untap those creatures.\nWhenever you cast a noncreature spell, you may draw a card. If you do, discard a card.', 'color': ['W', 'U', 'R'], 'mana_cost': 'URW'}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c386631(card.Card):
    "Rakshasa Deathdealer"
    def __init__(self):
        super(c386631, self).__init__(gameobject.Characteristics(**{'name': 'Rakshasa Deathdealer', 'text': '{B}{G}: Rakshasa Deathdealer gets +2/+2 until end of turn.\n{B}{G}: Regenerate Rakshasa Deathdealer.', 'color': ['B', 'G'], 'mana_cost': 'BG', 'power': 2, 'toughness': 2, 'subtype': ['Cat', 'Demon']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c417577(card.Card):
    "Angel of Invention"
    def __init__(self):
        super(c417577, self).__init__(gameobject.Characteristics(**{'name': 'Angel of Invention', 'text': 'Flying, vigilance, lifelink\nFabricate 2 (When this creature enters the battlefield, put two +1/+1 counters on it or create two 1/1 colorless Servo artifact creature tokens.)\nOther creatures you control get +1/+1.', 'color': ['W'], 'mana_cost': '3WW', 'power': 2, 'toughness': 1, 'subtype': ['Angel']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Flying, static_abilities.StaticAbilities.Lifelink, static_abilities.StaticAbilities.Vigilance]))

class c417632(card.Card):
    "Padeem, Consul of Innovation"
    def __init__(self):
        super(c417632, self).__init__(gameobject.Characteristics(**{'name': 'Padeem, Consul of Innovation', 'text': 'Artifacts you control have hexproof.\nAt the beginning of your upkeep, if you control the artifact with the highest converted mana cost or tied for the highest converted mana cost, draw a card.', 'color': ['U'], 'mana_cost': '3U', 'power': 1, 'toughness': 4, 'subtype': ['Vedalken', 'Artificer']}, supertype=[cardtype.SuperType.LEGENDARY], types=[cardtype.CardType.CREATURE], abilities=[]))

class c417752(card.Card):
    "Dovin Baan"
    def __init__(self):
        super(c417752, self).__init__(gameobject.Characteristics(**{'name': 'Dovin Baan', 'text': '+1: Until your next turn, up to one target creature gets -3/-0 and its activated abilities can\'t be activated.\n−1: You gain 2 life and draw a card.\n−7: You get an emblem with "Your opponents can\'t untap more than two permanents during their untap steps."', 'color': ['W', 'U'], 'mana_cost': '2WU', 'subtype': ['Dovin']}, supertype=[], types=[cardtype.CardType.PLANESWALKER], abilities=[]))

class c417757(card.Card):
    "Rashmi, Eternities Crafter"
    def __init__(self):
        super(c417757, self).__init__(gameobject.Characteristics(**{'name': 'Rashmi, Eternities Crafter', 'text': "Whenever you cast your first spell each turn, reveal the top card of your library. If it's a nonland card with converted mana cost less than that spell's, you may cast it without paying its mana cost. If you don't cast the revealed card, put it into your hand.", 'color': ['U', 'G'], 'mana_cost': '2GU', 'power': 2, 'toughness': 3, 'subtype': ['Elf', 'Druid']}, supertype=[cardtype.SuperType.LEGENDARY], types=[cardtype.CardType.CREATURE], abilities=[]))

class c417759(card.Card):
    "Saheeli Rai"
    def __init__(self):
        super(c417759, self).__init__(gameobject.Characteristics(**{'name': 'Saheeli Rai', 'text': "+1: Scry 1. Saheeli Rai deals 1 damage to each opponent.\n−2: Create a token that's a copy of target artifact or creature you control, except it's an artifact in addition to its other types. That token gains haste. Exile it at the beginning of the next end step.\n−7: Search your library for up to three artifact cards with different names, put them onto the battlefield, then shuffle your library.", 'color': ['U', 'R'], 'mana_cost': '1UR', 'subtype': ['Saheeli']}, supertype=[], types=[cardtype.CardType.PLANESWALKER], abilities=[]))

class c417788(card.Card):
    "Foundry Inspector"
    def __init__(self):
        super(c417788, self).__init__(gameobject.Characteristics(**{'name': 'Foundry Inspector', 'text': 'Artifact spells you cast cost {1} less to cast.', 'color': '', 'mana_cost': '3', 'power': 3, 'toughness': 2, 'subtype': ['Construct']}, supertype=[], types=[cardtype.CardType.ARTIFACT, cardtype.CardType.CREATURE], abilities=[]))

class c417795(card.Card):
    "Metalwork Colossus"
    def __init__(self):
        super(c417795, self).__init__(gameobject.Characteristics(**{'name': 'Metalwork Colossus', 'text': 'Metalwork Colossus costs {X} less to cast, where X is the total converted mana cost of noncreature artifacts you control.\nSacrifice two artifacts: Return Metalwork Colossus from your graveyard to your hand.', 'color': '', 'mana_cost': '11', 'power': 10, 'toughness': 10, 'subtype': ['Construct']}, supertype=[], types=[cardtype.CardType.ARTIFACT, cardtype.CardType.CREATURE], abilities=[]))

class c417808(card.Card):
    "Smuggler's Copter"
    def __init__(self):
        super(c417808, self).__init__(gameobject.Characteristics(**{'name': "Smuggler's Copter", 'text': "Flying\nWhenever Smuggler's Copter attacks or blocks, you may draw a card. If you do, discard a card.\nCrew 1 (Tap any number of creatures you control with total power 1 or more: This Vehicle becomes an artifact creature until end of turn.)", 'color': '', 'mana_cost': '2', 'subtype': ['Vehicle']}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[static_abilities.StaticAbilities.Flying]))

class c417815(card.Card):
    "Aether Hub"
    def __init__(self):
        super(c417815, self).__init__(gameobject.Characteristics(**{'name': 'Aether Hub', 'text': 'When Aether Hub enters the battlefield, you get {E} (an energy counter).\n{T}: Add {C} to your mana pool.\n{T}, Pay {E}: Add one mana of any color to your mana pool.', 'color': '', 'mana_cost': ''}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c417820(card.Card):
    "Inventors' Fair"
    def __init__(self):
        super(c417820, self).__init__(gameobject.Characteristics(**{'name': "Inventors' Fair", 'text': "At the beginning of your upkeep, if you control three or more artifacts, you gain 1 life.\n{T}: Add {C} to your mana pool.\n{4}, {T}, Sacrifice Inventors' Fair: Search your library for an artifact card, reveal it, put it into your hand, then shuffle your library. Activate this ability only if you control three or more artifacts.", 'color': '', 'mana_cost': ''}, supertype=[cardtype.SuperType.LEGENDARY], types=[cardtype.CardType.LAND], abilities=[]))

class c380410(card.Card):
    "Eidolon of the Great Revel"
    def __init__(self):
        super(c380410, self).__init__(gameobject.Characteristics(**{'name': 'Eidolon of the Great Revel', 'text': 'Whenever a player casts a spell with converted mana cost 3 or less, Eidolon of the Great Revel deals 2 damage to that player.', 'color': ['R'], 'mana_cost': 'RR', 'power': 2, 'toughness': 2, 'subtype': ['Spirit']}, supertype=[], types=[cardtype.CardType.ENCHANTMENT, cardtype.CardType.CREATURE], abilities=[]))

class c380495(card.Card):
    "Setessan Tactics"
    def __init__(self):
        super(c380495, self).__init__(gameobject.Characteristics(**{'name': 'Setessan Tactics', 'text': 'Strive — Setessan Tactics costs {G} more to cast for each target beyond the first.\nUntil end of turn, any number of target creatures each get +1/+1 and gain "{T}: This creature fights another target creature."', 'color': ['G'], 'mana_cost': '1G'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c244678(card.Card):
    "Heartless Summoning"
    def __init__(self):
        super(c244678, self).__init__(gameobject.Characteristics(**{'name': 'Heartless Summoning', 'text': 'Creature spells you cast cost {2} less to cast.\nCreatures you control get -1/-1.', 'color': ['B'], 'mana_cost': '1B'}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c241980(card.Card):
    "Clifftop Retreat"
    def __init__(self):
        super(c241980, self).__init__(gameobject.Characteristics(**{'name': 'Clifftop Retreat', 'text': 'Clifftop Retreat enters the battlefield tapped unless you control a Mountain or a Plains.\n{T}: Add {R} or {W} to your mana pool.', 'color': ['R', 'W'], 'mana_cost': ''}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c241988(card.Card):
    "Hinterland Harbor"
    def __init__(self):
        super(c241988, self).__init__(gameobject.Characteristics(**{'name': 'Hinterland Harbor', 'text': 'Hinterland Harbor enters the battlefield tapped unless you control a Forest or an Island.\n{T}: Add {G} or {U} to your mana pool.', 'color': ['G', 'U'], 'mana_cost': ''}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c241987(card.Card):
    "Sulfur Falls"
    def __init__(self):
        super(c241987, self).__init__(gameobject.Characteristics(**{'name': 'Sulfur Falls', 'text': 'Sulfur Falls enters the battlefield tapped unless you control an Island or a Mountain.\n{T}: Add {U} or {R} to your mana pool.', 'color': ['U', 'R'], 'mana_cost': ''}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c241983(card.Card):
    "Woodland Cemetery"
    def __init__(self):
        super(c241983, self).__init__(gameobject.Characteristics(**{'name': 'Woodland Cemetery', 'text': 'Woodland Cemetery enters the battlefield tapped unless you control a Swamp or a Forest.\n{T}: Add {B} or {G} to your mana pool.', 'color': ['B', 'G'], 'mana_cost': ''}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c430729(card.Card):
    "Nimble Obstructionist"
    def __init__(self):
        super(c430729, self).__init__(gameobject.Characteristics(**{'name': 'Nimble Obstructionist', 'text': "Flash\nFlying\nCycling {2}{U} ({2}{U}, Discard this card: Draw a card.)\nWhen you cycle Nimble Obstructionist, counter target activated or triggered ability you don't control.", 'color': ['U'], 'mana_cost': '2U', 'power': 3, 'toughness': 1, 'subtype': ['Bird', 'Wizard']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Flash, static_abilities.StaticAbilities.Flying]))

class c430738(card.Card):
    "Supreme Will"
    def __init__(self):
        super(c430738, self).__init__(gameobject.Characteristics(**{'name': 'Supreme Will', 'text': 'Choose one —\n• Counter target spell unless its controller pays {3}.\n• Look at the top four cards of your library. Put one of them into your hand and the rest on the bottom of your library in any order.', 'color': ['U'], 'mana_cost': '2U'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c430779(card.Card):
    "Earthshaker Khenra"
    def __init__(self):
        super(c430779, self).__init__(gameobject.Characteristics(**{'name': 'Earthshaker Khenra', 'text': "Haste\nWhen Earthshaker Khenra enters the battlefield, target creature with power less than or equal to Earthshaker Khenra's power can't block this turn.\nEternalize {4}{R}{R} ({4}{R}{R}, Exile this card from your graveyard: Create a token that's a copy of it, except it's a 4/4 black Zombie Jackal Warrior with no mana cost. Eternalize only as a sorcery.)", 'color': ['R'], 'mana_cost': '1R', 'power': 2, 'toughness': 1, 'subtype': ['Jackal', 'Warrior']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Haste]))

class c430818(card.Card):
    "Ramunap Excavator"
    def __init__(self):
        super(c430818, self).__init__(gameobject.Characteristics(**{'name': 'Ramunap Excavator', 'text': 'You may play land cards from your graveyard.', 'color': ['G'], 'mana_cost': '2G', 'power': 2, 'toughness': 3, 'subtype': ['Naga', 'Cleric']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c430830(card.Card):
    "Obelisk Spider"
    def __init__(self):
        super(c430830, self).__init__(gameobject.Characteristics(**{'name': 'Obelisk Spider', 'text': 'Reach\nWhenever Obelisk Spider deals combat damage to a creature, put a -1/-1 counter on that creature.\nWhenever you put one or more -1/-1 counters on a creature, each opponent loses 1 life and you gain 1 life.', 'color': ['B', 'G'], 'mana_cost': '1BG', 'power': 1, 'toughness': 4, 'subtype': ['Spider']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Reach]))

class c366470(card.Card):
    "Assemble the Legion"
    def __init__(self):
        super(c366470, self).__init__(gameobject.Characteristics(**{'name': 'Assemble the Legion', 'text': 'At the beginning of your upkeep, put a muster counter on Assemble the Legion. Then create a 1/1 red and white Soldier creature token with haste for each muster counter on Assemble the Legion.', 'color': ['W', 'R'], 'mana_cost': '3RW'}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c366473(card.Card):
    "Dimir Charm"
    def __init__(self):
        super(c366473, self).__init__(gameobject.Characteristics(**{'name': 'Dimir Charm', 'text': "Choose one —\n• Counter target sorcery spell.\n• Destroy target creature with power 2 or less.\n• Look at the top three cards of target player's library. Put one back and the rest into that player's graveyard.", 'color': ['U', 'B'], 'mana_cost': 'UB'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c126215(card.Card):
    "Sword of the Meek"
    def __init__(self):
        super(c126215, self).__init__(gameobject.Characteristics(**{'name': 'Sword of the Meek', 'text': 'Equipped creature gets +1/+2.\nEquip {2}\nWhenever a 1/1 creature enters the battlefield under your control, you may return Sword of the Meek from your graveyard to the battlefield, then attach it to that creature.', 'color': '', 'mana_cost': '2', 'subtype': ['Equipment']}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c394079(card.Card):
    "Mastery of the Unseen"
    def __init__(self):
        super(c394079, self).__init__(gameobject.Characteristics(**{'name': 'Mastery of the Unseen', 'text': "Whenever a permanent you control is turned face up, you gain 1 life for each creature you control.\n{3}{W}: Manifest the top card of your library. (Put it onto the battlefield face down as a 2/2 creature. Turn it face up any time for its mana cost if it's a creature card.)", 'color': ['W'], 'mana_cost': '1W'}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c391927(card.Card):
    "Soulfire Grand Master"
    def __init__(self):
        super(c391927, self).__init__(gameobject.Characteristics(**{'name': 'Soulfire Grand Master', 'text': 'Lifelink\nInstant and sorcery spells you control have lifelink.\n{2}{U/R}{U/R}: The next time you cast an instant or sorcery spell from your hand this turn, put that card into your hand instead of into your graveyard as it resolves.', 'color': ['W', 'U', 'R'], 'mana_cost': '1W', 'power': 2, 'toughness': 2, 'subtype': ['Human', 'Monk']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Lifelink]))

class c391937(card.Card):
    "Tasigur, the Golden Fang"
    def __init__(self):
        super(c391937, self).__init__(gameobject.Characteristics(**{'name': 'Tasigur, the Golden Fang', 'text': "Delve (Each card you exile from your graveyard while casting this spell pays for {1}.)\n{2}{G/U}{G/U}: Put the top two cards of your library into your graveyard, then return a nonland card of an opponent's choice from your graveyard to your hand.", 'color': ['B', 'G', 'U'], 'mana_cost': '5B', 'power': 4, 'toughness': 5, 'subtype': ['Human', 'Shaman']}, supertype=[cardtype.SuperType.LEGENDARY], types=[cardtype.CardType.CREATURE], abilities=[]))

class c391958(card.Card):
    "Whisperwood Elemental"
    def __init__(self):
        super(c391958, self).__init__(gameobject.Characteristics(**{'name': 'Whisperwood Elemental', 'text': 'At the beginning of your end step, manifest the top card of your library. (Put it onto the battlefield face down as a 2/2 creature. Turn it face up any time for its mana cost if it\'s a creature card.)\nSacrifice Whisperwood Elemental: Until end of turn, face-up nontoken creatures you control gain "When this creature dies, manifest the top card of your library."', 'color': ['G'], 'mana_cost': '3GG', 'power': 4, 'toughness': 4, 'subtype': ['Elemental']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c414292(card.Card):
    "Distended Mindbender"
    def __init__(self):
        super(c414292, self).__init__(gameobject.Characteristics(**{'name': 'Distended Mindbender', 'text': "Emerge {5}{B}{B} (You may cast this spell by sacrificing a creature and paying the emerge cost reduced by that creature's converted mana cost.)\nWhen you cast Distended Mindbender, target opponent reveals his or her hand. You choose from it a nonland card with converted mana cost 3 or less and a card with converted mana cost 4 or greater. That player discards those cards.", 'color': ['B'], 'mana_cost': '8', 'power': 5, 'toughness': 5, 'subtype': ['Eldrazi', 'Insect']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c414302(card.Card):
    "Blessed Alliance"
    def __init__(self):
        super(c414302, self).__init__(gameobject.Characteristics(**{'name': 'Blessed Alliance', 'text': 'Escalate {2} (Pay this cost for each mode chosen beyond the first.)\nChoose one or more —\n• Target player gains 4 life.\n• Untap up to two target creatures.\n• Target opponent sacrifices an attacking creature.', 'color': ['W'], 'mana_cost': '1W'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c414332(card.Card):
    "Selfless Spirit"
    def __init__(self):
        super(c414332, self).__init__(gameobject.Characteristics(**{'name': 'Selfless Spirit', 'text': 'Flying\nSacrifice Selfless Spirit: Creatures you control gain indestructible until end of turn.', 'color': ['W'], 'mana_cost': '1W', 'power': 2, 'toughness': 1, 'subtype': ['Spirit', 'Cleric']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Flying]))

class c414338(card.Card):
    "Thalia, Heretic Cathar"
    def __init__(self):
        super(c414338, self).__init__(gameobject.Characteristics(**{'name': 'Thalia, Heretic Cathar', 'text': 'First strike\nCreatures and nonbasic lands your opponents control enter the battlefield tapped.', 'color': ['W'], 'mana_cost': '2W', 'power': 3, 'toughness': 2, 'subtype': ['Human', 'Soldier']}, supertype=[cardtype.SuperType.LEGENDARY], types=[cardtype.CardType.CREATURE], abilities=[]))

class c414375(card.Card):
    "Wharf Infiltrator"
    def __init__(self):
        super(c414375, self).__init__(gameobject.Characteristics(**{'name': 'Wharf Infiltrator', 'text': "Skulk (This creature can't be blocked by creatures with greater power.)\nWhenever Wharf Infiltrator deals combat damage to a player, you may draw a card. If you do, discard a card.\nWhenever you discard a creature card, you may pay {2}. If you do, create a 3/2 colorless Eldrazi Horror creature token.", 'color': ['U'], 'mana_cost': '1U', 'power': 1, 'toughness': 1, 'subtype': ['Human', 'Horror']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c414463(card.Card):
    "Ishkanah, Grafwidow"
    def __init__(self):
        super(c414463, self).__init__(gameobject.Characteristics(**{'name': 'Ishkanah, Grafwidow', 'text': 'Reach\nDelirium — When Ishkanah, Grafwidow enters the battlefield, if there are four or more card types among cards in your graveyard, create three 1/2 green Spider creature tokens with reach.\n{6}{B}: Target opponent loses 1 life for each Spider you control.', 'color': ['G', 'B'], 'mana_cost': '4G', 'power': 3, 'toughness': 5, 'subtype': ['Spider']}, supertype=[cardtype.SuperType.LEGENDARY], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Reach]))

class c414467(card.Card):
    "Permeating Mass"
    def __init__(self):
        super(c414467, self).__init__(gameobject.Characteristics(**{'name': 'Permeating Mass', 'text': 'Whenever Permeating Mass deals combat damage to a creature, that creature becomes a copy of Permeating Mass.', 'color': ['G'], 'mana_cost': 'G', 'power': 1, 'toughness': 3, 'subtype': ['Spirit']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c414489(card.Card):
    "Grim Flayer"
    def __init__(self):
        super(c414489, self).__init__(gameobject.Characteristics(**{'name': 'Grim Flayer', 'text': 'Trample\nWhenever Grim Flayer deals combat damage to a player, look at the top three cards of your library. Put any number of them into your graveyard and the rest back on top of your library in any order.\nDelirium — Grim Flayer gets +2/+2 as long as there are four or more card types among cards in your graveyard.', 'color': ['B', 'G'], 'mana_cost': 'BG', 'power': 2, 'toughness': 2, 'subtype': ['Human', 'Warrior']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Trample]))

class c394490(card.Card):
    "Anafenza, Kin-Tree Spirit"
    def __init__(self):
        super(c394490, self).__init__(gameobject.Characteristics(**{'name': 'Anafenza, Kin-Tree Spirit', 'text': 'Whenever another nontoken creature enters the battlefield under your control, bolster 1. (Choose a creature with the least toughness among creatures you control and put a +1/+1 counter on it.)', 'color': ['W'], 'mana_cost': 'WW', 'power': 2, 'toughness': 2, 'subtype': ['Spirit', 'Soldier']}, supertype=[cardtype.SuperType.LEGENDARY], types=[cardtype.CardType.CREATURE], abilities=[]))

class c394597(card.Card):
    "Hidden Dragonslayer"
    def __init__(self):
        super(c394597, self).__init__(gameobject.Characteristics(**{'name': 'Hidden Dragonslayer', 'text': 'Lifelink\nMegamorph {2}{W} (You may cast this card face down as a 2/2 creature for {3}. Turn it face up any time for its megamorph cost and put a +1/+1 counter on it.)\nWhen Hidden Dragonslayer is turned face up, destroy target creature with power 4 or greater an opponent controls.', 'color': ['W'], 'mana_cost': '1W', 'power': 2, 'toughness': 1, 'subtype': ['Human', 'Warrior']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Lifelink]))

class c394714(card.Card):
    "Stratus Dancer"
    def __init__(self):
        super(c394714, self).__init__(gameobject.Characteristics(**{'name': 'Stratus Dancer', 'text': 'Flying\nMegamorph {1}{U} (You may cast this card face down as a 2/2 creature for {3}. Turn it face up any time for its megamorph cost and put a +1/+1 counter on it.)\nWhen Stratus Dancer is turned face up, counter target instant or sorcery spell.', 'color': ['U'], 'mana_cost': '1U', 'power': 2, 'toughness': 1, 'subtype': ['Djinn', 'Monk']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Flying]))

class c394695(card.Card):
    "Sidisi, Undead Vizier"
    def __init__(self):
        super(c394695, self).__init__(gameobject.Characteristics(**{'name': 'Sidisi, Undead Vizier', 'text': 'Deathtouch\nExploit (When this creature enters the battlefield, you may sacrifice a creature.)\nWhen Sidisi, Undead Vizier exploits a creature, you may search your library for a card, put it into your hand, then shuffle your library.', 'color': ['B'], 'mana_cost': '3BB', 'power': 4, 'toughness': 6, 'subtype': ['Zombie', 'Naga']}, supertype=[cardtype.SuperType.LEGENDARY], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Deathtouch]))

class c270445(card.Card):
    "Thalia, Guardian of Thraben"
    def __init__(self):
        super(c270445, self).__init__(gameobject.Characteristics(**{'name': 'Thalia, Guardian of Thraben', 'text': 'First strike\nNoncreature spells cost {1} more to cast.', 'color': ['W'], 'mana_cost': '1W', 'power': 2, 'toughness': 1, 'subtype': ['Human', 'Soldier']}, supertype=[cardtype.SuperType.LEGENDARY], types=[cardtype.CardType.CREATURE], abilities=[]))

class c243250(card.Card):
    "Geralf's Messenger"
    def __init__(self):
        super(c243250, self).__init__(gameobject.Characteristics(**{'name': "Geralf's Messenger", 'text': "Geralf's Messenger enters the battlefield tapped.\nWhen Geralf's Messenger enters the battlefield, target opponent loses 2 life.\nUndying (When this creature dies, if it had no +1/+1 counters on it, return it to the battlefield under its owner's control with a +1/+1 counter on it.)", 'color': ['B'], 'mana_cost': 'BBB', 'power': 3, 'toughness': 2, 'subtype': ['Zombie']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c262671(card.Card):
    "Strangleroot Geist"
    def __init__(self):
        super(c262671, self).__init__(gameobject.Characteristics(**{'name': 'Strangleroot Geist', 'text': "Haste\nUndying (When this creature dies, if it had no +1/+1 counters on it, return it to the battlefield under its owner's control with a +1/+1 counter on it.)", 'color': ['G'], 'mana_cost': 'GG', 'power': 2, 'toughness': 1, 'subtype': ['Spirit']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Haste]))

class c368961(card.Card):
    "Aetherling"
    def __init__(self):
        super(c368961, self).__init__(gameobject.Characteristics(**{'name': 'Aetherling', 'text': "{U}: Exile Aetherling. Return it to the battlefield under its owner's control at the beginning of the next end step.\n{U}: Aetherling can't be blocked this turn.\n{1}: Aetherling gets +1/-1 until end of turn.\n{1}: Aetherling gets -1/+1 until end of turn.", 'color': ['U'], 'mana_cost': '4UU', 'power': 4, 'toughness': 5, 'subtype': ['Shapeshifter']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c368973(card.Card):
    "Notion Thief"
    def __init__(self):
        super(c368973, self).__init__(gameobject.Characteristics(**{'name': 'Notion Thief', 'text': 'Flash\nIf an opponent would draw a card except the first one he or she draws in each of his or her draw steps, instead that player skips that draw and you draw a card.', 'color': ['U', 'B'], 'mana_cost': '2UB', 'power': 3, 'toughness': 1, 'subtype': ['Human', 'Rogue']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Flash]))

class c74647(card.Card):
    "Hokori, Dust Drinker"
    def __init__(self):
        super(c74647, self).__init__(gameobject.Characteristics(**{'name': 'Hokori, Dust Drinker', 'text': "Lands don't untap during their controllers' untap steps.\nAt the beginning of each player's upkeep, that player untaps a land he or she controls.", 'color': ['W'], 'mana_cost': '2WW', 'power': 2, 'toughness': 2, 'subtype': ['Spirit']}, supertype=[cardtype.SuperType.LEGENDARY], types=[cardtype.CardType.CREATURE], abilities=[]))

class c378433(card.Card):
    "Bile Blight"
    def __init__(self):
        super(c378433, self).__init__(gameobject.Characteristics(**{'name': 'Bile Blight', 'text': 'Target creature and all other creatures with the same name as that creature get -3/-3 until end of turn.', 'color': ['B'], 'mana_cost': 'BB'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c402001(card.Card):
    "Quarantine Field"
    def __init__(self):
        super(c402001, self).__init__(gameobject.Characteristics(**{'name': 'Quarantine Field', 'text': 'Quarantine Field enters the battlefield with X isolation counters on it.\nWhen Quarantine Field enters the battlefield, for each isolation counter on it, exile up to one target nonland permanent an opponent controls until Quarantine Field leaves the battlefield.', 'color': ['W'], 'mana_cost': 'XXWW'}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c402101(card.Card):
    "Zulaport Cutthroat"
    def __init__(self):
        super(c402101, self).__init__(gameobject.Characteristics(**{'name': 'Zulaport Cutthroat', 'text': 'Whenever Zulaport Cutthroat or another creature you control dies, each opponent loses 1 life and you gain 1 life.', 'color': ['B'], 'mana_cost': '1B', 'power': 1, 'toughness': 1, 'subtype': ['Human', 'Rogue', 'Ally']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c401912(card.Card):
    "Herald of Kozilek"
    def __init__(self):
        super(c401912, self).__init__(gameobject.Characteristics(**{'name': 'Herald of Kozilek', 'text': 'Devoid (This card has no color.)\nColorless spells you cast cost {1} less to cast.', 'color': ['U', 'R'], 'mana_cost': '1UR', 'power': 2, 'toughness': 4, 'subtype': ['Eldrazi', 'Drone']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c401931(card.Card):
    "Kiora, Master of the Depths"
    def __init__(self):
        super(c401931, self).__init__(gameobject.Characteristics(**{'name': 'Kiora, Master of the Depths', 'text': '+1: Untap up to one target creature and up to one target land.\n−2: Reveal the top four cards of your library. You may put a creature card and/or a land card from among them into your hand. Put the rest into your graveyard.\n−8: You get an emblem with "Whenever a creature enters the battlefield under your control, you may have it fight target creature." Then create three 8/8 blue Octopus creature tokens.', 'color': ['U', 'G'], 'mana_cost': '2GU', 'subtype': ['Kiora']}, supertype=[], types=[cardtype.CardType.PLANESWALKER], abilities=[]))

class c401943(card.Card):
    "Lumbering Falls"
    def __init__(self):
        super(c401943, self).__init__(gameobject.Characteristics(**{'name': 'Lumbering Falls', 'text': "Lumbering Falls enters the battlefield tapped.\n{T}: Add {G} or {U} to your mana pool.\n{2}{G}{U}: Lumbering Falls becomes a 3/3 green and blue Elemental creature with hexproof until end of turn. It's still a land.", 'color': ['G', 'U'], 'mana_cost': ''}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c402031(card.Card):
    "Shambling Vent"
    def __init__(self):
        super(c402031, self).__init__(gameobject.Characteristics(**{'name': 'Shambling Vent', 'text': "Shambling Vent enters the battlefield tapped.\n{T}: Add {W} or {B} to your mana pool.\n{1}{W}{B}: Shambling Vent becomes a 2/3 white and black Elemental creature with lifelink until end of turn. It's still a land.", 'color': ['W', 'B'], 'mana_cost': ''}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c240033(card.Card):
    "Sigarda, Host of Herons"
    def __init__(self):
        super(c240033, self).__init__(gameobject.Characteristics(**{'name': 'Sigarda, Host of Herons', 'text': "Flying, hexproof\nSpells and abilities your opponents control can't cause you to sacrifice permanents.", 'color': ['W', 'G'], 'mana_cost': '2GWW', 'power': 5, 'toughness': 5, 'subtype': ['Angel']}, supertype=[cardtype.SuperType.LEGENDARY], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Flying, static_abilities.StaticAbilities.Hexproof]))

class c426836(card.Card):
    "Glorybringer"
    def __init__(self):
        super(c426836, self).__init__(gameobject.Characteristics(**{'name': 'Glorybringer', 'text': "Flying, haste\nYou may exert Glorybringer as it attacks. When you do, it deals 4 damage to target non-Dragon creature an opponent controls. (An exerted creature won't untap during your next untap step.)", 'color': ['R'], 'mana_cost': '3RR', 'power': 4, 'toughness': 4, 'subtype': ['Dragon']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Flying, static_abilities.StaticAbilities.Haste]))

class c426837(card.Card):
    "Harsh Mentor"
    def __init__(self):
        super(c426837, self).__init__(gameobject.Characteristics(**{'name': 'Harsh Mentor', 'text': "Whenever an opponent activates an ability of an artifact, creature, or land on the battlefield, if it isn't a mana ability, Harsh Mentor deals 2 damage to that player.", 'color': ['R'], 'mana_cost': '1R', 'power': 2, 'toughness': 2, 'subtype': ['Human', 'Cleric']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c426851(card.Card):
    "Sweltering Suns"
    def __init__(self):
        super(c426851, self).__init__(gameobject.Characteristics(**{'name': 'Sweltering Suns', 'text': 'Sweltering Suns deals 3 damage to each creature.\nCycling {3} ({3}, Discard this card: Draw a card.)', 'color': ['R'], 'mana_cost': '1RR'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c426906(card.Card):
    "Nissa, Steward of Elements"
    def __init__(self):
        super(c426906, self).__init__(gameobject.Characteristics(**{'name': 'Nissa, Steward of Elements', 'text': "+2: Scry 2.\n0: Look at the top card of your library. If it's a land card or a creature card with converted mana cost less than or equal to the number of loyalty counters on Nissa, Steward of Elements, you may put that card onto the battlefield.\n−6: Untap up to two target lands you control. They become 5/5 Elemental creatures with flying and haste until end of turn. They're still lands.", 'color': ['U', 'G'], 'mana_cost': 'XGU', 'subtype': ['Nissa']}, supertype=[], types=[cardtype.CardType.PLANESWALKER], abilities=[]))

class c426907(card.Card):
    "Samut, Voice of Dissent"
    def __init__(self):
        super(c426907, self).__init__(gameobject.Characteristics(**{'name': 'Samut, Voice of Dissent', 'text': 'Flash\nDouble strike, vigilance, haste\nOther creatures you control have haste.\n{W}, {T}: Untap another target creature.', 'color': ['R', 'G', 'W'], 'mana_cost': '3RG', 'power': 3, 'toughness': 4, 'subtype': ['Human', 'Warrior']}, supertype=[cardtype.SuperType.LEGENDARY], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Flash, static_abilities.StaticAbilities.Haste, static_abilities.StaticAbilities.Vigilance]))

class c426936(card.Card):
    "Oracle's Vault"
    def __init__(self):
        super(c426936, self).__init__(gameobject.Characteristics(**{'name': "Oracle's Vault", 'text': "{2}, {T}: Exile the top card of your library. Until end of turn, you may play that card. Put a brick counter on Oracle's Vault.\n{T}: Exile the top card of your library. Until end of turn, you may play that card without paying its mana cost. Activate this ability only if there are three or more brick counters on Oracle's Vault.", 'color': '', 'mana_cost': '4'}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c423686(card.Card):
    "Felidar Guardian"
    def __init__(self):
        super(c423686, self).__init__(gameobject.Characteristics(**{'name': 'Felidar Guardian', 'text': "When Felidar Guardian enters the battlefield, you may exile another target permanent you control, then return that card to the battlefield under its owner's control.", 'color': ['W'], 'mana_cost': '3W', 'power': 1, 'toughness': 4, 'subtype': ['Cat', 'Beast']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c423696(card.Card):
    "Baral's Expertise"
    def __init__(self):
        super(c423696, self).__init__(gameobject.Characteristics(**{'name': "Baral's Expertise", 'text': "Return up to three target artifacts and/or creatures to their owners' hands.\nYou may cast a card with converted mana cost 4 or less from your hand without paying its mana cost.", 'color': ['U'], 'mana_cost': '3UU'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c423715(card.Card):
    "Trophy Mage"
    def __init__(self):
        super(c423715, self).__init__(gameobject.Characteristics(**{'name': 'Trophy Mage', 'text': 'When Trophy Mage enters the battlefield, you may search your library for an artifact card with converted mana cost 3, reveal it, put it into your hand, then shuffle your library.', 'color': ['U'], 'mana_cost': '2U', 'power': 2, 'toughness': 2, 'subtype': ['Human', 'Wizard']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c423742(card.Card):
    "Yahenni's Expertise"
    def __init__(self):
        super(c423742, self).__init__(gameobject.Characteristics(**{'name': "Yahenni's Expertise", 'text': 'All creatures get -3/-3 until end of turn.\nYou may cast a card with converted mana cost 3 or less from your hand without paying its mana cost.', 'color': ['B'], 'mana_cost': '2BB'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c423754(card.Card):
    "Kari Zev, Skyship Raider"
    def __init__(self):
        super(c423754, self).__init__(gameobject.Characteristics(**{'name': 'Kari Zev, Skyship Raider', 'text': "First strike, menace\nWhenever Kari Zev, Skyship Raider attacks, create a legendary 2/1 red Monkey creature token named Ragavan that's tapped and attacking. Exile that token at end of combat.", 'color': ['R'], 'mana_cost': '1R', 'power': 1, 'toughness': 3, 'subtype': ['Human', 'Pirate']}, supertype=[cardtype.SuperType.LEGENDARY], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Menace]))

class c423842(card.Card):
    "Scrap Trawler"
    def __init__(self):
        super(c423842, self).__init__(gameobject.Characteristics(**{'name': 'Scrap Trawler', 'text': 'Whenever Scrap Trawler or another artifact you control is put into a graveyard from the battlefield, return to your hand target artifact card in your graveyard with lesser converted mana cost.', 'color': '', 'mana_cost': '3', 'power': 3, 'toughness': 2, 'subtype': ['Construct']}, supertype=[], types=[cardtype.CardType.ARTIFACT, cardtype.CardType.CREATURE], abilities=[]))

