import typing

from BaseClasses import CollectionState, MultiWorld, Region, Entrance, Location
from worlds.AutoWorld import World

from dk64r.randomizer.Lists import Location as DK64RLocation
from dk64r.randomizer.LogicClasses import LocationLogic, TransitionFront
from worlds.generic.Rules import set_rule
from .Logic import LogicVarHolder
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


def create_regions(multiworld: MultiWorld, player: int, logic_holder: LogicVarHolder):    
    for level_regions in [
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
        for region_id in level_regions:
            location_logics = []
            region_obj = level_regions[region_id]
            for loc in region_obj.locations:
                if not loc.isAuxiliaryLocation:
                    location_logics.append(loc)
            multiworld.regions.append(create_region(multiworld, player, region_obj.name, location_logics, logic_holder))


def create_region(multiworld: MultiWorld, player: int, name: str, location_logics: typing.List[LocationLogic], logic_holder: LogicVarHolder) -> Region:
    new_region = Region(name, player, multiworld)
    if location_logics:
        for location_logic in location_logics:
            location_name = DK64RLocation.LocationListOriginal[location_logic.id].name
            loc_id = all_locations.get(location_name, 0)
            location = DK64Location(player, location_name, loc_id, new_region)
            set_rule(location, lambda state: hasDK64RLocation(state, logic_holder, location_logic))
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

    for region_list in [
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
        for region_obj in region_list.values():
            for exit in region_obj.exits:
                destination = region_list[exit.dest]
                try:
                    converted_logic = lambda state: hasDK64RTransition(state, logic_holder, exit)
                    connect(world, region_obj.name, destination.name, converted_logic)
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


def hasDK64RTransition(state: CollectionState, logic: LogicVarHolder, exit: TransitionFront):
    logic.UpdateFromArchipelagoItems(state)
    return exit.logic(logic)


def hasDK64RLocation(state: CollectionState, logic: LogicVarHolder, location: LocationLogic):
    logic.UpdateFromArchipelagoItems(state)
    return location.logic(logic)
