from functools import partial


godhome_event_names = ["Godhome_Flower_Quest", "Defeated_Pantheon_5", "GG_Atrium_Roof", "Defeated_Pantheon_1", "Defeated_Pantheon_2", "Defeated_Pantheon_3", "Opened_Pantheon_4", "Defeated_Pantheon_4", "GG_Atrium", "Hit_Pantheon_5_Unlock_Orb", "GG_Workshop", "Can_Damage_Crystal_Guardian", 'Defeated_Any_Soul_Warrior', "Defeated_Colosseum_3", "COMBAT[Radiance]", "COMBAT[Pantheon_1]", "COMBAT[Pantheon_2]", "COMBAT[Pantheon_3]", "COMBAT[Pantheon_4]", "COMBAT[Pantheon_5]", "COMBAT[Colosseum_3]", 'Warp-Junk_Pit_to_Godhome', 'Bench-Godhome_Atrium', 'Bench-Hall_of_Gods', "GODTUNERUNLOCK", "GG_Waterways", "Warp-Godhome_to_Junk_Pit", "NAILCOMBAT", "BOSS", "AERIALMINIBOSS"]


def set_godhome_rules(hk_world, hk_set_rule):
    player = hk_world.player
    fn = partial(hk_set_rule, hk_world)

    required_events = {
        "Godhome_Flower_Quest": lambda state: state.count('Defeated_Pantheon_5', player) and state.count('Room_Mansion[left1]', player) and state.count('Fungus3_49[right1]', player),

        "Defeated_Pantheon_5": lambda state: state.has('GG_Atrium_Roof', player) and state.has('WINGS', player) and (state.has('LEFTCLAW', player) or state.has('RIGHTCLAW', player)) and ((state.has('Defeated_Pantheon_1', player) and state.has('Defeated_Pantheon_2', player) and state.has('Defeated_Pantheon_3', player) and state.has('Defeated_Pantheon_4', player) and state.has('COMBAT[Radiance]', player))),
        "GG_Atrium_Roof": lambda state: state.has('GG_Atrium', player) and state.has('Hit_Pantheon_5_Unlock_Orb', player) and state.has('LEFTCLAW', player),

        "Defeated_Pantheon_1": lambda state: state.has('GG_Atrium', player) and ((state.has('Defeated_Gruz_Mother', player) and state.has('Defeated_False_Knight', player) and (state.has('Fungus1_29[left1]', player) or state.has('Fungus1_29[right1]', player)) and state.has('Defeated_Hornet_1', player) and state.has('Defeated_Gorb', player) and state.has('Defeated_Dung_Defender', player) and state.has('Defeated_Any_Soul_Warrior', player) and state.has('Defeated_Brooding_Mawlek', player))),
        "Defeated_Pantheon_2": lambda state: state.has('GG_Atrium', player) and ((state.has('Defeated_Xero', player) and state.has('Defeated_Crystal_Guardian', player) and state.has('Defeated_Soul_Master', player) and state.has('Defeated_Colosseum_2', player) and state.has('Defeated_Mantis_Lords', player) and state.has('Defeated_Marmu', player) and state.has('Defeated_Nosk', player) and state.has('Defeated_Flukemarm', player) and state.has('Defeated_Broken_Vessel', player))),
        "Defeated_Pantheon_3": lambda state: state.has('GG_Atrium', player) and ((state.has('Defeated_Hive_Knight', player) and state.has('Defeated_Elder_Hu', player) and state.has('Defeated_Collector', player) and state.has('Defeated_Colosseum_2', player) and state.has('Defeated_Grimm', player) and state.has('Defeated_Galien', player) and state.has('Defeated_Uumuu', player) and state.has('Defeated_Hornet_2', player))),
        "Opened_Pantheon_4": lambda state: state.has('GG_Atrium', player) and (state.has('Defeated_Pantheon_1', player) and state.has('Defeated_Pantheon_2', player) and state.has('Defeated_Pantheon_3', player)),
        "Defeated_Pantheon_4": lambda state: state.has('GG_Atrium', player) and state.has('Opened_Pantheon_4', player) and ((state.has('Defeated_Enraged_Guardian', player) and state.has('Defeated_Broken_Vessel', player) and state.has('Defeated_No_Eyes', player) and state.has('Defeated_Traitor_Lord', player) and state.has('Defeated_Dung_Defender', player) and state.has('Defeated_False_Knight', player) and state.has('Defeated_Markoth', player) and state.has('Defeated_Watcher_Knights', player) and state.has('Defeated_Soul_Master', player))),
        "GG_Atrium": lambda state: state.has('Warp-Junk_Pit_to_Godhome', player) and (state.has('RIGHTCLAW', player) or state.has('WINGS', player) or state.has('LEFTCLAW', player) and state.has('RIGHTSUPERDASH', player)) or state.has('GG_Workshop', player) and (state.has('LEFTCLAW', player) or state.has('RIGHTCLAW', player) and state.has('WINGS', player)) or state.has('Bench-Godhome_Atrium', player),
        "Hit_Pantheon_5_Unlock_Orb": lambda state: state.has('GG_Atrium', player) and state.has('WINGS', player) and (state.has('LEFTCLAW', player) or state.has('RIGHTCLAW', player)) and (((state.has('Queen_Fragment', player) and state.has('King_Fragment', player) and state.has('Void_Heart', player)) and state.has('Defeated_Pantheon_1', player) and state.has('Defeated_Pantheon_2', player) and state.has('Defeated_Pantheon_3', player) and state.has('Defeated_Pantheon_4', player))),
        "GG_Workshop": lambda state: state.has('GG_Atrium', player) or state.has('Bench-Hall_of_Gods', player),
        "Can_Damage_Crystal_Guardian": lambda state: state.has('UPSLASH', player) or state.has('LEFTSLASH', player) or state.has('RIGHTSLASH', player) or state._hk_option(player, 'ProficientCombat') and (state.has('CYCLONE', player) or state.has('Great_Slash', player)) or (state._hk_option(player, 'DifficultSkips') and state._hk_option(player, 'ProficientCombat')) and (state.has('CYCLONE', player) or state.has('Great_Slash', player)) and (state.has('DREAMNAIL', player) and (state.has('SPELLS', player) or state.has('FOCUS', player) and state.has('Spore_Shroom', player) or state.has('Glowing_Womb', player)) or state.has('Weaversong', player)),
        'Defeated_Any_Soul_Warrior': lambda state: state.has('Defeated_Sanctum_Warrior', player) or state.has('Defeated_Elegant_Warrior', player) or state.has('Room_Colosseum_01[left1]', player) and state.has('Defeated_Colosseum_3', player),
        "Defeated_Colosseum_3": lambda state: state.has('Room_Colosseum_01[left1]', player) and state.has('Can_Replenish_Geo', player) and ((state.has('LEFTCLAW', player) or state.has('RIGHTCLAW', player)) or ((state._hk_option(player, 'DifficultSkips') and state._hk_option(player, 'ProficientCombat')) and state.has('WINGS', player))) and state.has('COMBAT[Colosseum_3]', player),

        # MACROS
        "COMBAT[Radiance]": lambda state: (state.has('LEFTDASH', player) and state.has('RIGHTDASH', player)) and ((((state.count('LEFTDASH', player) > 1 or state.count('RIGHTDASH', player) > 1) and state.has('LEFTDASH', player)) and ((state.count('LEFTDASH', player) > 1 or state.count('RIGHTDASH', player) > 1) and state.has('RIGHTDASH', player))) or state.has('QUAKE', player)) and (state.count('FIREBALL', player) > 1 and state.has('UPSLASH', player) or state.count('SCREAM', player) > 1 and state.has('UPSLASH', player) or state._hk_option(player, 'RemoveSpellUpgrades') and (state.has('FIREBALL', player) or state.has('SCREAM', player)) and state.has('UPSLASH', player) or state._hk_option(player, 'ProficientCombat') and (state.has('FIREBALL', player) or state.has('SCREAM', player)) and (state.has('UPSLASH', player) or (state.has('LEFTSLASH', player) or state.has('RIGHTSLASH', player)) or state.has('Great_Slash', player)) or (state._hk_option(player, 'DifficultSkips') and state._hk_option(player, 'ProficientCombat'))),
        "COMBAT[Pantheon_1]": lambda state: state.has('AERIALMINIBOSS', player) and state.count('SPELLS', player) > 1 and (state.has('FOCUS', player) or (state._hk_option(player, 'DifficultSkips') and state._hk_option(player, 'ProficientCombat'))),
        "COMBAT[Pantheon_2]": lambda state: state.has('AERIALMINIBOSS', player) and state.count('SPELLS', player) > 1 and (state.has('FOCUS', player) or (state._hk_option(player, 'DifficultSkips') and state._hk_option(player, 'ProficientCombat'))) and state.has('Can_Damage_Crystal_Guardian', player),
        "COMBAT[Pantheon_3]": lambda state: state.has('AERIALMINIBOSS', player) and state.count('SPELLS', player) > 1 and (state.has('FOCUS', player) or (state._hk_option(player, 'DifficultSkips') and state._hk_option(player, 'ProficientCombat'))),
        "COMBAT[Pantheon_4]": lambda state: state.has('AERIALMINIBOSS', player) and (state.has('FOCUS', player) or (state._hk_option(player, 'DifficultSkips') and state._hk_option(player, 'ProficientCombat'))) and state.has('Can_Damage_Crystal_Guardian', player) and (state.has('LEFTDASH', player) and state.has('RIGHTDASH', player)) and ((((state.count('LEFTDASH', player) > 1 or state.count('RIGHTDASH', player) > 1) and state.has('LEFTDASH', player)) and ((state.count('LEFTDASH', player) > 1 or state.count('RIGHTDASH', player) > 1) and state.has('RIGHTDASH', player))) or state.has('QUAKE', player)) and (state.count('FIREBALL', player) > 1 and state.has('UPSLASH', player) or state.count('SCREAM', player) > 1 and state.has('UPSLASH', player) or state._hk_option(player, 'RemoveSpellUpgrades') and (state.has('FIREBALL', player) or state.has('SCREAM', player)) and state.has('UPSLASH', player) or state._hk_option(player, 'ProficientCombat') and (state.has('FIREBALL', player) or state.has('SCREAM', player)) and (state.has('UPSLASH', player) or (state.has('LEFTSLASH', player) or state.has('RIGHTSLASH', player)) or state.has('Great_Slash', player)) or (state._hk_option(player, 'DifficultSkips') and state._hk_option(player, 'ProficientCombat'))),
        "COMBAT[Pantheon_5]": lambda state: state.has('AERIALMINIBOSS', player) and state.has('FOCUS', player) and state.has('Can_Damage_Crystal_Guardian', player) and (state.has('LEFTDASH', player) and state.has('RIGHTDASH', player)) and ((((state.count('LEFTDASH', player) > 1 or state.count('RIGHTDASH', player) > 1) and state.has('LEFTDASH', player)) and ((state.count('LEFTDASH', player) > 1 or state.count('RIGHTDASH', player) > 1) and state.has('RIGHTDASH', player))) or state.has('QUAKE', player)) and (state.count('FIREBALL', player) > 1 and state.has('UPSLASH', player) or state.count('SCREAM', player) > 1 and state.has('UPSLASH', player) or state._hk_option(player, 'RemoveSpellUpgrades') and (state.has('FIREBALL', player) or state.has('SCREAM', player)) and state.has('UPSLASH', player) or state._hk_option(player, 'ProficientCombat') and (state.has('FIREBALL', player) or state.has('SCREAM', player)) and (state.has('UPSLASH', player) or (state.has('LEFTSLASH', player) or state.has('RIGHTSLASH', player)) or state.has('Great_Slash', player)) or (state._hk_option(player, 'DifficultSkips') and state._hk_option(player, 'ProficientCombat'))),
        "COMBAT[Colosseum_3]": lambda state: state.has('BOSS', player) and (state.has('FOCUS', player) or (state._hk_option(player, 'DifficultSkips') and state._hk_option(player, 'ProficientCombat'))),

        # MISC
        'Warp-Junk_Pit_to_Godhome': lambda state: state.has('GG_Waterways', player) and state.has('GODTUNERUNLOCK', player) and state.has('DREAMNAIL', player),
        'Bench-Godhome_Atrium': lambda state: state.has('GG_Atrium', player) and (state.has('RIGHTCLAW', player) and (state.has('RIGHTDASH', player) or state.has('LEFTCLAW', player) and state.has('RIGHTSUPERDASH', player) or state.has('WINGS', player)) or state.has('LEFTCLAW', player) and state.has('WINGS', player)),
        'Bench-Hall_of_Gods': lambda state: state.has('GG_Workshop', player) and ((state.has('LEFTCLAW', player) or state.has('RIGHTCLAW', player))),

        "GODTUNERUNLOCK": lambda state: state.count('SIMPLE', player) > 3,
        "GG_Waterways": lambda state: state.has('GG_Waterways[door1]', player) or state.has('GG_Waterways[right1]', player) and (state.has('LEFTSUPERDASH', player) or state.has('SWIM', player)) or state.has('Warp-Godhome_to_Junk_Pit', player),
        "Warp-Godhome_to_Junk_Pit": lambda state: state.has('Warp-Junk_Pit_to_Godhome', player) or state.has('GG_Atrium', player),

        # COMBAT MACROS
        "NAILCOMBAT": lambda state: (state.has('LEFTSLASH', player) or state.has('RIGHTSLASH', player)) or state.has('UPSLASH', player) or state._hk_option(player, 'ProficientCombat') and (state.has('CYCLONE', player) or state.has('Great_Slash', player)) or (state._hk_option(player, 'DifficultSkips') and state._hk_option(player, 'ProficientCombat')),
        "BOSS": lambda state: state.count('SPELLS', player) > 1 and ((state.has('LEFTDASH', player) or state.has('RIGHTDASH', player)) and ((state.has('LEFTSLASH', player) or state.has('RIGHTSLASH', player)) or state.has('UPSLASH', player)) or state._hk_option(player, 'ProficientCombat') and state.has('NAILCOMBAT', player)),
        "AERIALMINIBOSS": lambda state: (state.has('FIREBALL', player) or state.has('SCREAM', player)) and (state.has('LEFTDASH', player) or state.has('RIGHTDASH', player)) and ((state.has('LEFTSLASH', player) or state.has('RIGHTSLASH', player)) or state.has('UPSLASH', player)) or state._hk_option(player, 'ProficientCombat') and (state.has('FIREBALL', player) or state.has('SCREAM', player)) and ((state.has('LEFTSLASH', player) or state.has('RIGHTSLASH', player)) or state.has('UPSLASH', player)) or (state._hk_option(player, 'DifficultSkips') and state._hk_option(player, 'ProficientCombat')) and ((state.has('LEFTSLASH', player) or state.has('RIGHTSLASH', player)) or state.has('UPSLASH', player) or state.has('CYCLONE', player) or state.has('Great_Slash', player)),

    }

    for item, rule in required_events.items():
        fn(item, rule)
