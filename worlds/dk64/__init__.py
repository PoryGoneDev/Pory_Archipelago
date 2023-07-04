import os
import sys
import typing
import math
import threading

sys.path.append('./worlds/dk64/DK64R/')

from BaseClasses import Item, MultiWorld, Tutorial, ItemClassification
from .Items import DK64Item, ItemData, full_item_table, setup_items
from .Locations import DK64Location, all_locations, setup_locations
from .Options import dk64_options
from .Regions import create_regions, connect_regions
from .Rules import set_rules
from worlds.AutoWorld import WebWorld, World
import Patch


class DK64Web(WebWorld):
    theme = "jungle"

    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the Donkey Kong 64 randomizer connected to an Archipelago Multiworld.",
        "English",
        "setup_en.md",
        "setup/en",
        ["PoryGone"]
    )

    tutorials = [setup_en]


class DK64World(World):
    """
    Donkey Kong 64 is a 3D collectathon platforming game.
    Play as the whole DK Crew and rescue the Golden Banana hoard from King K. Rool.
    """
    game: str = "Donkey Kong 64"
    option_definitions = dk64_options
    topology_present = False
    data_version = 0

    item_name_to_id = {name: data.code for name, data in full_item_table.items()}
    location_name_to_id = all_locations

    web = DK64Web()
    
    def __init__(self, world: MultiWorld, player: int):
        self.rom_name_available_event = threading.Event()
        super().__init__(world, player)

    @classmethod
    def stage_assert_generate(cls, multiworld: MultiWorld):
        #rom_file = get_base_rom_path()
        #if not os.path.exists(rom_file):
        #    raise FileNotFoundError(rom_file)
        pass

    def _get_slot_data(self):
        return {
            #"death_link": self.world.death_link[self.player].value,
        }

    def create_regions(self) -> None:
        location_table = setup_locations(self.multiworld, self.player)
        create_regions(self.multiworld, self.player, location_table)

    def create_items(self) -> None:
        itempool: typing.List[DK64Item] = setup_items(self.multiworld, self.player)
        self.multiworld.itempool += itempool

    def set_rules(self):
        set_rules(self.multiworld, self.player)

    def generate_basic(self):
        connect_regions(self.multiworld, self.player)

        self.multiworld.get_location("Victory", self.player).place_locked_item(DK64Item("Victory", ItemClassification.progression, 0x000000, self.player)) # TEMP

    def generate_output(self, output_directory: str):
        try:
            # DK64_TODO: Handle patching via DK64R
            rompath = os.path.join(output_directory, f"{self.multiworld.get_out_file_name_base(self.player)}.sfc")
        except:
            raise
        finally:
            if os.path.exists(rompath):
                os.unlink(rompath)
            self.rom_name_available_event.set() # make sure threading continues and errors are collected

    def modify_multidata(self, multidata: dict):
        pass

    def fill_slot_data(self) -> dict:
        slot_data = self._get_slot_data()
        for option_name in dk64_options:
            option = getattr(self.multiworld, option_name)[self.player]
            slot_data[option_name] = option.value

        return slot_data

    def create_item(self, name: str, force_non_progression=False) -> Item:
        data = full_item_table[name]

        if force_non_progression:
            classification = ItemClassification.filler
        elif data.progression:
            classification = ItemClassification.progression
        else:
            classification = ItemClassification.filler

        created_item = DK64Item(name, classification, data.code, self.player)

        return created_item
