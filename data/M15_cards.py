from MTG import card
from MTG import gameobject
from MTG import cardtype
from MTG import abilities
from MTG import mana

class c383180(card.Card):
    "Ajani Steadfast"
    def __init__(self):
        super(c383180, self).__init__(gameobject.Characteristics(**{'subtype': ['Ajani'], 'name': 'Ajani Steadfast', 'text': '+1: Until end of turn, up to one target creature gets +1/+1 and gains first strike, vigilance, and lifelink.\n−2: Put a +1/+1 counter on each creature you control and a loyalty counter on each other planeswalker you control.\n−7: You get an emblem with "If a source would deal damage to you or a planeswalker you control, prevent all but 1 of that damage."', 'color': ['W'], 'mana_cost': '3W'}, supertype=[], types=[cardtype.CardType.PLANESWALKER], abilities=[abilities.StaticAbilities.Vigilance]))

class c383181(card.Card):
    "Ajani's Pridemate"
    def __init__(self):
        super(c383181, self).__init__(gameobject.Characteristics(**{'name': "Ajani's Pridemate", 'subtype': ['Cat', 'Soldier'], 'mana_cost': '1W', 'text': "Whenever you gain life, you may put a +1/+1 counter on Ajani's Pridemate.", 'toughness': 2, 'power': 2, 'color': ['W']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383185(card.Card):
    "Avacyn, Guardian Angel"
    def __init__(self):
        super(c383185, self).__init__(gameobject.Characteristics(**{'name': 'Avacyn, Guardian Angel', 'subtype': ['Angel'], 'mana_cost': '2WWW', 'text': 'Flying, vigilance\n{1}{W}: Prevent all damage that would be dealt to another target creature this turn by sources of the color of your choice.\n{5}{W}{W}: Prevent all damage that would be dealt to target player this turn by sources of the color of your choice.', 'toughness': 4, 'power': 5, 'color': ['W']}, supertype=[cardtype.SuperType.LEGENDARY], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Flying, abilities.StaticAbilities.Vigilance]))

class c383188(card.Card):
    "Battle Mastery"
    def __init__(self):
        super(c383188, self).__init__(gameobject.Characteristics(**{'subtype': ['Aura'], 'name': 'Battle Mastery', 'text': 'Enchant creature\nEnchanted creature has double strike. (It deals both first-strike and regular combat damage.)', 'color': ['W'], 'mana_cost': '2W'}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c383194(card.Card):
    "Boonweaver Giant"
    def __init__(self):
        super(c383194, self).__init__(gameobject.Characteristics(**{'name': 'Boonweaver Giant', 'subtype': ['Giant', 'Monk'], 'mana_cost': '6W', 'text': 'When Boonweaver Giant enters the battlefield, you may search your graveyard, hand, and/or library for an Aura card and put it onto the battlefield attached to Boonweaver Giant. If you search your library this way, shuffle it.', 'toughness': 4, 'power': 4, 'color': ['W']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383214(card.Card):
    "Congregate"
    def __init__(self):
        super(c383214, self).__init__(gameobject.Characteristics(**{'name': 'Congregate', 'text': 'Target player gains 2 life for each creature on the battlefield.', 'color': ['W'], 'mana_cost': '3W'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c383215(card.Card):
    "Constricting Sliver"
    def __init__(self):
        super(c383215, self).__init__(gameobject.Characteristics(**{'name': 'Constricting Sliver', 'subtype': ['Sliver'], 'mana_cost': '5W', 'text': 'Sliver creatures you control have "When this creature enters the battlefield, you may exile target creature an opponent controls until this creature leaves the battlefield."', 'toughness': 3, 'power': 3, 'color': ['W']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383223(card.Card):
    "Dauntless River Marshal"
    def __init__(self):
        super(c383223, self).__init__(gameobject.Characteristics(**{'name': 'Dauntless River Marshal', 'subtype': ['Human', 'Soldier'], 'mana_cost': '1W', 'text': 'Dauntless River Marshal gets +1/+1 as long as you control an Island.\n{3}{U}: Tap target creature.', 'toughness': 1, 'power': 2, 'color': ['W', 'U']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383224(card.Card):
    "Devouring Light"
    def __init__(self):
        super(c383224, self).__init__(gameobject.Characteristics(**{'name': 'Devouring Light', 'text': "Convoke (Your creatures can help cast this spell. Each creature you tap while casting this spell pays for {1} or one mana of that creature's color.)\nExile target attacking or blocking creature.", 'color': ['W'], 'mana_cost': '1WW'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[abilities.StaticAbilities.Convoke]))

class c383228(card.Card):
    "Divine Favor"
    def __init__(self):
        super(c383228, self).__init__(gameobject.Characteristics(**{'subtype': ['Aura'], 'name': 'Divine Favor', 'text': 'Enchant creature\nWhen Divine Favor enters the battlefield, you gain 3 life.\nEnchanted creature gets +1/+3.', 'color': ['W'], 'mana_cost': '1W'}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c383233(card.Card):
    "Ephemeral Shields"
    def __init__(self):
        super(c383233, self).__init__(gameobject.Characteristics(**{'name': 'Ephemeral Shields', 'text': 'Convoke (Your creatures can help cast this spell. Each creature you tap while casting this spell pays for {1} or one mana of that creature\'s color.)\nTarget creature gains indestructible until end of turn. (Damage and effects that say "destroy" don\'t destroy it.)', 'color': ['W'], 'mana_cost': '1W'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[abilities.StaticAbilities.Convoke]))

class c383239(card.Card):
    "First Response"
    def __init__(self):
        super(c383239, self).__init__(gameobject.Characteristics(**{'name': 'First Response', 'text': 'At the beginning of each upkeep, if you lost life last turn, create a 1/1 white Soldier creature token.', 'color': ['W'], 'mana_cost': '3W'}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c383253(card.Card):
    "Geist of the Moors"
    def __init__(self):
        super(c383253, self).__init__(gameobject.Characteristics(**{'name': 'Geist of the Moors', 'subtype': ['Spirit'], 'mana_cost': '1WW', 'text': 'Flying', 'toughness': 1, 'power': 3, 'color': ['W']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Flying]))

class c383265(card.Card):
    "Heliod's Pilgrim"
    def __init__(self):
        super(c383265, self).__init__(gameobject.Characteristics(**{'name': "Heliod's Pilgrim", 'subtype': ['Human', 'Cleric'], 'mana_cost': '2W', 'text': "When Heliod's Pilgrim enters the battlefield, you may search your library for an Aura card, reveal it, put it into your hand, then shuffle your library.", 'toughness': 2, 'power': 1, 'color': ['W']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383272(card.Card):
    "Hushwing Gryff"
    def __init__(self):
        super(c383272, self).__init__(gameobject.Characteristics(**{'name': 'Hushwing Gryff', 'subtype': ['Hippogriff'], 'mana_cost': '2W', 'text': "Flash\nFlying\nCreatures entering the battlefield don't cause abilities to trigger.", 'toughness': 1, 'power': 2, 'color': ['W']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Flash, abilities.StaticAbilities.Flying]))

class c383292(card.Card):
    "Kinsbaile Skirmisher"
    def __init__(self):
        super(c383292, self).__init__(gameobject.Characteristics(**{'name': 'Kinsbaile Skirmisher', 'subtype': ['Kithkin', 'Soldier'], 'mana_cost': '1W', 'text': 'When Kinsbaile Skirmisher enters the battlefield, target creature gets +1/+1 until end of turn.', 'toughness': 2, 'power': 2, 'color': ['W']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383303(card.Card):
    "Marked by Honor"
    def __init__(self):
        super(c383303, self).__init__(gameobject.Characteristics(**{'subtype': ['Aura'], 'name': 'Marked by Honor', 'text': "Enchant creature\nEnchanted creature gets +2/+2 and has vigilance. (Attacking doesn't cause it to tap.)", 'color': ['W'], 'mana_cost': '3W'}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c383304(card.Card):
    "Mass Calcify"
    def __init__(self):
        super(c383304, self).__init__(gameobject.Characteristics(**{'name': 'Mass Calcify', 'text': 'Destroy all nonwhite creatures.', 'color': ['W'], 'mana_cost': '5WW'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c383306(card.Card):
    "Meditation Puzzle"
    def __init__(self):
        super(c383306, self).__init__(gameobject.Characteristics(**{'name': 'Meditation Puzzle', 'text': "Convoke (Your creatures can help cast this spell. Each creature you tap while casting this spell pays for {1} or one mana of that creature's color.)\nYou gain 8 life.", 'color': ['W'], 'mana_cost': '3WW'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[abilities.StaticAbilities.Convoke]))

class c383309(card.Card):
    "Midnight Guard"
    def __init__(self):
        super(c383309, self).__init__(gameobject.Characteristics(**{'name': 'Midnight Guard', 'subtype': ['Human', 'Soldier'], 'mana_cost': '2W', 'text': 'Whenever another creature enters the battlefield, untap Midnight Guard.', 'toughness': 3, 'power': 2, 'color': ['W']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383332(card.Card):
    "Oppressive Rays"
    def __init__(self):
        super(c383332, self).__init__(gameobject.Characteristics(**{'subtype': ['Aura'], 'name': 'Oppressive Rays', 'text': "Enchant creature\nEnchanted creature can't attack or block unless its controller pays {3}.\nActivated abilities of enchanted creature cost {3} more to activate.", 'color': ['W'], 'mana_cost': 'W'}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c383333(card.Card):
    "Oreskos Swiftclaw"
    def __init__(self):
        super(c383333, self).__init__(gameobject.Characteristics(**{'name': 'Oreskos Swiftclaw', 'subtype': ['Cat', 'Warrior'], 'mana_cost': '1W', 'text': '', 'toughness': 1, 'power': 3, 'color': ['W']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383339(card.Card):
    "Paragon of New Dawns"
    def __init__(self):
        super(c383339, self).__init__(gameobject.Characteristics(**{'name': 'Paragon of New Dawns', 'subtype': ['Human', 'Soldier'], 'mana_cost': '3W', 'text': "Other white creatures you control get +1/+1.\n{W}, {T}: Another target white creature you control gains vigilance until end of turn. (Attacking doesn't cause it to tap.)", 'toughness': 2, 'power': 2, 'color': ['W']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383345(card.Card):
    "Pillar of Light"
    def __init__(self):
        super(c383345, self).__init__(gameobject.Characteristics(**{'name': 'Pillar of Light', 'text': 'Exile target creature with toughness 4 or greater.', 'color': ['W'], 'mana_cost': '2W'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c383352(card.Card):
    "Preeminent Captain"
    def __init__(self):
        super(c383352, self).__init__(gameobject.Characteristics(**{'name': 'Preeminent Captain', 'subtype': ['Kithkin', 'Soldier'], 'mana_cost': '2W', 'text': 'First strike (This creature deals combat damage before creatures without first strike.)\nWhenever Preeminent Captain attacks, you may put a Soldier creature card from your hand onto the battlefield tapped and attacking.', 'toughness': 2, 'power': 2, 'color': ['W']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383356(card.Card):
    "Raise the Alarm"
    def __init__(self):
        super(c383356, self).__init__(gameobject.Characteristics(**{'name': 'Raise the Alarm', 'text': 'Create two 1/1 white Soldier creature tokens.', 'color': ['W'], 'mana_cost': '1W'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c383358(card.Card):
    "Razorfoot Griffin"
    def __init__(self):
        super(c383358, self).__init__(gameobject.Characteristics(**{'name': 'Razorfoot Griffin', 'subtype': ['Griffin'], 'mana_cost': '3W', 'text': "Flying (This creature can't be blocked except by creatures with flying or reach.)\nFirst strike (This creature deals combat damage before creatures without first strike.)", 'toughness': 2, 'power': 2, 'color': ['W']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Flying]))

class c383361(card.Card):
    "Resolute Archangel"
    def __init__(self):
        super(c383361, self).__init__(gameobject.Characteristics(**{'name': 'Resolute Archangel', 'subtype': ['Angel'], 'mana_cost': '5WW', 'text': 'Flying\nWhen Resolute Archangel enters the battlefield, if your life total is less than your starting life total, it becomes equal to your starting life total.', 'toughness': 4, 'power': 4, 'color': ['W']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Flying]))

class c383363(card.Card):
    "Return to the Ranks"
    def __init__(self):
        super(c383363, self).__init__(gameobject.Characteristics(**{'name': 'Return to the Ranks', 'text': "Convoke (Your creatures can help cast this spell. Each creature you tap while casting this spell pays for {1} or one mana of that creature's color.)\nReturn X target creature cards with converted mana cost 2 or less from your graveyard to the battlefield.", 'color': ['W'], 'mana_cost': 'XWW'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[abilities.StaticAbilities.Convoke]))

class c383370(card.Card):
    "Sanctified Charge"
    def __init__(self):
        super(c383370, self).__init__(gameobject.Characteristics(**{'name': 'Sanctified Charge', 'text': 'Creatures you control get +2/+1 until end of turn. White creatures you control also gain first strike until end of turn. (They deal combat damage before creatures without first strike.)', 'color': ['W'], 'mana_cost': '4W'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c383374(card.Card):
    "Selfless Cathar"
    def __init__(self):
        super(c383374, self).__init__(gameobject.Characteristics(**{'name': 'Selfless Cathar', 'subtype': ['Human', 'Cleric'], 'mana_cost': 'W', 'text': '{1}{W}, Sacrifice Selfless Cathar: Creatures you control get +1/+1 until end of turn.', 'toughness': 1, 'power': 1, 'color': ['W']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383375(card.Card):
    "Seraph of the Masses"
    def __init__(self):
        super(c383375, self).__init__(gameobject.Characteristics(**{'name': 'Seraph of the Masses', 'subtype': ['Angel'], 'mana_cost': '5WW', 'text': "Convoke (Your creatures can help cast this spell. Each creature you tap while casting this spell pays for {1} or one mana of that creature's color.)\nFlying\nSeraph of the Masses's power and toughness are each equal to the number of creatures you control.", 'toughness': '*', 'power': '*', 'color': ['W']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Flying, abilities.StaticAbilities.Convoke]))

class c383386(card.Card):
    "Solemn Offering"
    def __init__(self):
        super(c383386, self).__init__(gameobject.Characteristics(**{'name': 'Solemn Offering', 'text': 'Destroy target artifact or enchantment. You gain 4 life.', 'color': ['W'], 'mana_cost': '2W'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c383391(card.Card):
    "Soul of Theros"
    def __init__(self):
        super(c383391, self).__init__(gameobject.Characteristics(**{'name': 'Soul of Theros', 'subtype': ['Avatar'], 'mana_cost': '4WW', 'text': 'Vigilance\n{4}{W}{W}: Creatures you control get +2/+2 and gain first strike and lifelink until end of turn.\n{4}{W}{W}, Exile Soul of Theros from your graveyard: Creatures you control get +2/+2 and gain first strike and lifelink until end of turn.', 'toughness': 6, 'power': 6, 'color': ['W']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Vigilance]))

class c383393(card.Card):
    "Soulmender"
    def __init__(self):
        super(c383393, self).__init__(gameobject.Characteristics(**{'name': 'Soulmender', 'subtype': ['Human', 'Cleric'], 'mana_cost': 'W', 'text': '{T}: You gain 1 life.', 'toughness': 1, 'power': 1, 'color': ['W']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383394(card.Card):
    "Spectra Ward"
    def __init__(self):
        super(c383394, self).__init__(gameobject.Characteristics(**{'subtype': ['Aura'], 'name': 'Spectra Ward', 'text': "Enchant creature\nEnchanted creature gets +2/+2 and has protection from all colors. This effect doesn't remove Auras. (It can't be blocked, targeted, or dealt damage by anything that's white, blue, black, red, or green.)", 'color': ['W'], 'mana_cost': '3WW'}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c383395(card.Card):
    "Spirit Bonds"
    def __init__(self):
        super(c383395, self).__init__(gameobject.Characteristics(**{'name': 'Spirit Bonds', 'text': 'Whenever a nontoken creature enters the battlefield under your control, you may pay {W}. If you do, create a 1/1 white Spirit creature token with flying.\n{1}{W}, Sacrifice a Spirit: Target non-Spirit creature gains indestructible until end of turn. (Damage and effects that say "destroy" don\'t destroy it.)', 'color': ['W'], 'mana_cost': '1W'}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c383407(card.Card):
    "Sungrace Pegasus"
    def __init__(self):
        super(c383407, self).__init__(gameobject.Characteristics(**{'name': 'Sungrace Pegasus', 'subtype': ['Pegasus'], 'mana_cost': '1W', 'text': "Flying (This creature can't be blocked except by creatures with flying or reach.)\nLifelink (Damage dealt by this creature also causes you to gain that much life.)", 'toughness': 2, 'power': 1, 'color': ['W']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Flying, abilities.StaticAbilities.Lifelink]))

class c383414(card.Card):
    "Tireless Missionaries"
    def __init__(self):
        super(c383414, self).__init__(gameobject.Characteristics(**{'name': 'Tireless Missionaries', 'subtype': ['Human', 'Cleric'], 'mana_cost': '4W', 'text': 'When Tireless Missionaries enters the battlefield, you gain 3 life.', 'toughness': 3, 'power': 2, 'color': ['W']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383418(card.Card):
    "Triplicate Spirits"
    def __init__(self):
        super(c383418, self).__init__(gameobject.Characteristics(**{'name': 'Triplicate Spirits', 'text': "Convoke (Your creatures can help cast this spell. Each creature you tap while casting this spell pays for {1} or one mana of that creature's color.)\nCreate three 1/1 white Spirit creature tokens with flying. (They can't be blocked except by creatures with flying or reach.)", 'color': ['W'], 'mana_cost': '4WW'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[abilities.StaticAbilities.Convoke]))

class c383430(card.Card):
    "Wall of Essence"
    def __init__(self):
        super(c383430, self).__init__(gameobject.Characteristics(**{'name': 'Wall of Essence', 'subtype': ['Wall'], 'mana_cost': '1W', 'text': "Defender (This creature can't attack.)\nWhenever Wall of Essence is dealt combat damage, you gain that much life.", 'toughness': 4, 'power': 0, 'color': ['W']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Defender]))

class c383435(card.Card):
    "Warden of the Beyond"
    def __init__(self):
        super(c383435, self).__init__(gameobject.Characteristics(**{'name': 'Warden of the Beyond', 'subtype': ['Human', 'Wizard'], 'mana_cost': '2W', 'text': "Vigilance (Attacking doesn't cause this creature to tap.)\nWarden of the Beyond gets +2/+2 as long as an opponent owns a card in exile.", 'toughness': 2, 'power': 2, 'color': ['W']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Vigilance]))

class c383177(card.Card):
    "Aeronaut Tinkerer"
    def __init__(self):
        super(c383177, self).__init__(gameobject.Characteristics(**{'name': 'Aeronaut Tinkerer', 'subtype': ['Human', 'Artificer'], 'mana_cost': '2U', 'text': "Aeronaut Tinkerer has flying as long as you control an artifact. (It can't be blocked except by creatures with flying or reach.)", 'toughness': 3, 'power': 2, 'color': ['U']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383178(card.Card):
    "Aetherspouts"
    def __init__(self):
        super(c383178, self).__init__(gameobject.Characteristics(**{'name': 'Aetherspouts', 'text': 'For each attacking creature, its owner puts it on the top or bottom of his or her library.', 'color': ['U'], 'mana_cost': '3UU'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c383183(card.Card):
    "Amphin Pathmage"
    def __init__(self):
        super(c383183, self).__init__(gameobject.Characteristics(**{'name': 'Amphin Pathmage', 'subtype': ['Salamander', 'Wizard'], 'mana_cost': '3U', 'text': "{2}{U}: Target creature can't be blocked this turn.", 'toughness': 2, 'power': 3, 'color': ['U']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383206(card.Card):
    "Chasm Skulker"
    def __init__(self):
        super(c383206, self).__init__(gameobject.Characteristics(**{'name': 'Chasm Skulker', 'subtype': ['Squid', 'Horror'], 'mana_cost': '2U', 'text': "Whenever you draw a card, put a +1/+1 counter on Chasm Skulker.\nWhen Chasm Skulker dies, create X 1/1 blue Squid creature tokens with islandwalk, where X is the number of +1/+1 counters on Chasm Skulker. (They can't be blocked as long as defending player controls an Island.)", 'toughness': 1, 'power': 1, 'color': ['U']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383207(card.Card):
    "Chief Engineer"
    def __init__(self):
        super(c383207, self).__init__(gameobject.Characteristics(**{'name': 'Chief Engineer', 'subtype': ['Vedalken', 'Artificer'], 'mana_cost': '1U', 'text': "Artifact spells you cast have convoke. (Your creatures can help cast those spells. Each creature you tap while casting an artifact spell pays for {1} or one mana of that creature's color.)", 'toughness': 3, 'power': 1, 'color': ['U']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383210(card.Card):
    "Chronostutter"
    def __init__(self):
        super(c383210, self).__init__(gameobject.Characteristics(**{'name': 'Chronostutter', 'text': "Put target creature into its owner's library second from the top.", 'color': ['U'], 'mana_cost': '5U'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c383216(card.Card):
    "Coral Barrier"
    def __init__(self):
        super(c383216, self).__init__(gameobject.Characteristics(**{'name': 'Coral Barrier', 'subtype': ['Wall'], 'mana_cost': '2U', 'text': "Defender (This creature can't attack.)\nWhen Coral Barrier enters the battlefield, create a 1/1 blue Squid creature token with islandwalk. (It can't be blocked as long as defending player controls an Island.)", 'toughness': 3, 'power': 1, 'color': ['U']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Defender]))

class c383225(card.Card):
    "Diffusion Sliver"
    def __init__(self):
        super(c383225, self).__init__(gameobject.Characteristics(**{'name': 'Diffusion Sliver', 'subtype': ['Sliver'], 'mana_cost': '1U', 'text': 'Whenever a Sliver creature you control becomes the target of a spell or ability an opponent controls, counter that spell or ability unless its controller pays {2}.', 'toughness': 1, 'power': 1, 'color': ['U']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383226(card.Card):
    "Dissipate"
    def __init__(self):
        super(c383226, self).__init__(gameobject.Characteristics(**{'name': 'Dissipate', 'text': "Counter target spell. If that spell is countered this way, exile it instead of putting it into its owner's graveyard.", 'color': ['U'], 'mana_cost': '1UU'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c383227(card.Card):
    "Divination"
    def __init__(self):
        super(c383227, self).__init__(gameobject.Characteristics(**{'name': 'Divination', 'text': 'Draw two cards.', 'color': ['U'], 'mana_cost': '2U'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c383230(card.Card):
    "Encrust"
    def __init__(self):
        super(c383230, self).__init__(gameobject.Characteristics(**{'subtype': ['Aura'], 'name': 'Encrust', 'text': "Enchant artifact or creature\nEnchanted permanent doesn't untap during its controller's untap step and its activated abilities can't be activated.", 'color': ['U'], 'mana_cost': '1UU'}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c383232(card.Card):
    "Ensoul Artifact"
    def __init__(self):
        super(c383232, self).__init__(gameobject.Characteristics(**{'subtype': ['Aura'], 'name': 'Ensoul Artifact', 'text': 'Enchant artifact\nEnchanted artifact is a creature with base power and toughness 5/5 in addition to its other types.', 'color': ['U'], 'mana_cost': '1U'}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c383248(card.Card):
    "Frost Lynx"
    def __init__(self):
        super(c383248, self).__init__(gameobject.Characteristics(**{'name': 'Frost Lynx', 'subtype': ['Elemental', 'Cat'], 'mana_cost': '2U', 'text': "When Frost Lynx enters the battlefield, tap target creature an opponent controls. That creature doesn't untap during its controller's next untap step.", 'toughness': 2, 'power': 2, 'color': ['U']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383249(card.Card):
    "Fugitive Wizard"
    def __init__(self):
        super(c383249, self).__init__(gameobject.Characteristics(**{'name': 'Fugitive Wizard', 'subtype': ['Human', 'Wizard'], 'mana_cost': 'U', 'text': '', 'toughness': 1, 'power': 1, 'color': ['U']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383256(card.Card):
    "Glacial Crasher"
    def __init__(self):
        super(c383256, self).__init__(gameobject.Characteristics(**{'name': 'Glacial Crasher', 'subtype': ['Elemental'], 'mana_cost': '4UU', 'text': "Trample (This creature can deal excess combat damage to defending player or planeswalker while attacking.)\nGlacial Crasher can't attack unless there is a Mountain on the battlefield.", 'toughness': 5, 'power': 5, 'color': ['U']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Trample]))

class c383273(card.Card):
    "Hydrosurge"
    def __init__(self):
        super(c383273, self).__init__(gameobject.Characteristics(**{'name': 'Hydrosurge', 'text': 'Target creature gets -5/-0 until end of turn.', 'color': ['U'], 'mana_cost': 'U'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c383274(card.Card):
    "Illusory Angel"
    def __init__(self):
        super(c383274, self).__init__(gameobject.Characteristics(**{'name': 'Illusory Angel', 'subtype': ['Angel', 'Illusion'], 'mana_cost': '2U', 'text': "Flying\nCast Illusory Angel only if you've cast another spell this turn.", 'toughness': 4, 'power': 4, 'color': ['U']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Flying]))

class c383278(card.Card):
    "Into the Void"
    def __init__(self):
        super(c383278, self).__init__(gameobject.Characteristics(**{'name': 'Into the Void', 'text': "Return up to two target creatures to their owners' hands.", 'color': ['U'], 'mana_cost': '3U'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c383280(card.Card):
    "Invisibility"
    def __init__(self):
        super(c383280, self).__init__(gameobject.Characteristics(**{'subtype': ['Aura'], 'name': 'Invisibility', 'text': "Enchant creature\nEnchanted creature can't be blocked except by Walls.", 'color': ['U'], 'mana_cost': 'UU'}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c383285(card.Card):
    "Jace, the Living Guildpact"
    def __init__(self):
        super(c383285, self).__init__(gameobject.Characteristics(**{'subtype': ['Jace'], 'name': 'Jace, the Living Guildpact', 'text': "+1: Look at the top two cards of your library. Put one of them into your graveyard.\n−3: Return another target nonland permanent to its owner's hand.\n−8: Each player shuffles his or her hand and graveyard into his or her library. You draw seven cards.", 'color': ['U'], 'mana_cost': '2UU'}, supertype=[], types=[cardtype.CardType.PLANESWALKER], abilities=[]))

class c383286(card.Card):
    "Jace's Ingenuity"
    def __init__(self):
        super(c383286, self).__init__(gameobject.Characteristics(**{'name': "Jace's Ingenuity", 'text': 'Draw three cards.', 'color': ['U'], 'mana_cost': '3UU'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c383287(card.Card):
    "Jalira, Master Polymorphist"
    def __init__(self):
        super(c383287, self).__init__(gameobject.Characteristics(**{'name': 'Jalira, Master Polymorphist', 'subtype': ['Human', 'Wizard'], 'mana_cost': '3U', 'text': '{2}{U}, {T}, Sacrifice another creature: Reveal cards from the top of your library until you reveal a nonlegendary creature card. Put that card onto the battlefield and the rest on the bottom of your library in a random order.', 'toughness': 2, 'power': 2, 'color': ['U']}, supertype=[cardtype.SuperType.LEGENDARY], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383288(card.Card):
    "Jorubai Murk Lurker"
    def __init__(self):
        super(c383288, self).__init__(gameobject.Characteristics(**{'name': 'Jorubai Murk Lurker', 'subtype': ['Leech'], 'mana_cost': '2U', 'text': 'Jorubai Murk Lurker gets +1/+1 as long as you control a Swamp.\n{1}{B}: Target creature gains lifelink until end of turn. (Damage dealt by the creature also causes its controller to gain that much life.)', 'toughness': 3, 'power': 1, 'color': ['U', 'B']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383291(card.Card):
    "Kapsho Kitefins"
    def __init__(self):
        super(c383291, self).__init__(gameobject.Characteristics(**{'name': 'Kapsho Kitefins', 'subtype': ['Fish'], 'mana_cost': '4UU', 'text': 'Flying\nWhenever Kapsho Kitefins or another creature enters the battlefield under your control, tap target creature an opponent controls.', 'toughness': 3, 'power': 3, 'color': ['U']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Flying]))

class c383305(card.Card):
    "Master of Predicaments"
    def __init__(self):
        super(c383305, self).__init__(gameobject.Characteristics(**{'name': 'Master of Predicaments', 'subtype': ['Sphinx'], 'mana_cost': '3UU', 'text': "Flying\nWhenever Master of Predicaments deals combat damage to a player, choose a card in your hand. That player guesses whether the card's converted mana cost is greater than 4. If the player guessed wrong, you may cast the card without paying its mana cost.", 'toughness': 4, 'power': 4, 'color': ['U']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Flying]))

class c383307(card.Card):
    "Mercurial Pretender"
    def __init__(self):
        super(c383307, self).__init__(gameobject.Characteristics(**{'name': 'Mercurial Pretender', 'subtype': ['Shapeshifter'], 'mana_cost': '4U', 'text': 'You may have Mercurial Pretender enter the battlefield as a copy of any creature you control, except it gains "{2}{U}{U}: Return this creature to its owner\'s hand."', 'toughness': 0, 'power': 0, 'color': ['U']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383311(card.Card):
    "Military Intelligence"
    def __init__(self):
        super(c383311, self).__init__(gameobject.Characteristics(**{'name': 'Military Intelligence', 'text': 'Whenever you attack with two or more creatures, draw a card.', 'color': ['U'], 'mana_cost': '1U'}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c383313(card.Card):
    "Mind Sculpt"
    def __init__(self):
        super(c383313, self).__init__(gameobject.Characteristics(**{'name': 'Mind Sculpt', 'text': 'Target opponent puts the top seven cards of his or her library into his or her graveyard.', 'color': ['U'], 'mana_cost': '1U'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c383324(card.Card):
    "Negate"
    def __init__(self):
        super(c383324, self).__init__(gameobject.Characteristics(**{'name': 'Negate', 'text': 'Counter target noncreature spell.', 'color': ['U'], 'mana_cost': '1U'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c383327(card.Card):
    "Nimbus of the Isles"
    def __init__(self):
        super(c383327, self).__init__(gameobject.Characteristics(**{'name': 'Nimbus of the Isles', 'subtype': ['Elemental'], 'mana_cost': '4U', 'text': "Flying (This creature can't be blocked except by creatures with flying or reach.)", 'toughness': 3, 'power': 3, 'color': ['U']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Flying]))

class c383338(card.Card):
    "Paragon of Gathering Mists"
    def __init__(self):
        super(c383338, self).__init__(gameobject.Characteristics(**{'name': 'Paragon of Gathering Mists', 'subtype': ['Human', 'Wizard'], 'mana_cost': '3U', 'text': 'Other blue creatures you control get +1/+1.\n{U}, {T}: Another target blue creature you control gains flying until end of turn.', 'toughness': 2, 'power': 2, 'color': ['U']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383341(card.Card):
    "Peel from Reality"
    def __init__(self):
        super(c383341, self).__init__(gameobject.Characteristics(**{'name': 'Peel from Reality', 'text': "Return target creature you control and target creature you don't control to their owners' hands.", 'color': ['U'], 'mana_cost': '1U'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c383351(card.Card):
    "Polymorphist's Jest"
    def __init__(self):
        super(c383351, self).__init__(gameobject.Characteristics(**{'name': "Polymorphist's Jest", 'text': 'Until end of turn, each creature target player controls loses all abilities and becomes a blue Frog with base power and toughness 1/1.', 'color': ['U'], 'mana_cost': '1UU'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c383354(card.Card):
    "Quickling"
    def __init__(self):
        super(c383354, self).__init__(gameobject.Characteristics(**{'name': 'Quickling', 'subtype': ['Faerie', 'Rogue'], 'mana_cost': '1U', 'text': "Flash (You may cast this spell any time you could cast an instant.)\nFlying\nWhen Quickling enters the battlefield, sacrifice it unless you return another creature you control to its owner's hand.", 'toughness': 2, 'power': 2, 'color': ['U']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Flash, abilities.StaticAbilities.Flying]))

class c383360(card.Card):
    "Research Assistant"
    def __init__(self):
        super(c383360, self).__init__(gameobject.Characteristics(**{'name': 'Research Assistant', 'subtype': ['Human', 'Wizard'], 'mana_cost': '1U', 'text': '{3}{U}, {T}: Draw a card, then discard a card.', 'toughness': 3, 'power': 1, 'color': ['U']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383389(card.Card):
    "Soul of Ravnica"
    def __init__(self):
        super(c383389, self).__init__(gameobject.Characteristics(**{'name': 'Soul of Ravnica', 'subtype': ['Avatar'], 'mana_cost': '4UU', 'text': 'Flying\n{5}{U}{U}: Draw a card for each color among permanents you control.\n{5}{U}{U}, Exile Soul of Ravnica from your graveyard: Draw a card for each color among permanents you control.', 'toughness': 6, 'power': 6, 'color': ['U']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Flying]))

class c383403(card.Card):
    "Statute of Denial"
    def __init__(self):
        super(c383403, self).__init__(gameobject.Characteristics(**{'name': 'Statute of Denial', 'text': 'Counter target spell. If you control a blue creature, draw a card, then discard a card.', 'color': ['U'], 'mana_cost': '2UU'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c383405(card.Card):
    "Stormtide Leviathan"
    def __init__(self):
        super(c383405, self).__init__(gameobject.Characteristics(**{'name': 'Stormtide Leviathan', 'subtype': ['Leviathan'], 'mana_cost': '5UUU', 'text': "Islandwalk (This creature can't be blocked as long as defending player controls an Island.)\nAll lands are Islands in addition to their other types.\nCreatures without flying or islandwalk can't attack.", 'toughness': 8, 'power': 8, 'color': ['U']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Islandwalk]))

class c383419(card.Card):
    "Turn to Frog"
    def __init__(self):
        super(c383419, self).__init__(gameobject.Characteristics(**{'name': 'Turn to Frog', 'text': 'Until end of turn, target creature loses all abilities and becomes a blue Frog with base power and toughness 1/1.', 'color': ['U'], 'mana_cost': '1U'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c383429(card.Card):
    "Void Snare"
    def __init__(self):
        super(c383429, self).__init__(gameobject.Characteristics(**{'name': 'Void Snare', 'text': "Return target nonland permanent to its owner's hand.", 'color': ['U'], 'mana_cost': 'U'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c383432(card.Card):
    "Wall of Frost"
    def __init__(self):
        super(c383432, self).__init__(gameobject.Characteristics(**{'name': 'Wall of Frost', 'subtype': ['Wall'], 'mana_cost': '1UU', 'text': "Defender\nWhenever Wall of Frost blocks a creature, that creature doesn't untap during its controller's next untap step.", 'toughness': 7, 'power': 0, 'color': ['U']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Defender]))

class c383437(card.Card):
    "Welkin Tern"
    def __init__(self):
        super(c383437, self).__init__(gameobject.Characteristics(**{'name': 'Welkin Tern', 'subtype': ['Bird'], 'mana_cost': '1U', 'text': "Flying (This creature can't be blocked except by creatures with flying or reach.)\nWelkin Tern can block only creatures with flying.", 'toughness': 1, 'power': 2, 'color': ['U']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Flying]))

class c383175(card.Card):
    "Accursed Spirit"
    def __init__(self):
        super(c383175, self).__init__(gameobject.Characteristics(**{'name': 'Accursed Spirit', 'subtype': ['Spirit'], 'mana_cost': '3B', 'text': "Intimidate (This creature can't be blocked except by artifact creatures and/or creatures that share a color with it.)", 'toughness': 2, 'power': 3, 'color': ['B']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Intimidate]))

class c383191(card.Card):
    "Black Cat"
    def __init__(self):
        super(c383191, self).__init__(gameobject.Characteristics(**{'name': 'Black Cat', 'subtype': ['Zombie', 'Cat'], 'mana_cost': '1B', 'text': 'When Black Cat dies, target opponent discards a card at random.', 'toughness': 1, 'power': 1, 'color': ['B']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383193(card.Card):
    "Blood Host"
    def __init__(self):
        super(c383193, self).__init__(gameobject.Characteristics(**{'name': 'Blood Host', 'subtype': ['Vampire'], 'mana_cost': '3BB', 'text': '{1}{B}, Sacrifice another creature: Put a +1/+1 counter on Blood Host and you gain 2 life.', 'toughness': 3, 'power': 3, 'color': ['B']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383201(card.Card):
    "Carrion Crow"
    def __init__(self):
        super(c383201, self).__init__(gameobject.Characteristics(**{'name': 'Carrion Crow', 'subtype': ['Zombie', 'Bird'], 'mana_cost': '2B', 'text': "Flying (This creature can't be blocked except by creatures with flying or reach.)\nCarrion Crow enters the battlefield tapped.", 'toughness': 2, 'power': 2, 'color': ['B']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Flying]))

class c383202(card.Card):
    "Caustic Tar"
    def __init__(self):
        super(c383202, self).__init__(gameobject.Characteristics(**{'subtype': ['Aura'], 'name': 'Caustic Tar', 'text': 'Enchant land\nEnchanted land has "{T}: Target player loses 3 life."', 'color': ['B'], 'mana_cost': '4BB'}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c383208(card.Card):
    "Child of Night"
    def __init__(self):
        super(c383208, self).__init__(gameobject.Characteristics(**{'name': 'Child of Night', 'subtype': ['Vampire'], 'mana_cost': '1B', 'text': 'Lifelink (Damage dealt by this creature also causes you to gain that much life.)', 'toughness': 1, 'power': 2, 'color': ['B']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Lifelink]))

class c383217(card.Card):
    "Covenant of Blood"
    def __init__(self):
        super(c383217, self).__init__(gameobject.Characteristics(**{'name': 'Covenant of Blood', 'text': "Convoke (Your creatures can help cast this spell. Each creature you tap while casting this spell pays for {1} or one mana of that creature's color.)\nCovenant of Blood deals 4 damage to target creature or player and you gain 4 life.", 'color': ['B'], 'mana_cost': '6B'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[abilities.StaticAbilities.Convoke]))

class c383218(card.Card):
    "Crippling Blight"
    def __init__(self):
        super(c383218, self).__init__(gameobject.Characteristics(**{'subtype': ['Aura'], 'name': 'Crippling Blight', 'text': "Enchant creature\nEnchanted creature gets -1/-1 and can't block.", 'color': ['B'], 'mana_cost': 'B'}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c383221(card.Card):
    "Cruel Sadist"
    def __init__(self):
        super(c383221, self).__init__(gameobject.Characteristics(**{'name': 'Cruel Sadist', 'subtype': ['Human', 'Assassin'], 'mana_cost': 'B', 'text': '{B}, {T}, Pay 1 life: Put a +1/+1 counter on Cruel Sadist.\n{2}{B}, {T}, Remove X +1/+1 counters from Cruel Sadist: Cruel Sadist deals X damage to target creature.', 'toughness': 1, 'power': 1, 'color': ['B']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383231(card.Card):
    "Endless Obedience"
    def __init__(self):
        super(c383231, self).__init__(gameobject.Characteristics(**{'name': 'Endless Obedience', 'text': "Convoke (Your creatures can help cast this spell. Each creature you tap while casting this spell pays for {1} or one mana of that creature's color.)\nPut target creature card from a graveyard onto the battlefield under your control.", 'color': ['B'], 'mana_cost': '4BB'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[abilities.StaticAbilities.Convoke]))

class c383234(card.Card):
    "Eternal Thirst"
    def __init__(self):
        super(c383234, self).__init__(gameobject.Characteristics(**{'subtype': ['Aura'], 'name': 'Eternal Thirst', 'text': 'Enchant creature\nEnchanted creature has lifelink and "Whenever a creature an opponent controls dies, put a +1/+1 counter on this creature." (Damage dealt by a creature with lifelink also causes its controller to gain that much life.)', 'color': ['B'], 'mana_cost': '1B'}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c383236(card.Card):
    "Feast on the Fallen"
    def __init__(self):
        super(c383236, self).__init__(gameobject.Characteristics(**{'name': 'Feast on the Fallen', 'text': 'At the beginning of each upkeep, if an opponent lost life last turn, put a +1/+1 counter on target creature you control.', 'color': ['B'], 'mana_cost': '2B'}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c383238(card.Card):
    "Festergloom"
    def __init__(self):
        super(c383238, self).__init__(gameobject.Characteristics(**{'name': 'Festergloom', 'text': 'Nonblack creatures get -1/-1 until end of turn.', 'color': ['B'], 'mana_cost': '2B'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c383240(card.Card):
    "Flesh to Dust"
    def __init__(self):
        super(c383240, self).__init__(gameobject.Characteristics(**{'name': 'Flesh to Dust', 'text': "Destroy target creature. It can't be regenerated.", 'color': ['B'], 'mana_cost': '3BB'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c383260(card.Card):
    "Gravedigger"
    def __init__(self):
        super(c383260, self).__init__(gameobject.Characteristics(**{'name': 'Gravedigger', 'subtype': ['Zombie'], 'mana_cost': '3B', 'text': 'When Gravedigger enters the battlefield, you may return target creature card from your graveyard to your hand.', 'toughness': 2, 'power': 2, 'color': ['B']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383275(card.Card):
    "In Garruk's Wake"
    def __init__(self):
        super(c383275, self).__init__(gameobject.Characteristics(**{'name': "In Garruk's Wake", 'text': "Destroy all creatures you don't control and all planeswalkers you don't control.", 'color': ['B'], 'mana_cost': '7BB'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c383276(card.Card):
    "Indulgent Tormentor"
    def __init__(self):
        super(c383276, self).__init__(gameobject.Characteristics(**{'name': 'Indulgent Tormentor', 'subtype': ['Demon'], 'mana_cost': '3BB', 'text': 'Flying\nAt the beginning of your upkeep, draw a card unless target opponent sacrifices a creature or pays 3 life.', 'toughness': 3, 'power': 5, 'color': ['B']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Flying]))

class c383297(card.Card):
    "Leeching Sliver"
    def __init__(self):
        super(c383297, self).__init__(gameobject.Characteristics(**{'name': 'Leeching Sliver', 'subtype': ['Sliver'], 'mana_cost': '1B', 'text': 'Whenever a Sliver you control attacks, defending player loses 1 life.', 'toughness': 1, 'power': 1, 'color': ['B']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383300(card.Card):
    "Liliana Vess"
    def __init__(self):
        super(c383300, self).__init__(gameobject.Characteristics(**{'subtype': ['Liliana'], 'name': 'Liliana Vess', 'text': '+1: Target player discards a card.\n−2: Search your library for a card, then shuffle your library and put that card on top of it.\n−8: Put all creature cards from all graveyards onto the battlefield under your control.', 'color': ['B'], 'mana_cost': '3BB'}, supertype=[], types=[cardtype.CardType.PLANESWALKER], abilities=[]))

class c383312(card.Card):
    "Mind Rot"
    def __init__(self):
        super(c383312, self).__init__(gameobject.Characteristics(**{'name': 'Mind Rot', 'text': 'Target player discards two cards.', 'color': ['B'], 'mana_cost': '2B'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c383320(card.Card):
    "Necrobite"
    def __init__(self):
        super(c383320, self).__init__(gameobject.Characteristics(**{'name': 'Necrobite', 'text': "Target creature gains deathtouch until end of turn. Regenerate it. (The next time that creature would be destroyed this turn, it isn't. Instead tap it, remove all damage from it, and remove it from combat. Any amount of damage a creature with deathtouch deals to a creature is enough to destroy it.)", 'color': ['B'], 'mana_cost': '2B'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c383321(card.Card):
    "Necrogen Scudder"
    def __init__(self):
        super(c383321, self).__init__(gameobject.Characteristics(**{'name': 'Necrogen Scudder', 'subtype': ['Horror'], 'mana_cost': '2B', 'text': 'Flying\nWhen Necrogen Scudder enters the battlefield, you lose 3 life.', 'toughness': 3, 'power': 3, 'color': ['B']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Flying]))

class c383322(card.Card):
    "Necromancer's Assistant"
    def __init__(self):
        super(c383322, self).__init__(gameobject.Characteristics(**{'name': "Necromancer's Assistant", 'subtype': ['Zombie'], 'mana_cost': '2B', 'text': "When Necromancer's Assistant enters the battlefield, put the top three cards of your library into your graveyard.", 'toughness': 1, 'power': 3, 'color': ['B']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383323(card.Card):
    "Necromancer's Stockpile"
    def __init__(self):
        super(c383323, self).__init__(gameobject.Characteristics(**{'name': "Necromancer's Stockpile", 'text': '{1}{B}, Discard a creature card: Draw a card. If the discarded card was a Zombie card, create a tapped 2/2 black Zombie creature token.', 'color': ['B'], 'mana_cost': '1B'}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c383326(card.Card):
    "Nightfire Giant"
    def __init__(self):
        super(c383326, self).__init__(gameobject.Characteristics(**{'name': 'Nightfire Giant', 'subtype': ['Zombie', 'Giant'], 'mana_cost': '4B', 'text': 'Nightfire Giant gets +1/+1 as long as you control a Mountain.\n{4}{R}: Nightfire Giant deals 2 damage to target creature or player.', 'toughness': 3, 'power': 4, 'color': ['B', 'R']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383330(card.Card):
    "Ob Nixilis, Unshackled"
    def __init__(self):
        super(c383330, self).__init__(gameobject.Characteristics(**{'name': 'Ob Nixilis, Unshackled', 'subtype': ['Demon'], 'mana_cost': '4BB', 'text': 'Flying, trample\nWhenever an opponent searches his or her library, that player sacrifices a creature and loses 10 life.\nWhenever another creature dies, put a +1/+1 counter on Ob Nixilis, Unshackled.', 'toughness': 4, 'power': 4, 'color': ['B']}, supertype=[cardtype.SuperType.LEGENDARY], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Flying, abilities.StaticAbilities.Trample]))

class c383340(card.Card):
    "Paragon of Open Graves"
    def __init__(self):
        super(c383340, self).__init__(gameobject.Characteristics(**{'name': 'Paragon of Open Graves', 'subtype': ['Skeleton', 'Warrior'], 'mana_cost': '3B', 'text': 'Other black creatures you control get +1/+1.\n{2}{B}, {T}: Another target black creature you control gains deathtouch until end of turn. (Any amount of damage it deals to a creature is enough to destroy it.)', 'toughness': 2, 'power': 2, 'color': ['B']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383366(card.Card):
    "Rotfeaster Maggot"
    def __init__(self):
        super(c383366, self).__init__(gameobject.Characteristics(**{'name': 'Rotfeaster Maggot', 'subtype': ['Insect'], 'mana_cost': '4B', 'text': "When Rotfeaster Maggot enters the battlefield, exile target creature card from a graveyard. You gain life equal to that card's toughness.", 'toughness': 5, 'power': 3, 'color': ['B']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383376(card.Card):
    "Shadowcloak Vampire"
    def __init__(self):
        super(c383376, self).__init__(gameobject.Characteristics(**{'name': 'Shadowcloak Vampire', 'subtype': ['Vampire'], 'mana_cost': '4B', 'text': "Pay 2 life: Shadowcloak Vampire gains flying until end of turn. (It can't be blocked except by creatures with flying or reach.)", 'toughness': 3, 'power': 4, 'color': ['B']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383383(card.Card):
    "Sign in Blood"
    def __init__(self):
        super(c383383, self).__init__(gameobject.Characteristics(**{'name': 'Sign in Blood', 'text': 'Target player draws two cards and loses 2 life.', 'color': ['B'], 'mana_cost': 'BB'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c383387(card.Card):
    "Soul of Innistrad"
    def __init__(self):
        super(c383387, self).__init__(gameobject.Characteristics(**{'name': 'Soul of Innistrad', 'subtype': ['Avatar'], 'mana_cost': '4BB', 'text': 'Deathtouch\n{3}{B}{B}: Return up to three target creature cards from your graveyard to your hand.\n{3}{B}{B}, Exile Soul of Innistrad from your graveyard: Return up to three target creature cards from your graveyard to your hand.', 'toughness': 6, 'power': 6, 'color': ['B']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Deathtouch]))

class c383396(card.Card):
    "Stab Wound"
    def __init__(self):
        super(c383396, self).__init__(gameobject.Characteristics(**{'subtype': ['Aura'], 'name': 'Stab Wound', 'text': "Enchant creature\nEnchanted creature gets -2/-2.\nAt the beginning of the upkeep of enchanted creature's controller, that player loses 2 life.", 'color': ['B'], 'mana_cost': '2B'}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c383402(card.Card):
    "Stain the Mind"
    def __init__(self):
        super(c383402, self).__init__(gameobject.Characteristics(**{'name': 'Stain the Mind', 'text': "Convoke (Your creatures can help cast this spell. Each creature you tap while casting this spell pays for {1} or one mana of that creature's color.)\nChoose a nonland card name. Search target player's graveyard, hand, and library for any number of cards with that name and exile them. Then that player shuffles his or her library.", 'color': ['B'], 'mana_cost': '4B'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[abilities.StaticAbilities.Convoke]))

class c383420(card.Card):
    "Typhoid Rats"
    def __init__(self):
        super(c383420, self).__init__(gameobject.Characteristics(**{'name': 'Typhoid Rats', 'subtype': ['Rat'], 'mana_cost': 'B', 'text': 'Deathtouch (Any amount of damage this deals to a creature is enough to destroy it.)', 'toughness': 1, 'power': 1, 'color': ['B']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Deathtouch]))

class c383422(card.Card):
    "Ulcerate"
    def __init__(self):
        super(c383422, self).__init__(gameobject.Characteristics(**{'name': 'Ulcerate', 'text': 'Target creature gets -3/-3 until end of turn. You lose 3 life.', 'color': ['B'], 'mana_cost': 'B'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c383424(card.Card):
    "Unmake the Graves"
    def __init__(self):
        super(c383424, self).__init__(gameobject.Characteristics(**{'name': 'Unmake the Graves', 'text': "Convoke (Your creatures can help cast this spell. Each creature you tap while casting this spell pays for {1} or one mana of that creature's color.)\nReturn up to two target creature cards from your graveyard to your hand.", 'color': ['B'], 'mana_cost': '4B'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[abilities.StaticAbilities.Convoke]))

class c383433(card.Card):
    "Wall of Limbs"
    def __init__(self):
        super(c383433, self).__init__(gameobject.Characteristics(**{'name': 'Wall of Limbs', 'subtype': ['Zombie', 'Wall'], 'mana_cost': '2B', 'text': "Defender (This creature can't attack.)\nWhenever you gain life, put a +1/+1 counter on Wall of Limbs.\n{5}{B}{B}, Sacrifice Wall of Limbs: Target player loses X life, where X is Wall of Limbs's power.", 'toughness': 3, 'power': 0, 'color': ['B']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Defender]))

class c383436(card.Card):
    "Waste Not"
    def __init__(self):
        super(c383436, self).__init__(gameobject.Characteristics(**{'name': 'Waste Not', 'text': 'Whenever an opponent discards a creature card, create a 2/2 black Zombie creature token.\nWhenever an opponent discards a land card, add {B}{B} to your mana pool.\nWhenever an opponent discards a noncreature, nonland card, draw a card.', 'color': ['B'], 'mana_cost': '1B'}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c383439(card.Card):
    "Witch's Familiar"
    def __init__(self):
        super(c383439, self).__init__(gameobject.Characteristics(**{'name': "Witch's Familiar", 'subtype': ['Frog'], 'mana_cost': '2B', 'text': '', 'toughness': 3, 'power': 2, 'color': ['B']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383440(card.Card):
    "Xathrid Slyblade"
    def __init__(self):
        super(c383440, self).__init__(gameobject.Characteristics(**{'name': 'Xathrid Slyblade', 'subtype': ['Human', 'Assassin'], 'mana_cost': '2B', 'text': "Hexproof (This creature can't be the target of spells or abilities your opponents control.)\n{3}{B}: Until end of turn, Xathrid Slyblade loses hexproof and gains first strike and deathtouch. (It deals combat damage before creatures without first strike. Any amount of damage it deals to a creature is enough to destroy it.)", 'toughness': 1, 'power': 2, 'color': ['B']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Hexproof]))

class c383443(card.Card):
    "Zof Shade"
    def __init__(self):
        super(c383443, self).__init__(gameobject.Characteristics(**{'name': 'Zof Shade', 'subtype': ['Shade'], 'mana_cost': '3B', 'text': '{2}{B}: Zof Shade gets +2/+2 until end of turn.', 'toughness': 2, 'power': 2, 'color': ['B']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383176(card.Card):
    "Act on Impulse"
    def __init__(self):
        super(c383176, self).__init__(gameobject.Characteristics(**{'name': 'Act on Impulse', 'text': 'Exile the top three cards of your library. Until end of turn, you may play cards exiled this way. (If you cast a spell this way, you still pay its costs. You can play a land this way only if you have an available land play remaining.)', 'color': ['R'], 'mana_cost': '2R'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c383179(card.Card):
    "Aggressive Mining"
    def __init__(self):
        super(c383179, self).__init__(gameobject.Characteristics(**{'name': 'Aggressive Mining', 'text': "You can't play lands.\nSacrifice a land: Draw two cards. Activate this ability only once each turn.", 'color': ['R'], 'mana_cost': '3R'}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c383182(card.Card):
    "Altac Bloodseeker"
    def __init__(self):
        super(c383182, self).__init__(gameobject.Characteristics(**{'name': 'Altac Bloodseeker', 'subtype': ['Human', 'Berserker'], 'mana_cost': '1R', 'text': 'Whenever a creature an opponent controls dies, Altac Bloodseeker gets +2/+0 and gains first strike and haste until end of turn. (It deals combat damage before creatures without first strike, and it can attack and {T} as soon as it comes under your control.)', 'toughness': 1, 'power': 2, 'color': ['R']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383190(card.Card):
    "Belligerent Sliver"
    def __init__(self):
        super(c383190, self).__init__(gameobject.Characteristics(**{'name': 'Belligerent Sliver', 'subtype': ['Sliver'], 'mana_cost': '2R', 'text': "Sliver creatures you control have menace. (They can't be blocked except by two or more creatures.)", 'toughness': 2, 'power': 2, 'color': ['R']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383192(card.Card):
    "Blastfire Bolt"
    def __init__(self):
        super(c383192, self).__init__(gameobject.Characteristics(**{'name': 'Blastfire Bolt', 'text': 'Blastfire Bolt deals 5 damage to target creature. Destroy all Equipment attached to that creature.', 'color': ['R'], 'mana_cost': '5R'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c383195(card.Card):
    "Borderland Marauder"
    def __init__(self):
        super(c383195, self).__init__(gameobject.Characteristics(**{'name': 'Borderland Marauder', 'subtype': ['Human', 'Warrior'], 'mana_cost': '1R', 'text': 'Whenever Borderland Marauder attacks, it gets +2/+0 until end of turn.', 'toughness': 2, 'power': 1, 'color': ['R']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383198(card.Card):
    "Brood Keeper"
    def __init__(self):
        super(c383198, self).__init__(gameobject.Characteristics(**{'name': 'Brood Keeper', 'subtype': ['Human', 'Shaman'], 'mana_cost': '3R', 'text': 'Whenever an Aura becomes attached to Brood Keeper, create a 2/2 red Dragon creature token with flying. It has "{R}: This creature gets +1/+0 until end of turn."', 'toughness': 3, 'power': 2, 'color': ['R']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383199(card.Card):
    "Burning Anger"
    def __init__(self):
        super(c383199, self).__init__(gameobject.Characteristics(**{'subtype': ['Aura'], 'name': 'Burning Anger', 'text': 'Enchant creature\nEnchanted creature has "{T}: This creature deals damage equal to its power to target creature or player."', 'color': ['R'], 'mana_cost': '4R'}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c383204(card.Card):
    "Chandra, Pyromaster"
    def __init__(self):
        super(c383204, self).__init__(gameobject.Characteristics(**{'subtype': ['Chandra'], 'name': 'Chandra, Pyromaster', 'text': "+1: Chandra, Pyromaster deals 1 damage to target player and 1 damage to up to one target creature that player controls. That creature can't block this turn.\n0: Exile the top card of your library. You may play it this turn.\n−7: Exile the top ten cards of your library. Choose an instant or sorcery card exiled this way and copy it three times. You may cast the copies without paying their mana costs.", 'color': ['R'], 'mana_cost': '2RR'}, supertype=[], types=[cardtype.CardType.PLANESWALKER], abilities=[]))

class c383211(card.Card):
    "Circle of Flame"
    def __init__(self):
        super(c383211, self).__init__(gameobject.Characteristics(**{'name': 'Circle of Flame', 'text': 'Whenever a creature without flying attacks you or a planeswalker you control, Circle of Flame deals 1 damage to that creature.', 'color': ['R'], 'mana_cost': '1R'}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c383212(card.Card):
    "Clear a Path"
    def __init__(self):
        super(c383212, self).__init__(gameobject.Characteristics(**{'name': 'Clear a Path', 'text': 'Destroy target creature with defender.', 'color': ['R'], 'mana_cost': 'R'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c383213(card.Card):
    "Cone of Flame"
    def __init__(self):
        super(c383213, self).__init__(gameobject.Characteristics(**{'name': 'Cone of Flame', 'text': 'Cone of Flame deals 1 damage to target creature or player, 2 damage to another target creature or player, and 3 damage to a third target creature or player.', 'color': ['R'], 'mana_cost': '3RR'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c383219(card.Card):
    "Crowd's Favor"
    def __init__(self):
        super(c383219, self).__init__(gameobject.Characteristics(**{'name': "Crowd's Favor", 'text': "Convoke (Your creatures can help cast this spell. Each creature you tap while casting this spell pays for {1} or one mana of that creature's color.)\nTarget creature gets +1/+0 and gains first strike until end of turn. (It deals combat damage before creatures without first strike.)", 'color': ['R'], 'mana_cost': 'R'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[abilities.StaticAbilities.Convoke]))

class c383220(card.Card):
    "Crucible of Fire"
    def __init__(self):
        super(c383220, self).__init__(gameobject.Characteristics(**{'name': 'Crucible of Fire', 'text': 'Dragon creatures you control get +3/+3.', 'color': ['R'], 'mana_cost': '3R'}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c383245(card.Card):
    "Forge Devil"
    def __init__(self):
        super(c383245, self).__init__(gameobject.Characteristics(**{'name': 'Forge Devil', 'subtype': ['Devil'], 'mana_cost': 'R', 'text': 'When Forge Devil enters the battlefield, it deals 1 damage to target creature and 1 damage to you.', 'toughness': 1, 'power': 1, 'color': ['R']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383246(card.Card):
    "Foundry Street Denizen"
    def __init__(self):
        super(c383246, self).__init__(gameobject.Characteristics(**{'name': 'Foundry Street Denizen', 'subtype': ['Goblin', 'Warrior'], 'mana_cost': 'R', 'text': 'Whenever another red creature enters the battlefield under your control, Foundry Street Denizen gets +1/+0 until end of turn.', 'toughness': 1, 'power': 1, 'color': ['R']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383247(card.Card):
    "Frenzied Goblin"
    def __init__(self):
        super(c383247, self).__init__(gameobject.Characteristics(**{'name': 'Frenzied Goblin', 'subtype': ['Goblin', 'Berserker'], 'mana_cost': 'R', 'text': "Whenever Frenzied Goblin attacks, you may pay {R}. If you do, target creature can't block this turn.", 'toughness': 1, 'power': 1, 'color': ['R']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383254(card.Card):
    "Generator Servant"
    def __init__(self):
        super(c383254, self).__init__(gameobject.Characteristics(**{'name': 'Generator Servant', 'subtype': ['Elemental'], 'mana_cost': '1R', 'text': '{T}, Sacrifice Generator Servant: Add {C}{C} to your mana pool. If that mana is spent on a creature spell, it gains haste until end of turn. (That creature can attack and {T} as soon as it comes under your control.)', 'toughness': 1, 'power': 2, 'color': ['R']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383257(card.Card):
    "Goblin Kaboomist"
    def __init__(self):
        super(c383257, self).__init__(gameobject.Characteristics(**{'name': 'Goblin Kaboomist', 'subtype': ['Goblin', 'Warrior'], 'mana_cost': '1R', 'text': 'At the beginning of your upkeep, create a colorless artifact token named Land Mine with "{R}, Sacrifice this artifact: This artifact deals 2 damage to target attacking creature without flying." Then flip a coin. If you lose the flip, Goblin Kaboomist deals 2 damage to itself.', 'toughness': 2, 'power': 1, 'color': ['R']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383258(card.Card):
    "Goblin Rabblemaster"
    def __init__(self):
        super(c383258, self).__init__(gameobject.Characteristics(**{'name': 'Goblin Rabblemaster', 'subtype': ['Goblin', 'Warrior'], 'mana_cost': '2R', 'text': 'Other Goblin creatures you control attack each turn if able.\nAt the beginning of combat on your turn, create a 1/1 red Goblin creature token with haste.\nWhenever Goblin Rabblemaster attacks, it gets +1/+0 until end of turn for each other attacking Goblin.', 'toughness': 2, 'power': 2, 'color': ['R']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383259(card.Card):
    "Goblin Roughrider"
    def __init__(self):
        super(c383259, self).__init__(gameobject.Characteristics(**{'name': 'Goblin Roughrider', 'subtype': ['Goblin', 'Knight'], 'mana_cost': '2R', 'text': '', 'toughness': 2, 'power': 3, 'color': ['R']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383262(card.Card):
    "Hammerhand"
    def __init__(self):
        super(c383262, self).__init__(gameobject.Characteristics(**{'subtype': ['Aura'], 'name': 'Hammerhand', 'text': "Enchant creature\nWhen Hammerhand enters the battlefield, target creature can't block this turn.\nEnchanted creature gets +1/+1 and has haste. (It can attack and {T} no matter when it came under your control.)", 'color': ['R'], 'mana_cost': 'R'}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c383264(card.Card):
    "Heat Ray"
    def __init__(self):
        super(c383264, self).__init__(gameobject.Characteristics(**{'name': 'Heat Ray', 'text': 'Heat Ray deals X damage to target creature.', 'color': ['R'], 'mana_cost': 'XR'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c383266(card.Card):
    "Hoarding Dragon"
    def __init__(self):
        super(c383266, self).__init__(gameobject.Characteristics(**{'name': 'Hoarding Dragon', 'subtype': ['Dragon'], 'mana_cost': '3RR', 'text': "Flying\nWhen Hoarding Dragon enters the battlefield, you may search your library for an artifact card, exile it, then shuffle your library.\nWhen Hoarding Dragon dies, you may put the exiled card into its owner's hand.", 'toughness': 4, 'power': 4, 'color': ['R']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Flying]))

class c383277(card.Card):
    "Inferno Fist"
    def __init__(self):
        super(c383277, self).__init__(gameobject.Characteristics(**{'subtype': ['Aura'], 'name': 'Inferno Fist', 'text': 'Enchant creature you control\nEnchanted creature gets +2/+0.\n{R}, Sacrifice Inferno Fist: Inferno Fist deals 2 damage to target creature or player.', 'color': ['R'], 'mana_cost': '1R'}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c383293(card.Card):
    "Kird Chieftain"
    def __init__(self):
        super(c383293, self).__init__(gameobject.Characteristics(**{'name': 'Kird Chieftain', 'subtype': ['Ape'], 'mana_cost': '3R', 'text': 'Kird Chieftain gets +1/+1 as long as you control a Forest.\n{4}{G}: Target creature gets +2/+2 and gains trample until end of turn. (If it would assign enough damage to its blockers to destroy them, you may have it assign the rest of its damage to defending player or planeswalker.)', 'toughness': 3, 'power': 3, 'color': ['R', 'G']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383294(card.Card):
    "Krenko's Enforcer"
    def __init__(self):
        super(c383294, self).__init__(gameobject.Characteristics(**{'name': "Krenko's Enforcer", 'subtype': ['Goblin', 'Warrior'], 'mana_cost': '1RR', 'text': "Intimidate (This creature can't be blocked except by artifact creatures and/or creatures that share a color with it.)", 'toughness': 2, 'power': 2, 'color': ['R']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Intimidate]))

class c383295(card.Card):
    "Kurkesh, Onakke Ancient"
    def __init__(self):
        super(c383295, self).__init__(gameobject.Characteristics(**{'name': 'Kurkesh, Onakke Ancient', 'subtype': ['Ogre', 'Spirit'], 'mana_cost': '2RR', 'text': "Whenever you activate an ability of an artifact, if it isn't a mana ability, you may pay {R}. If you do, copy that ability. You may choose new targets for the copy.", 'toughness': 3, 'power': 4, 'color': ['R']}, supertype=[cardtype.SuperType.LEGENDARY], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383296(card.Card):
    "Lava Axe"
    def __init__(self):
        super(c383296, self).__init__(gameobject.Characteristics(**{'name': 'Lava Axe', 'text': 'Lava Axe deals 5 damage to target player.', 'color': ['R'], 'mana_cost': '4R'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c383299(card.Card):
    "Lightning Strike"
    def __init__(self):
        super(c383299, self).__init__(gameobject.Characteristics(**{'name': 'Lightning Strike', 'text': 'Lightning Strike deals 3 damage to target creature or player.', 'color': ['R'], 'mana_cost': '1R'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c383310(card.Card):
    "Might Makes Right"
    def __init__(self):
        super(c383310, self).__init__(gameobject.Characteristics(**{'name': 'Might Makes Right', 'text': 'At the beginning of combat on your turn, if you control each creature on the battlefield with the greatest power, gain control of target creature an opponent controls until end of turn. Untap that creature. It gains haste until end of turn. (It can attack and {T} this turn.)', 'color': ['R'], 'mana_cost': '5R'}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c383314(card.Card):
    "Miner's Bane"
    def __init__(self):
        super(c383314, self).__init__(gameobject.Characteristics(**{'name': "Miner's Bane", 'subtype': ['Elemental'], 'mana_cost': '4RR', 'text': "{2}{R}: Miner's Bane gets +1/+0 and gains trample until end of turn. (If it would assign enough damage to its blockers to destroy them, you may have it assign the rest of its damage to defending player or planeswalker.)", 'toughness': 3, 'power': 6, 'color': ['R']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383337(card.Card):
    "Paragon of Fierce Defiance"
    def __init__(self):
        super(c383337, self).__init__(gameobject.Characteristics(**{'name': 'Paragon of Fierce Defiance', 'subtype': ['Human', 'Warrior'], 'mana_cost': '3R', 'text': 'Other red creatures you control get +1/+1.\n{R}, {T}: Another target red creature you control gains haste until end of turn. (It can attack and {T} this turn.)', 'toughness': 2, 'power': 2, 'color': ['R']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383367(card.Card):
    "Rummaging Goblin"
    def __init__(self):
        super(c383367, self).__init__(gameobject.Characteristics(**{'name': 'Rummaging Goblin', 'subtype': ['Goblin', 'Rogue'], 'mana_cost': '2R', 'text': '{T}, Discard a card: Draw a card.', 'toughness': 1, 'power': 1, 'color': ['R']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383372(card.Card):
    "Scrapyard Mongrel"
    def __init__(self):
        super(c383372, self).__init__(gameobject.Characteristics(**{'name': 'Scrapyard Mongrel', 'subtype': ['Hound'], 'mana_cost': '3R', 'text': 'As long as you control an artifact, Scrapyard Mongrel gets +2/+0 and has trample. (If it would assign enough damage to its blockers to destroy them, you may have it assign the rest of its damage to defending player or planeswalker.)', 'toughness': 3, 'power': 3, 'color': ['R']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383380(card.Card):
    "Shrapnel Blast"
    def __init__(self):
        super(c383380, self).__init__(gameobject.Characteristics(**{'name': 'Shrapnel Blast', 'text': 'As an additional cost to cast Shrapnel Blast, sacrifice an artifact.\nShrapnel Blast deals 5 damage to target creature or player.', 'color': ['R'], 'mana_cost': '1R'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c383381(card.Card):
    "Siege Dragon"
    def __init__(self):
        super(c383381, self).__init__(gameobject.Characteristics(**{'name': 'Siege Dragon', 'subtype': ['Dragon'], 'mana_cost': '5RR', 'text': 'Flying\nWhen Siege Dragon enters the battlefield, destroy all Walls your opponents control.\nWhenever Siege Dragon attacks, if defending player controls no Walls, it deals 2 damage to each creature without flying that player controls.', 'toughness': 5, 'power': 5, 'color': ['R']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Flying]))

class c383390(card.Card):
    "Soul of Shandalar"
    def __init__(self):
        super(c383390, self).__init__(gameobject.Characteristics(**{'name': 'Soul of Shandalar', 'subtype': ['Avatar'], 'mana_cost': '4RR', 'text': 'First strike\n{3}{R}{R}: Soul of Shandalar deals 3 damage to target player and 3 damage to up to one target creature that player controls.\n{3}{R}{R}, Exile Soul of Shandalar from your graveyard: Soul of Shandalar deals 3 damage to target player and 3 damage to up to one target creature that player controls.', 'toughness': 6, 'power': 6, 'color': ['R']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383404(card.Card):
    "Stoke the Flames"
    def __init__(self):
        super(c383404, self).__init__(gameobject.Characteristics(**{'name': 'Stoke the Flames', 'text': "Convoke (Your creatures can help cast this spell. Each creature you tap while casting this spell pays for {1} or one mana of that creature's color.)\nStoke the Flames deals 4 damage to target creature or player.", 'color': ['R'], 'mana_cost': '2RR'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[abilities.StaticAbilities.Convoke]))

class c383413(card.Card):
    "Thundering Giant"
    def __init__(self):
        super(c383413, self).__init__(gameobject.Characteristics(**{'name': 'Thundering Giant', 'subtype': ['Giant'], 'mana_cost': '3RR', 'text': 'Haste (This creature can attack and {T} as soon as it comes under your control.)', 'toughness': 3, 'power': 4, 'color': ['R']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Haste]))

class c383416(card.Card):
    "Torch Fiend"
    def __init__(self):
        super(c383416, self).__init__(gameobject.Characteristics(**{'name': 'Torch Fiend', 'subtype': ['Devil'], 'mana_cost': '1R', 'text': '{R}, Sacrifice Torch Fiend: Destroy target artifact.', 'toughness': 1, 'power': 2, 'color': ['R']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383431(card.Card):
    "Wall of Fire"
    def __init__(self):
        super(c383431, self).__init__(gameobject.Characteristics(**{'name': 'Wall of Fire', 'subtype': ['Wall'], 'mana_cost': '1RR', 'text': "Defender (This creature can't attack.)\n{R}: Wall of Fire gets +1/+0 until end of turn.", 'toughness': 5, 'power': 0, 'color': ['R']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Defender]))

class c383184(card.Card):
    "Ancient Silverback"
    def __init__(self):
        super(c383184, self).__init__(gameobject.Characteristics(**{'name': 'Ancient Silverback', 'subtype': ['Ape'], 'mana_cost': '4GG', 'text': "{G}: Regenerate Ancient Silverback. (The next time this creature would be destroyed this turn, it isn't. Instead tap it, remove all damage from it, and remove it from combat.)", 'toughness': 5, 'power': 6, 'color': ['G']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383187(card.Card):
    "Back to Nature"
    def __init__(self):
        super(c383187, self).__init__(gameobject.Characteristics(**{'name': 'Back to Nature', 'text': 'Destroy all enchantments.', 'color': ['G'], 'mana_cost': '1G'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c383200(card.Card):
    "Carnivorous Moss-Beast"
    def __init__(self):
        super(c383200, self).__init__(gameobject.Characteristics(**{'name': 'Carnivorous Moss-Beast', 'subtype': ['Plant', 'Elemental', 'Beast'], 'mana_cost': '4GG', 'text': '{5}{G}{G}: Put a +1/+1 counter on Carnivorous Moss-Beast.', 'toughness': 5, 'power': 4, 'color': ['G']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383205(card.Card):
    "Charging Rhino"
    def __init__(self):
        super(c383205, self).__init__(gameobject.Characteristics(**{'name': 'Charging Rhino', 'subtype': ['Rhino'], 'mana_cost': '3GG', 'text': "Charging Rhino can't be blocked by more than one creature.", 'toughness': 4, 'power': 4, 'color': ['G']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383209(card.Card):
    "Chord of Calling"
    def __init__(self):
        super(c383209, self).__init__(gameobject.Characteristics(**{'name': 'Chord of Calling', 'text': "Convoke (Your creatures can help cast this spell. Each creature you tap while casting this spell pays for {1} or one mana of that creature's color.)\nSearch your library for a creature card with converted mana cost X or less and put it onto the battlefield. Then shuffle your library.", 'color': ['G'], 'mana_cost': 'XGGG'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[abilities.StaticAbilities.Convoke]))

class c383229(card.Card):
    "Elvish Mystic"
    def __init__(self):
        super(c383229, self).__init__(gameobject.Characteristics(**{'name': 'Elvish Mystic', 'subtype': ['Elf', 'Druid'], 'mana_cost': 'G', 'text': '{T}: Add {G} to your mana pool.', 'toughness': 1, 'power': 1, 'color': ['G']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383237(card.Card):
    "Feral Incarnation"
    def __init__(self):
        super(c383237, self).__init__(gameobject.Characteristics(**{'name': 'Feral Incarnation', 'text': "Convoke (Your creatures can help cast this spell. Each creature you tap while casting this spell pays for {1} or one mana of that creature's color.)\nCreate three 3/3 green Beast creature tokens.", 'color': ['G'], 'mana_cost': '8G'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[abilities.StaticAbilities.Convoke]))

class c383252(card.Card):
    "Gather Courage"
    def __init__(self):
        super(c383252, self).__init__(gameobject.Characteristics(**{'name': 'Gather Courage', 'text': "Convoke (Your creatures can help cast this spell. Each creature you tap while casting this spell pays for {1} or one mana of that creature's color.)\nTarget creature gets +2/+2 until end of turn.", 'color': ['G'], 'mana_cost': 'G'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[abilities.StaticAbilities.Convoke]))

class c383255(card.Card):
    "Genesis Hydra"
    def __init__(self):
        super(c383255, self).__init__(gameobject.Characteristics(**{'name': 'Genesis Hydra', 'subtype': ['Plant', 'Hydra'], 'mana_cost': 'XGG', 'text': 'When you cast Genesis Hydra, reveal the top X cards of your library. You may put a nonland permanent card with converted mana cost X or less from among them onto the battlefield. Then shuffle the rest into your library.\nGenesis Hydra enters the battlefield with X +1/+1 counters on it.', 'toughness': 0, 'power': 0, 'color': ['G']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383267(card.Card):
    "Hornet Nest"
    def __init__(self):
        super(c383267, self).__init__(gameobject.Characteristics(**{'name': 'Hornet Nest', 'subtype': ['Insect'], 'mana_cost': '2G', 'text': "Defender (This creature can't attack.)\nWhenever Hornet Nest is dealt damage, create that many 1/1 green Insect creature tokens with flying and deathtouch. (Any amount of damage a creature with deathtouch deals to a creature is enough to destroy it.)", 'toughness': 2, 'power': 0, 'color': ['G']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Defender]))

class c383268(card.Card):
    "Hornet Queen"
    def __init__(self):
        super(c383268, self).__init__(gameobject.Characteristics(**{'name': 'Hornet Queen', 'subtype': ['Insect'], 'mana_cost': '4GGG', 'text': 'Flying\nDeathtouch (Any amount of damage this deals to a creature is enough to destroy it.)\nWhen Hornet Queen enters the battlefield, create four 1/1 green Insect creature tokens with flying and deathtouch.', 'toughness': 2, 'power': 2, 'color': ['G']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Deathtouch, abilities.StaticAbilities.Flying]))

class c383270(card.Card):
    "Hunt the Weak"
    def __init__(self):
        super(c383270, self).__init__(gameobject.Characteristics(**{'name': 'Hunt the Weak', 'text': "Put a +1/+1 counter on target creature you control. Then that creature fights target creature you don't control. (Each deals damage equal to its power to the other.)", 'color': ['G'], 'mana_cost': '3G'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c383271(card.Card):
    "Hunter's Ambush"
    def __init__(self):
        super(c383271, self).__init__(gameobject.Characteristics(**{'name': "Hunter's Ambush", 'text': 'Prevent all combat damage that would be dealt by nongreen creatures this turn.', 'color': ['G'], 'mana_cost': '2G'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c383279(card.Card):
    "Invasive Species"
    def __init__(self):
        super(c383279, self).__init__(gameobject.Characteristics(**{'name': 'Invasive Species', 'subtype': ['Insect'], 'mana_cost': '2G', 'text': "When Invasive Species enters the battlefield, return another permanent you control to its owner's hand.", 'toughness': 3, 'power': 3, 'color': ['G']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383290(card.Card):
    "Kalonian Twingrove"
    def __init__(self):
        super(c383290, self).__init__(gameobject.Characteristics(**{'name': 'Kalonian Twingrove', 'subtype': ['Treefolk', 'Warrior'], 'mana_cost': '5G', 'text': 'Kalonian Twingrove\'s power and toughness are each equal to the number of Forests you control.\nWhen Kalonian Twingrove enters the battlefield, create a green Treefolk Warrior creature token with "This creature\'s power and toughness are each equal to the number of Forests you control."', 'toughness': '*', 'power': '*', 'color': ['G']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383298(card.Card):
    "Life's Legacy"
    def __init__(self):
        super(c383298, self).__init__(gameobject.Characteristics(**{'name': "Life's Legacy", 'text': "As an additional cost to cast Life's Legacy, sacrifice a creature.\nDraw cards equal to the sacrificed creature's power.", 'color': ['G'], 'mana_cost': '1G'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c383301(card.Card):
    "Living Totem"
    def __init__(self):
        super(c383301, self).__init__(gameobject.Characteristics(**{'name': 'Living Totem', 'subtype': ['Plant', 'Elemental'], 'mana_cost': '3G', 'text': "Convoke (Your creatures can help cast this spell. Each creature you tap while casting this spell pays for {1} or one mana of that creature's color.)\nWhen Living Totem enters the battlefield, you may put a +1/+1 counter on another target creature.", 'toughness': 3, 'power': 2, 'color': ['G']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Convoke]))

class c383319(card.Card):
    "Naturalize"
    def __init__(self):
        super(c383319, self).__init__(gameobject.Characteristics(**{'name': 'Naturalize', 'text': 'Destroy target artifact or enchantment.', 'color': ['G'], 'mana_cost': '1G'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c383325(card.Card):
    "Netcaster Spider"
    def __init__(self):
        super(c383325, self).__init__(gameobject.Characteristics(**{'name': 'Netcaster Spider', 'subtype': ['Spider'], 'mana_cost': '2G', 'text': 'Reach (This creature can block creatures with flying.)\nWhenever Netcaster Spider blocks a creature with flying, Netcaster Spider gets +2/+0 until end of turn.', 'toughness': 3, 'power': 2, 'color': ['G']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Reach]))

class c383328(card.Card):
    "Nissa, Worldwaker"
    def __init__(self):
        super(c383328, self).__init__(gameobject.Characteristics(**{'subtype': ['Nissa'], 'name': 'Nissa, Worldwaker', 'text': "+1: Target land you control becomes a 4/4 Elemental creature with trample. It's still a land.\n+1: Untap up to four target Forests.\n−7: Search your library for any number of basic land cards, put them onto the battlefield, then shuffle your library. Those lands become 4/4 Elemental creatures with trample. They're still lands.", 'color': ['G'], 'mana_cost': '3GG'}, supertype=[], types=[cardtype.CardType.PLANESWALKER], abilities=[]))

class c383329(card.Card):
    "Nissa's Expedition"
    def __init__(self):
        super(c383329, self).__init__(gameobject.Characteristics(**{'name': "Nissa's Expedition", 'text': "Convoke (Your creatures can help cast this spell. Each creature you tap while casting this spell pays for {1} or one mana of that creature's color.)\nSearch your library for up to two basic land cards, put them onto the battlefield tapped, then shuffle your library.", 'color': ['G'], 'mana_cost': '4G'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[abilities.StaticAbilities.Convoke]))

class c383335(card.Card):
    "Overwhelm"
    def __init__(self):
        super(c383335, self).__init__(gameobject.Characteristics(**{'name': 'Overwhelm', 'text': "Convoke (Your creatures can help cast this spell. Each creature you tap while casting this spell pays for {1} or one mana of that creature's color.)\nCreatures you control get +3/+3 until end of turn.", 'color': ['G'], 'mana_cost': '5GG'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[abilities.StaticAbilities.Convoke]))

class c383336(card.Card):
    "Paragon of Eternal Wilds"
    def __init__(self):
        super(c383336, self).__init__(gameobject.Characteristics(**{'name': 'Paragon of Eternal Wilds', 'subtype': ['Human', 'Druid'], 'mana_cost': '3G', 'text': 'Other green creatures you control get +1/+1.\n{G}, {T}: Another target green creature you control gains trample until end of turn. (If it would assign enough damage to its blockers to destroy them, you may have it assign the rest of its damage to defending player or planeswalker.)', 'toughness': 2, 'power': 2, 'color': ['G']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383344(card.Card):
    "Phytotitan"
    def __init__(self):
        super(c383344, self).__init__(gameobject.Characteristics(**{'name': 'Phytotitan', 'subtype': ['Plant', 'Elemental'], 'mana_cost': '4GG', 'text': "When Phytotitan dies, return it to the battlefield tapped under its owner's control at the beginning of his or her next upkeep.", 'toughness': 2, 'power': 7, 'color': ['G']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383350(card.Card):
    "Plummet"
    def __init__(self):
        super(c383350, self).__init__(gameobject.Characteristics(**{'name': 'Plummet', 'text': 'Destroy target creature with flying.', 'color': ['G'], 'mana_cost': '1G'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c383357(card.Card):
    "Ranger's Guile"
    def __init__(self):
        super(c383357, self).__init__(gameobject.Characteristics(**{'name': "Ranger's Guile", 'text': "Target creature you control gets +1/+1 and gains hexproof until end of turn. (It can't be the target of spells or abilities your opponents control.)", 'color': ['G'], 'mana_cost': 'G'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c383359(card.Card):
    "Reclamation Sage"
    def __init__(self):
        super(c383359, self).__init__(gameobject.Characteristics(**{'name': 'Reclamation Sage', 'subtype': ['Elf', 'Shaman'], 'mana_cost': '2G', 'text': 'When Reclamation Sage enters the battlefield, you may destroy target artifact or enchantment.', 'toughness': 1, 'power': 2, 'color': ['G']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383362(card.Card):
    "Restock"
    def __init__(self):
        super(c383362, self).__init__(gameobject.Characteristics(**{'name': 'Restock', 'text': 'Return two target cards from your graveyard to your hand. Exile Restock.', 'color': ['G'], 'mana_cost': '3GG'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c383364(card.Card):
    "Roaring Primadox"
    def __init__(self):
        super(c383364, self).__init__(gameobject.Characteristics(**{'name': 'Roaring Primadox', 'subtype': ['Beast'], 'mana_cost': '3G', 'text': "At the beginning of your upkeep, return a creature you control to its owner's hand.", 'toughness': 4, 'power': 4, 'color': ['G']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383368(card.Card):
    "Runeclaw Bear"
    def __init__(self):
        super(c383368, self).__init__(gameobject.Characteristics(**{'name': 'Runeclaw Bear', 'subtype': ['Bear'], 'mana_cost': '1G', 'text': '', 'toughness': 2, 'power': 2, 'color': ['G']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383371(card.Card):
    "Satyr Wayfinder"
    def __init__(self):
        super(c383371, self).__init__(gameobject.Characteristics(**{'name': 'Satyr Wayfinder', 'subtype': ['Satyr'], 'mana_cost': '1G', 'text': 'When Satyr Wayfinder enters the battlefield, reveal the top four cards of your library. You may put a land card from among them into your hand. Put the rest into your graveyard.', 'toughness': 1, 'power': 1, 'color': ['G']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383377(card.Card):
    "Shaman of Spring"
    def __init__(self):
        super(c383377, self).__init__(gameobject.Characteristics(**{'name': 'Shaman of Spring', 'subtype': ['Elf', 'Shaman'], 'mana_cost': '3G', 'text': 'When Shaman of Spring enters the battlefield, draw a card.', 'toughness': 2, 'power': 2, 'color': ['G']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383382(card.Card):
    "Siege Wurm"
    def __init__(self):
        super(c383382, self).__init__(gameobject.Characteristics(**{'name': 'Siege Wurm', 'subtype': ['Wurm'], 'mana_cost': '5GG', 'text': "Convoke (Your creatures can help cast this spell. Each creature you tap while casting this spell pays for {1} or one mana of that creature's color.)\nTrample (This creature can deal excess combat damage to defending player or planeswalker while attacking.)", 'toughness': 5, 'power': 5, 'color': ['G']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Trample, abilities.StaticAbilities.Convoke]))

class c383392(card.Card):
    "Soul of Zendikar"
    def __init__(self):
        super(c383392, self).__init__(gameobject.Characteristics(**{'name': 'Soul of Zendikar', 'subtype': ['Avatar'], 'mana_cost': '4GG', 'text': 'Reach\n{3}{G}{G}: Create a 3/3 green Beast creature token.\n{3}{G}{G}, Exile Soul of Zendikar from your graveyard: Create a 3/3 green Beast creature token.', 'toughness': 6, 'power': 6, 'color': ['G']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Reach]))

class c383406(card.Card):
    "Sunblade Elf"
    def __init__(self):
        super(c383406, self).__init__(gameobject.Characteristics(**{'name': 'Sunblade Elf', 'subtype': ['Elf', 'Warrior'], 'mana_cost': 'G', 'text': 'Sunblade Elf gets +1/+1 as long as you control a Plains.\n{4}{W}: Creatures you control get +1/+1 until end of turn.', 'toughness': 1, 'power': 1, 'color': ['G', 'W']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383415(card.Card):
    "Titanic Growth"
    def __init__(self):
        super(c383415, self).__init__(gameobject.Characteristics(**{'name': 'Titanic Growth', 'text': 'Target creature gets +4/+4 until end of turn.', 'color': ['G'], 'mana_cost': '1G'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c383423(card.Card):
    "Undergrowth Scavenger"
    def __init__(self):
        super(c383423, self).__init__(gameobject.Characteristics(**{'name': 'Undergrowth Scavenger', 'subtype': ['Fungus', 'Horror'], 'mana_cost': '3G', 'text': 'Undergrowth Scavenger enters the battlefield with a number of +1/+1 counters on it equal to the number of creature cards in all graveyards.', 'toughness': 0, 'power': 0, 'color': ['G']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383426(card.Card):
    "Venom Sliver"
    def __init__(self):
        super(c383426, self).__init__(gameobject.Characteristics(**{'name': 'Venom Sliver', 'subtype': ['Sliver'], 'mana_cost': '1G', 'text': 'Sliver creatures you control have deathtouch. (Any amount of damage a creature with deathtouch deals to a creature is enough to destroy it.)', 'toughness': 1, 'power': 1, 'color': ['G']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383427(card.Card):
    "Verdant Haven"
    def __init__(self):
        super(c383427, self).__init__(gameobject.Characteristics(**{'subtype': ['Aura'], 'name': 'Verdant Haven', 'text': 'Enchant land\nWhen Verdant Haven enters the battlefield, you gain 2 life.\nWhenever enchanted land is tapped for mana, its controller adds one mana of any color to his or her mana pool (in addition to the mana the land produces).', 'color': ['G'], 'mana_cost': '2G'}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c383428(card.Card):
    "Vineweft"
    def __init__(self):
        super(c383428, self).__init__(gameobject.Characteristics(**{'subtype': ['Aura'], 'name': 'Vineweft', 'text': 'Enchant creature\nEnchanted creature gets +1/+1.\n{4}{G}: Return Vineweft from your graveyard to your hand.', 'color': ['G'], 'mana_cost': 'G'}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c383434(card.Card):
    "Wall of Mulch"
    def __init__(self):
        super(c383434, self).__init__(gameobject.Characteristics(**{'name': 'Wall of Mulch', 'subtype': ['Wall'], 'mana_cost': '1G', 'text': "Defender (This creature can't attack.)\n{G}, Sacrifice a Wall: Draw a card.", 'toughness': 4, 'power': 0, 'color': ['G']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Defender]))

class c383442(card.Card):
    "Yisan, the Wanderer Bard"
    def __init__(self):
        super(c383442, self).__init__(gameobject.Characteristics(**{'name': 'Yisan, the Wanderer Bard', 'subtype': ['Human', 'Rogue'], 'mana_cost': '2G', 'text': '{2}{G}, {T}, Put a verse counter on Yisan, the Wanderer Bard: Search your library for a creature card with converted mana cost equal to the number of verse counters on Yisan, put it onto the battlefield, then shuffle your library.', 'toughness': 3, 'power': 2, 'color': ['G']}, supertype=[cardtype.SuperType.LEGENDARY], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383251(card.Card):
    "Garruk, Apex Predator"
    def __init__(self):
        super(c383251, self).__init__(gameobject.Characteristics(**{'subtype': ['Garruk'], 'name': 'Garruk, Apex Predator', 'text': '+1: Destroy another target planeswalker.\n+1: Create a 3/3 black Beast creature token with deathtouch.\n−3: Destroy target creature. You gain life equal to its toughness.\n−8: Target opponent gets an emblem with "Whenever a creature attacks you, it gets +5/+5 and gains trample until end of turn."', 'color': ['B', 'G'], 'mana_cost': '5BG'}, supertype=[], types=[cardtype.CardType.PLANESWALKER], abilities=[]))

class c383385(card.Card):
    "Sliver Hivelord"
    def __init__(self):
        super(c383385, self).__init__(gameobject.Characteristics(**{'name': 'Sliver Hivelord', 'subtype': ['Sliver'], 'mana_cost': 'WUBRG', 'text': 'Sliver creatures you control have indestructible. (Damage and effects that say "destroy" don\'t destroy them.)', 'toughness': 5, 'power': 5, 'color': ['W', 'U', 'B', 'R', 'G']}, supertype=[cardtype.SuperType.LEGENDARY], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383186(card.Card):
    "Avarice Amulet"
    def __init__(self):
        super(c383186, self).__init__(gameobject.Characteristics(**{'subtype': ['Equipment'], 'name': 'Avarice Amulet', 'text': 'Equipped creature gets +2/+0 and has vigilance and "At the beginning of your upkeep, draw a card."\nWhenever equipped creature dies, target opponent gains control of Avarice Amulet.\nEquip {2} ({2}: Attach to target creature you control. Equip only as a sorcery.)', 'color': '', 'mana_cost': '4'}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c383196(card.Card):
    "Brawler's Plate"
    def __init__(self):
        super(c383196, self).__init__(gameobject.Characteristics(**{'subtype': ['Equipment'], 'name': "Brawler's Plate", 'text': 'Equipped creature gets +2/+2 and has trample. (It can deal excess combat damage to defending player or planeswalker while attacking.)\nEquip {4} ({4}: Attach to target creature you control. Equip only as a sorcery.)', 'color': '', 'mana_cost': '3'}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c383197(card.Card):
    "Bronze Sable"
    def __init__(self):
        super(c383197, self).__init__(gameobject.Characteristics(**{'name': 'Bronze Sable', 'subtype': ['Sable'], 'mana_cost': '2', 'text': '', 'toughness': 1, 'power': 2, 'color': ''}, supertype=[], types=[cardtype.CardType.ARTIFACT, cardtype.CardType.CREATURE], abilities=[]))

class c383412(card.Card):
    "The Chain Veil"
    def __init__(self):
        super(c383412, self).__init__(gameobject.Characteristics(**{'name': 'The Chain Veil', 'text': "At the beginning of your end step, if you didn't activate a loyalty ability of a planeswalker this turn, you lose 2 life.\n{4}, {T}: For each planeswalker you control, you may activate one of its loyalty abilities once this turn as though none of its loyalty abilities have been activated this turn.", 'color': '', 'mana_cost': '4'}, supertype=[cardtype.SuperType.LEGENDARY], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c383250(card.Card):
    "Gargoyle Sentinel"
    def __init__(self):
        super(c383250, self).__init__(gameobject.Characteristics(**{'name': 'Gargoyle Sentinel', 'subtype': ['Gargoyle'], 'mana_cost': '3', 'text': "Defender (This creature can't attack.)\n{3}: Until end of turn, Gargoyle Sentinel loses defender and gains flying.", 'toughness': 3, 'power': 3, 'color': ''}, supertype=[], types=[cardtype.CardType.ARTIFACT, cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Defender]))

class c383261(card.Card):
    "Grindclock"
    def __init__(self):
        super(c383261, self).__init__(gameobject.Characteristics(**{'name': 'Grindclock', 'text': '{T}: Put a charge counter on Grindclock.\n{T}: Target player puts the top X cards of his or her library into his or her graveyard, where X is the number of charge counters on Grindclock.', 'color': '', 'mana_cost': '2'}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c383263(card.Card):
    "Haunted Plate Mail"
    def __init__(self):
        super(c383263, self).__init__(gameobject.Characteristics(**{'subtype': ['Equipment'], 'name': 'Haunted Plate Mail', 'text': "Equipped creature gets +4/+4.\n{0}: Until end of turn, Haunted Plate Mail becomes a 4/4 Spirit artifact creature that's no longer an Equipment. Activate this ability only if you control no creatures.\nEquip {4} ({4}: Attach to target creature you control. Equip only as a sorcery.)", 'color': '', 'mana_cost': '4'}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c383269(card.Card):
    "Hot Soup"
    def __init__(self):
        super(c383269, self).__init__(gameobject.Characteristics(**{'subtype': ['Equipment'], 'name': 'Hot Soup', 'text': "Equipped creature can't be blocked.\nWhenever equipped creature is dealt damage, destroy it.\nEquip {3} ({3}: Attach to target creature you control. Equip only as a sorcery.)", 'color': '', 'mana_cost': '1'}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c383289(card.Card):
    "Juggernaut"
    def __init__(self):
        super(c383289, self).__init__(gameobject.Characteristics(**{'name': 'Juggernaut', 'subtype': ['Juggernaut'], 'mana_cost': '4', 'text': "Juggernaut attacks each turn if able.\nJuggernaut can't be blocked by Walls.", 'toughness': 3, 'power': 5, 'color': ''}, supertype=[], types=[cardtype.CardType.ARTIFACT, cardtype.CardType.CREATURE], abilities=[]))

class c383308(card.Card):
    "Meteorite"
    def __init__(self):
        super(c383308, self).__init__(gameobject.Characteristics(**{'name': 'Meteorite', 'text': 'When Meteorite enters the battlefield, it deals 2 damage to target creature or player.\n{T}: Add one mana of any color to your mana pool.', 'color': '', 'mana_cost': '5'}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c383331(card.Card):
    "Obelisk of Urd"
    def __init__(self):
        super(c383331, self).__init__(gameobject.Characteristics(**{'name': 'Obelisk of Urd', 'text': "Convoke (Your creatures can help cast this spell. Each creature you tap while casting this spell pays for {1} or one mana of that creature's color.)\nAs Obelisk of Urd enters the battlefield, choose a creature type.\nCreatures you control of the chosen type get +2/+2.", 'color': '', 'mana_cost': '6'}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[abilities.StaticAbilities.Convoke]))

class c383334(card.Card):
    "Ornithopter"
    def __init__(self):
        super(c383334, self).__init__(gameobject.Characteristics(**{'name': 'Ornithopter', 'subtype': ['Thopter'], 'mana_cost': '0', 'text': 'Flying', 'toughness': 2, 'power': 0, 'color': ''}, supertype=[], types=[cardtype.CardType.ARTIFACT, cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Flying]))

class c383342(card.Card):
    "Perilous Vault"
    def __init__(self):
        super(c383342, self).__init__(gameobject.Characteristics(**{'name': 'Perilous Vault', 'text': '{5}, {T}, Exile Perilous Vault: Exile all nonland permanents.', 'color': '', 'mana_cost': '4'}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c383343(card.Card):
    "Phyrexian Revoker"
    def __init__(self):
        super(c383343, self).__init__(gameobject.Characteristics(**{'name': 'Phyrexian Revoker', 'subtype': ['Horror'], 'mana_cost': '2', 'text': "As Phyrexian Revoker enters the battlefield, choose a nonland card name.\nActivated abilities of sources with the chosen name can't be activated.", 'toughness': 1, 'power': 2, 'color': ''}, supertype=[], types=[cardtype.CardType.ARTIFACT, cardtype.CardType.CREATURE], abilities=[]))

class c383353(card.Card):
    "Profane Memento"
    def __init__(self):
        super(c383353, self).__init__(gameobject.Characteristics(**{'name': 'Profane Memento', 'text': "Whenever a creature card is put into an opponent's graveyard from anywhere, you gain 1 life.", 'color': '', 'mana_cost': '1'}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c383365(card.Card):
    "Rogue's Gloves"
    def __init__(self):
        super(c383365, self).__init__(gameobject.Characteristics(**{'subtype': ['Equipment'], 'name': "Rogue's Gloves", 'text': 'Whenever equipped creature deals combat damage to a player, you may draw a card.\nEquip {2} ({2}: Attach to target creature you control. Equip only as a sorcery.)', 'color': '', 'mana_cost': '2'}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c383369(card.Card):
    "Sacred Armory"
    def __init__(self):
        super(c383369, self).__init__(gameobject.Characteristics(**{'name': 'Sacred Armory', 'text': '{2}: Target creature gets +1/+0 until end of turn.', 'color': '', 'mana_cost': '2'}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c383373(card.Card):
    "Scuttling Doom Engine"
    def __init__(self):
        super(c383373, self).__init__(gameobject.Characteristics(**{'name': 'Scuttling Doom Engine', 'subtype': ['Construct'], 'mana_cost': '6', 'text': "Scuttling Doom Engine can't be blocked by creatures with power 2 or less.\nWhen Scuttling Doom Engine dies, it deals 6 damage to target opponent.", 'toughness': 6, 'power': 6, 'color': ''}, supertype=[], types=[cardtype.CardType.ARTIFACT, cardtype.CardType.CREATURE], abilities=[]))

class c383378(card.Card):
    "Shield of the Avatar"
    def __init__(self):
        super(c383378, self).__init__(gameobject.Characteristics(**{'subtype': ['Equipment'], 'name': 'Shield of the Avatar', 'text': 'If a source would deal damage to equipped creature, prevent X of that damage, where X is the number of creatures you control.\nEquip {2} ({2}: Attach to target creature you control. Equip only as a sorcery.)', 'color': '', 'mana_cost': '1'}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c383388(card.Card):
    "Soul of New Phyrexia"
    def __init__(self):
        super(c383388, self).__init__(gameobject.Characteristics(**{'name': 'Soul of New Phyrexia', 'subtype': ['Avatar'], 'mana_cost': '6', 'text': 'Trample\n{5}: Permanents you control gain indestructible until end of turn.\n{5}, Exile Soul of New Phyrexia from your graveyard: Permanents you control gain indestructible until end of turn.', 'toughness': 6, 'power': 6, 'color': ''}, supertype=[], types=[cardtype.CardType.ARTIFACT, cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Trample]))

class c383397(card.Card):
    "Staff of the Death Magus"
    def __init__(self):
        super(c383397, self).__init__(gameobject.Characteristics(**{'name': 'Staff of the Death Magus', 'text': 'Whenever you cast a black spell or a Swamp enters the battlefield under your control, you gain 1 life.', 'color': '', 'mana_cost': '3'}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c383398(card.Card):
    "Staff of the Flame Magus"
    def __init__(self):
        super(c383398, self).__init__(gameobject.Characteristics(**{'name': 'Staff of the Flame Magus', 'text': 'Whenever you cast a red spell or a Mountain enters the battlefield under your control, you gain 1 life.', 'color': '', 'mana_cost': '3'}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c383399(card.Card):
    "Staff of the Mind Magus"
    def __init__(self):
        super(c383399, self).__init__(gameobject.Characteristics(**{'name': 'Staff of the Mind Magus', 'text': 'Whenever you cast a blue spell or an Island enters the battlefield under your control, you gain 1 life.', 'color': '', 'mana_cost': '3'}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c383400(card.Card):
    "Staff of the Sun Magus"
    def __init__(self):
        super(c383400, self).__init__(gameobject.Characteristics(**{'name': 'Staff of the Sun Magus', 'text': 'Whenever you cast a white spell or a Plains enters the battlefield under your control, you gain 1 life.', 'color': '', 'mana_cost': '3'}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c383401(card.Card):
    "Staff of the Wild Magus"
    def __init__(self):
        super(c383401, self).__init__(gameobject.Characteristics(**{'name': 'Staff of the Wild Magus', 'text': 'Whenever you cast a green spell or a Forest enters the battlefield under your control, you gain 1 life.', 'color': '', 'mana_cost': '3'}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c383417(card.Card):
    "Tormod's Crypt"
    def __init__(self):
        super(c383417, self).__init__(gameobject.Characteristics(**{'name': "Tormod's Crypt", 'text': "{T}, Sacrifice Tormod's Crypt: Exile all cards from target player's graveyard.", 'color': '', 'mana_cost': '0'}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c383421(card.Card):
    "Tyrant's Machine"
    def __init__(self):
        super(c383421, self).__init__(gameobject.Characteristics(**{'name': "Tyrant's Machine", 'text': '{4}, {T}: Tap target creature.', 'color': '', 'mana_cost': '2'}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c383438(card.Card):
    "Will-Forged Golem"
    def __init__(self):
        super(c383438, self).__init__(gameobject.Characteristics(**{'name': 'Will-Forged Golem', 'subtype': ['Golem'], 'mana_cost': '6', 'text': "Convoke (Your creatures can help cast this spell. Each creature you tap while casting this spell pays for {1} or one mana of that creature's color.)", 'toughness': 4, 'power': 4, 'color': ''}, supertype=[], types=[cardtype.CardType.ARTIFACT, cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Convoke]))

class c383189(card.Card):
    "Battlefield Forge"
    def __init__(self):
        super(c383189, self).__init__(gameobject.Characteristics(**{'name': 'Battlefield Forge', 'text': '{T}: Add {C} to your mana pool.\n{T}: Add {R} or {W} to your mana pool. Battlefield Forge deals 1 damage to you.', 'color': ['R', 'W'], 'mana_cost': ''}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c383203(card.Card):
    "Caves of Koilos"
    def __init__(self):
        super(c383203, self).__init__(gameobject.Characteristics(**{'name': 'Caves of Koilos', 'text': '{T}: Add {C} to your mana pool.\n{T}: Add {W} or {B} to your mana pool. Caves of Koilos deals 1 damage to you.', 'color': ['W', 'B'], 'mana_cost': ''}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c383222(card.Card):
    "Darksteel Citadel"
    def __init__(self):
        super(c383222, self).__init__(gameobject.Characteristics(**{'name': 'Darksteel Citadel', 'text': 'Indestructible\n{T}: Add {C} to your mana pool.', 'color': '', 'mana_cost': ''}, supertype=[], types=[cardtype.CardType.ARTIFACT, cardtype.CardType.LAND], abilities=[abilities.StaticAbilities.Indestructible]))

class c383235(card.Card):
    "Evolving Wilds"
    def __init__(self):
        super(c383235, self).__init__(gameobject.Characteristics(**{'name': 'Evolving Wilds', 'text': '{T}, Sacrifice Evolving Wilds: Search your library for a basic land card and put it onto the battlefield tapped. Then shuffle your library.', 'color': '', 'mana_cost': ''}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c383302(card.Card):
    "Llanowar Wastes"
    def __init__(self):
        super(c383302, self).__init__(gameobject.Characteristics(**{'name': 'Llanowar Wastes', 'text': '{T}: Add {C} to your mana pool.\n{T}: Add {B} or {G} to your mana pool. Llanowar Wastes deals 1 damage to you.', 'color': ['B', 'G'], 'mana_cost': ''}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c383355(card.Card):
    "Radiant Fountain"
    def __init__(self):
        super(c383355, self).__init__(gameobject.Characteristics(**{'name': 'Radiant Fountain', 'text': 'When Radiant Fountain enters the battlefield, you gain 2 life.\n{T}: Add {C} to your mana pool.', 'color': '', 'mana_cost': ''}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c383379(card.Card):
    "Shivan Reef"
    def __init__(self):
        super(c383379, self).__init__(gameobject.Characteristics(**{'name': 'Shivan Reef', 'text': '{T}: Add {C} to your mana pool.\n{T}: Add {U} or {R} to your mana pool. Shivan Reef deals 1 damage to you.', 'color': ['U', 'R'], 'mana_cost': ''}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c383384(card.Card):
    "Sliver Hive"
    def __init__(self):
        super(c383384, self).__init__(gameobject.Characteristics(**{'name': 'Sliver Hive', 'text': '{T}: Add {C} to your mana pool.\n{T}: Add one mana of any color to your mana pool. Spend this mana only to cast a Sliver spell.\n{5}, {T}: Create a 1/1 colorless Sliver creature token. Activate this ability only if you control a Sliver.', 'color': '', 'mana_cost': ''}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c383425(card.Card):
    "Urborg, Tomb of Yawgmoth"
    def __init__(self):
        super(c383425, self).__init__(gameobject.Characteristics(**{'name': 'Urborg, Tomb of Yawgmoth', 'text': 'Each land is a Swamp in addition to its other land types.', 'color': '', 'mana_cost': ''}, supertype=[cardtype.SuperType.LEGENDARY], types=[cardtype.CardType.LAND], abilities=[]))

class c383441(card.Card):
    "Yavimaya Coast"
    def __init__(self):
        super(c383441, self).__init__(gameobject.Characteristics(**{'name': 'Yavimaya Coast', 'text': '{T}: Add {C} to your mana pool.\n{T}: Add {G} or {U} to your mana pool. Yavimaya Coast deals 1 damage to you.', 'color': ['G', 'U'], 'mana_cost': ''}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c383347(card.Card):
    "Plains"
    def __init__(self):
        super(c383347, self).__init__(gameobject.Characteristics(**{'subtype': ['Plains'], 'name': 'Plains', 'text': '', 'color': ['W'], 'mana_cost': ''}, supertype=[cardtype.SuperType.BASIC], types=[cardtype.CardType.LAND], abilities=[]))

class c383346(card.Card):
    "Plains"
    def __init__(self):
        super(c383346, self).__init__(gameobject.Characteristics(**{'subtype': ['Plains'], 'name': 'Plains', 'text': '', 'color': ['W'], 'mana_cost': ''}, supertype=[cardtype.SuperType.BASIC], types=[cardtype.CardType.LAND], abilities=[]))

class c383348(card.Card):
    "Plains"
    def __init__(self):
        super(c383348, self).__init__(gameobject.Characteristics(**{'subtype': ['Plains'], 'name': 'Plains', 'text': '', 'color': ['W'], 'mana_cost': ''}, supertype=[cardtype.SuperType.BASIC], types=[cardtype.CardType.LAND], abilities=[]))

class c383349(card.Card):
    "Plains"
    def __init__(self):
        super(c383349, self).__init__(gameobject.Characteristics(**{'subtype': ['Plains'], 'name': 'Plains', 'text': '', 'color': ['W'], 'mana_cost': ''}, supertype=[cardtype.SuperType.BASIC], types=[cardtype.CardType.LAND], abilities=[]))

class c383284(card.Card):
    "Island"
    def __init__(self):
        super(c383284, self).__init__(gameobject.Characteristics(**{'subtype': ['Island'], 'name': 'Island', 'text': '', 'color': ['U'], 'mana_cost': ''}, supertype=[cardtype.SuperType.BASIC], types=[cardtype.CardType.LAND], abilities=[]))

class c383281(card.Card):
    "Island"
    def __init__(self):
        super(c383281, self).__init__(gameobject.Characteristics(**{'subtype': ['Island'], 'name': 'Island', 'text': '', 'color': ['U'], 'mana_cost': ''}, supertype=[cardtype.SuperType.BASIC], types=[cardtype.CardType.LAND], abilities=[]))

class c383283(card.Card):
    "Island"
    def __init__(self):
        super(c383283, self).__init__(gameobject.Characteristics(**{'subtype': ['Island'], 'name': 'Island', 'text': '', 'color': ['U'], 'mana_cost': ''}, supertype=[cardtype.SuperType.BASIC], types=[cardtype.CardType.LAND], abilities=[]))

class c383282(card.Card):
    "Island"
    def __init__(self):
        super(c383282, self).__init__(gameobject.Characteristics(**{'subtype': ['Island'], 'name': 'Island', 'text': '', 'color': ['U'], 'mana_cost': ''}, supertype=[cardtype.SuperType.BASIC], types=[cardtype.CardType.LAND], abilities=[]))

class c383409(card.Card):
    "Swamp"
    def __init__(self):
        super(c383409, self).__init__(gameobject.Characteristics(**{'subtype': ['Swamp'], 'name': 'Swamp', 'text': '', 'color': ['B'], 'mana_cost': ''}, supertype=[cardtype.SuperType.BASIC], types=[cardtype.CardType.LAND], abilities=[]))

class c383410(card.Card):
    "Swamp"
    def __init__(self):
        super(c383410, self).__init__(gameobject.Characteristics(**{'subtype': ['Swamp'], 'name': 'Swamp', 'text': '', 'color': ['B'], 'mana_cost': ''}, supertype=[cardtype.SuperType.BASIC], types=[cardtype.CardType.LAND], abilities=[]))

class c383411(card.Card):
    "Swamp"
    def __init__(self):
        super(c383411, self).__init__(gameobject.Characteristics(**{'subtype': ['Swamp'], 'name': 'Swamp', 'text': '', 'color': ['B'], 'mana_cost': ''}, supertype=[cardtype.SuperType.BASIC], types=[cardtype.CardType.LAND], abilities=[]))

class c383408(card.Card):
    "Swamp"
    def __init__(self):
        super(c383408, self).__init__(gameobject.Characteristics(**{'subtype': ['Swamp'], 'name': 'Swamp', 'text': '', 'color': ['B'], 'mana_cost': ''}, supertype=[cardtype.SuperType.BASIC], types=[cardtype.CardType.LAND], abilities=[]))

class c383315(card.Card):
    "Mountain"
    def __init__(self):
        super(c383315, self).__init__(gameobject.Characteristics(**{'subtype': ['Mountain'], 'name': 'Mountain', 'text': '', 'color': ['R'], 'mana_cost': ''}, supertype=[cardtype.SuperType.BASIC], types=[cardtype.CardType.LAND], abilities=[]))

class c383317(card.Card):
    "Mountain"
    def __init__(self):
        super(c383317, self).__init__(gameobject.Characteristics(**{'subtype': ['Mountain'], 'name': 'Mountain', 'text': '', 'color': ['R'], 'mana_cost': ''}, supertype=[cardtype.SuperType.BASIC], types=[cardtype.CardType.LAND], abilities=[]))

class c383318(card.Card):
    "Mountain"
    def __init__(self):
        super(c383318, self).__init__(gameobject.Characteristics(**{'subtype': ['Mountain'], 'name': 'Mountain', 'text': '', 'color': ['R'], 'mana_cost': ''}, supertype=[cardtype.SuperType.BASIC], types=[cardtype.CardType.LAND], abilities=[]))

class c383316(card.Card):
    "Mountain"
    def __init__(self):
        super(c383316, self).__init__(gameobject.Characteristics(**{'subtype': ['Mountain'], 'name': 'Mountain', 'text': '', 'color': ['R'], 'mana_cost': ''}, supertype=[cardtype.SuperType.BASIC], types=[cardtype.CardType.LAND], abilities=[]))

class c383244(card.Card):
    "Forest"
    def __init__(self):
        super(c383244, self).__init__(gameobject.Characteristics(**{'subtype': ['Forest'], 'name': 'Forest', 'text': '', 'color': ['G'], 'mana_cost': ''}, supertype=[cardtype.SuperType.BASIC], types=[cardtype.CardType.LAND], abilities=[]))

class c383242(card.Card):
    "Forest"
    def __init__(self):
        super(c383242, self).__init__(gameobject.Characteristics(**{'subtype': ['Forest'], 'name': 'Forest', 'text': '', 'color': ['G'], 'mana_cost': ''}, supertype=[cardtype.SuperType.BASIC], types=[cardtype.CardType.LAND], abilities=[]))

class c383243(card.Card):
    "Forest"
    def __init__(self):
        super(c383243, self).__init__(gameobject.Characteristics(**{'subtype': ['Forest'], 'name': 'Forest', 'text': '', 'color': ['G'], 'mana_cost': ''}, supertype=[cardtype.SuperType.BASIC], types=[cardtype.CardType.LAND], abilities=[]))

class c383241(card.Card):
    "Forest"
    def __init__(self):
        super(c383241, self).__init__(gameobject.Characteristics(**{'subtype': ['Forest'], 'name': 'Forest', 'text': '', 'color': ['G'], 'mana_cost': ''}, supertype=[cardtype.SuperType.BASIC], types=[cardtype.CardType.LAND], abilities=[]))

class c383160(card.Card):
    "Aegis Angel"
    def __init__(self):
        super(c383160, self).__init__(gameobject.Characteristics(**{'name': 'Aegis Angel', 'subtype': ['Angel'], 'mana_cost': '4WW', 'text': 'Flying (This creature can\'t be blocked except by creatures with flying or reach.)\nWhen Aegis Angel enters the battlefield, another target permanent gains indestructible for as long as you control Aegis Angel. (Effects that say "destroy" don\'t destroy it. A creature with indestructible can\'t be destroyed by damage.)', 'toughness': 5, 'power': 5, 'color': ['W']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Flying]))

class c383163(card.Card):
    "Divine Verdict"
    def __init__(self):
        super(c383163, self).__init__(gameobject.Characteristics(**{'name': 'Divine Verdict', 'text': 'Destroy target attacking or blocking creature.', 'color': ['W'], 'mana_cost': '3W'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c383166(card.Card):
    "Inspired Charge"
    def __init__(self):
        super(c383166, self).__init__(gameobject.Characteristics(**{'name': 'Inspired Charge', 'text': 'Creatures you control get +2/+1 until end of turn.', 'color': ['W'], 'mana_cost': '2WW'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c383171(card.Card):
    "Serra Angel"
    def __init__(self):
        super(c383171, self).__init__(gameobject.Characteristics(**{'name': 'Serra Angel', 'subtype': ['Angel'], 'mana_cost': '3WW', 'text': "Flying (This creature can't be blocked except by creatures with flying or reach.)\nVigilance (Attacking doesn't cause this creature to tap.)", 'toughness': 4, 'power': 4, 'color': ['W']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Flying, abilities.StaticAbilities.Vigilance]))

class c383161(card.Card):
    "Cancel"
    def __init__(self):
        super(c383161, self).__init__(gameobject.Characteristics(**{'name': 'Cancel', 'text': 'Counter target spell.', 'color': ['U'], 'mana_cost': '1UU'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c383167(card.Card):
    "Mahamoti Djinn"
    def __init__(self):
        super(c383167, self).__init__(gameobject.Characteristics(**{'name': 'Mahamoti Djinn', 'subtype': ['Djinn'], 'mana_cost': '4UU', 'text': "Flying (This creature can't be blocked except by creatures with flying or reach.)", 'toughness': 6, 'power': 5, 'color': ['U']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Flying]))

class c383168(card.Card):
    "Nightmare"
    def __init__(self):
        super(c383168, self).__init__(gameobject.Characteristics(**{'name': 'Nightmare', 'subtype': ['Nightmare', 'Horse'], 'mana_cost': '5B', 'text': "Flying (This creature can't be blocked except by creatures with flying or reach.)\nNightmare's power and toughness are each equal to the number of Swamps you control.", 'toughness': '*', 'power': '*', 'color': ['B']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Flying]))

class c383170(card.Card):
    "Sengir Vampire"
    def __init__(self):
        super(c383170, self).__init__(gameobject.Characteristics(**{'name': 'Sengir Vampire', 'subtype': ['Vampire'], 'mana_cost': '3BB', 'text': "Flying (This creature can't be blocked except by creatures with flying or reach.)\nWhenever a creature dealt damage by Sengir Vampire this turn dies, put a +1/+1 counter on Sengir Vampire.", 'toughness': 4, 'power': 4, 'color': ['B']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Flying]))

class c383174(card.Card):
    "Walking Corpse"
    def __init__(self):
        super(c383174, self).__init__(gameobject.Characteristics(**{'name': 'Walking Corpse', 'subtype': ['Zombie'], 'mana_cost': '1B', 'text': '', 'toughness': 2, 'power': 2, 'color': ['B']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383164(card.Card):
    "Furnace Whelp"
    def __init__(self):
        super(c383164, self).__init__(gameobject.Characteristics(**{'name': 'Furnace Whelp', 'subtype': ['Dragon'], 'mana_cost': '2RR', 'text': "Flying (This creature can't be blocked except by creatures with flying or reach.)\n{R}: Furnace Whelp gets +1/+0 until end of turn.", 'toughness': 2, 'power': 2, 'color': ['R']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Flying]))

class c383169(card.Card):
    "Seismic Strike"
    def __init__(self):
        super(c383169, self).__init__(gameobject.Characteristics(**{'name': 'Seismic Strike', 'text': 'Seismic Strike deals damage to target creature equal to the number of Mountains you control.', 'color': ['R'], 'mana_cost': '2R'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c383172(card.Card):
    "Shivan Dragon"
    def __init__(self):
        super(c383172, self).__init__(gameobject.Characteristics(**{'name': 'Shivan Dragon', 'subtype': ['Dragon'], 'mana_cost': '4RR', 'text': "Flying (This creature can't be blocked except by creatures with flying or reach.)\n{R}: Shivan Dragon gets +1/+0 until end of turn.", 'toughness': 5, 'power': 5, 'color': ['R']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Flying]))

class c383162(card.Card):
    "Centaur Courser"
    def __init__(self):
        super(c383162, self).__init__(gameobject.Characteristics(**{'name': 'Centaur Courser', 'subtype': ['Centaur', 'Warrior'], 'mana_cost': '2G', 'text': '', 'toughness': 3, 'power': 3, 'color': ['G']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383165(card.Card):
    "Garruk's Packleader"
    def __init__(self):
        super(c383165, self).__init__(gameobject.Characteristics(**{'name': "Garruk's Packleader", 'subtype': ['Beast'], 'mana_cost': '4G', 'text': 'Whenever another creature with power 3 or greater enters the battlefield under your control, you may draw a card.', 'toughness': 4, 'power': 4, 'color': ['G']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c383173(card.Card):
    "Terra Stomper"
    def __init__(self):
        super(c383173, self).__init__(gameobject.Characteristics(**{'name': 'Terra Stomper', 'subtype': ['Beast'], 'mana_cost': '3GGG', 'text': "Terra Stomper can't be countered.\nTrample (This creature can deal excess combat damage to defending player or planeswalker while attacking.)", 'toughness': 8, 'power': 8, 'color': ['G']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[abilities.StaticAbilities.Trample]))

