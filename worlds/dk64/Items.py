import typing

from BaseClasses import MultiWorld, Item, ItemClassification


class ItemData(typing.NamedTuple):
    code: typing.Optional[int]
    progression: bool
    quantity: int = 1
    event: bool = False


class DK64Item(Item):
    game: str = "Donkey Kong 64"


# Separate tables for each type of item.
junk_table = {

}

collectable_table = {

}

event_table = {
    "Victory": ItemData(0xD64000, True), # Temp
}

# Complete item table.
full_item_table = {
    **junk_table,
    **collectable_table,
    **event_table,
}


def setup_items(multiworld: MultiWorld, player: int) -> typing.Dict[str, DK64Item]:
    item_table = {}

    # DK64_TODO: Pull Items from DK64R

    return item_table

lookup_id_to_name: typing.Dict[int, str] = {data.code: item_name for item_name, data in full_item_table.items()}
