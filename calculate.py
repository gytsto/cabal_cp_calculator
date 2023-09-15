input_stats = {
    # attack
    "a_00_g": 0,
    "a_00_e": 0,
    "a_00_p": 0,
    # attack rate
    "a_01_g": 0,
    "a_01_e": 0,
    "a_01_p": 0,
    # crit rate
    "a_02_g": 0,
    "a_02_e": 0,
    "a_02_p": 0,
    # crit dmg
    "a_04_g": 0,
    "a_04_e": 0,
    "a_04_p": 0,
    # all skill amp
    "a_05_g": 0,
    "a_05_e": 0,
    "a_05_p": 0,
    # accuracy
    "a_06_g": 0,
    "a_06_e": 0,
    "a_06_p": 0,
    # penetration
    "a_07_g": 0,
    "a_07_e": 0,
    "a_07_p": 0,
    # add dmg
    "a_08_g": 0,
    "a_08_e": 0,
    "a_08_p": 0,
    # ignore evasion
    "a_10_g": 0,
    "a_10_e": 0,
    "a_10_p": 0,
    # ignore dmg red
    "a_11_g": 0,
    "a_11_e": 0,
    "a_11_p": 0,
    # final dmg increase
    "a_12_g": 0,
    "a_12_e": 0,
    "a_12_p": 0,
    # ignore resist crit rate
    "a_13_g": 0,
    "a_13_e": 0,
    "a_13_p": 0,
    # ignore resist crit dmg
    "a_14_g": 0,
    "a_14_e": 0,
    "a_14_p": 0,
    # ignore resist skill amp
    "a_15_g": 0,
    "a_15_e": 0,
    "a_15_p": 0,
    # normal dmg up
    "a_16_g": 0,
    "a_16_e": 0,
    "a_16_p": 0,
    # cancel ignore penetration
    "a_17_g": 0,
    "a_17_e": 0,
    "a_17_p": 0,
    # hp
    "d_18_g": 0,
    "d_18_e": 0,
    "d_18_p": 0,
    # defense
    "d_19_g": 0,
    "d_19_e": 0,
    "d_19_p": 0,
    # defense rate
    "d_20_g": 0,
    "d_20_e": 0,
    "d_20_p": 0,
    # evasion
    "d_21_g": 0,
    "d_21_e": 0,
    "d_21_p": 0,
    # dmg red
    "d_22_g": 0,
    "d_22_e": 0,
    "d_22_p": 0,
    # resit crit rate
    "d_23_g": 0,
    "d_23_e": 0,
    "d_23_p": 0,
    # resit crit dmg
    "d_24_g": 0,
    "d_24_e": 0,
    "d_24_p": 0,
    # resit skill amp
    "d_25_g": 0,
    "d_25_e": 0,
    "d_25_p": 0,
    # ignore penetration
    "d_26_g": 0,
    "d_26_e": 0,
    "d_26_p": 0,
    # ignore accuracy
    "d_27_g": 0,
    "d_27_e": 0,
    "d_27_p": 0,
    # final dmg decrease
    "d_28_g": 0,
    "d_28_e": 0,
    "d_28_p": 0,
    # cancel ignore dmg reduce
    "d_29_g": 0,
    "d_29_e": 0,
    "d_29_p": 0,
}

stats = [
    ["a", "00", 34.5],
    ["a", "01", 3],
    ["a", "02", 750],
    ["a", "04", 177],
    ["a", "05", 349],
    ["a", "06", 6.5],
    ["a", "07", 71],
    ["a", "08", 35],
    ["a", "10", 4.5],
    ["a", "11", 1604],
    ["a", "12", 16.8],
    ["a", "13", 574],
    ["a", "14", 142.5],
    ["a", "15", 267],
    ["a", "16", 85],
    ["a", "17", 47.8],
    ["d", "18", 5],
    ["d", "19", 21],
    ["d", "20", 2.4],
    ["d", "21", 5.3],
    ["d", "22", 19.5],
    ["d", "23", 636],
    ["d", "24", 150],
    ["d", "25", 296.5],
    ["d", "26", 53.1],
    ["d", "27", 5.3],
    ["d", "28", 1451],
    ["d", "29", 19.9],
]


def calc():
    general_cp = 0x0
    pve_cp = 0x0
    pvp_cp = 0x0
    pure_pve_cp = 0x0
    pure_pvp_cp = 0x0
    attack_ability_general = 0x0
    attack_ability_pve = 0x0
    attack_ability_pvp = 0x0
    defense_ability_general = 0x0
    defense_ability_pve = 0x0
    defense_ability_pvp = 0x0

    for stats_element in stats:
        type_and_id = str(stats_element[0x0]) + "_" + str(stats_element[0x1])

        type_and_id_general = type_and_id + "_g"
        type_and_id_pve = type_and_id + "_e"
        type_and_id_pvp = type_and_id + "_p"

        general_stat_value = input_stats[type_and_id_general] * float(stats_element[2])
        pve_stat_value = input_stats[type_and_id_pve] * float(stats_element[2])
        pvp_stat_value = input_stats[type_and_id_pvp] * float(stats_element[2])

        general_cp += general_stat_value
        pve_cp += general_stat_value + pve_stat_value
        pvp_cp += general_stat_value + pvp_stat_value
        pure_pve_cp += pve_stat_value
        pure_pvp_cp += pvp_stat_value

        # atack ability
        if stats_element[0x0] == "a":
            attack_ability_general += general_stat_value
            attack_ability_pve += pve_stat_value
            attack_ability_pvp += pvp_stat_value

        # defense ability
        if stats_element[0x0] == "d":
            defense_ability_general += general_stat_value
            defense_ability_pve += pve_stat_value
            defense_ability_pvp += pvp_stat_value

    print("general combat power", general_cp)
    print("pve combat power", pve_cp)
    print("pvp combat power", pvp_cp)
    print("pure pve combat power", pure_pve_cp)
    print("pure pvp combat power", pure_pvp_cp)
    print("attack ability general", attack_ability_general)
    print("attack ability pve", attack_ability_pve)
    print("attack ability pvp", attack_ability_pvp)
    print("defense ability general", defense_ability_general)
    print("defense ability pve", defense_ability_pve)
    print("defense ability pvp", defense_ability_pvp)
