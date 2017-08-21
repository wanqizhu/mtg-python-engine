from enum import Enum


class triggerConditions(Enum):
    # zone changes
    onPlay = 0
    onDraw = 1
    onDiscard = 2
    onEtB = 3
    onPlayfromHand = 4
    onEnterGrave = 5
    onDeath = 6
    onLeaveBattlefield = 7
    # phase (CONTROLLER ONLY or ALL PLAYERS)
    onUpkeep = 10
    onMain1 = 11
    onMain2 = 12
    onEnterCombat = 13
    onDeclareAttackers = 14
    onDeclareBlockers = 15
    onEndofCombat = 16
    onEndstep = 17
    onCleanup = 18
    # events
    onUntap = 8
    onTap = 9

    onDealDamageToPlayers = 19
    onDealDamageToCreatures = 20
    onDealDamage = 21
    onTakingDamage = 22
    onAttack = 23
    onBlock = 24
    # global events
    onRevolt = 30  # permanent leaving battlefield
    onControllerLifeLoss = 31
    onLifeLoss = 32
    onControllerLifeGain = 33
    onLifeGain = 34
    onCounterPutOnPermanent = 35
