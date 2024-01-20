import typing

from BaseClasses import MultiWorld, Region, Entrance, Location
from worlds.AutoWorld import World
from dk64r.randomizer.Lists import Item as DK64RItem
from dk64r.randomizer.Enums.Items import Items as DK64RItems

from dk64r.randomizer.Lists import Location as DK64RLocation
from dk64r.randomizer.Enums.Locations import Locations as DK64RLocations
from .Logic import LogicVarHolder
from dk64r.randomizer.Spoiler import Spoiler
from dk64r.randomizer.Settings import Settings
from dk64r.randomizer.LogicFiles import (
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

def connect_regions(world: World, logic_holder: LogicVarHolder):
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
                    converted_logic = lambda state: loc.logic(logic_holder)
                    connect(world, location.name, loc.id.name, converted_logic)
                except Exception:
                    pass
    pass


def connect(world: World, source: str, target: str, rule: typing.Optional[typing.Callable] = None):
    source_region = world.multiworld.get_region(source, world.player)
    target_region = world.multiworld.get_region(target, world.player)

    name = source + "->" + target
    player= None
    connection = Entrance(world.player, name, source_region)

    if rule:
        connection.access_rule = rule

    source_region.exits.append(connection)
    connection.connect(target_region)
