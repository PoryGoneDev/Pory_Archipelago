import typing

from BaseClasses import Location
from worlds.AutoWorld import World

from randomizer.Lists import Location as DK64RLocation

BASE_ID = 0xD64000

class DK64Location(Location):
    game: str = "Donkey Kong 64"

    def __init__(self, player: int, name: str = '', address: int = None, parent=None):
        super().__init__(player, name, address, parent)


level_location_table = {
    "TEMP": 0xD64000, # Temp
}

kong_location_table = {

}

boss_location_table = {

}

event_location_table = {
    "Victory": 0x00, # Temp
}

# Complete location table
all_locations = { location.name: (BASE_ID + index) for index, location in enumerate(DK64RLocation.LocationList)}

all_locations.update(event_location_table) # Temp for generating goal location


def setup_locations(world: World) -> typing.Dict[str, DK64Location]:
    location_table = {}

    # DK64_TODO: Pull Active Locations from DK64R

    # DEBUG
    #for k, v in all_locations.items():
    #    print(k + ": " + hex(v))

    return location_table


lookup_id_to_name: typing.Dict[int, str] = {id: name for name, id in all_locations.items()}
