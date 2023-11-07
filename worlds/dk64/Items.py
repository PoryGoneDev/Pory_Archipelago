import typing

from BaseClasses import Item, ItemClassification
from worlds.AutoWorld import World

from randomizer.Lists import Item as DK64RItem

BASE_ID = 0xD64000


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

# Complete item table
full_item_table = { item.name: ItemData(int(BASE_ID + index), item.playthrough) for index, item in DK64RItem.ItemList.items() }

full_item_table.update(event_table) # Temp for generating goal item


def setup_items(world: World) -> typing.Dict[str, DK64Item]:
    item_table = {}

    # DK64_TODO: Pull Active Items from DK64R

    # Example
    if world.options.goal == "krool":
        pass

    # DEBUG
    #for k, v in full_item_table.items():
    #    print(k + ": " + hex(v.code) + " | " + str(v.progression))

    return item_table

lookup_id_to_name: typing.Dict[int, str] = {data.code: item_name for item_name, data in full_item_table.items()}
