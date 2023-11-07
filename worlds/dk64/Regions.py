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

    # Set up the regions correctly.
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


def connect_regions(world: World):
    connect(world.multiworld, world.player, "Menu", "DK Isles")

    # Example Region Connection
    connect(world.multiworld, world.player, "DK Isles", "Test",
            lambda state: state.has(DK64RItem.ItemList[DK64RItems.GoldenBanana].name, world.player, 2))

    # DK64_TODO: Get region access requirements from DK64R

    pass


def create_region(multiworld: MultiWorld, player: int, name: str, locations=None) -> Region:
    ret = Region(name, player, multiworld)
    if locations:
        for locationName in locations:
            loc_id = all_locations.get(locationName, 0)

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
