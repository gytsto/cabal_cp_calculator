from calculate import *

# fmt: off
BASE_STATS = Stats(
    attack                    = StatValue(general = 2381, pve = 50 , pvp = 0),
    attack_rate               = StatValue(general = 7710, pve = 0  , pvp = 0),
    crit_rate                 = StatValue(general = 21  , pve = 0  , pvp = 0),
    crit_dmg                  = StatValue(general = 127 , pve = 21 , pvp = 8),
    all_skill_amp             = StatValue(general = 43  , pve = 8  , pvp = 2),
    accuracy                  = StatValue(general = 1510, pve = 0  , pvp = 0),
    penetration               = StatValue(general = 465 , pve = 30 , pvp = 0),
    add_dmg                   = StatValue(general = 136 , pve = 0  , pvp = 0),
    ignore_evasion            = StatValue(general = 475 , pve = 0  , pvp = 0),
    ignore_dmg_red            = StatValue(general = 92  , pve = 2  , pvp = 0),
    final_dmg_increase        = StatValue(general = 2   , pve = 0  , pvp = 0),
    ignore_resist_crit_rate   = StatValue(general = 10  , pve = 0  , pvp = 0),
    ignore_resist_crit_dmg    = StatValue(general = 47  , pve = 0  , pvp = 0),
    ignore_resist_skill_amp   = StatValue(general = 18  , pve = 0  , pvp = 0),
    normal_dmg_up             = StatValue(general = 63  , pve = 3  , pvp = 0),
    cancel_ignore_penetration = StatValue(general = 173 , pve = 0  , pvp = 0),
    hp                        = StatValue(general = 8648, pve = 0  , pvp = 0),
    defense                   = StatValue(general = 1382, pve = 106, pvp = 0),
    defense_rate              = StatValue(general = 7228, pve = 0  , pvp = 0),
    evasion                   = StatValue(general = 4004, pve = 0  , pvp = 0),
    dmg_red                   = StatValue(general = 627 , pve = 74 , pvp = 0),
    resit_crit_rate           = StatValue(general = 13  , pve = 0  , pvp = 0),
    resit_crit_dmg            = StatValue(general = 108 , pve = 0  , pvp = 0),
    resit_skill_amp           = StatValue(general = 26  , pve = 0  , pvp = 0),
    ignore_penetration        = StatValue(general = 276 , pve = 21 , pvp = 0),
    ignore_accuracy           = StatValue(general = 1363, pve = 0  , pvp = 0),
    final_dmg_decrease        = StatValue(general = 0   , pve = 0  , pvp = 0),
    cancel_ignore_dmg_reduce  = StatValue(general = 2   , pve = 0  , pvp = 0),
)
# fmt: on

cp, aa, da = calculate_combat_power(BASE_STATS)

print(f"combat power {cp}")
print(f"attack ability {aa}")
print(f"defense ability {da}")
