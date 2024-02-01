import typing

from Options import Choice, Range, Option, Toggle, DeathLink, DefaultOnToggle, OptionList

from randomizer.Enums.Settings import SettingsStringEnum
from randomizer.Enums.Settings import SettingsStringTypeMap
from randomizer.Enums.Settings import SettingsStringDataType
from randomizer.Enums.Settings import SettingsMap as DK64RSettingsMap


# DK64_TODO: Get Options from DK64R

class Goal(Choice):
    """
    Determines the goal of the seed
    """
    display_name = "Goal"
    option_krool = 0
    default = 0


def GenerateDK64Options() -> typing.Dict[str, type(Option)]:
    dk64_options: typing.Dict[str, type(Option)] = {}

    for setting_id, setting_type in SettingsStringTypeMap.items():

        if setting_type == SettingsStringDataType.bool:
            new_option = type(str(setting_id).split(".")[1], (Toggle, ), { "display_name": str(setting_id).split(".")[1] })
            new_option.__doc__ = setting_type.__doc__
            dk64_options[str(setting_id).split(".")[1]] = new_option

    dk64_options["goal"] = Goal
    return dk64_options


dk64_options: typing.Dict[str, type(Option)] = {
#    "death_link": DeathLink,
#    "goal": Goal,
#    "activate_all_bananaports": ActivateAllBananaports,
#    "alter_switch_allocation": false,
#    "auto_keys": true,
#    "bananaport_rando": "in_level",
#    "blocker_0": 1,
#    "blocker_1": 2,
#    "blocker_2": 3,
#    "blocker_3": 4,
#    "blocker_4": 5,
#    "blocker_5": 6,
#    "blocker_6": 7,
#    "blocker_7": 8,
#    "blocker_text": 40,
#    "bonus_barrel_auto_complete": false,
#    "bonus_barrel_rando": true,
#    "boss_kong_rando": true,
#    "boss_location_rando": true,
#    "cb_rando":false,
#    "coin_rando":false,
#    "coin_door_item": "opened",
#    "coin_door_item_count": 1,
#    "crown_door_item": "opened",
#    "crown_door_item_count": 1,
#    "crown_enemy_rando": "easy",
#    "crown_placement_rando": false,
#    "damage_amount": "default",
#    "enable_shop_hints": true,
#    "disable_tag_barrels": false,
#    "dpad_display": "on",
#    "enable_tag_anywhere": true,
#    "enemies_selected": [],
#    "enemy_rando": true,
#    "enemy_speed_rando": true,
#    "fast_gbs": true,
#    "fast_warps": true,
#    "fps_display": false,
#    "free_trade_setting": "none",
#    "generate_spoilerlog": true,
#    "glitches_selected":[],
#    "hard_blockers": false,
#    "hard_bosses": false,
#    "hard_enemies": false,
#    "hard_level_progression": false,
#    "hard_shooting": false,
#    "hard_troff_n_scoff": false,
#    "helm_hurry": false,
#    "helm_setting": "skip_start",
#    "helmhurry_list_starting_time": 0,
#    "helmhurry_list_golden_banana": 0,
#    "helmhurry_list_blueprint": 0,
#    "helmhurry_list_company_coins": 0,
#    "helmhurry_list_move": 0,
#    "helmhurry_list_banana_medal": 0,
#    "helmhurry_list_rainbow_coin": 0,
#    "helmhurry_list_boss_key": 0,
#    "helmhurry_list_battle_crown": 0,
#    "helmhurry_list_bean": 0,
#    "helmhurry_list_pearl": 0,
#    "helmhurry_list_kongs": 0,
#    "helmhurry_list_fairies": 0,
#    "helmhurry_list_colored_bananas": 0,
#    "helmhurry_list_ice_traps": 0,
#    "high_req": true,
#    "item_rando_list_selected": [],
#    "item_reward_previews": true,
#    "kasplat_rando_setting": "vanilla_locations",
#    "key_8_helm": false,
#    "keys_random": false,
#    "kong_rando": true,
#    "krool_access": true,
#    "krool_key_count": 8,
#    "krool_phase_count": 3,
#    "krool_phase_order_rando": true,
#    "krool_random": false,
#    "krusha_ui": "no_slot",
#    "helm_phase_order_rando": true,
#    "helm_random": false,
#    "helm_phase_count": 3,
#    "level_randomization": "level_order",
#    "logic_type": "glitchless",
#    "maximize_helm_blocker": true,
#    "medal_cb_req": 75,
#    "medal_requirement": 15,
#    "microhints_enabled": "all",
#    "minigames_list_selected": [],
#    "misc_changes_selected": [],
#    "move_rando": "on",
#    "no_healing": false,
#    "no_melons": false,
#    "open_levels": false,
#    "open_lobbies": false,
#    "perma_death": false,
#    "portal_numbers": true,
#    "puzzle_rando": true,
#    "quality_of_life": true,
#    "random_fairies": false,
#    "random_medal_requirement": false,
#    "random_patches": true,
#    "random_prices": "low",
#    "random_starting_region": false,
#    "randomize_blocker_required_amounts": true,
#    "randomize_cb_required_amounts": true,
#    "randomize_pickups": false,
#    "rareware_gb_fairies": 20,
#    "select_keys": false,
#    "shockwave_status": "vanilla",
#    "shop_indicator": true,
#    "shorten_boss": true,
#    "shuffle_items": false,
#    "shuffle_shops": true,
#    "smaller_shops": false,
#    "starting_keys_list_selected": [],
#    "starting_kongs_count": 3,
#    "starting_moves_count": 4,
#    "starting_random": false,
#    "tns_location_rando": false,
#    "training_barrels": "normal",
#    "troff_0": 1,
#    "troff_1": 2,
#    "troff_2": 3,
#    "troff_3": 4,
#    "troff_4": 5,
#    "troff_5": 6,
#    "troff_6": 7,
#    "troff_text": 300,
#    "vanilla_door_rando": false,
#    "warp_level_list_selected": [],
#    "warp_to_isles": true,
#    "win_condition": "beat_krool",
#    "wrinkly_available": false,
#    "wrinkly_hints": "standard",
#    "wrinkly_location_rando": false
}