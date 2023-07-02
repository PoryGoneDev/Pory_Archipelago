import typing

from BaseClasses import MultiWorld, Location


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

all_locations = {
    **level_location_table,
    **boss_location_table,
    **kong_location_table,
    **event_location_table,
}


def setup_locations(multiworld: MultiWorld, player: int) -> typing.Dict[str, DK64Location]:
    location_table = {}

    # DK64_TODO: Pull Locations from DK64R

    return location_table


lookup_id_to_name: typing.Dict[int, str] = {id: name for name, id in all_locations.items()}
