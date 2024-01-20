import typing

from BaseClasses import Item, ItemClassification
from worlds.AutoWorld import World
from types import SimpleNamespace

from dk64r.randomizer.Lists import Item as DK64RItem
from dk64r.randomizer.Enums.Items import Items as DK64RItems
from dk64r.randomizer.ItemPool import AllItemsUnrestricted

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

lookup_id_to_name: typing.Dict[int, str] = {data.code: item_name for item_name, data in full_item_table.items()}

full_item_table.update(event_table) # Temp for generating goal item


def setup_items(world: World) -> typing.List[DK64Item]:
    item_table = []

    # TODO: This is unrestricted, we should update this to the restricted function based on the actual value
    all_items_unrestricted = AllItemsUnrestricted(SimpleNamespace(**{"shockwave_status": False, "starting_kongs_count": 5}))
   
    for seed_item in all_items_unrestricted:
        if seed_item.name not in ["TestItem"]:
            item = DK64RItem.ItemList[seed_item]
            if item.type in [DK64RItems.JunkCrystal, DK64RItems.JunkMelon, DK64RItems.JunkAmmo, DK64RItems.JunkFilm, DK64RItems.JunkOrange, DK64RItems.CrateMelon]:
                classification = ItemClassification.filler
            elif item.type in [DK64RItems.FakeItem]:
                classification = ItemClassification.trap
            elif item.playthrough == True:
                classification = ItemClassification.progression
            else:
                classification = ItemClassification.useful
            item_table.append(DK64Item(item.name, classification, full_item_table[item.name], world.player))

    # Example of accessing Option result
    if world.options.goal == "krool":
        pass

    # DEBUG
    #for k, v in full_item_table.items():
    #    print(k + ": " + hex(v.code) + " | " + str(v.progression))

    return item_table
