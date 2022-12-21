# spritelayer cargos are sandboxed into their own module to avoid them spawning tentacles into train.py etc

from gestalt_graphics.gestalt_graphics import GestaltGraphicsAutomobilesTransporter

from spritelayer_cargo import SpritelayerCargo, CargoSetBase


class AutomobilesSpritelayerCargo(SpritelayerCargo):
    """Base class for automobile spritelayer cargo - cars, trucks, tractors etc."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.base_id = "automobiles"
        self.gestalt_graphics = GestaltGraphicsAutomobilesTransporter(liveries=None)

    @property
    def all_platform_types_with_floor_heights(self):
        # extend this when adding more platform types
        # y offset: positive = down in spritesheet (y origin at top)
        # the origin was set up for intermodal cars, at solebar height, so standard automobiles actually need shifted up 1px, hence -1
        return {
            "default": -1,
            "low_floor": 0,
            "double_deck_lower": -1,
            "double_deck_upper": -5,
        }


class DefaultAutomobilesCargoSetBase(CargoSetBase):
    """Sparse base class to set compatible platform types and sprite placement template"""

    def __init__(self, **kwargs):
        self.compatible_platform_types = ["default"]
        super().__init__(**kwargs)
        self.graphics_template_subtype_name = "default"


class LowFloorAutomobilesCargoSetBase(CargoSetBase):
    """Sparse base class to set compatible platform types and sprite placement template"""

    def __init__(self, **kwargs):
        self.compatible_platform_types = ["low_floor"]
        super().__init__(**kwargs)
        self.graphics_template_subtype_name = "low_floor"


class DoubleDeckAutomobilesCargoSetBase(CargoSetBase):
    """Sparse base class to set compatible platform types and sprite placement template"""

    def __init__(self, **kwargs):
        self.compatible_platform_types = ["double_deck_lower", "double_deck_upper"]
        super().__init__(**kwargs)
        self.graphics_template_subtype_name = "double_deck" # arguably should be 'dropped deck' or something as appropriate


"""
class DefaultCars20pxCargoSet(DefaultAutomobilesCargoSetBase):
    def __init__(self, **kwargs):
        self.length = 20
        super().__init__(**kwargs)
        self.variants = [
            ["cars_1_15_foot_red", "cars_1_15_foot_red"],
            ["cars_1_15_foot_red", "cars_1_15_foot_blue"],
            ["cars_1_15_foot_red", "cars_1_15_foot_grey"],
            ["cars_1_15_foot_red", "cars_1_15_foot_mint_green"],
            ["cars_1_15_foot_grey", "cars_1_15_foot_grey"],
            ["cars_1_15_foot_grey", "cars_1_15_foot_red"],
            ["cars_1_15_foot_grey", "cars_1_15_foot_blue"],
            ["cars_1_15_foot_1CC", "cars_1_15_foot_mint_green"],
            ["cars_1_15_foot_blue", "cars_1_15_foot_grey"],
            ["cars_1_15_foot_blue", "cars_1_15_foot_blue"],
            ["cars_1_15_foot_mint_green", "cars_1_15_foot_red"],
            ["cars_1_15_foot_mint_green", "cars_1_15_foot_blue"],
            ["cars_1_15_foot_mint_green", "cars_1_15_foot_mint_green"],
        ]
"""


class DefaultCars24pxCargoSet(DefaultAutomobilesCargoSetBase):
    def __init__(self, **kwargs):
        self.length = 24
        super().__init__(**kwargs)
        self.variants = [
            ["cars_1_15_foot_mint_green", "cars_1_15_foot_mint_green", "cars_1_15_foot_grey"],
            ["cars_1_15_foot_red", "cars_1_15_foot_red", "cars_1_15_foot_grey"],
            ["cars_1_15_foot_red", "cars_1_15_foot_red", "cars_1_15_foot_red"],
            ["cars_1_15_foot_red", "cars_1_15_foot_red", "cars_1_15_foot_mint_green"],
            ["cars_1_15_foot_red", "cars_1_15_foot_grey", "cars_1_15_foot_grey"],
            ["cars_1_15_foot_grey", "cars_1_15_foot_grey", "cars_1_15_foot_grey"],
            ["cars_1_15_foot_1CC", "cars_1_15_foot_mint_green", "cars_1_15_foot_mint_green"],
            ["cars_1_15_foot_mint_green", "cars_1_15_foot_red", "cars_1_15_foot_red"],
            ["cars_1_15_foot_blue", "cars_1_15_foot_blue", "cars_1_15_foot_blue"],
            ["cars_1_15_foot_blue", "cars_1_15_foot_grey", "cars_1_15_foot_blue"],
            ["cars_1_15_foot_blue", "cars_1_15_foot_blue", "cars_1_15_foot_red"],
            ["cars_1_15_foot_mint_green", "cars_1_15_foot_blue", "cars_1_15_foot_red"],
        ]


class DefaultCars32pxCargoSet(DefaultAutomobilesCargoSetBase):
    def __init__(self, **kwargs):
        self.length = 32
        super().__init__(**kwargs)
        self.variants = [
            ["cars_1_15_foot_mint_green", "cars_1_15_foot_mint_green", "cars_1_15_foot_grey", "cars_1_15_foot_grey"],
            ["cars_1_15_foot_red", "cars_1_15_foot_red", "cars_1_15_foot_grey", "cars_1_15_foot_grey"],
            ["cars_1_15_foot_red", "cars_1_15_foot_red", "cars_1_15_foot_red", "cars_1_15_foot_grey"],
            ["cars_1_15_foot_red", "cars_1_15_foot_red", "cars_1_15_foot_mint_green", "cars_1_15_foot_grey"],
            ["cars_1_15_foot_red", "cars_1_15_foot_grey", "cars_1_15_foot_grey", "cars_1_15_foot_grey"],
            ["cars_1_15_foot_grey", "cars_1_15_foot_grey", "cars_1_15_foot_grey", "cars_1_15_foot_grey"],
            ["cars_1_15_foot_1CC", "cars_1_15_foot_mint_green", "cars_1_15_foot_mint_green", "cars_1_15_foot_grey"],
            ["cars_1_15_foot_mint_green", "cars_1_15_foot_red", "cars_1_15_foot_red", "cars_1_15_foot_grey"],
            ["cars_1_15_foot_blue", "cars_1_15_foot_blue", "cars_1_15_foot_blue", "cars_1_15_foot_grey"],
            ["cars_1_15_foot_blue", "cars_1_15_foot_grey", "cars_1_15_foot_blue", "cars_1_15_foot_grey"],
            ["cars_1_15_foot_blue", "cars_1_15_foot_blue", "cars_1_15_foot_red", "cars_1_15_foot_grey"],
            ["cars_1_15_foot_mint_green", "cars_1_15_foot_blue", "cars_1_15_foot_red", "cars_1_15_foot_grey"],
        ]


class LowFloorCars24pxCargoSet(LowFloorAutomobilesCargoSetBase):
    def __init__(self, **kwargs):
        self.length = 24
        super().__init__(**kwargs)
        self.variants = [
            ["cars_1_15_foot_mint_green", "cars_1_15_foot_mint_green", "cars_1_15_foot_grey"],
            ["cars_1_15_foot_red", "cars_1_15_foot_red", "cars_1_15_foot_grey"],
            ["cars_1_15_foot_red", "cars_1_15_foot_red", "cars_1_15_foot_red"],
            ["cars_1_15_foot_red", "cars_1_15_foot_red", "cars_1_15_foot_mint_green"],
            ["cars_1_15_foot_red", "cars_1_15_foot_grey", "cars_1_15_foot_grey"],
            ["cars_1_15_foot_grey", "cars_1_15_foot_grey", "cars_1_15_foot_grey"],
            ["cars_1_15_foot_1CC", "cars_1_15_foot_mint_green", "cars_1_15_foot_mint_green"],
            ["cars_1_15_foot_mint_green", "cars_1_15_foot_red", "cars_1_15_foot_red"],
            ["cars_1_15_foot_blue", "cars_1_15_foot_blue", "cars_1_15_foot_blue"],
            ["cars_1_15_foot_blue", "cars_1_15_foot_grey", "cars_1_15_foot_blue"],
            ["cars_1_15_foot_blue", "cars_1_15_foot_blue", "cars_1_15_foot_red"],
            ["cars_1_15_foot_mint_green", "cars_1_15_foot_blue", "cars_1_15_foot_red"],
        ]


class LowFloorCars32pxCargoSet(LowFloorAutomobilesCargoSetBase):
    def __init__(self, **kwargs):
        self.length = 32
        super().__init__(**kwargs)
        self.variants = [
            ["cars_1_15_foot_mint_green", "cars_1_15_foot_mint_green", "cars_1_15_foot_grey", "cars_1_15_foot_grey"],
            ["cars_1_15_foot_red", "cars_1_15_foot_red", "cars_1_15_foot_grey", "cars_1_15_foot_grey"],
            ["cars_1_15_foot_red", "cars_1_15_foot_red", "cars_1_15_foot_red", "cars_1_15_foot_grey"],
            ["cars_1_15_foot_red", "cars_1_15_foot_red", "cars_1_15_foot_mint_green", "cars_1_15_foot_grey"],
            ["cars_1_15_foot_red", "cars_1_15_foot_grey", "cars_1_15_foot_grey", "cars_1_15_foot_grey"],
            ["cars_1_15_foot_grey", "cars_1_15_foot_grey", "cars_1_15_foot_grey", "cars_1_15_foot_grey"],
            ["cars_1_15_foot_1CC", "cars_1_15_foot_mint_green", "cars_1_15_foot_mint_green", "cars_1_15_foot_grey"],
            ["cars_1_15_foot_mint_green", "cars_1_15_foot_red", "cars_1_15_foot_red", "cars_1_15_foot_grey"],
            ["cars_1_15_foot_blue", "cars_1_15_foot_blue", "cars_1_15_foot_blue", "cars_1_15_foot_grey"],
            ["cars_1_15_foot_blue", "cars_1_15_foot_grey", "cars_1_15_foot_blue", "cars_1_15_foot_grey"],
            ["cars_1_15_foot_blue", "cars_1_15_foot_blue", "cars_1_15_foot_red", "cars_1_15_foot_grey"],
            ["cars_1_15_foot_mint_green", "cars_1_15_foot_blue", "cars_1_15_foot_red", "cars_1_15_foot_grey"],
        ]


class DoubleDeckCars20pxCargoSet(DoubleDeckAutomobilesCargoSetBase):
    def __init__(self, **kwargs):
        self.length = 20
        super().__init__(**kwargs)
        self.variants = [
            ["cars_1_15_foot_red", "cars_1_15_foot_red"],
            ["cars_1_15_foot_red", "cars_1_15_foot_blue"],
            ["cars_1_15_foot_red", "cars_1_15_foot_grey"],
            ["cars_1_15_foot_red", "cars_1_15_foot_mint_green"],
            ["cars_1_15_foot_grey", "cars_1_15_foot_grey"],
            ["cars_1_15_foot_grey", "cars_1_15_foot_red"],
            ["cars_1_15_foot_grey", "cars_1_15_foot_blue"],
            ["cars_1_15_foot_1CC", "cars_1_15_foot_mint_green"],
            ["cars_1_15_foot_blue", "cars_1_15_foot_grey"],
            ["cars_1_15_foot_blue", "cars_1_15_foot_blue"],
            ["cars_1_15_foot_mint_green", "cars_1_15_foot_red"],
            ["cars_1_15_foot_mint_green", "cars_1_15_foot_blue"],
            ["cars_1_15_foot_mint_green", "cars_1_15_foot_mint_green"],
        ]


class DoubleDeckCars24pxCargoSet(DoubleDeckAutomobilesCargoSetBase):
    def __init__(self, **kwargs):
        self.length = 24
        super().__init__(**kwargs)
        self.variants = [
            ["cars_1_15_foot_mint_green", "cars_1_15_foot_mint_green", "cars_1_15_foot_grey"],
            ["cars_1_15_foot_red", "cars_1_15_foot_red", "cars_1_15_foot_grey"],
            ["cars_1_15_foot_red", "cars_1_15_foot_red", "cars_1_15_foot_red"],
            ["cars_1_15_foot_red", "cars_1_15_foot_red", "cars_1_15_foot_mint_green"],
            ["cars_1_15_foot_red", "cars_1_15_foot_grey", "cars_1_15_foot_grey"],
            ["cars_1_15_foot_grey", "cars_1_15_foot_grey", "cars_1_15_foot_grey"],
            ["cars_1_15_foot_1CC", "cars_1_15_foot_mint_green", "cars_1_15_foot_mint_green"],
            ["cars_1_15_foot_mint_green", "cars_1_15_foot_red", "cars_1_15_foot_red"],
            ["cars_1_15_foot_blue", "cars_1_15_foot_blue", "cars_1_15_foot_blue"],
            ["cars_1_15_foot_blue", "cars_1_15_foot_grey", "cars_1_15_foot_blue"],
            ["cars_1_15_foot_blue", "cars_1_15_foot_blue", "cars_1_15_foot_red"],
            ["cars_1_15_foot_mint_green", "cars_1_15_foot_blue", "cars_1_15_foot_red"],
        ]


class DoubleDeckCars32pxCargoSet(DoubleDeckAutomobilesCargoSetBase):
    def __init__(self, **kwargs):
        self.length = 32
        super().__init__(**kwargs)
        self.variants = [
            ["cars_1_15_foot_mint_green", "cars_1_15_foot_mint_green", "cars_1_15_foot_grey", "cars_1_15_foot_grey"],
            ["cars_1_15_foot_red", "cars_1_15_foot_red", "cars_1_15_foot_grey", "cars_1_15_foot_grey"],
            ["cars_1_15_foot_red", "cars_1_15_foot_red", "cars_1_15_foot_red", "cars_1_15_foot_grey"],
            ["cars_1_15_foot_red", "cars_1_15_foot_red", "cars_1_15_foot_mint_green", "cars_1_15_foot_grey"],
            ["cars_1_15_foot_red", "cars_1_15_foot_grey", "cars_1_15_foot_grey", "cars_1_15_foot_grey"],
            ["cars_1_15_foot_grey", "cars_1_15_foot_grey", "cars_1_15_foot_grey", "cars_1_15_foot_grey"],
            ["cars_1_15_foot_1CC", "cars_1_15_foot_mint_green", "cars_1_15_foot_mint_green", "cars_1_15_foot_grey"],
            ["cars_1_15_foot_mint_green", "cars_1_15_foot_red", "cars_1_15_foot_red", "cars_1_15_foot_grey"],
            ["cars_1_15_foot_blue", "cars_1_15_foot_blue", "cars_1_15_foot_blue", "cars_1_15_foot_grey"],
            ["cars_1_15_foot_blue", "cars_1_15_foot_grey", "cars_1_15_foot_blue", "cars_1_15_foot_grey"],
            ["cars_1_15_foot_blue", "cars_1_15_foot_blue", "cars_1_15_foot_red", "cars_1_15_foot_grey"],
            ["cars_1_15_foot_mint_green", "cars_1_15_foot_blue", "cars_1_15_foot_red", "cars_1_15_foot_grey"],
        ]


class Trucks16pxCargoSet(DefaultAutomobilesCargoSetBase):
    def __init__(self, **kwargs):
        self.length = 16
        super().__init__(**kwargs)
        self.variants = [["trucks_1_20_foot_1CC"]]


class Trucks20pxCargoSet(DefaultAutomobilesCargoSetBase):
    def __init__(self, **kwargs):
        self.length = 20
        super().__init__(**kwargs)
        self.variants = [["trucks_1_20_foot_1CC"], ["trucks_1_20_foot_1CC"]]


class Trucks24pxCargoSet(DefaultAutomobilesCargoSetBase):
    def __init__(self, **kwargs):
        self.length = 24
        super().__init__(**kwargs)
        self.variants = [["trucks_1_20_foot_1CC", "trucks_1_20_foot_1CC"]]


class Trucks32pxCargoSet(DefaultAutomobilesCargoSetBase):
    def __init__(self, **kwargs):
        self.length = 32
        super().__init__(**kwargs)
        self.variants = [
            ["trucks_1_20_foot_1CC", "trucks_1_20_foot_1CC", "trucks_1_20_foot_1CC"],
            ["trucks_1_20_foot_1CC", "trucks_1_20_foot_1CC", "trucks_1_20_foot_1CC"],
        ]


subtype_to_cargo_set_mapping = {
    "cars": [
        DefaultCars24pxCargoSet,
        DefaultCars32pxCargoSet,
        LowFloorCars24pxCargoSet,
        LowFloorCars32pxCargoSet,
        DoubleDeckCars20pxCargoSet,
        DoubleDeckCars24pxCargoSet,
        DoubleDeckCars32pxCargoSet,
    ],
    #"trucks": [
    #    Trucks16pxCargoSet,
    #    Trucks20pxCargoSet,
    #    Trucks24pxCargoSet,
    #    Trucks32pxCargoSet,
    #],
}


def main():
    # first register automobiles with DFLT in their filename, which will be used for:
    # - for known cargos with only one visual variant
    # - specific known classes (as default, or fallback where the class might still have further cargo specific sprites)
    # - all other cargos / classes not handled explicitly, which will fall back to box
    for subtype in subtype_to_cargo_set_mapping.keys():
        # exclude these types which don't have a meaningful 'default' as the graphics are ALWAYS cargo-specific
        if subtype not in [
            "bulk",
        ]:
            subtype_suffix = "DFLT"
            for spritelayer_cargo_set_type in subtype_to_cargo_set_mapping[subtype]:
                spritelayer_cargo_set_type(
                    subtype=subtype,
                    subtype_suffix=subtype_suffix,
                    spritelayer_cargo_type=AutomobilesSpritelayerCargo,
                )

    # then register automobiles with cargo labels in their filename e.g. bulk_COAL, tank_PETR etc
    # cargo label mapping returns "cargo_label: (subtype, subtype_suffix)"
    for subtype, subtype_suffix in set(
        GestaltGraphicsAutomobilesTransporter(liveries=None).cargo_label_mapping.values()
    ):
        # exclude DFLT, handled explicitly elsewhere
        if subtype_suffix != "DFLT":
            for spritelayer_cargo_set_type in subtype_to_cargo_set_mapping[subtype]:
                spritelayer_cargo_set_type(
                    subtype=subtype,
                    subtype_suffix=subtype_suffix,
                    spritelayer_cargo_type=AutomobilesSpritelayerCargo,
                )
