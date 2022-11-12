import typing
import copy

from BaseClasses import MultiWorld


mission_orders: typing.List[typing.List[int]] = [
    [1, 2, 3, 4, 5],
    [1, 2, 3, 5, 4],
    [1, 2, 4, 3, 5],
    [1, 2, 4, 5, 3],
    [1, 2, 5, 3, 4],
    [1, 2, 5, 4, 3],

    [1, 3, 2, 4, 5],
    [1, 3, 2, 5, 4],
    [1, 3, 4, 2, 5],
    [1, 3, 4, 5, 2],
    [1, 3, 5, 2, 4],
    [1, 3, 5, 4, 2],

    [1, 4, 2, 3, 5],
    [1, 4, 2, 5, 3],
    [1, 4, 3, 2, 5],
    [1, 4, 3, 5, 2],
    [1, 4, 5, 2, 3],
    [1, 4, 5, 3, 2],

    [1, 5, 2, 3, 4],
    [1, 5, 2, 4, 3],
    [1, 5, 3, 2, 4],
    [1, 5, 3, 4, 2],
    [1, 5, 4, 2, 3],
    [1, 5, 4, 3, 2],

    [2, 1, 3, 4, 5],
    [2, 1, 3, 5, 4],
    [2, 1, 4, 3, 5],
    [2, 1, 4, 5, 3],
    [2, 1, 5, 3, 4],
    [2, 1, 5, 4, 3],

    [2, 3, 1, 4, 5],
    [2, 3, 1, 5, 4],
    [2, 3, 4, 1, 5],
    [2, 3, 4, 5, 1],
    [2, 3, 5, 1, 4],
    [2, 3, 5, 4, 1],

    [2, 4, 1, 3, 5],
    [2, 4, 1, 5, 3],
    [2, 4, 3, 1, 5],
    [2, 4, 3, 5, 1],
    [2, 4, 5, 1, 3],
    [2, 4, 5, 3, 1],

    [2, 5, 1, 3, 4],
    [2, 5, 1, 4, 3],
    [2, 5, 3, 1, 4],
    [2, 5, 3, 4, 1],
    [2, 5, 4, 1, 3],
    [2, 5, 4, 3, 1],

    [4, 1, 2, 3, 5],
    [4, 1, 2, 5, 3],
    [4, 1, 3, 2, 5],
    [4, 1, 3, 5, 2],
    [4, 1, 5, 3, 2],
    [4, 1, 5, 2, 3],

    [4, 3, 1, 2, 5],
    [4, 3, 1, 5, 2],
    [4, 3, 2, 1, 5],
    [4, 3, 2, 5, 1],
    [4, 3, 5, 1, 2],
    [4, 3, 5, 2, 1],

    [4, 2, 1, 3, 5],
    [4, 2, 1, 5, 3],
    [4, 2, 3, 1, 5],
    [4, 2, 3, 5, 1],
    [4, 2, 5, 1, 3],
    [4, 2, 5, 3, 1],

    [4, 5, 1, 3, 2],
    [4, 5, 1, 2, 3],
    [4, 5, 2, 1, 3],
    [4, 5, 2, 3, 1],
    [4, 5, 3, 1, 2],
    [4, 5, 3, 2, 1],
]

### 0: Speed
### 1: Mech
### 2: Hunt
### 3: Kart
### 4: Cannon's Core
level_styles: typing.List[int] = [
    0,
    2,
    1,
    0,
    0,
    2,
    1,
    2,
    3,
    1,
    0,
    2,
    1,
    2,
    0,
    0,

    1,
    2,
    1,
    0,
    2,
    1,
    1,
    2,
    0,
    3,
    0,
    2,
    1,
    0,

    4,
]



def get_mission_table(multiworld: MultiWorld, player: int):
    mission_table: typing.Dict[int, int] = {}

    speed_active_missions: typing.List[int] = [1]
    mech_active_missions: typing.List[int] = [1]
    hunt_active_missions: typing.List[int] = [1]
    kart_active_missions: typing.List[int] = [1]
    cannons_core_active_missions: typing.List[int] = [1]

    # Add included missions
    for i in range(2,6):
        if getattr(multiworld, "speed_mission_" + str(i), None)[player]:
            speed_active_missions.append(i)

        if getattr(multiworld, "mech_mission_" + str(i), None)[player]:
            mech_active_missions.append(i)

        if getattr(multiworld, "hunt_mission_" + str(i), None)[player]:
            hunt_active_missions.append(i)

        if getattr(multiworld, "kart_mission_" + str(i), None)[player]:
            kart_active_missions.append(i)

        if getattr(multiworld, "cannons_core_mission_" + str(i), None)[player]:
            cannons_core_active_missions.append(i)

    active_missions: typing.List[typing.List[int]] = [
        speed_active_missions,
        mech_active_missions,
        hunt_active_missions,
        kart_active_missions,
        cannons_core_active_missions
    ]

    for level in range(31):
        level_style = level_styles[level]

        level_active_missions: typing.List[int] = copy.deepcopy(active_missions[level_style])
        level_chosen_missions: typing.List[int] = []

        # The first mission must be M1, M2, or M4
        first_mission = 1

        if multiworld.mission_shuffle[player]:
            first_mission = multiworld.random.choice([mission for mission in level_active_missions if mission in [1, 2, 4]])

        level_active_missions.remove(first_mission)

        # Place Active Missions in the chosen mission list
        for mission in level_active_missions:
            if mission not in level_chosen_missions:
                level_chosen_missions.append(mission)

        if multiworld.mission_shuffle[player]:
            multiworld.random.shuffle(level_chosen_missions)

        level_chosen_missions.insert(0, first_mission)

        # Fill in the non-included missions
        for i in range(2,6):
            if i not in level_chosen_missions:
                level_chosen_missions.append(i)

        # Determine which mission order index we have, for conveying to the mod
        for i in range(len(mission_orders)):
            if mission_orders[i] == level_chosen_missions:
                level_mission_index = i
                break

        print("End: ", level_chosen_missions)
        mission_table[level] = level_mission_index

    return mission_table
