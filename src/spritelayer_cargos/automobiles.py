# spritelayer cargos are sandboxed into their own module to avoid them spawning tentacles into train.py etc

from gestalt_graphics.gestalt_graphics import GestaltGraphicsAutomobileTransporter

import spritelayer_cargo
from spritelayer_cargo import CargoBase

from spritelayer_cargos import registered_spritelayer_cargos


class AutomobileCargo(CargoBase):
    """Base class for automobile cargos - cars, trucks, tractors etc."""

    # - multiple vehicle types exist, e.g. cars, trucks, tractors etc
    # - unknown and generic cargos default to ????
    def __init__(self, **kwargs):
        self.base_id = "automobiles"
        super().__init__(**kwargs)
        self.gestalt_graphics = GestaltGraphicsAutomobileTransporter()
        # extend this when adding more platform types
        # y offset: positive = down in spritesheet (y origin at top)
        self.all_platform_types_with_floor_heights = {
            "default": 0,
            "low_floor": 1,
        }


class AutomobileDefaultAndLowFloorCargoBase(AutomobileCargo):
    """ Sparse base class to set compatible platform types and sprite placement template """

    # class properties, we want them available without __init__ for...reasons
    compatible_platform_types = ["default", "low_floor"]
    template_subtype_name = "default"


class Trucks16px(AutomobileDefaultAndLowFloorCargoBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.length = 16
        self.variants = [["trucks_1_1CC"], ["trucks_1_1CC"], ["trucks_1_1CC"]]


class Trucks20px(AutomobileDefaultAndLowFloorCargoBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.length = 20
        self.variants = [["trucks_1_1CC"], ["trucks_1_1CC"], ["trucks_1_1CC"]]


class Trucks24px(AutomobileDefaultAndLowFloorCargoBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.length = 24
        self.variants = [["trucks_1_1CC", "trucks_1_1CC"], ["trucks_1_1CC"]]


class Trucks32px(AutomobileDefaultAndLowFloorCargoBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.length = 32
        self.variants = [
            ["trucks_1_1CC", "trucks_1_1CC", "trucks_1_1CC"],
            ["trucks_1_1CC", "trucks_1_1CC", "trucks_1_1CC"],
        ]


cargo_subtype_to_subclass_mapping = {"box": [Trucks16px, Trucks24px, Trucks32px]}
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
    for subtype in cargo_subtype_to_subclass_mapping.keys():
        # exclude these types which don't have a meaningful 'default' as the graphics are ALWAYS cargo-specific
        if subtype not in [
            "bulk",
        ]:
            subtype_suffix = "DFLT"
            spritelayer_cargo.register_cargo(
                cargo_subtype_to_subclass_mapping, subtype, subtype_suffix
            )

    # then register automobiles with cargo labels in their filename e.g. bulk_COAL, tank_PETR etc
    # cargo label mapping returns "cargo_label: (subtype, subtype_suffix)"
    for subtype, subtype_suffix in set(
        GestaltGraphicsAutomobileTransporter().cargo_label_mapping.values()
    ):
        # exclude DFLT, handled explicitly elsewhere
        if subtype_suffix != "DFLT":
            spritelayer_cargo.register_cargo(
                cargo_subtype_to_subclass_mapping, subtype, subtype_suffix
            )
