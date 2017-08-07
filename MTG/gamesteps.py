from enum import Enum

class Phase(Enum):
    BEGINNING = 0
    PRECOMBAT_MAIN = 1
    COMBAT = 2
    POSTCOMBAT_MAIN = 3
    ENDING = 4

    @property
    def steps(self):
        return {
            Phase.BEGINNING: (Step.UNTAP, Step.UPKEEP, Step.DRAW),
            Phase.PRECOMBAT_MAIN: (Step.PRECOMBAT_MAIN,),
            Phase.COMBAT: (
                Step.BEGINNING_OF_COMBAT,
                Step.DECLARE_ATTACKERS,
                Step.DECLARE_BLOCKERS,
                Step.FIRST_STRIKE_COMBAT_DAMAGE,
                Step.COMBAT_DAMAGE,
                Step.END_OF_COMBAT
            ),
            Phase.POSTCOMBAT_MAIN: (Step.POSTCOMBAT_MAIN,),
            Phase.ENDING: (Step.END, Step.CLEANUP)
        }[self]


class Step(Enum):
    UNTAP = 0
    UPKEEP = 1
    DRAW = 2
    PRECOMBAT_MAIN = 3
    BEGINNING_OF_COMBAT = 4
    DECLARE_ATTACKERS = 5
    DECLARE_BLOCKERS = 6
    FIRST_STRIKE_COMBAT_DAMAGE = 7
    COMBAT_DAMAGE = 8
    END_OF_COMBAT = 9
    POSTCOMBAT_MAIN = 10
    END = 11
    CLEANUP = 12

    @property
    def phase(self):
        return {
            Step.UNTAP: Phase.BEGINNING,
            Step.UPKEEP: Phase.BEGINNING,
            Step.DRAW: Phase.BEGINNING,
            Step.PRECOMBAT_MAIN: Phase.PRECOMBAT_MAIN,
            Step.BEGINNING_OF_COMBAT: Phase.COMBAT,
            Step.DECLARE_ATTACKERS: Phase.COMBAT,
            Step.DECLARE_BLOCKERS: Phase.COMBAT,
            Step.FIRST_STRIKE_COMBAT_DAMAGE: Phase.COMBAT,
            Step.COMBAT_DAMAGE: Phase.COMBAT,
            Step.END_OF_COMBAT: Phase.COMBAT,
            Step.POSTCOMBAT_MAIN: Phase.POSTCOMBAT_MAIN,
            Step.END: Phase.ENDING,
            Step.CLEANUP: Phase.ENDING
        }[self]