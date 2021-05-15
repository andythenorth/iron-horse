# spritelayer cargos are sandboxed into their own module to avoid them spawning tentacles into train.py etc

from gestalt_graphics.gestalt_graphics import GestaltGraphicsAutomobileTransporter

from spritelayer_cargo import SpritelayerCargo, CargoSetBase


class AutomobilesSpritelayerCargo(SpritelayerCargo):
    """Base class for automobile spritelayer cargo - cars, trucks, tractors etc."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.base_id = "automobiles"
        self.gestalt_graphics = GestaltGraphicsAutomobileTransporter()

    @property
    def all_platform_types_with_floor_heights(self):
        # extend this when adding more platform types
        # y offset: positive = down in spritesheet (y origin at top)
        return {
            "default": 0,
            "low_floor": 1,
        }


class DefaultAndLowFloorAutomobilesCargoSetBase(CargoSetBase):
    """ Sparse base class to set compatible platform types and sprite placement template """

    def __init__(self, **kwargs):
        self.compatible_platform_types = ["default", "low_floor"]
        super().__init__(**kwargs)
        self.graphics_template_subtype_name = "default"


class Trucks16pxCargoSet(DefaultAndLowFloorAutomobilesCargoSetBase):
    def __init__(self, **kwargs):
        self.length = 16
        super().__init__(**kwargs)
        self.variants = [["trucks_1_1CC"], ["trucks_1_1CC"], ["trucks_1_1CC"]]


class Trucks20pxCargoSet(DefaultAndLowFloorAutomobilesCargoSetBase):
    def __init__(self, **kwargs):
        self.length = 20
        super().__init__(**kwargs)
        self.variants = [["trucks_1_1CC"], ["trucks_1_1CC"], ["trucks_1_1CC"]]


class Trucks24pxCargoSet(DefaultAndLowFloorAutomobilesCargoSetBase):
    def __init__(self, **kwargs):
        self.length = 24
        super().__init__(**kwargs)
        self.variants = [["trucks_1_1CC", "trucks_1_1CC"], ["trucks_1_1CC"]]


class Trucks32pxCargoSet(DefaultAndLowFloorAutomobilesCargoSetBase):
    def __init__(self, **kwargs):
        self.length = 32
        super().__init__(**kwargs)
        self.variants = [
            ["trucks_1_1CC", "trucks_1_1CC", "trucks_1_1CC"],
            ["trucks_1_1CC", "trucks_1_1CC", "trucks_1_1CC"],
        ]


subtype_to_cargo_set_mapping = {
    "box": [Trucks16pxCargoSet, Trucks20pxCargoSet, Trucks24pxCargoSet, Trucks32pxCargoSet]
}
"""
    "bulk": [
        IntermodalFlatCar16pxStandardCargo,
        IntermodalFlatCar24pxStandardCargo,
        IntermodalFlatCar32pxNo40FootCargo,  # note special case for 32px
        IntermodalCargoSprinter32px20FootOnlyCargo,
    ],
    "chemicals_tank": [
        IntermodalFlatCar16pxStandardCargo,
        IntermodalFlatCar24pxStandardCargo,
        IntermodalFlatCar32pxStandardCargo,
        IntermodalCargoSprinter32pxStandardCargo,
    ],
    "cryo_tank": [
        IntermodalFlatCar16pxStandardCargo,
        IntermodalFlatCar24pxStandardCargo,
        IntermodalFlatCar32pxStandardCargo,
        IntermodalCargoSprinter32pxStandardCargo,
    ],
    "curtain_side": [
        IntermodalFlatCar16pxStandardCargo,
        IntermodalFlatCar24px40FootOnlyCargo,  # note special case for 24px
        IntermodalFlatCar32px30FootOnlyCargo,  # note special case for 24px
        IntermodalCargoSprinter32px40FootOnlyCargo,
    ],
    "edibles_tank": [
        IntermodalFlatCar16pxStandardCargo,
        IntermodalFlatCar24pxStandardCargo,
        IntermodalFlatCar32pxStandardCargo,
        IntermodalCargoSprinter32pxStandardCargo,
    ],
    "stake_flatrack": [
        IntermodalFlatCar16pxStandardCargo,
        IntermodalFlatCar24px40FootOnlyCargo,  # note special case for 24px
        IntermodalFlatCar32px30FootOnlyCargo,  # note special case for 24px
        IntermodalCargoSprinter32px40FootOnlyCargo,
    ],
    "livestock": [
        IntermodalFlatCar16pxStandardCargo,
        IntermodalFlatCar24pxStandardCargo,
        IntermodalFlatCar32pxStandardCargo,
        IntermodalCargoSprinter32pxStandardCargo,
    ],
    "reefer": [
        IntermodalFlatCar16pxStandardCargo,
        IntermodalFlatCar24pxStandardCargo,
        IntermodalFlatCar32pxStandardCargo,
        IntermodalCargoSprinter32pxStandardCargo,
    ],
    "tank": [
        IntermodalFlatCar16pxStandardCargo,
        IntermodalFlatCar24pxStandardCargo,
        IntermodalFlatCar32pxStandardCargo,
        IntermodalCargoSprinter32pxStandardCargo,
    ],
    "wood": [
        IntermodalFlatCar16pxStandardCargo,
        IntermodalFlatCar24px40FootOnlyCargo,  # note special case for 24px
        IntermodalFlatCar32px30FootOnlyCargo,  # note special case for 24px
        IntermodalCargoSprinter32px40FootOnlyCargo,
    ],
"""


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
        GestaltGraphicsAutomobileTransporter().cargo_label_mapping.values()
    ):
        # exclude DFLT, handled explicitly elsewhere
        if subtype_suffix != "DFLT":
            for spritelayer_cargo_set_type in subtype_to_cargo_set_mapping[subtype]:
                spritelayer_cargo_set_type(
                    subtype=subtype,
                    subtype_suffix=subtype_suffix,
                    spritelayer_cargo_type=AutomobilesSpritelayerCargo,
                )
