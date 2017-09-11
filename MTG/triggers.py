from enum import Enum


class triggerConditions(Enum):
    # values over 1000 are initiated by the player (e.g. 'WHENEVER a creature etb...')
    # 2000+ are controller specific; 1000+ are game/any-player specific

    # otherwise the conditions refer to the card itself
    # e.g. onDiscard means when THIS card is discarded
    # zone changes
    onPlay = 0
    onDraw = 1
    onDiscard = 2
    onEtB = 3
    onPlayfromHand = 4
    onEnterGrave = 5
    onDeath = 6
    onLeaveBattlefield = 7
    # phase (ALL PLAYERS)
    onUpkeep = 1110
    onMain1 = 1111
    onMain2 = 1112
    onEnterCombat = 1113
    onDeclareAttackers = 1114
    onDeclareBlockers = 1115
    onEndofCombat = 1116
    onEndstep = 1117
    onCleanup = 1118
    # phase (CONTROLLER ONLY)
    onControllerUpkeep = 2110
    onControllerMain1 = 2111
    onControllerMain2 = 2112
    onControllerEnterCombat = 2113
    onControllerDeclareAttackers = 2114
    onControllerDeclareBlockers = 2115
    onControllerEndofCombat = 2116
    onControllerEndstep = 2117
    onControllerCleanup = 2118
    # events
    onUntap = 8
    onTap = 9

    onDealDamageToPlayers = 19
    onDealDamageToCreatures = 20
    onDealDamage = 21
    onTakeDamage = 22
    onAttack = 23
    onBlock = 24
    onCombatDamage = 25
    onCombatDamageToPlayers = 26
    onCombatDamageToCreatures = 27
    onTakeCombatDamage = 28
    # global events


    onLifeLoss = 1000
    onControllerLifeLoss = 2000
    onLifeGain = 1001
    onControllerLifeGain = 2001
    onCounterPutOnPermanent = 1002
    onControllerCounterPutOnPermanent = 2002
    onDrawCard = 1003
    onControllerDrawCard = 2003
    onPlayerDiscard = 1004
    onControllerDiscard = 2004

    onPermanentLtB = 1030
    onRevolt = 2030  # controller permanent leaving battlefield
    onPermanentEtB = 1031
    onControllerPermanentEtB = 2031
    onCreatureEtB = 1032
    onControllerCreatureEtB = 2032


