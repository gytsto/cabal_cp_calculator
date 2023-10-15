from dataclasses import dataclass
from enum import Enum, auto


class StatType(Enum):
    Attack = auto()
    Defense = auto()


@dataclass
class StatValue:
    general: int = 0
    pve: int = 0
    pvp: int = 0


@dataclass
class Stat:
    VALUE_TYPE: StatType
    MULTIPLIER: float
    value: StatValue


# fmt: off
class Stats:
    def __init__(
        self,
        attack: StatValue = StatValue(),
        attack_rate: StatValue = StatValue(),
        crit_rate: StatValue = StatValue(),
        crit_dmg: StatValue = StatValue(),
        all_skill_amp: StatValue = StatValue(),
        accuracy: StatValue = StatValue(),
        penetration: StatValue = StatValue(),
        add_dmg: StatValue = StatValue(),
        ignore_evasion: StatValue = StatValue(),
        ignore_dmg_red: StatValue = StatValue(),
        final_dmg_increase: StatValue = StatValue(),
        ignore_resist_crit_rate: StatValue = StatValue(),
        ignore_resist_crit_dmg: StatValue = StatValue(),
        ignore_resist_skill_amp: StatValue = StatValue(),
        normal_dmg_up: StatValue = StatValue(),
        cancel_ignore_penetration: StatValue = StatValue(),
        hp: StatValue = StatValue(),
        defense: StatValue = StatValue(),
        defense_rate: StatValue = StatValue(),
        evasion: StatValue = StatValue(),
        dmg_red: StatValue = StatValue(),
        resit_crit_rate: StatValue = StatValue(),
        resit_crit_dmg: StatValue = StatValue(),
        resit_skill_amp: StatValue = StatValue(),
        ignore_penetration: StatValue = StatValue(),
        ignore_accuracy: StatValue = StatValue(),
        final_dmg_decrease: StatValue = StatValue(),
        cancel_ignore_dmg_reduce: StatValue = StatValue(),
    ):
        self.items : dict[str, Stat] = {
            "attack"                   : Stat(VALUE_TYPE = StatType.Attack , MULTIPLIER = 34.5 , value = attack),
            "attack_rate"              : Stat(VALUE_TYPE = StatType.Attack , MULTIPLIER = 3    , value = attack_rate),
            "crit_rate"                : Stat(VALUE_TYPE = StatType.Attack , MULTIPLIER = 750  , value = crit_rate),
            "crit_dmg"                 : Stat(VALUE_TYPE = StatType.Attack , MULTIPLIER = 177  , value = crit_dmg),
            "all_skill_amp"            : Stat(VALUE_TYPE = StatType.Attack , MULTIPLIER = 349  , value = all_skill_amp),
            "accuracy"                 : Stat(VALUE_TYPE = StatType.Attack , MULTIPLIER = 6.5  , value = accuracy),
            "penetration"              : Stat(VALUE_TYPE = StatType.Attack , MULTIPLIER = 71   , value = penetration),
            "add_dmg"                  : Stat(VALUE_TYPE = StatType.Attack , MULTIPLIER = 35   , value = add_dmg),
            "ignore_evasion"           : Stat(VALUE_TYPE = StatType.Attack , MULTIPLIER = 4.5  , value = ignore_evasion),
            "ignore_dmg_red"           : Stat(VALUE_TYPE = StatType.Attack , MULTIPLIER = 16.8 , value = ignore_dmg_red),
            "final_dmg_increase"       : Stat(VALUE_TYPE = StatType.Attack , MULTIPLIER = 1604 , value = final_dmg_increase),
            "ignore_resist_crit_rate"  : Stat(VALUE_TYPE = StatType.Attack , MULTIPLIER = 574  , value = ignore_resist_crit_rate),
            "ignore_resist_crit_dmg"   : Stat(VALUE_TYPE = StatType.Attack , MULTIPLIER = 142.5, value = ignore_resist_crit_dmg),
            "ignore_resist_skill_amp"  : Stat(VALUE_TYPE = StatType.Attack , MULTIPLIER = 267  , value = ignore_resist_skill_amp),
            "normal_dmg_up"            : Stat(VALUE_TYPE = StatType.Attack , MULTIPLIER = 85   , value = normal_dmg_up),
            "cancel_ignore_penetration": Stat(VALUE_TYPE = StatType.Attack , MULTIPLIER = 47.8 , value = cancel_ignore_penetration),
            "hp"                       : Stat(VALUE_TYPE = StatType.Defense, MULTIPLIER = 5    , value = hp),
            "defense"                  : Stat(VALUE_TYPE = StatType.Defense, MULTIPLIER = 21   , value = defense),
            "defense_rate"             : Stat(VALUE_TYPE = StatType.Defense, MULTIPLIER = 2.4  , value = defense_rate),
            "evasion"                  : Stat(VALUE_TYPE = StatType.Defense, MULTIPLIER = 5.3  , value = evasion),
            "dmg_red"                  : Stat(VALUE_TYPE = StatType.Defense, MULTIPLIER = 19.5 , value = dmg_red),
            "resit_crit_rate"          : Stat(VALUE_TYPE = StatType.Defense, MULTIPLIER = 636  , value = resit_crit_rate),
            "resit_crit_dmg"           : Stat(VALUE_TYPE = StatType.Defense, MULTIPLIER = 150  , value = resit_crit_dmg),
            "resit_skill_amp"          : Stat(VALUE_TYPE = StatType.Defense, MULTIPLIER = 296.5, value = resit_skill_amp),
            "ignore_penetration"       : Stat(VALUE_TYPE = StatType.Defense, MULTIPLIER = 53.1 , value = ignore_penetration),
            "ignore_accuracy"          : Stat(VALUE_TYPE = StatType.Defense, MULTIPLIER = 5.3  , value = ignore_accuracy),
            "final_dmg_decrease"       : Stat(VALUE_TYPE = StatType.Defense, MULTIPLIER = 1451 , value = final_dmg_decrease),
            "cancel_ignore_dmg_reduce" : Stat(VALUE_TYPE = StatType.Defense, MULTIPLIER = 19.9 , value = cancel_ignore_dmg_reduce),
        }
# fmt: on


def calculate_combat_power(stats: Stats):
    general_cp = 0
    pure_pve_cp = 0
    pure_pvp_cp = 0
    attack_ability_general = 0
    attack_ability_pve = 0
    attack_ability_pvp = 0
    defense_ability_general = 0
    defense_ability_pve = 0
    defense_ability_pvp = 0

    for _, stats_element in stats.items.items():
        general_stat_value = stats_element.value.general * stats_element.MULTIPLIER
        pve_stat_value = stats_element.value.pve * stats_element.MULTIPLIER
        pvp_stat_value = stats_element.value.pvp * stats_element.MULTIPLIER

        general_cp += general_stat_value
        pure_pve_cp += pve_stat_value
        pure_pvp_cp += pvp_stat_value

        # atack ability
        if stats_element.VALUE_TYPE == StatType.Attack:
            attack_ability_general += general_stat_value
            attack_ability_pve += pve_stat_value
            attack_ability_pvp += pvp_stat_value

        # defense ability
        if stats_element.VALUE_TYPE == StatType.Defense:
            defense_ability_general += general_stat_value
            defense_ability_pve += pve_stat_value
            defense_ability_pvp += pvp_stat_value

    return (
        StatValue(int(general_cp), int(pure_pve_cp), int(pure_pvp_cp)),
        StatValue(
            int(attack_ability_general),
            int(attack_ability_pve),
            int(attack_ability_pvp),
        ),
        StatValue(
            int(defense_ability_general),
            int(defense_ability_pve),
            int(defense_ability_pvp),
        ),
    )
