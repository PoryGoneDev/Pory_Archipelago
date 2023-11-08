import typing

from BaseClasses import MultiWorld, Region, Entrance, Location
from worlds.AutoWorld import World

from randomizer.Lists import Item as DK64RItem
from randomizer.Enums.Items import Items as DK64RItems

from randomizer.Lists import Location as DK64RLocation
from randomizer.Enums.Locations import Locations as DK64RLocations

BASE_ID = 0xD64000

class DK64Location(Location):
    game: str = "Donkey Kong 64"

    def __init__(self, player: int, name: str = '', address: int = None, parent=None):
        super().__init__(player, name, address, parent)


# Complete location table
all_locations = { location.name: (BASE_ID + index) for index, location in enumerate(DK64RLocation.LocationList)}
all_locations.update({"Victory": 0x00}) # Temp for generating goal location
lookup_id_to_name: typing.Dict[int, str] = {id: name for name, id in all_locations.items()}


def create_regions(multiworld: MultiWorld, player: int):
    menu_region = create_region(multiworld, player, "Menu")
    test_region = create_region(multiworld, player, "Test", ["Victory"])

    multiworld.regions += [
        menu_region,
        test_region,
    ]

    # Example Region Creation
    dk_isles_region_locations = [
        DK64RLocation.LocationList[DK64RLocations.IslesVinesTrainingBarrel].name,
        DK64RLocation.LocationList[DK64RLocations.IslesSwimTrainingBarrel].name,
        DK64RLocation.LocationList[DK64RLocations.IslesOrangesTrainingBarrel].name,
        DK64RLocation.LocationList[DK64RLocations.IslesBarrelsTrainingBarrel].name,
    ]
    multiworld.regions.append(create_region(multiworld, player, "DK Isles", dk_isles_region_locations))

    # DK64_TODO: Get Regions from DK64R


def create_region(multiworld: MultiWorld, player: int, name: str, locations=None) -> Region:
    new_region = Region(name, player, multiworld)
    if locations:
        for location_name in locations:
            loc_id = all_locations.get(location_name, 0)

            location = DK64Location(player, location_name, loc_id, new_region)
            new_region.locations.append(location)

    return new_region


def connect_regions(world: World):
    connect(world, "Menu", "DK Isles")

    # Example Region Connection
    connect(world, "DK Isles", "Test",
            lambda state: state.has(DK64RItem.ItemList[DK64RItems.GoldenBanana].name, world.player, 2))

    # DK64_TODO: Get region access requirements from DK64R

    pass


def connect(world: World, source: str, target: str,
            rule: typing.Optional[typing.Callable] = None):
    source_region = world.multiworld.get_region(source, world.player)
    target_region = world.multiworld.get_region(target, world.player)

    name = source + "->" + target

    connection = Entrance(world.player, name, source_region)

    if rule:
        connection.access_rule = rule

    source_region.exits.append(connection)
    connection.connect(target_region)
