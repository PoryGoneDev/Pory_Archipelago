import typing

from BaseClasses import MultiWorld, Region, Entrance, Location
from worlds.AutoWorld import World
import re
import inspect
from randomizer.Lists import Item as DK64RItem
from randomizer.Enums.Items import Items as DK64RItems

from randomizer.Lists import Location as DK64RLocation
from randomizer.Enums.Locations import Locations as DK64RLocations
from randomizer.LogicFiles import (
    AngryAztec,
    CreepyCastle,
    CrystalCaves,
    DKIsles,
    FungiForest,
    HideoutHelm,
    JungleJapes,
    FranticFactory,
    GloomyGalleon,
    Shops,
)

BASE_ID = 0xD64000


class DK64Location(Location):
    game: str = "Donkey Kong 64"

    def __init__(self, player: int, name: str = "", address: int = None, parent=None):
        super().__init__(player, name, address, parent)


# Complete location table
all_locations = {location.name: (BASE_ID + index) for index, location in enumerate(DK64RLocation.LocationListOriginal)}
all_locations.update({"Victory": 0x00})  # Temp for generating goal location
lookup_id_to_name: typing.Dict[int, str] = {id: name for name, id in all_locations.items()}


def create_regions(multiworld: MultiWorld, player: int):
    menu_region = create_region(multiworld, player, "Menu")
    test_region = create_region(multiworld, player, "Test", ["Victory"])

    multiworld.regions += [
        menu_region,
        test_region,
    ]

    def _logic_region(GroupedRegion):
        for location in GroupedRegion:
            location_list = []
            region_obj = GroupedRegion[location]
            for loc in region_obj.locations:
                location_list.append(loc.id.name)
            multiworld.regions.append(create_region(multiworld, player, location.name, location_list))

    for region in [
        AngryAztec.LogicRegions,
        CreepyCastle.LogicRegions,
        CrystalCaves.LogicRegions,
        DKIsles.LogicRegions,
        FungiForest.LogicRegions,
        HideoutHelm.LogicRegions,
        JungleJapes.LogicRegions,
        FranticFactory.LogicRegions,
        GloomyGalleon.LogicRegions,
        Shops.LogicRegions,
    ]:
        _logic_region(region)


def create_region(multiworld: MultiWorld, player: int, name: str, locations=None) -> Region:
    new_region = Region(name, player, multiworld)
    if locations:
        for location_name in locations:
            loc_id = all_locations.get(location_name, 0)

            location = DK64Location(player, location_name, loc_id, new_region)
            new_region.locations.append(location)

    return new_region
from textwrap import dedent

def get_lambda_source(lambda_func):
    source = inspect.getsource(lambda_func)
    # Normalize the string
    source = dedent(source)

    # Find the lambda keyword and then match balanced parentheses
    lambda_match = re.search(r'\blambda\b[^:]+:(?:[^()]|\([^()]*\))+', source)

    if lambda_match:
        return lambda_match.group()
    else:
        raise ValueError("No valid lambda expression found")
def new_logic(original_logic):
    # Extract the original lambda's source code if possible
    try:
        source_code = get_lambda_source(original_logic).strip()
    except:
        # If the source code can't be extracted, fallback to a default behavior or raise an error
        raise ValueError("Could not extract logic source code")

    # Apply the rules to transform the logic
    updated_source_code = source_code
    if " and " in source_code or " or " in source_code:
        # Split the logic into individual conditions and process each one
        conditions = source_code[source_code.find("lambda"):].split(" and ")
        updated_conditions = []
        for condition in conditions:
            if condition.strip().startswith("not l.settings."):
                updated_conditions.append(condition.replace("l.settings.", "world.options."))
            elif condition.strip().startswith("l.") and not condition.strip().startswith("l.is"):
                var_name = condition.strip()[2:]
                updated_conditions.append(f"l.has(\"{var_name.capitalize()}\")")
            else:
                updated_conditions.append(condition)
        updated_source_code = " and ".join(updated_conditions)
    else:
        # Process single condition
        if source_code.strip().startswith("not l.settings."):
            updated_source_code = source_code.replace("l.settings.", "world.options.")
        elif source_code.strip().startswith("l.") and not source_code.strip().startswith("l.is"):
            var_name = source_code.strip()[2:]
            updated_source_code = f"l.has(\"{var_name.capitalize()}\")"
        # else leave True, False, and is... conditions unchanged

    # Return the updated lambda function, compiled from the new source code
    print(updated_source_code[source_code.find("lambda"):])
    return eval(updated_source_code[source_code.find("lambda"):])

def connect_regions(world: World):
    # connect(world, "Menu", "DK Isles")

    # # Example Region Connection
    # connect(
    #     world,
    #     "DK Isles",
    #     "Test",
    #     lambda state: state.has(DK64RItem.ItemList[DK64RItems.GoldenBanana].name, world.player, 2),
    # )

    # DK64_TODO: Get region access requirements from DK64R
    for region in [
        AngryAztec.LogicRegions,
        CreepyCastle.LogicRegions,
        CrystalCaves.LogicRegions,
        DKIsles.LogicRegions,
        FungiForest.LogicRegions,
        HideoutHelm.LogicRegions,
        JungleJapes.LogicRegions,
        FranticFactory.LogicRegions,
        GloomyGalleon.LogicRegions,
        Shops.LogicRegions,
    ]:
        for location in region:
            region_obj = region[location]
            for loc in region_obj.locations:
                try:
                    converted_logic = new_logic(loc.logic)
                    print(converted_logic)
                    connect(world, location.name, loc.id.name, converted_logic)
                except Exception:
                    pass
    pass


def connect(world: World, source: str, target: str, rule: typing.Optional[typing.Callable] = None):
    source_region = world.multiworld.get_region(source, world.player)
    target_region = world.multiworld.get_region(target, world.player)

    name = source + "->" + target
    player= None
    connection = Entrance(player, name, source_region)

    if rule:
        connection.access_rule = rule

    source_region.exits.append(connection)
    connection.connect(target_region)
