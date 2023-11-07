import typing

from BaseClasses import MultiWorld, Region, Entrance
from worlds.AutoWorld import World
from .Items import DK64Item
from .Locations import DK64Location


def create_regions(multiworld, player: int, active_locations):
    menu_region = create_region(multiworld, player, active_locations, "Menu")
    test_region = create_region(multiworld, player, active_locations, "Test", ["Victory"])

    # DK64_TODO: Get Regions from DK64R

    # Set up the regions correctly.
    multiworld.regions += [
        menu_region,
        test_region,
    ]


def connect_regions(world: World):
    connect(world.multiworld, world.player, "Menu", "Test")

    # DK64_TODO: Get region access requirements from DK64R

    pass


def create_region(multiworld: MultiWorld, player: int, active_locations, name: str, locations=None) -> Region:
    ret = Region(name, player, multiworld)
    if locations:
        for locationName in locations:
            loc_id = active_locations.get(locationName, 0)

            location = DK64Location(player, locationName, loc_id, ret)
            ret.locations.append(location)

    return ret


def connect(multiworld: MultiWorld, player: int, source: str, target: str,
            rule: typing.Optional[typing.Callable] = None):
    source_region = multiworld.get_region(source, player)
    target_region = multiworld.get_region(target, player)

    name = source + "->" + target

    connection = Entrance(player, name, source_region)

    if rule:
        connection.access_rule = rule

    source_region.exits.append(connection)
    connection.connect(target_region)
